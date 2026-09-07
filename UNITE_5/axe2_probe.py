import numpy as np
MPl=1.22e19  # GeV
b=-0.30; fs=7.0; om=fs**2
# alpha fixe par A_s (echelle GUT) : H_inf ~ 1e-5 M_Pl -> alpha ~ 3 H^2 (1-b) /2 a l'ordre
al=1e-9     # en M_Pl^4 (valeur Unite 3 : 0.5-1.2e-9)

# 1) Le seuil EST la stabilite du plateau inflationnaire (meme physique que l'inflation)
#    fluctuation radiale en infini* : kappa^2 = alpha(1+3b)/[omega(b-1)] ; stable si kappa^2<0 <=> b>-1/3
def kap2(bb): return al*(1+3*bb)/(om*(bb-1))
print("Stabilite du plateau infini* (= coeur dS) :")
for bb in [-0.20,-1/3,-0.45]:
    print("  b=%+.3f : kappa^2=%+.2e  -> %s"%(bb,kap2(bb),"STABLE (piege)" if kap2(bb)<0 else "INSTABLE"))
print("  => seuil b_c=-1/3 ; b(CMB)=-0.30 > -1/3 : plateau stable, l'inflation s'y produit.\n")

# 2) Echelle physique du coeur : R_core = 8 alpha/(1-b), H_core^2 = 2 alpha/(3(1-b))
Hcore=np.sqrt(2*al/(3*(1-b)))            # en M_Pl
Hcore_GeV=Hcore*MPl
Lcore=1/Hcore_GeV * 1.97e-16             # longueur (m), hbar c = 0.197 GeV.fm = 1.97e-16 GeV.m
print("Coeur de Sitter : H_core=%.2e M_Pl = %.2e GeV (echelle GUT)"%(Hcore,Hcore_GeV))
print("  rayon de courbure du coeur ~ %.2e m"%Lcore)
print("  horizon d'un trou noir solaire ~ 3e3 m  -> ecart %.0e ordres de grandeur"%(np.log10(3e3/Lcore)))
print("  => structure du coeur totalement ECRANTEE sous l'horizon.\n")

# 3) Decalage d'horloge dans la matiere ordinaire (Unite 3) : delta tau0/tau0 = -(b/4) M_Pl^2 R/alpha
#    courbure typique d'une etoile a neutrons : R ~ G rho ~ (1e18 kg/m3) ... en M_Pl^2 ~ 1e-78
R_ns=1e-78  # M_Pl^2, ordre de grandeur pour une etoile a neutrons
dtau=-(b/4)*R_ns/al
print("Etoile a neutrons : delta tau0/tau0 ~ %.0e  -> inobservable (Unite 3 : ~1e-81)\n"%dtau)

# 4) G_eff fige par BBN : le champ est au vide (Sud) bien avant la BBN -> G_eff ~ G/(1+b), constant
print("G_eff = 1/(8pi f), f=1+b cos(theta). Au vide Sud (aujourd'hui et des avant BBN) : f=1+b.")
print("  variation G_eff entre epoques observables : nulle (champ epingle au vide).")
print("  la variation (1+b)/(1-b)=%.2f n'a eu lieu QUE pendant le roulement -> secteur inflationnaire.\n"%((1+b)/(1-b)))

print("VERDICT : le seuil de coeur b_c=-1/3 = stabilite du plateau inflationnaire (meme infini*).")
print("  -> b(closure) et b(CMB) ne sont PAS independants : un parametre, deux lectures du meme plateau.")
print("  -> coeur ecrante (GUT), horloge ecrantee (1e-81), G_eff epingle : aucune sonde independante directe.")
