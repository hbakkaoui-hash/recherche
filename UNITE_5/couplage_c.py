import numpy as np
b=-0.30; fs=7.0; om=fs**2; al=1e-9   # alpha ~ A_s (echelle GUT), M_Pl=1
ths=1.48                              # theta au passage d'horizon (N*=55)
# constante de decroissance du (pseudo-)Goldstone azimutal : f_phi = sqrt(omega) sin theta = fs sin theta
fphi=fs*np.sin(ths)
# echelle d'inflation
f=1+b*np.cos(ths); U=al*(1-np.cos(ths))/f**2; Hinf=np.sqrt(U/3)
# canal 3 (axion-like, SI la matiere portait une charge U(1)) : isocourbure ~ (H/(2 pi f_phi))^2
iso_axion=(Hinf/(2*np.pi*fphi))**2
print("theta* = %.3f"%ths)
print("f_phi = fs sin(theta*) = %.3f M_Pl   (super-planckienne -> couplage 1/f_phi supprime)"%fphi)
print("H_inf = %.3e M_Pl"%Hinf)
print("H_inf/(2 pi f_phi) = %.3e"%(Hinf/(2*np.pi*fphi)))
print("canal 3 (matiere chargee, NON motive) : iso ~ (H/2pi f_phi)^2 = %.2e  -> negligeable"%iso_axion)
print("\ncanal 1 (conforme) : f,V ne dependent que de theta -> phi absent -> c=0")
print("                     (+ photon aveugle Weyl ; delta tau0/tau0 ~ 1e-81 dans la matiere [Unite 3])")
print("canal 2 (Page-Wootters) : H_eff=eps H_sys UNIVERSEL -> delta phi = decalage de temps universel")
print("                     = mode ADIABATIQUE (pas d'isocourbure) ; et eps=1-1e-112 au vide")
print("\n=> c_iso ~ 0 par trois arguments independants. Confirme E1 de l'Unite 3.")
