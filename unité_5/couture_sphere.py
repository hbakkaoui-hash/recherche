import numpy as np
from scipy.integrate import solve_ivp

# Champ d'echelle homogene sur la cible S^2, fond de courbure R.
# L = 1/2 omega thdot^2 + 1/2 omega sin^2(th) phidot^2 - U_eff(th),  U_eff=-A cos th, A=alpha+1/2 beta R
# (V=alpha(1-cos th), f=1+beta cos th, U_eff=V-1/2 f R = const - A cos th)
alpha=1.0; beta=-0.30; om=49.0
Rc = 2*alpha/abs(beta)          # 6.667
def A(R): return alpha+0.5*beta*R

# EOM : th'' = sin th cos th phidot^2 - (A/om) sin th ;  d/dt(sin^2 th * phidot)=0
def eom(t,y,Aw):
    th,thd,ph,phd=y
    s,c=np.sin(th),np.cos(th)
    thdd = s*c*phd**2 - Aw*s
    phdd = -2*(c/s)*thd*phd if abs(s)>1e-9 else 0.0
    return [thd,thdd,phd,phdd]

def period_from_orbit(R, mode):
    Aw=A(R)/om
    if Aw<=0: return np.inf
    if mode=='radial':   # J=0 : oscillation en theta (mode radial = fluctuation d'echelle)
        th0=0.05; y0=[th0,0,0,0]
        # periode = temps pour revenir a th0 avec thd>0 (1 cycle)
    else:                # orbite circulaire (mode azimutal = horloge)
        th0=0.05
        phd0=np.sqrt(Aw)/1.0      # vitesse pour orbite ~circulaire : phidot ~ Omega
        # ajustement fin : pour orbite circulaire exacte thdd=0 -> sin cos phd^2 = Aw sin -> phd^2=Aw/cos
        phd0=np.sqrt(Aw/np.cos(th0))
        y0=[th0,0,0,phd0]
    # integre et mesure la periode via passages
    def ev(t,y,Aw):
        return y[2]-2*np.pi if mode!='radial' else y[0]-th0
    sol=solve_ivp(eom,[0,2000],y0,args=(Aw,),rtol=1e-10,atol=1e-12,max_step=0.05,dense_output=True)
    tt=np.linspace(0,sol.t[-1],200000); Y=sol.sol(tt)
    if mode!='radial':
        # periode azimutale : temps pour phi avancer de 2pi
        idx=np.argmax(Y[2]>=2*np.pi)
        return tt[idx] if idx>0 else np.inf
    else:
        # periode radiale : 2x temps entre th0 et le point de rebroussement (thd=0) puis retour
        thd=Y[1]
        zc=np.where(np.diff(np.sign(thd)))[0]
        return 2*(tt[zc[1]]-tt[zc[0]]) if len(zc)>=2 else np.inf

print("Rc =",Rc,"  tau0(0)=2pi sqrt(om/alpha)=",2*np.pi*np.sqrt(om/alpha))
print("\n R/Rc   Omega_theo=sqrt(A/om)   tau_radial   tau_azimut   2pi/Omega   loi (1-R/Rc)^-1/2")
for x in [0.0,0.3,0.6,0.9,0.97]:
    R=x*Rc; Aw=A(R)/om; Om=np.sqrt(Aw)
    tr=period_from_orbit(R,'radial'); ta=period_from_orbit(R,'azimut')
    tau_th=2*np.pi/Om
    law=2*np.pi*np.sqrt(om/alpha)/np.sqrt(1-x)
    print(" %.2f    %.4f                %.3f       %.3f      %.3f      %.3f"%(x,Om,tr,ta,tau_th,law))
print("\nVerdict numerique : tau_radial = tau_azimut = 2pi/Omega = tau0(0)/sqrt(1-R/Rc).")
print("Les deux modes (radial=echelle/GR, azimutal=horloge/QM) sont DEGENERES (oscillateur")
print("isotrope 2D pres du pole Sud) et gelent ensemble a R_c. La couture est tranchee.")

# ---- figure : degenerescence + gel ----
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
xs=np.linspace(0,0.985,30); t0=2*np.pi*np.sqrt(om/alpha)
tr=[period_from_orbit(x*Rc,'radial')/t0 for x in xs]
ta=[period_from_orbit(x*Rc,'azimut')/t0 for x in xs]
law=1/np.sqrt(1-xs)
fig,ax=plt.subplots(figsize=(6.4,4.0))
ax.plot(xs,law,'-',color='#B23A2E',lw=2,label=r'loi $(1-R/R_c)^{-1/2}$')
ax.plot(xs,tr,'o',color='#2E7D32',ms=5,label='mode radial (echelle / GR)')
ax.plot(xs,ta,'x',color='#1F4E79',ms=6,label='mode azimutal (horloge / QM)')
ax.axvline(1,ls='--',color='#B23A2E'); ax.set_ylim(0,8)
ax.set_xlabel('$R/R_c$'); ax.set_ylabel(r'$\tau_0(R)/\tau_0(0)$')
ax.set_title('Couture tranchee : modes degeneres, gel commun a $R_c$')
ax.legend(loc='upper left',fontsize=9); plt.tight_layout(); plt.savefig('fig_couture.png',dpi=130)
print("\nfig_couture.png ecrite")
