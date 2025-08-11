# Recomendado: ejecutar con PowerShell (x64)
$ErrorActionPreference = "Stop"

# 1) Descarga del instalador
$MinicondaUrl = "https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe"
$Installer = "$env:TEMP\Miniconda3-latest-Windows-x86_64.exe"
Invoke-WebRequest -Uri $MinicondaUrl -OutFile $Installer

# 2) Instalación silenciosa (JustMe, agrega a PATH)
& $Installer /S /InstallationType=JustMe /AddToPath=1 /RegisterPython=0 /D=$env:USERPROFILE\miniconda3

# 3) Cargar conda y crear entorno
$CondaExe = "$env:USERPROFILE\miniconda3\Scripts\conda.exe"
& $CondaExe init powershell
& $CondaExe env update -n robotics -f .\environment.yml
Write-Host "✅ Miniconda + entorno 'robotics' listo. Cierra/abre PowerShell y ejecuta: conda activate robotics"
