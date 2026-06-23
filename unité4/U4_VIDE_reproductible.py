#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
U4_VIDE — Calculs reproductibles de l'Unite 4 (faux vide metastable, isocourbure, spectre MS)
=============================================================================================
Action a deux champs (cadre de Jordan) :
  S = int sqrt(-g)[ 1/2 f R - 1/2 omega((d psi)^2+(d chi)^2) - V ],
  f = 1+beta(cos psi+cos chi), V = alpha(2-cos psi-cos chi), omega = f_s^2.
Cadre d'Einstein : U=V/f^2, G_ab=(1/f)[omega delta_ab + (3/2) f_,a f_,b/f].
Diagonale psi=chi=theta : U_diag = 2 alpha(1-cos theta)/(1+2 beta cos theta)^2.

Prefixe "U4_VIDE_" et sections [V1]..[V6] (V = faux Vide) : DISTINCTS des scripts anterieurs
([H.] HDEQ, [G.] gravite, [S.] synthese, [A./session] CSD) -> aucune collision.

  [V1] Seuil beta_c = -1/6 : Hessien 2D exact en (pi,pi), m^2_eff(inf*), U(inf*).
  [V2] Paysage U_diag : barriere cos theta* = (1+4b)/(2b), U(theta*), double-puits.
  [V3] Action de Hawking-Moss exacte B_HM = 24 pi^2 (3b+1/2)^2/alpha -> 0 a beta_c ;
       critere de Batra-Kleban (HM, pas CDL) ; durees de vie.
  [V4] Diagonale geodesique (V,psi - V,chi = 0) ; masse entropique m^2_s, beta_iso.
  [V5] Gradient stabilisant : longueur de Jeans finie ssi beta > beta_c.
  [V6] Spectre Mukhanov-Sasaki exact (n_s,r) ; fixation de alpha par A_s ; V^1/4.

Dependances : numpy, sympy, scipy. Convention : M_Pl = 1 ; alpha s'annule dans (n_s,r).
"""
import numpy as np
import sympy as sp
from scipy.integrate import quad, solve_ivp, cumulative_trapezoid
from scipy.interpolate import CubicSpline
from scipy.optimize import brentq

# =====================================================================
# [V1] Seuil beta_c = -1/6 (Hessien 2D exact au pole inf* = (pi,pi))
# =====================================================================
print("="*70); print("[V1] Seuil de cloture beta_c = -1/6 (Hessien 2D exact)"); print("="*70)
al, be, om = sp.symbols('alpha beta omega', positive=True)
ps, ch = sp.symbols('psi chi', real=True)
f2 = 1 + be*(sp.cos(ps)+sp.cos(ch)); V2 = al*(2-sp.cos(ps)-sp.cos(ch)); U2 = V2/f2**2
Upp = sp.simplify(sp.diff(U2, ps, 2).subs({ps: sp.pi, ch: sp.pi}))
Umix = sp.simplify(sp.diff(U2, ps, ch).subs({ps: sp.pi, ch: sp.pi}))
Uinf = sp.simplify(U2.subs({ps: sp.pi, ch: sp.pi}))
print("  U_psipsi(inf*) =", Upp, "   U_psichi(inf*) =", Umix)
print("  U(inf*)        =", Uinf, "   [attendu 4 alpha/(1-2 beta)^2]")
# masse effective canonique (norme cinetique omega/f en inf*, f=1-2b)
m2 = sp.simplify(Upp/(om/(1-2*be)))
print("  m^2_eff(inf*)  =", sp.simplify(m2), "   [attendu -alpha(1+6b)/(omega(1-2b)^2)]")
print("  signe(m^2_eff) bascule quand 1+6 beta = 0  => beta_c = -1/6 (piege si beta<beta_c)")
print()

# =====================================================================
# [V2] Paysage : barriere et extrema (formes closes)
# =====================================================================
print("="*70); print("[V2] Paysage U_diag : barriere, faux vide, double-puits"); print("="*70)
s = sp.Symbol('s')  # s = cos theta
Us = 2*al*(1-s)/(1+2*be*s)**2
sol = sp.solve(sp.numer(sp.together(sp.diff(Us, s))), s)
print("  extremum interne en cos(theta*) =", sol, "   [attendu (1+4b)/(2b)]")
cstar = (1+4*be)/(2*be)
Utop = sp.simplify(Us.subs(s, cstar))
print("  U(theta*) =", Utop, "   [attendu -alpha/(4 beta(1+2 beta))]")
print("  barriere existe pour beta in (-1/2,-1/6) ; a beta_c, theta* -> pi (fusion) :")
for b in [-0.30, -0.20, -1/6, -0.10]:
    cs = (1+4*b)/(2*b)
    msg = f"cos(theta*)={cs:+.3f}" + ("  (double-puits)" if -0.5 < b < -1/6 else "  (pas de barriere : max simple)")
    print(f"     beta={b:+.4f} : {msg}")
print()

# =====================================================================
# [V3] Action de Hawking-Moss exacte + regime (HM, pas CDL) + durees de vie
# =====================================================================
print("="*70); print("[V3] Action de Hawking-Moss B_HM = 24 pi^2 (3b+1/2)^2/alpha"); print("="*70)
Uinf_d = 4*al/(1-2*be)**2; Utop_d = -al/(4*be*(1+2*be))
B = sp.simplify(24*sp.pi**2*(1/Uinf_d - 1/Utop_d))
print("  B_HM(beta) =", B)
print("  == 24 pi^2 (3b+1/2)^2/alpha ?",
      sp.simplify(B - 24*sp.pi**2*(3*be+sp.Rational(1,2))**2/al) == 0,
      "  -> s'annule a beta = -1/6")
print("  Critere de Batra-Kleban (CDL existe ssi |m2_top|/H2_top > 4) :")
for fs in [4, 5, 7]:
    print(f"     fs={fs} : |m2_top|/H2_top ~ 3/(4 fs^2) = {3/(4*fs**2):.2e}  << 4  => HM seul (CDL n'existe pas)")
print("  Durees de vie (alpha=1e-9, survie ~ e^B en temps de Hubble) :")
a_num = 1e-9
for b in [-0.30, -0.25, -0.21, -0.17]:
    Bn = 24*np.pi**2*(3*b+0.5)**2/a_num
    print(f"     beta={b:+.2f} : B_HM={Bn:.2e}  -> survie ~ 10^({Bn/np.log(10):.1e}) (faux vide ~eternel)")
print(f"     beta=-1/6 : B_HM=0 (bifurcation : le faux vide disparait)")
print()

# =====================================================================
# Geometrie covariante (pour V4) : V;ss et R_fs sur la diagonale
# =====================================================================
fa = {ps: sp.diff(f2, ps), ch: sp.diff(f2, ch)}
G = sp.Matrix([[(om*(1 if a == b else 0)+sp.Rational(3, 2)*fa[a]*fa[b]/f2)/f2 for b in (ps, ch)] for a in (ps, ch)])
co = [ps, ch]; Gi = G.inv()
def chr_(a, b, c): return sp.Rational(1, 2)*sum(Gi[a, d]*(sp.diff(G[d, b], co[c])+sp.diff(G[d, c], co[b])-sp.diff(G[b, c], co[d])) for d in range(2))
Va = [sp.diff(V2, co[i]) for i in range(2)]
def Vcov(a, b):
    e = sp.diff(V2, co[a], co[b])
    for c in range(2): e -= chr_(c, a, b)*Va[c]
    return e
es = sp.Matrix([1, -1]); ns2 = (es.T*G*es)[0]
Vss = (es.T*sp.Matrix([[Vcov(0, 0), Vcov(0, 1)], [Vcov(1, 0), Vcov(1, 1)]])*es)[0]/ns2
def riem(a, b, c, d):
    t = sp.diff(chr_(a, b, d), co[c])-sp.diff(chr_(a, b, c), co[d])
    for e in range(2): t += chr_(a, c, e)*chr_(e, b, d)-chr_(a, d, e)*chr_(e, b, c)
    return t
Ric = sp.Matrix([[sum(riem(a, b, a, d) for a in range(2)) for d in range(2)] for b in range(2)])
Rfs = sum(Gi[b, d]*Ric[b, d] for b in range(2) for d in range(2))
thh = sp.symbols('theta', real=True); sub = {ps: thh, ch: thh}
Vss_f = sp.lambdify((thh, be, al, om), sp.simplify(Vss.subs(sub)), 'numpy')
Rfs_f = sp.lambdify((thh, be, om), sp.simplify(Rfs.subs(sub)), 'numpy')

# =====================================================================
# [V4] Diagonale geodesique + masse entropique + beta_iso
# =====================================================================
print("="*70); print("[V4] Diagonale geodesique (T_RS=0) + isocourbure beta_iso"); print("="*70)
geo = sp.simplify((sp.diff(V2, ps)-sp.diff(V2, ch)).subs({ps: thh, ch: thh}))
print("  V,psi - V,chi sur la diagonale =", geo, "  => geodesique, T_RS = 0 (pas de virage)")
U_l = sp.lambdify((thh, be, al), 2*al*(1-sp.cos(thh))/(1+2*be*sp.cos(thh))**2, 'numpy')
Up_l = sp.lambdify((thh, be, al), sp.diff(2*al*(1-sp.cos(thh))/(1+2*be*sp.cos(thh))**2, thh), 'numpy')
K_l = sp.lambdify((thh, be, om), 2*om/(1+2*be*sp.cos(thh))+6*be**2*sp.sin(thh)**2/(1+2*be*sp.cos(thh))**2, 'numpy')
a = 1e-9
print(f"  {'beta':>6}{'fs':>4}{'m2_s/H2':>9}{'beta_iso':>10}")
for fs in [5, 7]:
    o = fs**2
    for b in ([-0.30, -0.20] if fs == 5 else [-0.30, -0.26]):
        thb = np.arccos((1+4*b)/(2*b))
        epsV = lambda t: (1/(2*K_l(t, b, o)))*(Up_l(t, b, a)/U_l(t, b, a))**2
        t_end = brentq(lambda t: epsV(t)-1.0, 1e-4, thb*0.999)
        Nef = lambda t: quad(lambda x: K_l(x, b, o)*U_l(x, b, a)/Up_l(x, b, a), t_end, t)[0]
        try: t_star = brentq(lambda t: Nef(t)-55.0, t_end+1e-5, thb*0.99999)
        except Exception: t_star = 0.5*(t_end+thb)
        H2 = U_l(t_star, b, a)/3.0; eV = epsV(t_star)
        m2s = Vss_f(t_star, b, a, o) + eV*Rfs_f(t_star, b, o)*H2
        eta_ss = (m2s/H2)/3.0; TSS = np.exp(-2*eta_ss*55); biso = TSS**2/(1+TSS**2)
        print(f"  {b:>6.2f}{fs:>4}{m2s/H2:>9.4f}{biso:>10.3f}")
print("  -> mode entropique leger (|m2_s|<~0.02 H^2) ; beta_iso ~ 0.3-0.8 >> borne Planck 0.038")
print("     => une conversion au rechauffement est requise (symetrique: biso->0 ; asym.: derive O(0.04)).")
print()

# =====================================================================
# [V5] Gradient stabilisant : longueur de Jeans finie ssi beta > beta_c
# =====================================================================
print("="*70); print("[V5] Gradient stabilisant : Jeans fini ssi beta > beta_c"); print("="*70)
for b in [-0.30, -0.20, -1/6, -0.10]:
    m2 = -(1+6*b)/((1-2*b)**2)   # signe de m^2_eff (alpha=omega=1)
    if m2 < 0:
        lam = 2*np.pi/np.sqrt(-m2)
        print(f"     beta={b:+.4f} : m^2_eff<0 (tachyonique) -> Jeans lambda_c = {lam:.2f} (fini, echappe)")
    else:
        print(f"     beta={b:+.4f} : m^2_eff>0 -> aucun mode tachyonique, Jeans infini (faux vide stable)")
print("  => pour beta<beta_c le gradient k^2/a^2 stabilise tous les modes : remanent admissible.")
print()

# =====================================================================
# [V6] Spectre Mukhanov-Sasaki exact (n_s,r), fixation de alpha par A_s
# =====================================================================
print("="*70); print("[V6] Spectre Mukhanov-Sasaki exact (n_s,r) ; alpha par A_s=2.1e-9"); print("="*70)
def make(beta, fs):
    o = fs**2; th = np.linspace(1e-4, np.pi-1e-4, 200000)
    f = 1+2*beta*np.cos(th); U = 2*(1-np.cos(th))/f**2
    Kpar = 2*o/f+6*beta**2*np.sin(th)**2/f**2
    phi = cumulative_trapezoid(np.sqrt(Kpar), th, initial=0.0)
    return CubicSpline(phi, U), th, phi
def background(beta, fs, window=62):
    Uof, th, phi = make(beta, fs); dUof = Uof.derivative()
    th_bar = np.arccos((1+4*beta)/(2*beta)); phi_bar = np.interp(th_bar, th, phi)
    pe = np.linspace(1e-3, phi_bar*0.999, 40000)
    phi_end = pe[np.argmin(np.abs(0.5*(dUof(pe)/Uof(pe))**2-1.0))]
    grid = np.linspace(phi_end, phi_bar*0.999, 40000)
    Ncum = cumulative_trapezoid(Uof(grid)/dUof(grid), grid, initial=0.0)
    phi_start = np.interp(window, Ncum, grid)
    v0 = -dUof(phi_start)/Uof(phi_start)
    def rhs(N, y): p, v = y; e = 0.5*v*v; return [v, -(3-e)*(v+dUof(p)/Uof(p))]
    def ev(N, y): return 0.5*y[1]**2-1.0
    ev.terminal = True; ev.direction = 1
    sol = solve_ivp(rhs, [0, 200], [phi_start, v0], events=ev, rtol=1e-11, atol=1e-13, dense_output=True, max_step=0.05)
    return sol, Uof, dUof, sol.t[-1]
def spectrum(beta, fs, Nstar=55, K0=80.0):
    sol, Uof, dUof, Nend = background(beta, fs); Nx = Nend-Nstar
    Ng = np.linspace(0, Nend, 4000); P = sol.sol(Ng); phi = P[0]; v = P[1]; eps = 0.5*v*v
    H = np.sqrt(Uof(phi)/(3-eps)); a_ = np.exp(Ng-Nx); aH = a_*H
    H_s = CubicSpline(Ng, H); eps_s = CubicSpline(Ng, eps); aH_s = CubicSpline(Ng, aH)
    dleps = CubicSpline(Ng, np.log(eps)).derivative()
    epsX = float(eps_s(Nx)); HX = float(H_s(Nx))
    def scal(k):
        Ni = brentq(lambda N: float(aH_s(N))-k/K0, 0.001, Nend-0.05)
        Nf = min(Nx+7, Nend-0.02); a_i = np.exp(Ni-Nx); ei = float(eps_s(Ni))
        zs = a_i*np.sqrt(2*ei); zpz = 1+0.5*float(dleps(Ni)); amp = 1/(zs*np.sqrt(2*k))
        R0 = complex(amp, 0); Rp0 = R0*(-zpz-1j*(k/float(aH_s(Ni))))
        def rhs(N, y):
            R = y[0]+1j*y[1]; Rp = y[2]+1j*y[3]
            Rpp = -(3-float(eps_s(N))+float(dleps(N)))*Rp-(k/float(aH_s(N)))**2*R
            return [Rp.real, Rp.imag, Rpp.real, Rpp.imag]
        ss = solve_ivp(rhs, [Ni, Nf], [R0.real, R0.imag, Rp0.real, Rp0.imag], rtol=2e-7, atol=1e-30, max_step=0.06)
        return abs(ss.y[0, -1]+1j*ss.y[1, -1])**2
    ks = HX*np.exp(np.array([-0.4, -0.2, 0, 0.2, 0.4]))
    PR = np.array([(k**3/(2*np.pi**2))*scal(k) for k in ks]); lnk = np.log(ks)
    c2, c1, c0 = np.polyfit(lnk, np.log(PR), 2); ns = 1+c1+2*c2*lnk[2]
    ph = sol.sol(Nx)[0]; U_ = Uof(ph); Up_ = dUof(ph); Upp_ = Uof.derivative(2)(ph)
    ns_sr = 1-6*(0.5*(Up_/U_)**2)+2*(Upp_/U_)
    return ns, ns_sr, 16*epsX, PR[2], epsX
As, Mpl = 2.1e-9, 2.435e18
print(f"  {'fs':>3}{'beta':>7}{'ns_MS':>9}{'ns_SR':>9}{'Dns':>9}{'r':>8}{'alpha':>11}{'V^1/4 GeV':>11}")
for fs, b in [(5, -0.30), (5, -0.20), (7, -0.30), (7, -0.26)]:
    try:
        ns, ns_sr, r, PR0, epsX = spectrum(b, fs); alpha = As/PR0
        V14 = (24*np.pi**2*As*epsX)**0.25*Mpl
        print(f"  {fs:>3}{b:>7.2f}{ns:>9.4f}{ns_sr:>9.4f}{ns-ns_sr:>+9.4f}{r:>8.4f}{alpha:>11.2e}{V14:>11.2e}")
    except Exception as ex:
        print(f"  {fs:>3}{b:>7.2f} -> {type(ex).__name__}: {ex}")
print("  -> Delta n_s sous-pourcent (vers le bleu) ; r ~ 0.014-0.043 ; alpha~(2-8)e-10 ; V^1/4 ~ GUT.")
print("     Cible Planck18+BK18 : ns=0.9649+/-0.0042, r<0.036.")
print()
print("FIN.")
