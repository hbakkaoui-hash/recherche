#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
U2_GRAV — Calculs reproductibles du papier de gravite (dualite d'echelle, mono-axe)
===================================================================================
Modele : S = int sqrt(-g)[ 1/2 f R - 1/2 omega (d psi)^2 - V ],
         f = 1 + beta cos psi,  V = alpha (1 - cos psi),  omega = f_s^2.
Repere d'Einstein : U = V/f^2,  K = omega/f + (3/2)(f'/f)^2,  dphi = sqrt(K) dpsi.

Nom prefixe "U2_GRAV_" et sections codees [G1]..[G5] (G = gravite) pour eviter toute
confusion avec d'autres jeux de scripts ([H.] HDEQ, [A.] dualite compactifiee).

  [G1] Geometrie + positivite : U, K (forme close) ; K>0 <=> f>0 <=> |beta|<1 (mono-axe).
  [G2] Seuil de cloture beta_c = -1/3 : signe de kappa^2 (piege / echappement).
  [G3] Coeur de Sitter : H^2 = 2 alpha/[3(1-beta)], r_H = 1/H, Kretschmann = 24 H^4.
  [G4] Inflation : (n_s, r) a N=55 (roulement lent, metrique K) -> reproduit la Table 2.
  [G5] Topologie : charge N, soliton M_{N=1} = 8 sqrt(omega alpha), demi-soliton 4 sqrt(omega alpha).

Dependances : numpy, sympy, scipy.
"""
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.optimize import brentq

# =====================================================================
# [G1] Geometrie en repere d'Einstein et positivite
# =====================================================================
print("=" * 70); print("[G1] Geometrie (repere d'Einstein) et positivite"); print("=" * 70)
psi, beta, om = sp.symbols('psi beta omega', real=True)
f = 1 + beta*sp.cos(psi)
V = (1 - sp.cos(psi))                      # alpha = 1 (s'annule dans les rapports)
U = V/f**2
K = om/f + sp.Rational(3, 2)*(sp.diff(f, psi)/f)**2
print("  U(psi)/alpha =", U)
print("  K(psi)       =", sp.simplify(K))
# positivite : K>0 <=> f>0 <=> 1+beta cos psi>0 pour tout psi <=> |beta|<1 (mono-axe)
for b in [-0.7, -0.49, 0.0, 0.49, 0.99]:
    fmin = 1 - abs(b)                       # min sur psi de 1+beta cos psi
    print(f"  beta={b:+.2f} : min_psi f = {fmin:+.3f}  -> f>0 : {fmin>0}")
print("  => borne correcte du modele MONO-AXE : |beta|<1  (et non beta in (-1/2,1/2)).")
print("     beta=-0.7 (Table 1) est donc admissible.")
print()

# =====================================================================
# [G2] Seuil de cloture beta_c = -1/3
# =====================================================================
print("=" * 70); print("[G2] Seuil de cloture beta_c = -1/3"); print("=" * 70)
# kappa^2 = alpha(1+3beta)/[omega(beta-1)] ; stable (piege) <=> kappa^2<0 <=> beta>-1/3
kap2 = lambda b: (1 + 3*b)/(b - 1)          # signe de kappa^2 (alpha,omega>0)
for b in [-0.7, -0.4, -1/3, -0.3, 0.0, 0.3]:
    etat = "piege (stable)" if kap2(b) < 0 else ("seuil" if abs(b+1/3) < 1e-9 else "echappement")
    print(f"  beta={b:+.4f} : kappa^2 ~ {kap2(b):+.4f}  -> {etat}")
root = brentq(lambda b: 1 + 3*b, -0.9, 0.9)
print(f"  racine (1+3beta)=0 : beta_c = {root:.6f}  (= -1/3)")
print()

# =====================================================================
# [G3] Coeur de Sitter
# =====================================================================
print("=" * 70); print("[G3] Coeur de Sitter (pole infini*)"); print("=" * 70)
alpha_val = 1e-4
for b in [-0.3, -0.7]:
    H2 = 2*alpha_val/(3*(1 - b))
    H = np.sqrt(H2); rH = 1/H
    rH_theo = np.sqrt(3*(1 - b)/(2*alpha_val))
    Kret = 24*H2**2
    print(f"  beta={b:+.2f} : H^2={H2:.3e}, r_H=1/H={rH:.3f}, "
          f"sqrt(3(1-b)/2a)={rH_theo:.3f} (ratio {rH/rH_theo:.4f}), Kretschmann=24H^4={Kret:.3e}")
print()

# =====================================================================
# [G4] Inflation : (n_s, r) a N=55  (reproduit la Table 2)
# =====================================================================
print("=" * 70); print("[G4] Inflation : (n_s, r) a N=55  vs Table 2"); print("=" * 70)
b1, om1 = sp.symbols('b1 om1', real=True)
f1 = 1 + b1*sp.cos(psi); U1 = (1 - sp.cos(psi))/f1**2
K1 = om1/f1 + sp.Rational(3, 2)*(sp.diff(f1, psi)/f1)**2
ld = lambda e: sp.lambdify((psi, b1, om1), e, 'numpy')
Uf, Upf, Uppf = ld(U1), ld(sp.diff(U1, psi)), ld(sp.diff(U1, psi, 2))
Kf, Kpf = ld(K1), ld(sp.diff(K1, psi))


def obs(b, fs, N=55):
    w = fs**2
    eps = lambda t: Upf(t, b, w)**2/(2*Kf(t, b, w)*Uf(t, b, w)**2)
    eta = lambda t: (Uppf(t, b, w)/Kf(t, b, w)
                     - Upf(t, b, w)*Kpf(t, b, w)/(2*Kf(t, b, w)**2))/Uf(t, b, w)
    dN = lambda t: Uf(t, b, w)*Kf(t, b, w)/Upf(t, b, w)
    ts = np.linspace(1e-3, np.pi - 1e-3, 4000)
    ev = np.array([eps(t) for t in ts])
    cr = [i for i in range(len(ts)-1) if (ev[i]-1)*(ev[i+1]-1) < 0]
    te = brentq(lambda t: eps(t)-1, ts[cr[0]], ts[cr[0]+1])
    tstar = brentq(lambda x: quad(dN, te, x, limit=200)[0]-N, te+1e-4, np.pi-1e-3)
    e, h = eps(tstar), eta(tstar)
    return 1 - 6*e + 2*h, 16*e

table2 = [(0.0, 7, 0.960, 0.078), (0.3, 7, 0.949, 0.128), (0.6, 7, 0.930, 0.193),
          (-0.3, 5, 0.958, 0.017), (-0.3, 7, 0.960, 0.036)]
print(f"  {'beta':>6}{'f_s':>5}{'n_s(calc)':>11}{'r(calc)':>10}{'n_s(Tab2)':>11}{'r(Tab2)':>9}")
for b, fs, ns_t, r_t in table2:
    ns, r = obs(b, fs)
    print(f"  {b:>6.2f}{fs:>5}{ns:>11.3f}{r:>10.3f}{ns_t:>11.3f}{r_t:>9.3f}")
# fixation de alpha par A_s et running (cas central beta=-0.3, fs=7)
b, fs, w = -0.3, 7, 49.0
eps = lambda t: Upf(t, b, w)**2/(2*Kf(t, b, w)*Uf(t, b, w)**2)
dN = lambda t: Uf(t, b, w)*Kf(t, b, w)/Upf(t, b, w)
ts = np.linspace(1e-3, np.pi-1e-3, 4000); ev = np.array([eps(t) for t in ts])
cr = [i for i in range(len(ts)-1) if (ev[i]-1)*(ev[i+1]-1) < 0]
te = brentq(lambda t: eps(t)-1, ts[cr[0]], ts[cr[0]+1])
tstar = brentq(lambda x: quad(dN, te, x, limit=200)[0]-55, te+1e-4, np.pi-1e-3)
As, Mpl = 2.1e-9, 2.435e18
alpha = As*24*np.pi**2*eps(tstar)/Uf(tstar, b, w)
V14 = alpha**0.25*Mpl
print(f"  alpha fixe par A_s : alpha = {alpha:.2e} M_Pl^4,  V^1/4 = {V14:.2e} GeV (echelle GUT)")
print()

# =====================================================================
# [G5] Charge topologique et masse du soliton
# =====================================================================
print("=" * 70); print("[G5] Topologie : charge, soliton, demi-soliton"); print("=" * 70)
# borne de Bogomol'nyi : M_{N=1} = 2 sqrt(omega alpha) * int_0^{2pi} |sin(psi/2)| dpsi
I = quad(lambda x: abs(np.sin(x/2)), 0, 2*np.pi)[0]
print(f"  int_0^2pi |sin(psi/2)| dpsi = {I:.4f}  (exact = 4)")
print(f"  => M_{{N=1}} = 2 sqrt(omega alpha) * {I:.0f} = 8 sqrt(omega alpha)   (soliton entier)")
Ih = quad(lambda x: abs(np.sin(x/2)), 0, np.pi)[0]
print(f"  demi-soliton (psi: -pi->0) : energie = 2 sqrt(omega alpha) * {Ih:.0f} = "
      f"4 sqrt(omega alpha)  (N=1/2, non protege)")
# charge N = (1/2pi)(psi_f - psi_i)
for (pi_, pf_) in [(-np.pi, 0.0), (0.0, 2*np.pi)]:
    print(f"  psi: {pi_:+.3f} -> {pf_:+.3f} : N = {(pf_-pi_)/(2*np.pi):.3f}")
print()
print("FIN.")
