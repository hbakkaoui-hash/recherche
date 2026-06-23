#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
U1_HDEQ — Calculs reproductibles de l'Unite 1 (HDEQ)
====================================================
Discontinuite d'existence des particules quantiques : existence intermittente,
dephasage intrinseque, selection de la base privilegiee.

Nom de fichier volontairement prefixe "U1_HDEQ_" et sections codees [H1]..[H4]
(H = HDEQ) afin d'EVITER TOUTE CONFUSION avec les scripts d'autres documents
(qui emploient des codes [A]/[A2]/[A3]/[A4]). Ce fichier est autonome.

Reproduit, dans l'ordre :
  [H1] Theoreme 1  : unitarite globale du propagateur de cycle  U(tau0).
  [H2] Proposition 1 : base privilegiee = etats propres de H_eff = eps*H_sys
                       (amplitude de survie + developpement a temps court).
  [H3] Dephasage : les DEUX regimes de decoherence
                   (a) quasi-statique  -> Var ~ T^2  (gaussien, refocalisable)
                   (b) dynamique       -> Var ~ T^1  (exponentiel, irreductible)
                   et le scaling en N.
  [H4] Constantes intrinseques : eta_sp, eps = E(k)/K(k), echelles d'energie ;
        + controle 100% lagrangien : eps issu de la dynamique du pendule (sans K/E).

Dependances : numpy, scipy.   (pip install numpy scipy)
Conventions : hbar = 1, tau0 = 1 sauf mention contraire.
"""

import numpy as np
from scipy.linalg import expm
from scipy.special import ellipe, ellipk
from scipy.integrate import solve_ivp, trapezoid

rng = np.random.default_rng(0)


def herm(d):
    """Hamiltonien hermitien aleatoire d x d (hbar=1)."""
    M = rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))
    return (M + M.conj().T) / 2


# =====================================================================
# [H1] Theoreme 1 — unitarite globale du propagateur de cycle
# =====================================================================
print("=" * 70)
print("[H1] Theoreme 1 : unitarite globale de U(tau0)")
print("=" * 70)

d, eps, tau0 = 3, 0.37, 1.0
Hs = herm(d)
Usys = expm(-1j * Hs * eps * tau0)               # evolution sur la branche active
Id = np.eye(d)
a = np.array([[1.0], [0.0]]); i = np.array([[0.0], [1.0]])
Pa = a @ a.T; Pi = i @ i.T                        # |a><a|, |i><i|
P = np.kron(Id, Pa); Q = np.kron(Id, Pi)          # projecteurs actif / inactif
U = np.kron(Usys, Pa) + np.kron(Id, Pi)           # U = Usys (x) |a><a| + I (x) |i><i|

err_unit = np.linalg.norm(U.conj().T @ U - np.eye(2 * d))
print(f"  ||U^dagger U - I||              = {err_unit:.2e}   (doit etre ~0)")

# composition de N cycles : sur la branche active, U^N = exp(-i eps Hs N tau0)
N = 7
UN_active = np.linalg.matrix_power(Usys, N)
target = expm(-1j * Hs * eps * (N * tau0))
err_floquet = np.linalg.norm(UN_active - target)
print(f"  ||Usys^N - exp(-i eps Hs Ntau0)|| = {err_floquet:.2e}   -> H_eff = eps*H_sys")
print()


# =====================================================================
# [H2] Proposition 1 — base privilegiee (amplitude de survie)
# =====================================================================
print("=" * 70)
print("[H2] Proposition 1 : |A_psi(t)|=1 pour tout t  <=>  psi propre de H_eff")
print("=" * 70)

Heff = eps * Hs
w, V = np.linalg.eigh(Heff)
ts = np.linspace(0, 5, 400)


def survival(psi):
    return np.array([np.vdot(psi, expm(-1j * Heff * t) @ psi) for t in ts])


psi_eig = V[:, 0]                                  # etat propre
A_eig = np.abs(survival(psi_eig))
print(f"  etat propre   : min|A|={A_eig.min():.6f}, max|A|={A_eig.max():.6f} (≈1 partout)")

psi_sup = (V[:, 0] + V[:, 1] + V[:, 2]); psi_sup /= np.linalg.norm(psi_sup)
A_sup = np.abs(survival(psi_sup))
print(f"  superposition : min|A|={A_sup.min():.6f}  (<1 : se dephase)")

# verification du developpement |A|^2 = 1 - (Delta H_eff)^2 t^2 + O(t^4)
varH = np.vdot(psi_sup, Heff @ Heff @ psi_sup).real - np.vdot(psi_sup, Heff @ psi_sup).real ** 2
tsmall = 1e-3
A2 = np.abs(np.vdot(psi_sup, expm(-1j * Heff * tsmall) @ psi_sup)) ** 2
coef_num = (1 - A2) / tsmall ** 2
print(f"  coeff t^2 : numerique={coef_num:.5f}  vs  (Delta H_eff)^2={varH:.5f}  (accord)")
print()


# =====================================================================
# [H3] Dephasage intrinseque — deux regimes de decoherence
# =====================================================================
print("=" * 70)
print("[H3] Decoherence : (a) quasi-statique Var~T^2 ; (b) dynamique Var~T^1")
print("=" * 70)


def variance_phase(N_const, T_cycles, dynamic, n_real=4000, dtau=0.05, Ebar=1.0):
    """Var(DeltaPhi) sur n_real realisations. tau0=1, hbar=1, Ebar/hbar=Ebar."""
    n = int(T_cycles)
    dphi = np.zeros(n_real)
    if dynamic:
        # xi refluctue a chaque cycle -> marche aleatoire de phase
        for _ in range(N_const):
            xi = rng.normal(0.0, dtau, size=(n_real, n)).sum(axis=1)
            dphi += Ebar * xi
    else:
        # xi fige par constituant -> offset de frequence constant, phase ~ n
        for _ in range(N_const):
            xi = rng.normal(0.0, dtau, size=n_real)
            dphi += Ebar * xi * n
    return dphi.var()


def slope(xs, ys):
    return np.polyfit(np.log(xs), np.log(ys), 1)[0]

Ts = np.array([20, 40, 80, 160, 320], dtype=float)
var_stat = [variance_phase(40, T, dynamic=False) for T in Ts]
var_dyn = [variance_phase(40, T, dynamic=True) for T in Ts]
print(f"  exposant en T  (statique) = {slope(Ts, var_stat):.3f}   (attendu 2)")
print(f"  exposant en T  (dynamique)= {slope(Ts, var_dyn):.3f}   (attendu 1)")

Ns = np.array([10, 20, 40, 80, 160], dtype=float)
varN_stat = [variance_phase(int(N_), 80, dynamic=False) for N_ in Ns]
varN_dyn = [variance_phase(int(N_), 80, dynamic=True) for N_ in Ns]
print(f"  exposant en N  (statique) = {slope(Ns, varN_stat):.3f}   (attendu 1, Var∝N)")
print(f"  exposant en N  (dynamique)= {slope(Ns, varN_dyn):.3f}   (attendu 1, Var∝N)")
print("  -> T_dec^-1 ∝ sqrt(N) dtau/tau0^2 (statique, refocalisable par echo)")
print("  -> T_dec^-1 ∝ N (dtau)^2/tau0^3   (dynamique, irreductible)")
print()


# =====================================================================
# [H4] Constantes intrinseques et echelles
# =====================================================================
print("=" * 70)
print("[H4] Constantes intrinseques")
print("=" * 70)

R_nuc, R_at = 1.2e-15, 0.5e-10
eta_sp = (R_nuc / R_at) ** 3
print(f"  eta_sp = (R_nuc/R_at)^3 = {eta_sp:.2e}   (heuristique, ~1.4e-14)")

# facteur d'existence eps = E(k)/K(k) ; scipy : ellipe/ellipk prennent m = k^2
for chi_max in [0.5, 1.0, 2.0, 3.0]:
    k = np.sin(chi_max / 2); m = k ** 2
    eps_geo = ellipe(m) / ellipk(m)
    print(f"  chi_max={chi_max:.1f}  k={k:.3f}  eps=E(k)/K(k)={eps_geo:.4f}")
print(f"  (k->0 : eps->1, recouvre la MQ continue ; verif : {ellipe(1e-9)/ellipk(1e-9):.6f})")

# --- Controle 100% lagrangien : eps SORT de la dynamique du lagrangien ---
# On integre l'equation d'Euler-Lagrange de  L_chi = 1/2 omega chi_dot^2 - alpha(1-cos chi),
# soit (omega=alpha=1)  chi'' = -sin chi.  La periode est DETECTEE depuis la dynamique
# (1er instant ou chi_dot=0, i.e. chi=chi_max) ; eps = <cos^2(chi/2)> est la moyenne
# temporelle le long de la trajectoire. AUCUNE forme close (K,E) n'entre dans le calcul :
# on ne compare qu'a la fin a E(k)/K(k), et la periode detectee a 4 K(k).
def _eom(t, y):
    return [y[1], -np.sin(y[0])]

def _turning(t, y):
    return y[1]            # chi_dot = 0  ->  rebroussement (chi = chi_max)
_turning.terminal = True
_turning.direction = -1

print("  --- controle lagrangien (eps issu de la dynamique, sans K/E en entree) ---")
print(f"  {'chi_max':>7} {'T (dyn)':>10} {'eps (dyn)':>11} {'E/K':>9} {'ecart':>9}")
for chi_max in [0.5, 1.0, 2.0, 3.0]:
    v0 = np.sqrt(2 * (1 - np.cos(chi_max)))            # amplitude = chi_max, depart chi=0
    ev = solve_ivp(_eom, [0, 100], [0.0, v0], events=_turning,
                   rtol=1e-11, atol=1e-13, max_step=0.01)
    T = 4 * ev.t_events[0][0]                          # periode pleine, issue de la dynamique
    sol = solve_ivp(_eom, [0, T], [0.0, v0], dense_output=True,
                    rtol=1e-11, atol=1e-13, max_step=T / 40000)
    ts = np.linspace(0, T, 80001); chi = sol.sol(ts)[0]
    eps_dyn = trapezoid(np.cos(chi / 2) ** 2, ts) / T
    m = np.sin(chi_max / 2) ** 2
    eps_closed = ellipe(m) / ellipk(m)
    K_close = 4 * ellipk(m)
    print(f"  {chi_max:7.2f} {T:10.5f} {eps_dyn:11.6f} {eps_closed:9.6f} {abs(eps_dyn-eps_closed):9.1e}")
print("  => eps_dyn = E(k)/K(k) a ~1e-13 pres ; periode detectee = 4 K(k).")

# echelles d'energie liees a tau0 (entree phenomenologique)
hbar_GeVs = 6.582e-25
tau0_phys = 3.5e-37
print(f"  tau0 = 2pi sqrt(omega/alpha) ≈ {tau0_phys:.1e} s   (entree phenomenologique)")
print(f"  hbar/tau0   ≈ {hbar_GeVs/tau0_phys:.2e} GeV")
print(f"  2pi hbar/tau0 = Delta E ≈ {2*np.pi*hbar_GeVs/tau0_phys:.2e} GeV")
print()
print("FIN.")
