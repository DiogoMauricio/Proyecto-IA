# Chatbot Dialogflow con Flask

Este proyecto levanta un servidor Flask que sirve la interfaz web del chatbot y reenvia los mensajes a Dialogflow.

## Requisitos

- Python 3.10 o superior
- Conexion a internet
- Una cuenta de Google Cloud con acceso a Dialogflow
- El archivo de credenciales `credencialesDialogFlow.json`

## Archivos del proyecto

- `app.py`: backend Flask y conexion con Dialogflow
- `index.html`: interfaz web del chatbot
- `credencialesDialogFlow.json`: credenciales de Google Cloud

## Dependencias de Python

Instala estas librerias:

```bash
pip install flask flask-cors google-cloud-dialogflow
```

## Como ejecutar el proyecto

1. Abre una terminal en la carpeta del proyecto.
2. Instala las dependencias si aun no lo hiciste.
3. Ejecuta el servidor:

```bash
python app.py
```

4. Abre el navegador en esta direccion:

```text
http://127.0.0.1:5000
```

## Como moverlo a otro equipo

En el otro equipo debes copiar estos archivos:

- `app.py`
- `index.html`
- `credencialesDialogFlow.json`

Luego debes:

1. Instalar Python 3.10 o superior.
2. Instalar las dependencias:

```bash
pip install flask flask-cors google-cloud-dialogflow
```

3. Verificar que el archivo `credencialesDialogFlow.json` este en la misma carpeta que `app.py`.
4. Ejecutar:

```bash
python app.py
```

5. Abrir en el navegador:

```text
http://127.0.0.1:5000
```

## Configuracion actual del proyecto

El backend esta configurado actualmente con estos valores en `app.py`:

- `PROJECT_ID = "impresi-n3d-chatbot-ggdo"`
- `SESSION_ID = "chatbot_IA__id"`
- `LANGUAGE_CODE = "es"`

Ademas, el proyecto define automaticamente la variable de entorno `GOOGLE_APPLICATION_CREDENTIALS` apuntando al archivo local de credenciales.

## Importante

- El puerto `5000` debe estar libre.
- El archivo de credenciales no debe compartirse publicamente.
- El equipo donde se ejecute debe tener acceso a internet para conectarse a Dialogflow.
- La interfaz hace las peticiones a `http://127.0.0.1:5000/chat`, por lo que backend y navegador deben ejecutarse en la misma maquina si no cambias esa URL.

## Problemas comunes

### Error al instalar librerias

Prueba:

```bash
python -m pip install flask flask-cors google-cloud-dialogflow
```

### Error de credenciales

Verifica que el archivo `credencialesDialogFlow.json` exista en la carpeta del proyecto y que pertenezca al proyecto correcto de Google Cloud.

### El navegador no carga respuestas

Revisa que:

- `python app.py` siga ejecutandose
- no haya errores en la terminal
- el puerto `5000` no este bloqueado
- haya conexion a internet

## Recomendacion opcional

Para evitar conflictos entre proyectos, puedes crear un entorno virtual:

```bash
python -m venv .venv
```

En Windows PowerShell:

```bash
.venv\Scripts\Activate.ps1
```

Despues instala las dependencias y ejecuta el proyecto normalmente.