# === Animación de giros con RTB + SpatialMath (Python) ===
import numpy as np
import matplotlib.pyplot as plt

from spatialmath import SE3
from spatialmath.base import trplot, tranimate, trotx, troty, trotz

# --- Sistema fijo (marco de referencia) ---
FixedSystem = SE3()        # 4x4 identidad (equivalente a eye(4))
ax = trplot(FixedSystem.A, frame='W', color='r',
            dims=[-1, 1, -1, 1, -1, 1],  # ajusta el volumen de vista a gusto
            block=False)
ax.grid(True)              # cuadrícula

# --- Primera rotación: Rx(theta) ---
theta = 56  # grados
R1 = SE3.Rx(np.deg2rad(theta))   # homogénea 4x4 con rotación Rx
ResFinal = R1                     # guarda resultado acumulado

# anima desde identidad hasta R1
tranimate(R1.A, ax=ax, frame='1',
          dims=[-1, 1, -1, 1, -1, 1],
          nframes=60, block=False)

# --- Segunda rotación: Ry(beta) compuesta con la anterior ---
beta = 69  # grados
R2 = SE3.Ry(np.deg2rad(beta)) * ResFinal   # ojo: orden a la izquierda (mundo fijo)
ResFinal = R2

# anima de R1 a R2
tranimate(R2.A, ax=ax, frame='1',
          dims=[-1, 1, -1, 1, -1, 1],
          nframes=60, block=False)

# --- Tercera rotación: Rz(gamma) compuesta con las anteriores ---
gamma = 48  # grados
R3 = SE3.Rz(np.deg2rad(gamma)) * ResFinal
ResFinal = R3

# anima de R2 a R3
tranimate(R3.A, ax=ax, frame='1',
          dims=[-1, 1, -1, 1, -1, 1],
          nframes=60, block=False)  # último tramo puede ser block=True

plt.show()
