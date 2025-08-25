import numpy as np
import matplotlib.pyplot as plt

from spatialmath import SE3
from spatialmath.base import trplot, tranimate, trotx, troty, trotz

theta = 30
betha = 45
gamma = -20

R1 = SE3.Rx(np.deg2rad(theta))
R2 = SE3.Rz(np.deg2rad(betha))
R3 = SE3.Ry(np.deg2rad(gamma))

print(R1)
print(R2)
print(R3)

# Desde 
R_Post = R1*R2*R3
print("MAtriz post multiplicada:")
print(R_Post)

# Desde
R_Pre = R3*R2*R1
print("MAtriz pre multiplicada:")
print(R_Pre)

# --- Sistema fijo (marco de referencia) ---
FixedSystem = SE3()        # 4x4 identidad (equivalente a eye(4))
ax = trplot(FixedSystem.A, frame='W', color='r',
            dims=[-1, 1, -1, 1, -1, 1],  # ajusta el volumen de vista a gusto
            block=False)
ax.grid(True)   

tranimate(R_Post.A, ax=ax, frame='1',
          dims=[-1, 1, -1, 1, -1, 1],
          nframes=60, block=False)

plt.show()