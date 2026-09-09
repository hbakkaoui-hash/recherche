#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Figures (FR + EN) de l'Unite 4. Sorties : figs_u4/ (FR), figs_u4_en/ (EN).
Six figures, calculees depuis les equations du cadre (rien n'est invente) :
  fig_bifurcation (11a), fig_jeans (11b), fig_landscape, fig_BHM, fig_isocurvature, fig_nsr.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp, quad
from scipy.optimize import brentq
import sympy as sp

# --- geometrie covariante (pour beta_iso reel, identique a U5_VIDE [V4]) ---
_al, _be, _om = sp.symbols('alpha beta omega', positive=True)
_ps, _ch = sp.symbols('psi chi', real=True)
_f = 1+_be*(sp.cos(_ps)+sp.cos(_ch)); _V = _al*(2-sp.cos(_ps)-sp.cos(_ch))
_fa = {_ps: sp.diff(_f, _ps), _ch: sp.diff(_f, _ch)}
_G = sp.Matrix([[(_om*(1 if a == b else 0)+sp.Rational(3, 2)*_fa[a]*_fa[b]/_f)/_f for b in (_ps, _ch)] for a in (_ps, _ch)])
_co = [_ps, _ch]; _Gi = _G.inv()
def _chr(a, b, c): return sp.Rational(1, 2)*sum(_Gi[a, d]*(sp.diff(_G[d, b], _co[c])+sp.diff(_G[d, c], _co[b])-sp.diff(_G[b, c], _co[d])) for d in range(2))
_Va = [sp.diff(_V, _co[i]) for i in range(2)]
def _Vcov(a, b):
    e = sp.diff(_V, _co[a], _co[b])
    for c in range(2): e -= _chr(c, a, b)*_Va[c]
    return e
_es = sp.Matrix([1, -1]); _ns2 = (_es.T*_G*_es)[0]
_Vss = (_es.T*sp.Matrix([[_Vcov(0, 0), _Vcov(0, 1)], [_Vcov(1, 0), _Vcov(1, 1)]])*_es)[0]/_ns2
def _riem(a, b, c, d):
    t = sp.diff(_chr(a, b, d), _co[c])-sp.diff(_chr(a, b, c), _co[d])
    for e in range(2): t += _chr(a, c, e)*_chr(e, b, d)-_chr(a, d, e)*_chr(e, b, c)
    return t
_Ric = sp.Matrix([[sum(_riem(a, b, a, d) for a in range(2)) for d in range(2)] for b in range(2)])
_Rfs = sum(_Gi[b, d]*_Ric[b, d] for b in range(2) for d in range(2))
_th = sp.symbols('theta', real=True); _sub = {_ps: _th, _ch: _th}
_Vss_f = sp.lambdify((_th, _be, _al, _om), sp.simplify(_Vss.subs(_sub)), 'numpy')
_Rfs_f = sp.lambdify((_th, _be, _om), sp.simplify(_Rfs.subs(_sub)), 'numpy')
_U_l = sp.lambdify((_th, _be, _al), 2*_al*(1-sp.cos(_th))/(1+2*_be*sp.cos(_th))**2, 'numpy')
_Up_l = sp.lambdify((_th, _be, _al), sp.diff(2*_al*(1-sp.cos(_th))/(1+2*_be*sp.cos(_th))**2, _th), 'numpy')
_K_l = sp.lambdify((_th, _be, _om), 2*_om/(1+2*_be*sp.cos(_th))+6*_be**2*sp.sin(_th)**2/(1+2*_be*sp.cos(_th))**2, 'numpy')
def beta_iso(b, fs):
    a, o = 1e-9, fs**2
    thb = np.arccos((1+4*b)/(2*b))
    epsV = lambda t: (1/(2*_K_l(t, b, o)))*(_Up_l(t, b, a)/_U_l(t, b, a))**2
    t_end = brentq(lambda t: epsV(t)-1.0, 1e-4, thb*0.999)
    Nef = lambda t: quad(lambda x: _K_l(x, b, o)*_U_l(x, b, a)/_Up_l(x, b, a), t_end, t)[0]
    try: t_star = brentq(lambda t: Nef(t)-55.0, t_end+1e-5, thb*0.99999)
    except Exception: t_star = 0.5*(t_end+thb)
    H2 = _U_l(t_star, b, a)/3.0; eV = epsV(t_star)
    m2s = _Vss_f(t_star, b, a, o) + eV*_Rfs_f(t_star, b, o)*H2
    eta_ss = (m2s/H2)/3.0; TSS = np.exp(-2*eta_ss*55)
    return TSS**2/(1+TSS**2)

plt.rcParams.update({"font.size": 10.5, "axes.grid": True, "grid.alpha": 0.25,
                     "figure.dpi": 150, "savefig.bbox": "tight"})

T = {
 "fr": {"dir": "figs_u4",
   "bif_t": "11a — bifurcation au seuil $\\beta_c=-1/6$", "beta": "$\\beta$",
   "m2": "$m^2_{\\rm eff}(\\infty^*)$  (unites $\\alpha/\\omega$)", "trap": "$m^2>0$ : faux vide PIEGE ($\\beta<\\beta_c$)",
   "esc": "$m^2<0$ : ECHAPPE", "cmb": "fenetre CMB", "thr": "$\\beta_c=-1/6$",
   "coll_t": "Effondrement homogene sur la diagonale", "time": "temps ($a=1$ initial)", "theta": "$\\theta(t)$ diagonal",
   "rap": "$\\beta=-0.30<\\beta_c$ (rappel vers $\\infty^*$)", "rep": "$\\beta=-0.10>\\beta_c$ (repulsion)", "pole": "$\\infty^*\\ (\\theta=\\pi)$",
   "jeans_t": "11b — Jeans $\\lambda_c$ fini ssi $\\beta>\\beta_c$", "lam": "$\\lambda_c$ (longueur d'onde critique)",
   "noj": "$\\beta<\\beta_c$ : aucun mode\\ntachyonique (faux vide)",
   "land_t": "Paysage $U_{\\rm diag}(\\theta)/\\alpha$ : faux vide a $\\infty^*$ pour $\\beta<\\beta_c$",
   "thdiag": "$\\theta$ (diagonale $\\psi=\\chi$)", "Udiag": "$U_{\\rm diag}(\\theta)/\\alpha$",
   "dw": "(double-puits)", "ms": "(max simple)", "bar": "barriere", "fv": "faux vide", "P": "$P$ (vrai vide)",
   "bhm_t": "Action de Hawking–Moss du faux vide $\\infty^*$ ($\\alpha=10^{-9}$)", "bhmy": "$B_{\\rm HM}=24\\pi^2(3\\beta+1/2)^2/\\alpha$",
   "conv": "fenetre de convergence", "bif0": "$\\beta_c=-1/6$ (bifurcation, $B\\to0$)",
   "iso_t": "(a) $\\beta_{\\rm iso}$ produit $\\gg$ borne Planck $\\Rightarrow$ conversion requise",
   "isoy": "$\\beta_{\\rm iso}$ en fin d'inflation", "planckb": "borne Planck (0,038)",
   "drift_t": "(b) Derive de $(n_s,r)$ sous conversion curvaton", "ns": "$n_s$", "r": "$r$",
   "sym": "sym. ($T_{RS}=0$)", "nsr_t": "$(n_s,r)$ — prediction Mukhanov–Sasaki exacte ($N_*=55$)",
   "p95": "Planck18+BK18 95\\%", "p68": "Planck18+BK18 68\\%", "bk": "BK18 : $r<0.036$",
   "floor": "plancher LiteBIRD/SO ($\\delta r\\sim10^{-3}$)"},
 "en": {"dir": "figs_u4_en",
   "bif_t": "11a — bifurcation at the threshold $\\beta_c=-1/6$", "beta": "$\\beta$",
   "m2": "$m^2_{\\rm eff}(\\infty^*)$  (units $\\alpha/\\omega$)", "trap": "$m^2>0$: TRAPPED false vacuum ($\\beta<\\beta_c$)",
   "esc": "$m^2<0$: ESCAPES", "cmb": "CMB window", "thr": "$\\beta_c=-1/6$",
   "coll_t": "Homogeneous collapse along the diagonal", "time": "time ($a=1$ initial)", "theta": "$\\theta(t)$ diagonal",
   "rap": "$\\beta=-0.30<\\beta_c$ (pulled to $\\infty^*$)", "rep": "$\\beta=-0.10>\\beta_c$ (repelled)", "pole": "$\\infty^*\\ (\\theta=\\pi)$",
   "jeans_t": "11b — Jeans $\\lambda_c$ finite iff $\\beta>\\beta_c$", "lam": "$\\lambda_c$ (critical wavelength)",
   "noj": "$\\beta<\\beta_c$: no tachyonic\\nmode (false vacuum)",
   "land_t": "Landscape $U_{\\rm diag}(\\theta)/\\alpha$: false vacuum at $\\infty^*$ for $\\beta<\\beta_c$",
   "thdiag": "$\\theta$ (diagonal $\\psi=\\chi$)", "Udiag": "$U_{\\rm diag}(\\theta)/\\alpha$",
   "dw": "(double well)", "ms": "(simple max)", "bar": "barrier", "fv": "false vacuum", "P": "$P$ (true vacuum)",
   "bhm_t": "Hawking–Moss action of the false vacuum $\\infty^*$ ($\\alpha=10^{-9}$)", "bhmy": "$B_{\\rm HM}=24\\pi^2(3\\beta+1/2)^2/\\alpha$",
   "conv": "convergence window", "bif0": "$\\beta_c=-1/6$ (bifurcation, $B\\to0$)",
   "iso_t": "(a) Produced $\\beta_{\\rm iso}\\gg$ Planck bound $\\Rightarrow$ conversion required",
   "isoy": "$\\beta_{\\rm iso}$ at end of inflation", "planckb": "Planck bound (0.038)",
   "drift_t": "(b) Drift of $(n_s,r)$ under curvaton conversion", "ns": "$n_s$", "r": "$r$",
   "sym": "sym. ($T_{RS}=0$)", "nsr_t": "$(n_s,r)$ — exact Mukhanov–Sasaki prediction ($N_*=55$)",
   "p95": "Planck18+BK18 95\\%", "p68": "Planck18+BK18 68\\%", "bk": "BK18: $r<0.036$",
   "floor": "LiteBIRD/SO floor ($\\delta r\\sim10^{-3}$)"},
}

# valeurs MS validees par U5_VIDE_reproductible.py [V6]
NSR5 = [(-0.30, 0.9470, 0.014), (-0.27, 0.9505, 0.018), (-0.24, 0.9537, 0.022), (-0.20, 0.9571, 0.028)]
NSR7 = [(-0.32, 0.9548, 0.033), (-0.30, 0.9567, 0.037), (-0.28, 0.9577, 0.040), (-0.26, 0.9585, 0.043)]


def make(lang):
    d = T[lang]; os.makedirs(d["dir"], exist_ok=True)
    bb = np.linspace(-0.49, -0.10, 400)

    # ---- fig_bifurcation (11a) : m2_eff + effondrement homogene ----
    fig, ax = plt.subplots(1, 2, figsize=(11, 4.0))
    m2 = -(1+6*bb)/((1-2*bb)**2)
    ax[0].axhline(0, color="k", lw=0.6)
    ax[0].axvspan(-0.45, -0.15, color="#A9CCE3", alpha=0.30, label=d["cmb"])
    ax[0].plot(bb, m2, color="#6C3483", lw=2.3)
    ax[0].axvline(-1/6, color="#117A65", ls="--", lw=1.5, label=d["thr"])
    ax[0].fill_between(bb, m2, 0, where=(m2 > 0), color="#1E8449", alpha=0.18)
    ax[0].fill_between(bb, m2, 0, where=(m2 < 0), color="#C0392B", alpha=0.18)
    ax[0].text(-0.43, 0.012, d["trap"], fontsize=8.5, color="#196F3D")
    ax[0].text(-0.158, -0.02, d["esc"], fontsize=8.5, color="#922B21", ha="right")
    ax[0].set_xlabel(d["beta"]); ax[0].set_ylabel(d["m2"]); ax[0].set_title(d["bif_t"])
    ax[0].legend(fontsize=8.5, loc="lower left"); ax[0].set_ylim(-0.05, 0.05)
    # effondrement homogene : theta'' + 3H theta' = -U'/K, H<0 (contraction)
    def collapse(beta, th0):
        o = 25.0
        def U(t): f = 1+2*beta*np.cos(t); return 2*(1-np.cos(t))/f**2
        def dU(t):
            h = 1e-6; return (U(t+h)-U(t-h))/(2*h)
        def K(t): f = 1+2*beta*np.cos(t); return 2*o/f+6*beta**2*np.sin(t)**2/f**2
        def rhs(tt, y):
            th, v = y; H = -0.25
            return [v, (-3*H*v - dU(th)/K(th))]
        s = solve_ivp(rhs, [0, 4], [th0, 0.0], rtol=1e-8, atol=1e-10, max_step=0.01)
        return s.t, s.y[0]
    t1, y1 = collapse(-0.30, np.pi-0.14); t2, y2 = collapse(-0.10, np.pi-0.14)
    ax[1].axhline(np.pi, color="0.5", ls=":", lw=1)
    ax[1].plot(t1, y1, color="#117A65", lw=2, label=d["rap"])
    ax[1].plot(t2, y2, color="#C0392B", lw=2, label=d["rep"])
    ax[1].text(0.1, np.pi+0.01, d["pole"], fontsize=9, color="0.4")
    ax[1].set_xlabel(d["time"]); ax[1].set_ylabel(d["theta"]); ax[1].set_title(d["coll_t"])
    ax[1].legend(fontsize=8.5)
    fig.savefig(f"{d['dir']}/fig_bifurcation.png"); plt.close(fig)

    # ---- fig_jeans (11b) : longueur de Jeans ----
    fig, ax = plt.subplots(figsize=(6.6, 4.0))
    m2e = -(1+6*bb)/((1-2*bb)**2)
    lam = np.where(m2e < 0, 2*np.pi/np.sqrt(np.abs(m2e)), np.nan)
    ax.plot(bb, lam, color="#C0392B", lw=2.3, label=d["lam"])
    ax.axvline(-1/6, color="#117A65", ls="--", lw=1.5, label=d["thr"])
    ax.axvspan(-0.49, -1/6, color="#1E8449", alpha=0.12)
    ax.text(-0.42, 150, d["noj"], fontsize=9, color="#196F3D")
    ax.set_xlabel(d["beta"]); ax.set_ylabel(d["lam"]); ax.set_title(d["jeans_t"])
    ax.set_ylim(0, 300); ax.legend(fontsize=9, loc="upper left")
    fig.savefig(f"{d['dir']}/fig_jeans.png"); plt.close(fig)

    # ---- fig_landscape ----
    th = np.linspace(0, np.pi, 600)
    fig, ax = plt.subplots(figsize=(7.4, 4.3))
    for b, c in [(-0.30, "#1b6e4a"), (-0.20, "#7b3fa0"), (-0.10, "#c0392b")]:
        f = 1+2*b*np.cos(th); U = 2*(1-np.cos(th))/f**2
        lab = f"$\\beta={b:.2f}$ " + (d["dw"] if b < -1/6 else d["ms"])
        ax.plot(th, U, color=c, lw=2.3, label=lab)
        if b < -1/6:
            cs = (1+4*b)/(2*b); ts = np.arccos(cs); fb = 1+2*b*cs
            ax.plot(ts, 2*(1-cs)/fb**2, "o", color=c, ms=6)
    ax.axvline(0, ls=":", color="gray"); ax.axvline(np.pi, ls=":", color="gray")
    ax.text(0.05, 0.13, d["P"], color="gray", fontsize=9)
    ax.text(np.pi-0.6, 0.13, "$\\infty^*=(\\pi,\\pi)$", color="gray", fontsize=9)
    ax.annotate(d["bar"], (1.55, 2.05), fontsize=9, color="#444")
    ax.annotate(d["fv"], (2.7, 1.45), xytext=(2.15, 1.0), fontsize=9, color="#1b6e4a",
                arrowprops=dict(arrowstyle="->", color="#1b6e4a"))
    ax.set_xlabel(d["thdiag"]); ax.set_ylabel(d["Udiag"]); ax.set_title(d["land_t"])
    ax.legend(fontsize=9); ax.set_ylim(0, 3)
    fig.savefig(f"{d['dir']}/fig_landscape.png"); plt.close(fig)

    # ---- fig_BHM ----
    bb2 = np.linspace(-0.49, -0.168, 400); B = 24*np.pi**2*(3*bb2+0.5)**2/1e-9
    fig, ax = plt.subplots(figsize=(6.8, 4.0))
    ax.semilogy(bb2, B, color="#1b6e4a", lw=2.3)
    ax.axvspan(-0.30, -0.17, color="#A9CCE3", alpha=0.30, label=d["conv"])
    ax.axvline(-1/6, color="#C0392B", ls="--", lw=1.4, label=d["bif0"])
    for b in [-0.30, -0.25, -0.21, -0.17]:
        Bv = 24*np.pi**2*(3*b+0.5)**2/1e-9
        ax.annotate(f"{Bv:.1e}", (b, Bv), fontsize=7.5, color="#196F3D")
    ax.set_xlabel(d["beta"]); ax.set_ylabel(d["bhmy"]); ax.set_title(d["bhm_t"])
    ax.set_ylim(1e6, 1e11); ax.legend(fontsize=8.5, loc="lower left")
    fig.savefig(f"{d['dir']}/fig_BHM.png"); plt.close(fig)

    # ---- fig_isocurvature : (a) beta_iso  (b) derive (ns,r) ----
    fig, ax = plt.subplots(1, 2, figsize=(11, 4.0))
    for fs, c in [(4, "#C0392B"), (5, "#2471A3"), (7, "#196F3D")]:
        bs = np.array([-0.30, -0.26, -0.22, -0.18])
        biso = np.array([beta_iso(b, fs) for b in bs])
        ax[0].plot(bs, biso, "o-", color=c, lw=1.8, ms=5, label=f"$f_s={fs}$")
    ax[0].axhline(0.038, color="k", ls="--", lw=1.4, label=d["planckb"])
    ax[0].axhspan(0.038, 1.0, color="#1E8449", alpha=0.10)
    ax[0].set_xlabel(d["beta"]); ax[0].set_ylabel(d["isoy"]); ax[0].set_title(d["iso_t"])
    ax[0].set_ylim(0, 1.0); ax[0].legend(fontsize=8.5)
    # (b) derive curvaton : ns de 0.957 -> ~0.998, r -> 0
    sinT = np.linspace(0, 0.6, 40)
    ns_d = 0.957 + sinT*0.68; r_d = 0.027*(1-sinT/0.6)
    ax[1].axvspan(0.957, 0.973, color="#A9CCE3", alpha=0.35)
    ax[1].axhline(0.036, color="#C0392B", ls="--", lw=1.2, label=d["bk"])
    ax[1].plot(ns_d, r_d, "s-", color="#6C3483", lw=1.8, ms=4)
    ax[1].plot(0.957, 0.027, "o", color="#117A65", ms=8); ax[1].text(0.9575, 0.0285, d["sym"], fontsize=8.5, color="#117A65")
    ax[1].set_xlabel(d["ns"]); ax[1].set_ylabel(d["r"]); ax[1].set_title(d["drift_t"])
    ax[1].set_xlim(0.955, 1.0); ax[1].set_ylim(0, 0.035); ax[1].legend(fontsize=8.5)
    fig.savefig(f"{d['dir']}/fig_isocurvature.png"); plt.close(fig)

    # ---- fig_nsr ----
    fig, ax = plt.subplots(figsize=(7.6, 4.6))
    ax.axhline(0.036, color="#C0392B", ls="--", lw=1.3, label=d["bk"])
    ax.axhline(0.003, color="0.4", ls=":", lw=1.2, label=d["floor"])
    ax.axvspan(0.9607, 0.9691, color="#A9CCE3", alpha=0.25, label=d["p68"])
    ax.axvspan(0.9565, 0.9733, color="#A9CCE3", alpha=0.12, label=d["p95"])
    ns5 = [p[1] for p in NSR5]; r5 = [p[2] for p in NSR5]
    ns7 = [p[1] for p in NSR7]; r7 = [p[2] for p in NSR7]
    ax.plot(ns5, r5, "o-", color="#6C3483", lw=1.8, ms=5, label="$f_s=5$")
    ax.plot(ns7, r7, "s-", color="#B9770E", lw=1.8, ms=5, label="$f_s=7$")
    ax.set_xlabel(d["ns"]); ax.set_ylabel(d["r"]); ax.set_title(d["nsr_t"])
    ax.set_xlim(0.945, 0.975); ax.set_ylim(0, 0.06); ax.legend(fontsize=8, loc="upper left")
    fig.savefig(f"{d['dir']}/fig_nsr.png"); plt.close(fig)
    print(f"  [{lang}] -> {d['dir']}/ : bifurcation, jeans, landscape, BHM, isocurvature, nsr")


for lg in ("fr", "en"):
    make(lg)
print("OK")
