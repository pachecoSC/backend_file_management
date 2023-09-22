# RMSystemPy

## entorno virtual
### crear entorno
para instalar versiones de librerias y que estas no afecten con otros proyectos es necesario crear un ambiente virtual

"ctrl" + "Shift" +"p" y elegir la opcion de "crear ambiente", crea una carpeta .venv

o por comandos en la terminal

>python -m venv .venv


### levantar entorno virual
para levantar el servidor en la terminal primero debemos activar la carpeta virtual
>source .venv/Scripts/activate

NOTA: si es la primera vez debe levantar los requerimientos que se encuentran en la parte inferior antes de usar el comando uvicorn, solo es necesario la primera vez


despues de este comendo aparece (.venv) en la terminal y luego ya se puede levantar el servidor
>uvicorn main:app --reload
### desactivar el entorno virtual
para desactivar la carpeta o entorno virtual
>deactivate

documentacion de la aplicacion, se genera de modo automatico
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc


## instalar todas las dependencias
requisito: requirements.txt

para poder instalar todas las dependencias sin hacerlo una por una realizar el siguiente comando
>pip install -r requirements.txt

## actualizar archivo de dependencias
hacerlo de manera automatica
>pip freeze > requirements.txt

## convertir en ejecutable
se agrega las siguientes lineas en el /main.py
def serve():
    """Serve the web application."""
    uvicorn.run(app, port=8001)

if __name__ == "__main__":
    serve()

despues de guardar usamos el siguiente comando y crea la carpeta /dist y el ejecutable main.exe
>pyinstaller --onefile main.py