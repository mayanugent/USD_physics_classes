import numpy as np

def intensity(y_mm,lam_nm):
    if y_mm == 0:
        return 1
    
    lam = lam_nm*1e-9
    y = y_mm * 1e-3
    
    L=3
    d = 0.25e-3
    a = d/5
    
    k = 2*np.pi / lam
    
    th = np.arctan(y/L)
    
    return np.cos(k*d/2 * np.sin(th))**2 * np.sin(k*a/2 * np.sin(th))**2 / (k*a *np.sin(th)/2)**2
