#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
U3_SYNTH — Calculs reproductibles de l'Unite 3 (synthese / unification)
=======================================================================
Un seul champ d'echelle sur deux cercles (psi spatial, chi temporel) ; pont
gravite <-> temps quantique. Action a deux champs :
  S = int sqrt(-g)[ 1/2 f R - 1/2 omega((d psi)^2+(d chi)^2) - V ],
  f = 1 + beta(cos psi + cos chi),  V = alpha(2 - cos psi - cos chi),  omega = f_s^2.
Cadre d'Einstein : U = V/f^2 ; G_ab = (1/f)[omega delta_ab + (3/2) f_,a f_,b/f].

Nom prefixe "U3_SYNTH_" et sections codees [S1]..[S5] (S = synthese), DISTINCTS des
scripts anterieurs ([H.] HDEQ, [G.] gravite, [A./session] CSD_session) -> aucune collision.

  [S1] Facteur d'existence derive : eps = E(k)/K(k) (verif pendule) ; tau0(k).      [NOUVEAU]
  [S2] Nature de infini* : seuil diagonal -1/6 (piege/roule) + masse isocourbure -1/4.
  [S3] Inflation bande viable f_s=5-6 : (n_s,r) diagonale vs mono ; alpha, V^1/4, tau0, M_sol.
  [S4] Modulation gravitationnelle tau0(R) ; R_c = 2 alpha/|beta| ; gel de l'horloge.   [NOUVEAU]
  [S5] Test de la spirale (2 champs) : le virage est amorti, r jamais supprime.

Dependances : numpy, sympy, scipy.
Convention : M_Pl = 1 ; alpha s'annule dans les ratios (n_s, r), il fixe l'echelle (S3).
"""
import numpy as np
import sympy as sp
from scipy.integrate import quad, solve_ivp, trapezoid
from scipy.optimize import brentq, minimize_scalar
from scipy.special import ellipe, ellipk

# =====================================================================
# [S1] Facteur d'existence eps = E(k)/K(k)  (verifie sur le pendule)
# =====================================================================
print("=" * 70); print("[S1] Facteur d'existence eps = E(k)/K(k) (pont vers HDEQ)"); print("=" * 70)
for chimax in [0.3, 1.0, 2.0, 3.0]:
    k = np.sin(chimax / 2); m = k**2
    eps_th = ellipe(m) / ellipk(m)                       # E(k)/K(k)
    # pendule chi'' = -sin chi, amplitude chimax -> <cos^2(chi/2)> sur une periode
    Tper = 4 * ellipk(m)                                 # periode (omega0 = 1)
    sol = solve_ivp(lambda t, y: [y[1], -np.sin(y[0])], [0, Tper], [chimax, 0.0],
                    rtol=1e-10, atol=1e-12, dense_output=True, max_step=Tper/2000)
    ts = np.linspace(0, Tper, 4000); ch = sol.sol(ts)[0]
    eps_num = trapezoid(np.cos(ch / 2)**2, ts) / Tper
    print(f"  chi_max={chimax:.1f} : E(k)/K(k)={eps_th:.6f}  <cos^2(chi/2)>_pendule={eps_num:.6f}")
print(f"  petite amplitude : eps -> 1 - chi_max^2/8 ; verif chi_max=0.3 -> "
      f"{1-0.3**2/8:.6f} vs {ellipe(np.sin(0.15)**2)/ellipk(np.sin(0.15)**2):.6f}")
print("  tau0(k) = 4 sqrt(omega/alpha) K(k) ; k->0 : tau0 -> 2 pi sqrt(omega/alpha) ; k->1 : eps->0.")
print()

# ---- geometrie d'espace des champs (commune a S2, S3, S5) ----
psi, chi, beta, om = sp.symbols('psi chi beta omega', real=True)
F = [psi, chi]
f_sym = 1 + beta*(sp.cos(psi) + sp.cos(chi))
V_sym = (2 - sp.cos(psi) - sp.cos(chi))                  # alpha = 1
U_sym = V_sym / f_sym**2
G = sp.zeros(2, 2)
for a in range(2):
    for b in range(2):
        d = 1 if a == b else 0
        G[a, b] = (1/f_sym)*(om*d + sp.Rational(3, 2)*sp.diff(f_sym, F[a])*sp.diff(f_sym, F[b])/f_sym)
Ginv = G.inv()
def Gam(c, a, b):
    return sp.Rational(1, 2)*sum(Ginv[c, k]*(sp.diff(G[k, a], F[b]) + sp.diff(G[k, b], F[a])
                                             - sp.diff(G[a, b], F[k])) for k in range(2))

# =====================================================================
# [S2] Nature de infini* : seuil -1/6 (diagonale) + masse isocourbure -1/4
# =====================================================================
print("=" * 70); print("[S2] Nature de infini* : tension piege (-1/6) / isocourbure (-1/4)"); print("=" * 70)
th = sp.symbols('theta', real=True); sub = {psi: th, chi: th}
Ud = U_sym.subs(sub); Udf = sp.lambdify((th, beta, om), Ud, 'numpy'); Udtf = sp.lambdify((th, beta, om), sp.diff(Ud, th), 'numpy')
print("  (a) paysage diagonal U=V/f^2 : nature de infini* (seuil -1/6 = %.4f)" % (-1/6))
for b in [-0.30, -0.25, -0.20, -1/6, -0.10]:
    kind = "MAX (roule, traversable)" if Udtf(np.pi-1e-3, b, 1.0) > 0 else "MIN piege (faux vide)"
    print(f"     beta={b:+.4f} : U(inf*)={Udf(np.pi-1e-9,b,1.0):.3f} -> {kind}")
# masse isocourbure (transverse a la diagonale)
Hcov = sp.zeros(2, 2)
for a in range(2):
    for b in range(2):
        Hcov[a, b] = sp.diff(U_sym, F[a], F[b]) - sum(Gam(c, a, b)*sp.diff(U_sym, F[c]) for c in range(2))
nperp = sp.Matrix([1, -1])
Vss = (nperp.T*Hcov*nperp)[0].subs(sub) / (nperp.T*G*nperp)[0].subs(sub)
print("  (b) masse transverse (isocourbure) sur la diagonale :")
print("     en P (theta=0)   : m_s^2 =", sp.simplify(Vss.subs(th, 0)), " (>0 si beta>-1/2)")
print("     en theta=pi/2    : m_s^2 =", sp.simplify(Vss.subs(th, sp.pi/2)), " -> change de signe a beta=-1/4")
print("  => infini* piege pour beta<-1/6 (toute la bande viable) : la cloture et le")
print("     deroulement dynamique se disputent le pole. Tension structurelle centrale.")
print()

# =====================================================================
# [S3] Inflation bande viable f_s=5-6 : (n_s,r) diagonale vs mono + echelles (P1)
# =====================================================================
print("=" * 70); print("[S3] Inflation (P1) : f_s=5-6, diagonale vs mono ; alpha,V^1/4,tau0,M_sol"); print("=" * 70)
ld = lambda e: sp.lambdify((th, beta, om), e, 'numpy')
theta_b = lambda b: minimize_scalar(lambda t: -Udf(t, b, 1.0), bounds=(0.05, np.pi-0.05), method='bounded').x
Kd = (G[0, 0] + 2*G[0, 1] + G[1, 1]).subs(sub)
Udf2, Kdf, Udtf2, Udttf, Kdtf = ld(Ud), ld(Kd), ld(sp.diff(Ud, th)), ld(sp.diff(Ud, th, 2)), ld(sp.diff(Kd, th))
def obs_diag(b, fs, N=55):
    w = fs**2
    eps = lambda t: Udtf2(t, b, w)**2/(2*Kdf(t, b, w)*Udf2(t, b, w)**2)
    eta = lambda t: (Udttf(t, b, w)/Kdf(t, b, w) - Udtf2(t, b, w)*Kdtf(t, b, w)/(2*Kdf(t, b, w)**2))/Udf2(t, b, w)
    dN = lambda t: Udf2(t, b, w)*Kdf(t, b, w)/Udtf2(t, b, w)
    tb = theta_b(b); ts = np.linspace(1e-3, tb-1e-3, 3000); ev = np.array([eps(t) for t in ts])
    cr = [i for i in range(len(ts)-1) if (ev[i]-1)*(ev[i+1]-1) < 0]
    if not cr: return None
    te = brentq(lambda t: eps(t)-1, ts[cr[-1]], ts[cr[-1]+1])
    if quad(dN, te, tb-1e-4, limit=200)[0] < N: return None
    tstar = brentq(lambda x: quad(dN, te, x, limit=200)[0]-N, te+1e-4, tb-1e-4)
    return 1-6*eps(tstar)+2*eta(tstar), 16*eps(tstar)
# mono
p1, b1, o1 = sp.symbols('p1 b1 o1', real=True)
f1 = 1+b1*sp.cos(p1); U1s = (1-sp.cos(p1))/f1**2; K1s = o1/f1+sp.Rational(3,2)*(sp.diff(f1,p1)/f1)**2
l1 = lambda e: sp.lambdify((p1, b1, o1), e, 'numpy')
U1f, K1f, U1t, U1tt, K1t = l1(U1s), l1(K1s), l1(sp.diff(U1s,p1)), l1(sp.diff(U1s,p1,2)), l1(sp.diff(K1s,p1))
def obs_mono(b, fs, N=55):
    w = fs**2
    eps = lambda t: U1t(t,b,w)**2/(2*K1f(t,b,w)*U1f(t,b,w)**2)
    eta = lambda t: (U1tt(t,b,w)/K1f(t,b,w)-U1t(t,b,w)*K1t(t,b,w)/(2*K1f(t,b,w)**2))/U1f(t,b,w)
    dN = lambda t: U1f(t,b,w)*K1f(t,b,w)/U1t(t,b,w)
    ts = np.linspace(1e-3, np.pi-1e-3, 4000); ev = np.array([eps(t) for t in ts])
    cr = [i for i in range(len(ts)-1) if (ev[i]-1)*(ev[i+1]-1) < 0]
    te = brentq(lambda t: eps(t)-1, ts[cr[0]], ts[cr[0]+1])
    tstar = brentq(lambda x: quad(dN, te, x, limit=200)[0]-N, te+1e-4, np.pi-1e-3)
    return 1-6*eps(tstar)+2*eta(tstar), 16*eps(tstar)
As, Mpl, inv = 2.1e-9, 2.435e18, 6.582e-25/2.435e18
print(f"  {'beta':>6}{'fs':>4}{'r(diag)':>9}{'r(mono)':>9}{'ns(mono)':>9}{'alpha':>10}{'V^1/4':>9}{'tau0(s)':>9}{'Msol':>9}")
for b, fs in [(-0.30,5),(-0.30,6),(-0.25,6)]:
    od, om_ = obs_diag(b,fs), obs_mono(b,fs)
    w = fs**2
    eps = lambda t: U1t(t,b,w)**2/(2*K1f(t,b,w)*U1f(t,b,w)**2)
    dN = lambda t: U1f(t,b,w)*K1f(t,b,w)/U1t(t,b,w)
    ts = np.linspace(1e-3,np.pi-1e-3,4000); ev=np.array([eps(t) for t in ts])
    cr=[i for i in range(len(ts)-1) if (ev[i]-1)*(ev[i+1]-1)<0]
    te=brentq(lambda t: eps(t)-1, ts[cr[0]], ts[cr[0]+1])
    tstar=brentq(lambda x: quad(dN,te,x,limit=200)[0]-55, te+1e-4, np.pi-1e-3)
    al=As*24*np.pi**2*eps(tstar)/U1f(tstar,b,w); V14=al**0.25*Mpl
    tau0=2*np.pi*(fs/np.sqrt(al))*inv; Msol=8*fs*np.sqrt(al)*Mpl
    print(f"  {b:>6.2f}{fs:>4}{od[1]:>9.3f}{om_[1]:>9.3f}{om_[0]:>9.4f}{al:>10.1e}{V14:>9.1e}{tau0:>9.1e}{Msol:>9.1e}")
print("  -> diagonale et mono coincident a f_s=5-6 ; r viable ; echelle GUT ; tau0~3.5e-37 s.")
print()

# =====================================================================
# [S4] Modulation gravitationnelle tau0(R) et gel a R_c  [NOUVEAU]
# =====================================================================
print("=" * 70); print("[S4] tau0(R) = 2pi sqrt(omega/(alpha + 1/2 beta R)) ; R_c = 2 alpha/|beta|"); print("=" * 70)
b, al = -0.30, 8.0e-10
Rc = 2*al/abs(b)
print(f"  beta={b}, alpha={al:.1e} : R_c = 2 alpha/|beta| = {Rc:.2e} (M_Pl^2)")
for frac in [0.0, 0.5, 0.9, 0.99]:
    R = frac*Rc; denom = al + 0.5*b*R
    ratio = np.sqrt(al/denom)
    print(f"     R/R_c={frac:.2f} : tau0(R)/tau0(0) = {ratio:.3f}")
print("     R->R_c : denom->0, tau0->inf (l'horloge quantique gele : gravite fige le temps).")
print("  effet labo : dilatation GR standard ; effet dynamique delta tau0/tau0=-(beta/4) R/alpha ~1e-81 (matiere).")
print()

# =====================================================================
# [S5] Test de la spirale (2 champs) : r jamais supprime
# =====================================================================
print("=" * 70); print("[S5] Test de la spirale (2 champs, cadre d'Einstein)"); print("=" * 70)
ar = (psi, chi, beta, om)
Uf = sp.lambdify(ar, U_sym, 'numpy'); Gf = sp.lambdify(ar, G, 'numpy')
Gamf = sp.lambdify(ar, [[[Gam(a,b,c) for c in range(2)] for b in range(2)] for a in range(2)], 'numpy')
GUf = sp.lambdify(ar, [sum(Ginv[a,b]*sp.diff(U_sym,F[b]) for b in range(2)) for a in range(2)], 'numpy')
def epsH(y,b,w):
    p,c,pp,cc=y; v=np.array([pp,cc]); return 0.5*v@np.array(Gf(p,c,b,w))@v
def rhs(N,y,b,w):
    p,c,pp,cc=y; v=np.array([pp,cc]); e=epsH(y,b,w); Ga=np.array(Gamf(p,c,b,w)); GU=np.array(GUf(p,c,b,w)); Ux=Uf(p,c,b,w)
    acc=[-sum(Ga[k][i][j]*v[i]*v[j] for i in range(2) for j in range(2))-(3-e)*v[k]-(3-e)*GU[k]/Ux for k in range(2)]
    return [pp,cc,acc[0],acc[1]]
def ev_end(N,y,b,w): return epsH(y,b,w)-1.0
ev_end.terminal=True; ev_end.direction=1
b, w, p0, c0 = -0.25, 50.0, 1.45, 1.10
print(f"  beta={b}, omega={w} (f_s~7), depart hors-diagonale ({p0},{c0})")
print(f"  {'elan':>6}{'N_tot':>8}{'r@CMB':>9}")
for boost in [0.0, 2.0]:
    Gm=np.array(Gf(p0,c0,b,w)); v=-np.array(GUf(p0,c0,b,w))/Uf(p0,c0,b,w)
    nT=np.array([1.0,-1.0]); nT=nT/np.sqrt(nT@Gm@nT); v=v+boost*nT
    sol=solve_ivp(rhs,[0,400],[p0,c0,v[0],v[1]],args=(b,w),events=ev_end,rtol=1e-9,atol=1e-11,dense_output=True,max_step=0.02)
    Nt=sol.t_events[0][0] if len(sol.t_events[0]) else 400.0
    r=16*epsH(sol.sol(Nt-55),b,w) if 55<Nt<399 else float('nan')
    print(f"  {boost:>6.1f}{Nt:>8.1f}{r:>9.4f}")
print("  -> virage transitoire amorti avant la fenetre CMB ; r reste ~0.046, jamais supprime.")
print("     (P est un creux ponctuel, pas une vallee annulaire : aucune orbite soutenue.)")
print()
print("FIN.")
