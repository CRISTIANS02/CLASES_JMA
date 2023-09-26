# ENTORNOS VIRTUALES 
## *PYENV*
 *Es u manejador de wersiones de **PYTHON** y cambiar entre ellos  segun  los requerimientos del proyecto  con el cual nesecitamos trabajar* ( ya no se usa)
**PIP** Es iun manejador de paquetes   es un comando que  me permite  instalar paquetes de **python** en nuestros proyectos--version



**COMSNDOS PARA CREAR UN ENTORNO VIRTUAL**
1. Nos ubicamos en la carpeta que deseamos crear el entorno virtual
 ```bash
cd<ruta del archivo>
#EJEMPLO
cd nombre_carpeta/ entorno_uno
```
2. Crear  el entorno virtual con el siguiente  comando

 ```bash
python -m venv < n ombre de nuestro entorno virtual>
#ejemplo
python -m venv mi_entorno

 ```
 3. Para activar el entorno virtual con el gitbash como terminal predeterminada corremos el siguiente comando solo para  windows

```bash
source venv/Scripts/activate
```

```bas
venv\Scripts\Activate.PS1
```

# para activar en power shell
 para poder ejecucutarlo en power shell como  terminal prederterninado ejecutar el siguinte comando



 ```bash
 venv\Scripts\Activate.ps1
 ```
 # PARA INSTALAR PAQUETES EN NUESTRO ENTORNO VIRTUAL
 Primero verificamos que no tengamos el paquete instyalado y lo listamos con el siguiente comando,debemos tener nuestro entorno virtual
 ```bash
 pip list
 
 ```
luego instalaremos el sigiente comando
```bash
 pip install <nombre del paquete>
 install pandas
 
 ```