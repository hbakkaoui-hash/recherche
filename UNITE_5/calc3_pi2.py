import sympy as sp
import numpy as np

print("="*70)
print("CANAL pi_2 : existe-t-il un monopole d'echelle statique a energie finie ?")
print("="*70)

# ---------- (a) Energie du herisson de degre 1, action minimale ----------
# n(theta_t=vartheta, phi_t=varphi) = r-chapeau (degre 1 sur S^2 spatial).
# Densite gradient = omega/r^2 ; densite potentielle = V(vartheta)=alpha(1-cos vartheta).
om,alpha,r,R = sp.symbols('omega alpha r R', positive=True)
vth=sp.symbols('vartheta')
# integrale angulaire
Igrad = sp.integrate( (1)*sp.sin(vth), (vth,0,sp.pi) )*2*sp.pi   # |grad n|^2 r^2 = 2 ; /2*omega -> omega ; ang int of 1
ang_grad = sp.integrate(2*sp.sin(vth),(vth,0,sp.pi))*sp.pi      # int |dn|^2 r^2 dOmega = int (2) dOmega = 2*4pi/... 
# faisons proprement:
dOmega_int_grad = sp.integrate(2*sp.sin(vth),(vth,0,sp.pi))*2*sp.pi  # = 2 * 4pi
dOmega_int_V    = sp.integrate((1-sp.cos(vth))*sp.sin(vth),(vth,0,sp.pi))*2*sp.pi
print("\n(a) Herisson rigide n = r-chapeau :")
print("   int_{S^2} |dn|^2 dOmega        =", dOmega_int_grad, "/r^2  -> densite lineique")
print("   int_{S^2} (1-cos vartheta)dOmega =", dOmega_int_V, " (= 4*pi)")
Egrad = sp.Rational(1,2)*om*dOmega_int_grad*sp.integrate(1,(r,0,R))   # (1/2)omega * (8pi) * int dr
Epot  = alpha*dOmega_int_V*sp.integrate(r**2,(r,0,R))
print("   E_grad(R) =", sp.simplify(Egrad), "   -> divergence LINEAIRE en R (type monopole global)")
print("   E_pot(R)  =", sp.simplify(Epot),  "   -> divergence CUBIQUE en R")
print("   => energie totale infinie. Le potentiel a vide unique interdit le monopole localise.")

# ---------- (b) Theoreme de Derrick (lump localise, degre conserve par effondrement) ----------
mu,T2,T0=sp.symbols('mu T2 T0',positive=True)
E = T2/mu + T0/mu**3          # en D=3 : gradient ~ mu^{-1}, potentiel ~ mu^{-3}
dE=sp.diff(E,mu)
print("\n(b) Derrick (re-echelle x->mu x, D=3) :  E(mu)=T2/mu + T0/mu^3")
print("   dE/dmu =", sp.simplify(dE), "  < 0  pour tout mu>0  (T2,T0>=0)")
print("   => aucun minimum : la texture s'effondre (mu->infini), degre perdu en un point singulier.")
print("   Stabiliser exigerait un terme croissant en mu (Skyrme ~ mu^{+1}), ABSENT de l'action minimale.")

# ---------- (c) Borne potentielle pour TOUTE application de degre 1 ----------
# Une application de degre 1 S^2->S^2 est surjective : son image couvre toute la cible.
# Donc sur chaque coquille a l'infini, int V(n) dOmega >= (minorant strictement positif).
# Minorant grossier : V>=0, =0 au seul pole Sud ; pour une carte de degre 1, l'aire couverte
# au-dela de tout voisinage du Sud est bornee inferieurement => int V dOmega >= c>0.
# Consequence : densite d'energie ~ c*alpha a grand r -> CONSTANTE -> Lambda effectif -> de Sitter,
# pas un objet localise asymptotiquement plat. Donc PAS de "trou noir regulier" issu de pi_2.
print("\n(c) Toute carte de degre 1 est surjective : int_{S^2} V(n) dOmega >= c>0 sur chaque coquille.")
print("   => densite ~ const a l'infini -> asymptotique de Sitter (Lambda_eff ~ alpha), non localisee.")
print("   Le secteur pi_2 minimal ne produit donc PAS de trou noir regulier : la cloture survit.")
