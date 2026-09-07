#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Figures (FR + EN) fideles au papier de gravite. Sorties : figs/ (FR), figs_en/ (EN)."""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({"font.size": 11, "axes.grid": True, "grid.alpha": 0.25,
                     "figure.dpi": 150, "savefig.bbox": "tight"})

L = {
 "fr": {"dir": "figs",
   "t1": "Paysage du potentiel (repere d'Einstein)", "P": "$P$ (vrai vide)",
   "cmb": " (CMB)", "esc": " (echappement)",
   "t2": "Predictions $(n_s,r)$ a $N=55$ vs Planck + BK18",
   "xns": "indice spectral scalaire $n_s$", "yr": "rapport tenseur/scalaire $r$",
   "planck": "Planck $n_s$ ($\\pm0.004$)", "bk": "BK18 : $r<0.036$ (exclu au-dessus)",
   "st": {"big": "r trop grand", "exc": "exclu", "comp": "compatible", "edge": "au bord"},
   "t3": "Seuil de cloture $\\beta_c=-1/3$ et bande CMB viable",
   "y3": "diagnostic de stabilite  $\\propto -\\kappa^2$  :  $(1+3\\beta)/(1-\\beta)$",
   "trap": "$\\beta>-1/3$ : piege\n($\\infty^*$ stable, SdS)",
   "escape": "$\\beta<-1/3$ : echappement\n(branche roulante singuliere)"},
 "en": {"dir": "figs_en",
   "t1": "Potential landscape (Einstein frame)", "P": "$P$ (true vacuum)",
   "cmb": " (CMB)", "esc": " (escape)",
   "t2": "Predictions $(n_s,r)$ at $N=55$ vs Planck + BK18",
   "xns": "scalar spectral index $n_s$", "yr": "tensor-to-scalar ratio $r$",
   "planck": "Planck $n_s$ ($\\pm0.004$)", "bk": "BK18: $r<0.036$ (excluded above)",
   "st": {"big": "r too large", "exc": "excluded", "comp": "compatible", "edge": "borderline"},
   "t3": "Closure threshold $\\beta_c=-1/3$ and viable CMB band",
   "y3": "radial stability diagnostic  $\\propto -\\kappa^2$  :  $(1+3\\beta)/(1-\\beta)$",
   "trap": "$\\beta>-1/3$: trapped\n($\\infty^*$ stable, SdS)",
   "escape": "$\\beta<-1/3$: escape\n(singular rolling branch)"},
}


def make(lang):
    d = L[lang]; os.makedirs(d["dir"], exist_ok=True)
    # --- Fig 1 : paysage ---
    psi = np.linspace(-np.pi, np.pi, 1000)
    fig, ax = plt.subplots(figsize=(6.6, 4.0))
    for beta, col, ls in [(0.3, "#B03A2E", "-"), (0.0, "#7B7D7D", "--"),
                          (-0.3, "#1E8449", "-"), (-0.7, "#2471A3", "-")]:
        f = 1 + beta*np.cos(psi); U = (1 - np.cos(psi))/f**2
        lab = f"$\\beta={beta:+.1f}$" + (d["cmb"] if beta == -0.3 else (d["esc"] if beta == -0.7 else ""))
        ax.plot(psi, U, ls, color=col, lw=2, label=lab)
    for x in (0, np.pi, -np.pi):
        ax.axvline(x, color="k", lw=0.6, ls=":")
    ax.text(0.05, 0.15, d["P"], fontsize=9, color="0.3")
    ax.text(np.pi-1.05, 2.6, "$\\infty^*=(\\pm\\pi)$", fontsize=9, color="0.3")
    ax.set_xlabel("$\\psi$"); ax.set_ylabel("$U(\\psi)/\\alpha = (1-\\cos\\psi)/(1+\\beta\\cos\\psi)^2$")
    ax.set_xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
    ax.set_xticklabels(["$-\\pi$", "$-\\pi/2$", "0", "$\\pi/2$", "$\\pi$"])
    ax.set_ylim(0, 3.2); ax.set_xlim(-np.pi, np.pi); ax.set_title(d["t1"])
    ax.legend(loc="upper center", fontsize=9, framealpha=0.9)
    fig.savefig(f"{d['dir']}/fig_paysage.png"); plt.close(fig)

    # --- Fig 2 : (ns, r) ---
    pts = [(0.960, 0.078, "$\\beta=0,\\ f_s=7$", "big", "#B03A2E"),
           (0.949, 0.128, "$\\beta=+0.3$", "exc", "#B03A2E"),
           (0.930, 0.193, "$\\beta=+0.6$", "exc", "#B03A2E"),
           (0.958, 0.017, "$\\beta=-0.3,\\ f_s=5$", "comp", "#1E8449"),
           (0.960, 0.036, "$\\beta=-0.3,\\ f_s=7$", "edge", "#B9770E")]
    fig, ax = plt.subplots(figsize=(6.6, 4.2))
    ax.axvspan(0.9649-0.004, 0.9649+0.004, color="#2471A3", alpha=0.12, label=d["planck"])
    ax.axhline(0.036, color="#B03A2E", ls="--", lw=1.3, label=d["bk"])
    ax.axhspan(0.036, 0.25, color="#B03A2E", alpha=0.06)
    for ns, r, lab, stat, col in pts:
        ax.scatter(ns, r, s=60, color=col, zorder=5, edgecolor="k", lw=0.5)
        ax.annotate(lab, (ns, r), textcoords="offset points", xytext=(6, 5), fontsize=8.5)
    ax.set_xlabel(d["xns"]); ax.set_ylabel(d["yr"])
    ax.set_xlim(0.925, 0.972); ax.set_ylim(0, 0.21); ax.set_title(d["t2"])
    ax.legend(loc="upper left", fontsize=8.5, framealpha=0.9)
    fig.savefig(f"{d['dir']}/fig_nsr.png"); plt.close(fig)

    # --- Fig 3 : seuil ---
    beta = np.linspace(-0.9, 0.9, 1000); S = (1 + 3*beta)/(1 - beta)
    fig, ax = plt.subplots(figsize=(6.6, 4.0))
    ax.axhline(0, color="k", lw=0.8); ax.axvline(-1/3, color="k", ls="--", lw=1.2)
    ax.fill_between(beta, 0, S, where=(beta > -1/3), color="#1E8449", alpha=0.18)
    ax.fill_between(beta, S, 0, where=(beta < -1/3), color="#B03A2E", alpha=0.18)
    ax.plot(beta, S, color="#34495E", lw=2.2)
    ax.axvspan(-0.5, -0.15, color="#2471A3", alpha=0.12)
    yc = (1+3*(-0.3))/(1-(-0.3))
    ax.scatter([-0.3], [yc], s=70, color="#2471A3", zorder=6, edgecolor="k", lw=0.5)
    ax.annotate("$\\beta\\approx-0.3$ (CMB)", (-0.3, yc), textcoords="offset points",
                xytext=(8, -2), fontsize=9, color="#1F618D")
    ax.text(0.05, 1.6, d["trap"], fontsize=9, color="#196F3D")
    ax.text(-0.86, -1.7, d["escape"], fontsize=9, color="#922B21")
    ax.annotate("$\\beta_c=-1/3$", (-1/3, 2.2), fontsize=10, ha="center")
    ax.set_xlabel("$\\beta$"); ax.set_ylabel(d["y3"])
    ax.set_xlim(-0.9, 0.9); ax.set_ylim(-2.5, 2.7); ax.set_title(d["t3"])
    fig.savefig(f"{d['dir']}/fig_seuil.png"); plt.close(fig)
    print(f"  [{lang}] -> {d['dir']}/ : fig_paysage, fig_nsr, fig_seuil")


for lg in ("fr", "en"):
    make(lg)
print("OK")
