import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d

# Branche roulante statique, repere d'Einstein. Modele meridien (= Unite 2).
beta=-0.30; om=49.0; alpha=1.0
def f(t):  return 1+beta*np.cos(t)
def fp(t): return -beta*np.sin(t)
def U(t):  return alpha*(1-np.cos(t))/f(t)**2
def Ut(t): return (alpha*np.sin(t)*f(t)**2 - alpha*(1-np.cos(t))*2*f(t)*fp(t))/f(t)**4
def K(t):  return om/f(t)+1.5*(fp(t)/f(t))**2

# champ canonique phi(theta)=int sqrt(K) dtheta ; on tabule U(phi), U'(phi)
tg=np.linspace(1e-4,np.pi-1e-4,6000)
phig=np.concatenate([[0],np.cumsum(np.sqrt(K(tg))[1:]*np.diff(tg))])
phi_of_t=interp1d(tg,phig); t_of_phi=interp1d(phig,tg,bounds_error=False,fill_value=(tg[0],tg[-1]))
def Uphi(phi):
    t=float(t_of_phi(phi)); return U(t)
def Upphi(phi):
    t=float(t_of_phi(phi)); return Ut(t)/np.sqrt(K(t))   # U'(phi)=U_theta/sqrt(K)

# Equations statiques (G=T, 8piG=1): variables y=[m, Phi, phi, dphi]
def rhs(r,y):
    m,Phi,phi,dphi=y
    e2L=1.0/(1-2*m/r)
    rho=0.5*dphi**2/e2L + Uphi(phi)
    pr =0.5*dphi**2/e2L - Uphi(phi)
    mp = 0.5*r**2*rho
    Php= e2L*(m/r**2 + 0.5*r*pr)
    Lp = (mp/r - m/r**2)/(1-2*m/r)     # Lambda' from m
    ddphi = e2L*Upphi(phi) - (Php-Lp+2/r)*dphi
    return [mp,Php,ddphi if False else dphi, ddphi]
# fix ordering: y=[m,Phi,phi,dphi]; dy=[m',Phi',phi',dphi']
def rhs(r,y):
    m,Phi,phi,dphi=y
    if 1-2*m/r<=1e-9: return [0,0,0,0]
    e2L=1.0/(1-2*m/r)
    rho=0.5*dphi**2/e2L + Uphi(phi)
    pr =0.5*dphi**2/e2L - Uphi(phi)
    mp = 0.5*r**2*rho
    Php= e2L*(m/r**2 + 0.5*r*pr)
    Lp = e2L*(0.5*r*rho - m/r**2)       # Lambda' = e2L(m/r^2)' ... use direct: from e^{-2L}=1-2m/r
    Lp = (m/r**2 - mp/r)*e2L
    ddphi = e2L*Upphi(phi) - (Php-Lp+2/r)*dphi
    return [mp,Php,dphi,ddphi]

# Centre regulier en theta_c (zone roulante), phi'(0)=0, m(0)=0
for tc in [1.6, 2.0, 2.4]:
    phic=float(phi_of_t(tc)); ddphic=Upphi(phic)/3.0
    r0=1e-3
    y0=[ (1.0/6)*r0**3*(Uphi(phic)) , 0.0, phic+0.5*ddphic*r0**2, ddphic*r0 ]
    def horizon(r,y): return (1-2*y[0]/r)-1e-6
    horizon.terminal=True; horizon.direction=-1
    sol=solve_ivp(rhs,[r0,2000],y0,events=horizon,rtol=1e-9,atol=1e-12,max_step=0.5,dense_output=True)
    rr=sol.t; m=sol.y[0]; phi=sol.y[2]; dphi=sol.y[3]
    th=np.array([float(t_of_phi(p)) for p in phi])
    e2L=1.0/(1-2*m/rr)
    # Ricci scalaire R = (dphi)^2 + 4U  (e^{-2L} dphi^2 + 4U) ; et 2m/r
    grad2=dphi**2/e2L
    Rscal=grad2+4*np.array([Uphi(p) for p in phi])
    twoM=2*m/rr
    print("theta_c=%.2f : arret r=%.3f  2m/r_max=%.4f  e^{2Lambda}_max=%.2e  theta(fin)=%.3f (Sud=0)"
          %(tc, rr[-1], twoM.max(), e2L.max(), th[-1]))
    if sol.t_events[0].size: print("           -> surface 2m/r->1 atteinte a r=%.3f : horizon"%sol.t_events[0][0])
print("\nLecture: le champ partant de la zone roulante n'atteint PAS le pole Sud (theta->0) en restant")
print("regulier ; la geometrie rencontre 2m/r->1 a r fini (horizon) avec gradient non nul -> pas de")
print("coeur de Sitter regulier interpolant. Conforme a Unite 2 (branche roulante singuliere).")
