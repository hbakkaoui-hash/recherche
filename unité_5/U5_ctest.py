import numpy as np
from scipy.integrate import solve_ivp

# Einstein-frame single-field model on a meridian (phi=const) of S2_scale.
# Identical in form to the torus single-axis model (Unite 2): f=1+b cos t, V=a(1-cos t).
# t = latitude theta (North=pi=infinity, South=0=Planck).
b   = -0.30      # beta in viable band
fs  = 7.0
om  = fs**2      # omega
a   = 1.0        # alpha cancels in monotonicity / in (1/H^3) ratios

def f(t):  return 1 + b*np.cos(t)
def U(t):  return a*(1-np.cos(t))/f(t)**2          # Einstein-frame potential V/f^2
def Ut(t): # dU/dtheta
    num = a*np.sin(t)*f(t)**2 - a*(1-np.cos(t))*2*f(t)*(-b*np.sin(t))
    return num/f(t)**4
def K(t):  # field-space metric ω/f + (3/2)(f'/f)^2 ; f' = -b sin t
    fp = -b*np.sin(t)
    return om/f(t) + 1.5*(fp/f(t))**2

# slow-roll background in e-folds N: dtheta/dN = -U_theta/(U*K)
def rhs(N, y):
    t = y[0]
    return [-Ut(t)/(U(t)*K(t))]

t0 = 2.5  # displaced off the North maximum, rolling down the meridian
sol = solve_ivp(rhs, [0,400], [t0], dense_output=True, rtol=1e-10, atol=1e-12, max_step=0.05)
N = np.linspace(0, sol.t[-1], 400)
th = sol.sol(N)[0]
th = np.clip(th, 1e-6, np.pi)
cth = np.cos(th)
H2 = U(th)/3.0                       # slow-roll H^2 = U/3 (M_Pl=1)
H  = np.sqrt(H2)
C  = H**(-3)                         # cosmological FGPW-type c-function ~ 1/H^(d-1), d=4

def mono(x): 
    d = np.diff(x)
    return (np.all(d<=1e-12), np.all(d>=-1e-12))  # (nonincreasing, nondecreasing)

print("theta range:        %.3f -> %.3f   (pi=%.3f)"%(th[0],th[-1],np.pi))
print("theta monotone dec? ", mono(th)[0])
print("cos(theta) mono inc?", mono(cth)[1])
print("H monotone dec?     ", mono(H)[0])
print("C=1/H^3 mono inc?   ", mono(C)[1])
# C as a function of cos(theta): is it single-valued & monotone?
order = np.argsort(cth)
Cs = C[order]
print("C(cos th) mono inc? ", mono(Cs)[1])
print("sample (cos th, H/H0, C/C0):")
for i in [0,100,200,300,399]:
    print("  %+.3f   %.4f   %.4e"%(cth[i], H[i]/H[0], C[i]/C[0]))
