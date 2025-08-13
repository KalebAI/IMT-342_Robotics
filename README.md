# IMT-342 Robotics • Entorno docente (ROS 2 Jazzy + Miniconda + Robotics Toolbox)

Repositorio público con scripts y guías para preparar el entorno de la asignatura **IMT-342 Robótica** en **Ubuntu 24.04** y **Windows 10/11**.

## Contenidos
- **Ubuntu 24.04**: ROS 2 **Jazzy**, Gazebo (ros-gz), workspace `ros2_ws` y Miniconda.
- **Windows 10/11**: Miniconda + **Robotics Toolbox (Python)** para prácticas de cinemática y transformadas espaciales.
- **Jupyter/VS Code**: cuaderno ejemplo `examples/rtb_spatial_transforms.ipynb` para estudiar **transformadas espaciales** con `spatialmath`/`roboticstoolbox`.

> **Recomendado**: usar **SSH** para `git push` y evitar contraseñas. Si ya configuraste SSH, no hay nada extra que hacer para este repo.

---

## Requisitos
- Ubuntu 24.04 (Noble) **o** Windows 10/11.
- Git y curl (Ubuntu), PowerShell (Windows).
- Conexión a internet.

## Instalación rápida (Ubuntu 24.04)
> Instala Miniconda, ROS 2 Jazzy y crea un workspace de ejemplo.
```bash
# 1) Clonar
git clone git@github.com:KalebAI/IMT-342_Robotics.git
cd IMT-342_Robotics
chmod +x scripts/*.sh || true

# 2) Miniconda + entorno (Python, RTB, Jupyter, etc.)
./scripts/install_miniconda_ubuntu.sh

# 3) ROS 2 Jazzy + Gazebo (ros-gz)
./scripts/setup_ros2_ubuntu24.sh

# 4) Workspace y demos
./scripts/create_ros2_ws.sh

# 5) (Opcional) activar overlay en nuevas terminales
./scripts/activate_ros2_overlay.sh
```

### Verificación rápida (Ubuntu)
Abrir **dos** terminales, en ambas:
```bash
source /opt/ros/jazzy/setup.bash
```
- Terminal A:
```bash
ros2 run demo_nodes_cpp talker
```
- Terminal B:
```bash
ros2 run demo_nodes_py listener
```

### Jupyter/VS Code (Ubuntu)
```bash
conda activate robotics
jupyter lab
# o abre la carpeta en VS Code y selecciona el kernel 'robotics'
```

## Instalación rápida (Windows 10/11)
> Instala **Miniconda** y crea el entorno `robotics` con RTB.
```powershell
git clone git@github.com:KalebAI/IMT-342_Robotics.git
cd IMT-342_Robotics
Set-ExecutionPolicy Bypass -Scope Process -Force
.\scripts\install_miniconda_windows.ps1
conda activate robotics
python -c "import roboticstoolbox as rtb; import spatialmath as sm; print(rtb.__version__, sm.__version__)"
```
Abrir **VS Code** → seleccionar el **kernel**/intérprete de `conda` (entorno `robotics`) para ejecutar el notebook de ejemplo en `examples/rtb_spatial_transforms.ipynb`.

---

## Estructura sugerida
```
IMT-342_Robotics/
├─ README.md
├─ LICENSE
├─ .gitignore
├─ environment.yml
├─ scripts/
│  ├─ install_miniconda_ubuntu.sh
│  ├─ install_miniconda_windows.ps1
│  ├─ setup_ros2_ubuntu24.sh
│  ├─ create_ros2_ws.sh
│  └─ activate_ros2_overlay.sh
├─ .vscode/
│  └─ extensions.json
└─ examples/
   └─ rtb_spatial_transforms.ipynb
```

> Los scripts de `scripts/` puedes adaptarlos a tus necesidades (paquetes específicos, robots, etc.).

---

## Problemas comunes
- **403 al hacer `git push` por HTTPS**: GitHub ya no acepta contraseña; usa **SSH** (recomendado) o **token (PAT)** como contraseña.
- **`rviz2` o `gz` no abren**: verifica drivers gráficos y que hayas ejecutado `source /opt/ros/jazzy/setup.bash`.
- **No aparece el kernel en Jupyter/VS Code**: ejecuta `conda activate robotics && python -m ipykernel install --user --name robotics`.

---

## Licencia
Este repositorio se distribuye bajo la licencia indicada en `LICENSE`. Por defecto: **MIT**.

---

## Créditos
- **Autor:** Kaleb Irahola Azad
- **Año:** 2025
