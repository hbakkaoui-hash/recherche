import numpy as np
from scipy.integrate import solve_ivp
b=-0.30; om=49.0; al=1.0
def f(t):return 1+b*np.cos(t)
def fp(t):return -b*np.sin(t)
def U(t):return al*(1-np.cos(t))/f(t)**2
def Gtt(t):return om/f(t)+1.5*(fp(t)/f(t))**2
def Gpp(t):return om*np.sin(t)**2/f(t)
def dnum(g,t,h=1e-6):return (g(t+h)-g(t-h))/(2*h)
def ddnum(g,t,h=1e-5):return (g(t+h)-2*g(t)+g(t-h))/h**2
def Up(t):return dnum(U,t)
def Upp(t):return ddnum(U,t)
def eps(t):return (Up(t)/U(t))**2/(2*Gtt(t))
def etaV(t):return (1.0/U(t))*(Upp(t)/Gtt(t)-Up(t)*dnum(Gtt,t)/(2*Gtt(t)**2))
def H2(t):return U(t)/3.0

# fond : dtheta/dN=-(1/Gtt)U'/U, evenement eps=1 (terminal)
def rhs(N,y):
    t=max(min(y[0],np.pi-1e-9),1e-9); return [-(1.0/Gtt(t))*Up(t)/U(t)]
def ev_eps1(N,y):return eps(max(min(y[0],np.pi-1e-9),1e-9))-1.0
ev_eps1.terminal=True; ev_eps1.direction=1
t0=np.pi-0.02
sol=solve_ivp(rhs,[0,1e5],[t0],events=ev_eps1,dense_output=True,rtol=1e-11,atol=1e-13,max_step=1.0)
Nend=sol.t_events[0][0] if sol.t_events[0].size else sol.t[-1]
th_end=sol.y_events[0][0][0] if sol.t_events[0].size else sol.y[0,-1]
print("Fin d'inflation : N_tot=%.2f, theta_end=%.4f, eps_end=%.3f"%(Nend,th_end,eps(th_end)))

# masse entropique (champ entropique = phi), Vss analytique + courbure
def Vss(t):return (dnum(Gpp,t)*Up(t))/(2*Gpp(t)*Gtt(t))
def Rfs(t):
    def integ(x):return dnum(Gpp,x)/np.sqrt(Gtt(x)*Gpp(x))
    return 2*(-1.0/(2*np.sqrt(Gtt(t)*Gpp(t)))*dnum(integ,t))
def Ms2H2(t):return (Vss(t)+eps(t)*Rfs(t)*H2(t))/H2(t)

print("\n N*    theta*   eps      n_s      r       M_s^2/H^2   (m_s^2/H^2 sans courbure)")
for Nb in [60,55,50]:
    Nx=Nend-Nb
    if Nx<0: print("  (pas assez d'e-folds pour N*=%d)"%Nb); continue
    t=sol.sol(Nx)[0]; e=eps(t)
    ns=1-6*e+2*etaV(t); r=16*e
    print(" %d   %.4f   %.5f  %.4f   %.4f   %+.5f     %+.5f"
          %(Nb,t,e,ns,r,Ms2H2(t),Vss(t)/H2(t)))

print("\nProfil le long du roulement :")
for tt in [3.0,2.8,2.5,2.0,1.5,1.0,0.5]:
    print("  theta=%.2f : M_s^2/H^2=%+.5f   eps=%.5f   Gpp=%.3f"%(tt,Ms2H2(tt),eps(tt),Gpp(tt)))

# figure : M_s^2/H^2 le long du roulement, en e-folds avant la fin
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
Nb=np.linspace(0,80,300); ths=np.array([sol.sol(Nend-x)[0] for x in Nb])
ms=np.array([Ms2H2(t) for t in ths]); ee=np.array([eps(t) for t in ths])
fig,ax=plt.subplots(1,2,figsize=(11,4))
ax[0].axhspan(-0.01,0.01,color='0.9'); ax[0].axhline(0,color='k',lw=.6)
ax[0].plot(Nb,ms,color='#1F4E79',lw=2)
ax[0].axvspan(50,60,color='#B23A2E',alpha=0.12)
ax[0].set_xlabel("$N$ (e-folds avant la fin)"); ax[0].set_ylabel("$M_s^2/H^2$ (mode entropique)")
ax[0].set_title("Masse entropique : legere, ~tachyonique a l'horizon"); ax[0].invert_xaxis(); ax[0].grid(alpha=.3)
ax[0].text(55,0.05,"horizon\n$N_*\\approx55$",color='#B23A2E',ha='center',fontsize=9)
ax[1].plot(Nb,ee,color='#2E7D32',lw=2); ax[1].axvspan(50,60,color='#B23A2E',alpha=0.12)
ax[1].set_xlabel("$N$ (e-folds avant la fin)"); ax[1].set_ylabel(r"$\epsilon$"); ax[1].invert_xaxis()
ax[1].set_title("Roulement adiabatique ($n_s=0.96$, $r=0.036$)"); ax[1].grid(alpha=.3)
plt.tight_layout(); plt.savefig('fig_axe1.png',dpi=130); print("fig_axe1.png ecrite")

# estimation beta_iso ~ 2 eps (champ entropique leger, sans virage) au point horizon
ts=sol.sol(Nend-55)[0]
print("\nA N*=55 : eps=%.4f -> P_S/P_zeta ~ 2 eps = %.4f  (prefacteur de couplage horloge-matiere <=1)"
      %(eps(ts),2*eps(ts)))
print("tilt isocourbure n_iso-1 ~ 2 M_s^2/(3H^2) = %.5f  (quasi invariant d'echelle, fixe par la geometrie)"
      %(2*Ms2H2(ts)/3))
