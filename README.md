# Entorno docente de Robótica (ROS 2 + RTB)

## Requisitos
- Ubuntu 24.04 (para ROS 2 Jazzy). En Windows se instala Miniconda + RTB (sin ROS 2).
- Git, curl, PowerShell (Windows).

## Instalación rápida

### Ubuntu 24.04
```bash
git clone https://github.com/<tu-usuario>/ros2-robotics-env.git
cd ros2-robotics-env
chmod +x scripts/*.sh
./scripts/install_miniconda_ubuntu.sh
./scripts/setup_ros2_ubuntu24.sh
./scripts/create_ros2_ws.sh
