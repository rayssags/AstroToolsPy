import matplotlib.pyplot as plt
import numpy as np

plt.figure()

Xmin, Xmax         = -1.2, 1.2   # Define the maximum and minimum limit in X-axis
Ymin, Ymax         = -1.5, 1.0   # Define the maximum and minimum limit in Y-axis


# Kewley+01 ------------------------------------------
X = np.linspace(-1.5,0.3)
Y = (0.61/( X  - 0.47  )) + 1.19

# Schawinski+07 --------------------------------------
X3 = np.linspace(-0.180,1.5)
Y3 = 1.05*X3 + 0.45

# Kauffmann+03 ---------------------------------------
Xk = np.linspace(-1.5,0.)
Yk = 0.61/(Xk -0.05) + 1.3

# Regions --------------------------------------------
plt.plot(X,   Y, '-' , color='blue', lw=3, label='Kewley+01'    ) # Kewley+01
plt.plot(X3, Y3, '-', color='blue', lw=3, label='Schawinski+07') # Schawinski+07
plt.plot(Xk, Yk, '--', color='blue', lw=3, label='Kauffmann+03' ) # Kauffmann+03

# Axi name here ...
Nsize = 9
plt.xlabel(r'log([NII] $\lambda$ 6583/H$\alpha$)',fontsize=Nsize)
plt.ylabel(r'log([OIII] $\lambda$ 5007/H$\beta$)',fontsize=Nsize)
plt.tick_params(labelsize = Nsize)
plt.ylim(Ymin, Ymax)
plt.xlim(Xmin, Xmax)

plt.show()
