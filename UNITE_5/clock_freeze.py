import sympy as sp
# Champ d'horloge chi (axe-temps / azimut). EOM Jordan : omega*Box(chi)=V_chi - 1/2 f_chi R
# V = alpha(2 - cos psi - cos chi)  => V_chi = alpha sin chi
# f = 1 + beta(cos psi + cos chi)   => f_chi = -beta sin chi
# Force = d/dchi U_eff avec U_eff = V - (1/2) f R  (R = scalaire de Ricci, fond)
chi,alpha,beta,R,om = sp.symbols('chi alpha beta R omega', positive=False)
alpha=sp.Symbol('alpha',positive=True); om=sp.Symbol('omega',positive=True)
beta=sp.Symbol('beta',negative=True)   # beta<0 dans la fenetre viable
R=sp.Symbol('R',nonnegative=True)
Ueff = alpha*(2-sp.cos(chi)) - sp.Rational(1,2)*(1+beta*sp.cos(chi))*R   # parties en chi seulement
dU  = sp.diff(Ueff,chi)
d2U = sp.diff(Ueff,chi,2)
print("U_eff'(chi)   =", sp.simplify(dU), "  -> equilibre chi=0")
m2 = sp.simplify(d2U.subs(chi,0)/om)     # masse^2 effective = U''/omega au minimum chi=0
print("m_chi^2(R)    = U''(0)/omega =", m2)
Rc = sp.solve(sp.Eq(d2U.subs(chi,0),0), R)[0]
print("annulation a  R_c =", sp.simplify(Rc), " = 2 alpha/|beta|")
# forme factorisee
m2f = sp.simplify((alpha/om)*(1 - R/(2*alpha/(-beta))))
print("verif m^2 = (alpha/omega)(1-R/R_c) ?", sp.simplify(m2-m2f)==0)

# Periode harmonique tau0(R)=2pi/Omega, Omega=sqrt(m^2)
print("\ntau0(R)/tau0(0) = 1/sqrt(1-R/R_c)   (loi en racine, [preuve])")
print("tau0(0)=2 pi sqrt(omega/alpha)=2 pi f_s/sqrt(alpha)")

# ---- Interlock : courbure du coeur de Sitter vs seuil de gel ----
Lam = 2*alpha/(1-beta)             # G = -Lam g  (branche gelee Nord)
Rcore = 4*Lam                      # scalaire de Ricci de Sitter en 4D : R=4 Lambda
Rc_val= -2*alpha/beta              # 2 alpha/|beta|
print("\nR_core = 4 Lambda_eff =", sp.simplify(Rcore))
print("R_c    =", Rc_val)
bsol = sp.solve(sp.Eq(Rcore,Rc_val),beta)
print("R_core = R_c   <=>   beta =", bsol, "  (= beta_c = -1/3 !)")

# numerique pour la figure
import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
fig,ax=plt.subplots(1,2,figsize=(10,3.6))
x=np.linspace(0,0.999,400)
ax[0].plot(x,1-x,lw=2,color='#2E7D32')
ax[0].axhline(0,color='k',lw=.6); ax[0].axvline(1,ls='--',color='#B23A2E')
ax[0].set_xlabel('$R/R_c$'); ax[0].set_ylabel('$m_\\chi^2 \\,/\\,(\\alpha/\\omega)$')
ax[0].set_title("Masse de l'horloge : $m_\\chi^2=(\\alpha/\\omega)(1-R/R_c)$")
ax[0].text(1.01,0.05,'$R_c=2\\alpha/|\\beta|$',color='#B23A2E',rotation=90,va='bottom')
ax[1].plot(x,1/np.sqrt(1-x),lw=2,color='#1F4E79')
ax[1].axvline(1,ls='--',color='#B23A2E'); ax[1].set_ylim(0,8)
ax[1].set_xlabel('$R/R_c$'); ax[1].set_ylabel('$\\tau_0(R)/\\tau_0(0)$')
ax[1].set_title("Periode : $\\tau_0\\propto(1-R/R_c)^{-1/2}\\to\\infty$")
plt.tight_layout(); plt.savefig('fig_freeze.png',dpi=130)

fig2,ax2=plt.subplots(figsize=(6,3.8))
b=np.linspace(-0.49,-0.10,400); a=1.0
Rcore_n=8*a/(1-b); Rc_n=-2*a/b
ax2.plot(b,Rcore_n,lw=2,color='#2E7D32',label='$R_{core}=8\\alpha/(1-\\beta)$ (coeur dS)')
ax2.plot(b,Rc_n,lw=2,color='#1F4E79',label='$R_c=2\\alpha/|\\beta|$ (gel horloge)')
ax2.axvline(-1/3,ls='--',color='#B23A2E'); ax2.plot(-1/3,8*a/(1+1/3),'o',color='#B23A2E')
ax2.text(-1/3,8*a/(1+1/3)+1.5,'$\\beta_c=-1/3$\n$R_{core}=R_c=6\\alpha$',color='#B23A2E',ha='center')
ax2.set_xlabel('$\\beta$'); ax2.set_ylabel('courbure $/\\alpha$'); ax2.set_ylim(3,12)
ax2.legend(loc='upper left',fontsize=9); ax2.set_title("Interlock : coeur dS rencontre le seuil de gel a $\\beta_c=-1/3$")
plt.tight_layout(); plt.savefig('fig_interlock.png',dpi=130)
print("\nfigures: fig_freeze.png, fig_interlock.png")
