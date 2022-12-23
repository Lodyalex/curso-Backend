Entorno Virtual
Creación
// interprete -m modulo nombre_carpeta
python -m venv venv
Activar el entorno
# Windows (PowerShell)
cd venv
cd Scripts
activate.bat | Activate.ps1
cd ..
cd ..

# Windows (GitBash)
source venv/Scripts/activate

# Linux | MacOS
source venv/bin/activate
Desactivar el entorno
# Windows (PowerShell)
cd venv
cd Scripts
deactivate.bat
cd ..
cd ..

# Windows (GitBash) | Linux | MacOS
deactivate
PIP
Listar las librerias instaladas
pip list
Instalar librerias
pip install nombre_libreria
Desinstalar librerias
pip uninstall nombre_libreria
Crear archivo de instalación de paquetes (requirements.txt)
pip freeze > requirements.txt
Instalar librerias desde requirements.txt
pip install -r requirements.txt