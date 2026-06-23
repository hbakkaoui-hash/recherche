import numpy as np
from scipy.special import ellipk          # ellipk(m), m=k^2
from scipy.integrate import solve_ivp

# Pres du vide de Planck : pendule spherique, potentiel -A cos(theta), metrique omega(dth^2+sin^2 th dph^2)
# Omega_0 = sqrt(A/omega).  On compare les DEUX modes a amplitude angulaire 'a'.
# Mode horloge (orbite circulaire a theta_o=a) : phidot = Omega_0 / sqrt(cos a)   [exact]
# Mode echelle (pendule radial, amplitude a)   : Omega = Omega_0 * (pi/2)/K(sin(a/2)) [exact]

def f_clock(a):  return 1/np.sqrt(np.cos(a))
def f_scale(a):  return (np.pi/2)/ellipk(np.sin(a/2)**2)   # /Omega_0
def split(a):    return f_clock(a)-f_scale(a)

print("a(rad)  Om_clock/Om0  Om_scale/Om0   split=DeltaOm/Om0   5/16*a^2   (split)/a^2")
for a in [0.05,0.1,0.2,0.3,0.4,0.5]:
    s=split(a)
    print(" %.2f    %.6f      %.6f       %.6e     %.6e   %.5f"
          %(a,f_clock(a),f_scale(a),s,5/16*a**2,s/a**2))

# coefficient limite
aa=np.array([0.02,0.03,0.04]); coef=np.polyfit(aa**2,[split(x) for x in aa],1)[0]
print("\ncoefficient a->0 de split/a^2 :",round(coef,5)," (theorie 5/16 =",round(5/16,5),")")
print("signe : l'HORLOGE (azimutal/QM) tourne PLUS VITE que le mode d'echelle (radial/GR).")

# ---- precession du pendule spherique (face invariante) : orbite elliptique ----
# EOM: th'' = sin th cos th phd^2 - Om0^2 sin th ;  d/dt(sin^2 th phd)=0.  Om0=1 (unites).
def eom(t,y):
    th,thd,ph,phd=y; s,c=np.sin(th),np.cos(th)
    return [thd, s*c*phd**2 - s, phd, (-2*c/s*thd*phd if abs(s)>1e-9 else 0)]
# lancer une ellipse : a theta=a0 avec une petite vitesse azimutale (orbite non circulaire)
a0=0.30; J_over=0.3   # fraction de la vitesse circulaire -> ellipse
phd0=J_over*np.sqrt(1/np.cos(a0))
y0=[a0,0,0,phd0]
sol=solve_ivp(eom,[0,400],y0,rtol=1e-11,atol=1e-13,max_step=0.02,dense_output=True)
tt=np.linspace(0,sol.t[-1],400000); Y=sol.sol(tt); th=Y[0]; ph=Y[2]
# apsides = maxima de theta ; angle phi a chaque apoapside -> precession par cycle radial
mx=(np.diff(np.sign(np.diff(th)))<0).nonzero()[0]+1
phi_ap=ph[mx]
dphi=np.diff(phi_ap)              # avance azimutale entre deux apoapsides successifs
prec=np.mean(dphi)-np.pi         # exces sur pi (ellipse centree non precessante -> pi)
# amplitudes angulaires de l'ellipse
th_max=th[mx].mean(); th_min=th[(np.diff(np.sign(np.diff(th)))>0).nonzero()[0]+1].mean()
print("\nPrecession (pendule spherique), ellipse th in [%.3f,%.3f]:"%(th_min,th_max))
print("  avance phi entre apoapsides =",round(np.mean(dphi),5)," rad  (base pi=%.5f)"%np.pi)
print("  precession par cycle radial =",round(prec,5)," rad,  signe>0 = prograde (sens du mouvement)")
print("  formule Olsson (3/8) th_max th_min =",round(3/8*th_max*th_min,5)," rad")

print("\n--- precession : test du prefacteur (3 pi/8) theta_min theta_max ---")
print("  mesure =",round(prec,5),"  (3pi/8) th_min th_max =",round(3*np.pi/8*th_max*th_min,5))

# figures
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
fig,ax=plt.subplots(1,2,figsize=(11,4.2))
ag=np.linspace(0,0.55,200)
ax[0].plot(ag,[split(a) for a in ag],color='#1F4E79',lw=2,label=r'exact $1/\sqrt{\cos a}-\frac{\pi/2}{K(\sin(a/2))}$')
ax[0].plot(ag,5/16*ag**2,'--',color='#B23A2E',lw=1.6,label=r'$\frac{5}{16}a^2$ (ordre dominant)')
ax[0].set_xlabel('amplitude $a$ (rad)'); ax[0].set_ylabel(r'$\Delta\Omega/\Omega_0=(\Omega_{\rm horloge}-\Omega_{\rm echelle})/\Omega_0$')
ax[0].set_title("Levee de degenerescence QM-GR"); ax[0].legend(fontsize=9); ax[0].grid(alpha=.3)
# orbite precessante (rosette) dans le plan tangent (x,y)=(th cos ph, th sin ph)
x=th*np.cos(ph); y=th*np.sin(ph)
ax[1].plot(x,y,color='#2E7D32',lw=0.7)
ax[1].plot(0,0,'k+'); ax[1].set_aspect('equal'); ax[1].set_title("Orbite precessante (pendule spherique)")
ax[1].set_xlabel(r'$\theta\cos\varphi$'); ax[1].set_ylabel(r'$\theta\sin\varphi$')
plt.tight_layout(); plt.savefig('fig_levee.png',dpi=130); print("fig_levee.png ecrite")
