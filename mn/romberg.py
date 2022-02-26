import numpy as np
from scipy import integrate

def romberg(f,a,b):
    return integrate.romberg(f,a,b,show=True)