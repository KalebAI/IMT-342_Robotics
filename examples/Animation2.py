import numpy as np
import matplotlib.pyplot as plt
from spatialmath import SO3, SE3


# ---- Parámetros del espacio de visualización ----
DIMS     = (-0.8, 0.8, -0.8, 0.8, -0.8, 0.8)   # límites de la vista
SCALE    = 0.5                                  # longitud de los ejes dibujados
PAUSE    = 0.015                                # velocidad de animación (seg/frame)
N_STEPS_ROT = 60                                # pasos por rotación
N_STEPS_TRA = 60                                # pasos por traslación

# ---- Utilidades de dibujo (triadas con etiquetas x,y,z) ----
def draw_frame_static(ax, T4, label, scale=SCALE,
                      colx='r', coly='g', colz='b'):
    """Dibuja una triada estática para la pose T (4x4)."""
    R = T4[:3,:3]
    p = T4[:3, 3]
    o = p
    x = o + scale * R[:,0]
    y = o + scale * R[:,1]
    z = o + scale * R[:,2]
    ax.plot([o[0], x[0]], [o[1], x[1]], [o[2], x[2]], colx, lw=2)
    ax.plot([o[0], y[0]], [o[1], y[1]], [o[2], y[2]], coly, lw=2)
    ax.plot([o[0], z[0]], [o[1], z[1]], [o[2], z[2]], colz, lw=2)
    ax.text(o[0], o[1], o[2], label)
    ax.text(x[0], x[1], x[2], 'x')
    ax.text(y[0], y[1], y[2], 'y')
    ax.text(z[0], z[1], z[2], 'z')

def draw_frame_dynamic(ax, T4, scale=SCALE, color='0.5'):
    """Crea triada dinámica (líneas actualizables) para T (4x4)."""
    R = T4[:3,:3]
    p = T4[:3, 3]
    o = p
    x = o + scale * R[:,0]
    y = o + scale * R[:,1]
    z = o + scale * R[:,2]
    lx, = ax.plot([o[0], x[0]], [o[1], x[1]], [o[2], x[2]], color, lw=1.5)
    ly, = ax.plot([o[0], y[0]], [o[1], y[1]], [o[2], y[2]], color, lw=1.5)
    lz, = ax.plot([o[0], z[0]], [o[1], z[1]], [o[2], z[2]], color, lw=1.5)
    return lx, ly, lz

def update_frame_dynamic(lines, T4, scale=SCALE):
    """Actualiza las líneas de la triada dinámica."""
    R = T4[:3,:3]
    p = T4[:3, 3]
    o = p
    x = o + scale * R[:,0]
    y = o + scale * R[:,1]
    z = o + scale * R[:,2]
    # X
    lines[0].set_data([o[0], x[0]], [o[1], x[1]])
    lines[0].set_3d_properties([o[2], x[2]])
    # Y
    lines[1].set_data([o[0], y[0]], [o[1], y[1]])
    lines[1].set_3d_properties([o[2], y[2]])
    # Z
    lines[2].set_data([o[0], z[0]], [o[1], z[1]])
    lines[2].set_3d_properties([o[2], z[2]])

# ---- Incrementos SE(3) ----
def step_rot(axis, dtheta_rad):
    return {'x': SE3.Rx, 'y': SE3.Ry, 'z': SE3.Rz}[axis](dtheta_rad)

def step_trans(axis, d):
    return {'x': SE3.Tx, 'y': SE3.Ty, 'z': SE3.Tz}[axis](d)

def compose(T, S, mode):
    """Compone T con S según modo: post (cuerpo) o pre (mundo)."""
    return (T * S) if mode == 'post' else (S * T)

def animate_operation(ax, T_start, kind, axis, amount, mode,
                      n_steps_rot=N_STEPS_ROT, n_steps_tra=N_STEPS_TRA,
                      pause=PAUSE):
    """
    Anima una operación sobre T_start:
      kind: 'rot' (amount en grados) o 'trans' (amount en metros)
      axis: 'x' | 'y' | 'z'
      mode: 'post' (cuerpo fijo) o 'pre' (mundo fijo)
    Retorna T_final.
    """
    T = T_start
    dyn = draw_frame_dynamic(ax, T.A)  # triada gris
    if kind == 'rot':
        dtheta = np.deg2rad(amount) / n_steps_rot
        for _ in range(n_steps_rot):
            T = compose(T, step_rot(axis, dtheta), mode)
            update_frame_dynamic(dyn, T.A); plt.pause(pause)
    else:
        d = amount / n_steps_tra
        for _ in range(n_steps_tra):
            T = compose(T, step_trans(axis, d), mode)
            update_frame_dynamic(dyn, T.A); plt.pause(pause)
    # limpia triada dinámica
    for h in dyn: h.remove()
    return T

# ---- Animación comparativa: POST y PRE lado a lado ----
def animate_sequence(ops, mode='post', title=''):
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_title(title or f"Secuencia {mode.upper()} (ROT+TRANS)")
    ax.set_xlim(DIMS[0:2]); ax.set_ylim(DIMS[2:4]); ax.set_zlim(DIMS[4:6])
    ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z'); ax.grid(True)
    # Mundo W y sello identidad 0
    draw_frame_static(ax, SE3().A, 'W', colx='r', coly='g', colz='b')
    T = SE3()
    draw_frame_static(ax, T.A, '0', colx='0.3', coly='0.3', colz='0.3')
    # Ejecuta operaciones una a una
    for i, (kind, axis, amount) in enumerate(ops, start=1):
        T = animate_operation(ax, T, kind, axis, amount, mode=mode)
        draw_frame_static(ax, T.A, str(i), colx='r', coly='g', colz='b')
        print("Matriz TH ", i)
        print(T)
    plt.show()

# ===========================================
# 1) CÁLCULO (operaciones puras)
# ===========================================
# Parámetros base (puedes cambiarlos)
theta = 30     # rotación en X (deg)
beta  = 45     # rotación en Z (deg)
gamma = -20    # rotación en Y (deg)
tx    = 0.5    # traslación en X (m)
tz    = 0.8    # traslación en Z (m)


# Secuencias de operaciones mezclando ROT + TRANS
# Formato: ('rot'|'trans', eje, valor)  -> valor en grados para rot, metros para trans
ops = [
    ('rot',  'x', theta),
    ('trans','z', tz),
    ('rot',  'z', beta),
    ('trans','x', tx),
    ('rot',  'y', gamma),
]


# ====== Ejecuta ambas variantes: POST (cuerpo) y PRE (mundo) ======
# POST
print("Con referenica local (POST MULTIPLICACIÓN:) \n")
animate_sequence(ops, mode='post', title='Cuerpo fijo (post-multiplicación)')
# PRE
print("Con referenica local (PRE MULTIPLICACIÓN:) \n")
animate_sequence(ops, mode='pre',  title='Mundo fijo (pre-multiplicación)')
