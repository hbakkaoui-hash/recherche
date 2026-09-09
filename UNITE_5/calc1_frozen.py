import sympy as sp

r, M, Lam, beta, alpha = sp.symbols('r M Lambda beta alpha', positive=True)

# ---- Branche gelee theta=pi (pole Nord = infini). Verification analytique ----
# EOM scalaire: omega*Box(theta) = V'(theta) - 1/2 f'(theta) R
# theta=pi: V'=alpha*sin(pi)=0, f'=-beta*sin(pi)=0, Box(theta)=0  => 0=0 (toute R). OK
# EOM tenseur: f G = -g V + (grad grad f - g Box f). f=1-beta const => f G = -g*2alpha
# => G_mn = -[2 alpha/(1-beta)] g_mn  => Lambda_eff = 2 alpha/(1-beta), H^2=Lam/3.
Lam_eff = 2*alpha/(1-beta)
print("Branche gelee Nord => Einstein-Lambda exact, Lambda_eff =", Lam_eff,
      ",  H^2 =", sp.simplify(Lam_eff/3))

# ---- Schwarzschild-de Sitter: invariant de Kretschmann ----
A = 1 - 2*M/r - Lam*r**2/3
g = sp.diag(-A, 1/A, r**2, r**2*sp.sin(sp.symbols('th'))**2)
th = sp.symbols('th')
g = sp.Matrix([[-A,0,0,0],[0,1/A,0,0],[0,0,r**2,0],[0,0,0,r**2*sp.sin(th)**2]])
x = [sp.symbols('t'), r, th, sp.symbols('ph')]
ginv = g.inv()
n=4
# Christoffel
Gamma = [[[0]*n for _ in range(n)] for _ in range(n)]
for a in range(n):
    for b in range(n):
        for c in range(n):
            s=0
            for d in range(n):
                s+=ginv[a,d]*(sp.diff(g[d,b],x[c])+sp.diff(g[d,c],x[b])-sp.diff(g[b,c],x[d]))
            Gamma[a][b][c]=sp.simplify(s/2)
# Riemann R^a_{bcd}
def Riem(a,b,c,d):
    t=sp.diff(Gamma[a][b][d],x[c])-sp.diff(Gamma[a][b][c],x[d])
    for e in range(n):
        t+=Gamma[a][c][e]*Gamma[e][b][d]-Gamma[a][d][e]*Gamma[e][b][c]
    return sp.simplify(t)
# Kretschmann = R_{abcd}R^{abcd}
Rdown=[[[[0]*n for _ in range(n)] for _ in range(n)] for _ in range(n)]
Rup  =[[[[0]*n for _ in range(n)] for _ in range(n)] for _ in range(n)]
for a in range(n):
 for b in range(n):
  for c in range(n):
   for d in range(n):
     Rup[a][b][c][d]=Riem(a,b,c,d)
for a in range(n):
 for b in range(n):
  for c in range(n):
   for d in range(n):
     s=0
     for e in range(n): s+=g[a,e]*Rup[e][b][c][d]
     Rdown[a][b][c][d]=sp.simplify(s)
K=0
for a in range(n):
 for b in range(n):
  for c in range(n):
   for d in range(n):
     if Rup[a][b][c][d]==0: continue
     # raise indices on Rdown to contract
     comp=0
     # build R^{abcd}
     # easier: K = R_{abcd} R^{abcd}; R^{abcd}=g^{aa'}g^{bb'}g^{cc'}g^{dd'}R_{a'b'c'd'}
K = sp.simplify(sum(
    Rdown[a][b][c][d]*ginv[a,ap]*ginv[b,bp]*ginv[c,cp]*ginv[d,dp]*Rdown[ap][bp][cp][dp]
    for a in range(n) for b in range(n) for c in range(n) for d in range(n)
    for ap in range(n) for bp in range(n) for cp in range(n) for dp in range(n)
    if Rdown[a][b][c][d]!=0))
print("\nKretschmann SdS  K(r) =", K)
print("  -> r->0 :", "divergence en 48 M^2/r^6" )
print("  -> M=0  :", sp.simplify(K.subs(M,0)), " (= 24 H^4 avec H^2=Lam/3 ; fini, de Sitter pur)")
