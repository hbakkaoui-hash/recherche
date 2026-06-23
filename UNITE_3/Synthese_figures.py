#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Figures (FR + EN) de l'Unite 3 (synthese). Sorties : figs_u3/ (FR), figs_u3_en/ (EN)."""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.special import ellipe, ellipk

plt.rcParams.update({"font.size": 11, "axes.grid": True, "grid.alpha": 0.25,
                     "figure.dpi": 150, "savefig.bbox": "tight"})

L = {
 "fr": {"dir": "figs_u3",
   "t1": "Facteur d'existence  $\\varepsilon = E(k)/K(k)$  (derive)",
   "x1": "amplitude  $\\chi_{\\max}$", "y1": "$\\varepsilon$",
   "c1a": "$\\varepsilon = E(k)/K(k)$", "c1b": "petite amplitude  $1-\\chi_{\\max}^2/8$",
   "a1a": "$\\varepsilon\\to1$ : MQ continue", "a1b": "$\\varepsilon\\to0$ : suspension (separatrice)",
   "t2": "Paysage diagonal $U(\\theta)/\\alpha$ : $\\infty^*$ piege vs traversable",
   "x2": "$\\theta$  (diagonale $\\psi=\\chi$)", "y2": "$U(\\theta)/\\alpha$",
   "trap": "piege (faux vide)", "P": "$P$ (vrai vide)",
   "t3": "La gravite fige l'horloge : $\\tau_0(R)\\to\\infty$ a $R_c$",
   "x3": "$R/R_c$", "y3": "$\\tau_0(R)/\\tau_0(0)$", "rc": "$R_c=2\\alpha/|\\beta|$ : horloge gelee"},
 "en": {"dir": "figs_u3_en",
   "t1": "Existence factor  $\\varepsilon = E(k)/K(k)$  (derived)",
   "x1": "amplitude  $\\chi_{\\max}$", "y1": "$\\varepsilon$",
   "c1a": "$\\varepsilon = E(k)/K(k)$", "c1b": "small amplitude  $1-\\chi_{\\max}^2/8$",
   "a1a": "$\\varepsilon\\to1$: continuous QM", "a1b": "$\\varepsilon\\to0$: suspension (separatrix)",
   "t2": "Diagonal landscape $U(\\theta)/\\alpha$: $\\infty^*$ trapped vs traversable",
   "x2": "$\\theta$  (diagonal $\\psi=\\chi$)", "y2": "$U(\\theta)/\\alpha$",
   "trap": "trapped (false vacuum)", "P": "$P$ (true vacuum)",
   "t3": "Gravity freezes the clock: $\\tau_0(R)\\to\\infty$ at $R_c$",
   "x3": "$R/R_c$", "y3": "$\\tau_0(R)/\\tau_0(0)$", "rc": "$R_c=2\\alpha/|\\beta|$: clock frozen"},
}


def make(lang):
    d = L[lang]; os.makedirs(d["dir"], exist_ok=True)
    # --- Fig 1 : eps = E(k)/K(k) ---
    chimax = np.linspace(1e-3, np.pi-1e-3, 600)
    k = np.sin(chimax/2); eps = ellipe(k**2)/ellipk(k**2)
    fig, ax = plt.subplots(figsize=(6.4, 4.0))
    ax.plot(chimax, eps, color="#1E8449", lw=2.2, label=d["c1a"])
    ax.plot(chimax, 1-chimax**2/8, "--", color="#B9770E", lw=1.6, label=d["c1b"])
    ax.set_ylim(0, 1.05); ax.set_xlim(0, np.pi)
    ax.set_xticks([0, np.pi/2, np.pi]); ax.set_xticklabels(["0", "$\\pi/2$", "$\\pi$"])
    ax.annotate(d["a1a"], (0.1, 0.97), fontsize=9, color="#196F3D")
    ax.annotate(d["a1b"], (np.pi-1.55, 0.08), fontsize=9, color="#922B21")
    ax.set_xlabel(d["x1"]); ax.set_ylabel(d["y1"]); ax.set_title(d["t1"])
    ax.legend(loc="upper right", fontsize=9, framealpha=0.9)
    fig.savefig(f"{d['dir']}/fig_epsilon.png"); plt.close(fig)

    # --- Fig 2 : paysage diagonal (la tension infini*) ---
    th = np.linspace(0, np.pi, 800)
    fig, ax = plt.subplots(figsize=(6.6, 4.1))
    for b, col, lab in [(-0.30, "#1E8449", "$\\beta=-0.30$"), (-0.25, "#2471A3", "$\\beta=-0.25$"),
                        (-1/6, "#7B7D7D", "$\\beta=-1/6$"), (-0.10, "#B03A2E", "$\\beta=-0.10$")]:
        f = 1 + 2*b*np.cos(th); U = 2*(1-np.cos(th))/f**2
        ax.plot(th, U, color=col, lw=2, label=lab)
        if b < -1/6:  # infini* piege : marquer le minimum en pi
            ax.scatter([np.pi], [2*(1-np.cos(np.pi))/(1+2*b*np.cos(np.pi))**2], s=30, color=col, zorder=5)
    ax.axvline(np.pi, color="k", lw=0.6, ls=":")
    ax.text(0.06, 0.12, d["P"], fontsize=9, color="0.3")
    ax.text(np.pi-0.5, 0.35, "$\\infty^*$", fontsize=11, color="0.3")
    ax.annotate(d["trap"], (np.pi-0.02, 1.55), fontsize=9, color="#196F3D", ha="right")
    ax.set_xticks([0, np.pi/2, np.pi]); ax.set_xticklabels(["0 ($P$)", "$\\pi/2$", "$\\pi$ ($\\infty^*$)"])
    ax.set_xlim(0, np.pi); ax.set_ylim(0, 3.0)
    ax.set_xlabel(d["x2"]); ax.set_ylabel(d["y2"]); ax.set_title(d["t2"])
    ax.legend(loc="upper left", fontsize=9, framealpha=0.9)
    fig.savefig(f"{d['dir']}/fig_pole.png"); plt.close(fig)

    # --- Fig 3 : tau0(R) gel a Rc ---
    x = np.linspace(0, 0.985, 500); ratio = 1/np.sqrt(1 - x)
    fig, ax = plt.subplots(figsize=(6.4, 4.0))
    ax.plot(x, ratio, color="#6C3483", lw=2.2)
    ax.axvline(1.0, color="#B03A2E", ls="--", lw=1.4)
    ax.annotate(d["rc"], (1.0, 5.5), fontsize=9, color="#922B21", ha="right", rotation=90, va="top")
    ax.set_xlim(0, 1.08); ax.set_ylim(0, 9)
    ax.set_xlabel(d["x3"]); ax.set_ylabel(d["y3"]); ax.set_title(d["t3"])
    fig.savefig(f"{d['dir']}/fig_tau0R.png"); plt.close(fig)
    print(f"  [{lang}] -> {d['dir']}/ : fig_epsilon, fig_pole, fig_tau0R")


for lg in ("fr", "en"):
    make(lg)
print("OK")
