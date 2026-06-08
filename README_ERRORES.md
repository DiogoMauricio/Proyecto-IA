# Guia de errores y soluciones

Este documento explica los errores mas comunes al ejecutar este proyecto en otra computadora y como resolverlos.

## 1. Error: `python` no se reconoce como comando

### Causa

Python no esta instalado o no fue agregado al PATH del sistema.

### Solucion

1. Instala Python desde su instalador oficial.
2. Durante la instalacion, marca la opcion para agregar Python al PATH.
3. Cierra y vuelve a abrir la terminal.
4. Verifica con:

```bash
python --version
```

Si no funciona, prueba tambien:

```bash
py --version
```

## 2. Error: `No module named flask`

### Causa

Las dependencias del proyecto no estan instaladas.

### Solucion

Ejecuta:

```bash
pip install flask flask-cors google-cloud-dialogflow
```

Si sigue fallando, prueba:

```bash
python -m pip install flask flask-cors google-cloud-dialogflow
```

## 3. Error: `No module named google.cloud`

### Causa

La libreria de Dialogflow no fue instalada correctamente.

### Solucion

Ejecuta:

```bash
python -m pip install google-cloud-dialogflow
```

Luego vuelve a correr:

```bash
python app.py
```

## 4. Error de credenciales de Google Cloud

### Posibles mensajes

- `DefaultCredentialsError`
- `File ... credencialesDialogFlow.json was not found`
- errores de autenticacion o permisos

### Causa

El archivo `credencialesDialogFlow.json` no existe, esta en otra carpeta o no pertenece al proyecto correcto de Google Cloud.

### Solucion

1. Verifica que `credencialesDialogFlow.json` este en la misma carpeta que `app.py`.
2. Confirma que el archivo no este vacio o dañado.
3. Asegurate de que la cuenta de servicio tenga permisos para Dialogflow.
4. Verifica que el proyecto configurado en el codigo sea el correcto.

## 5. Error: el servidor inicia pero el navegador no responde

### Causa

El backend no esta corriendo en el puerto esperado o el navegador esta abriendo una ruta incorrecta.

### Solucion

1. Ejecuta el proyecto con:

```bash
python app.py
```

2. Abre exactamente esta direccion:

```text
http://127.0.0.1:5000
```

3. No abras `index.html` con doble clic. Debes abrirlo a traves del servidor Flask.

## 6. Error: `Address already in use` o puerto ocupado

### Causa

El puerto `5000` ya esta siendo usado por otro programa.

### Solucion

Opcion 1: cerrar el proceso que usa el puerto.

En Windows:

```bash
netstat -ano | findstr :5000
```

Luego identifica el PID y cierralo.

Opcion 2: cambiar el puerto en `app.py`.

Busca esta linea:

```python
app.run(debug=True, port=5000, use_reloader=False)
```

Y cambia `5000` por otro valor, por ejemplo `8000`.

Si cambias el puerto, tambien debes actualizar la URL del frontend en `index.html`.

## 7. Error: el chat abre pero no responde mensajes

### Causa

El frontend si carga, pero la llamada a Dialogflow falla o el backend devuelve error.

### Solucion

Revisa lo siguiente:

1. Que `python app.py` siga activo en la terminal.
2. Que haya conexion a internet.
3. Que las credenciales sean validas.
4. Que el proyecto de Dialogflow exista y este accesible.
5. Que no haya firewall o proxy bloqueando la salida a Google Cloud.

## 8. Error: `HTTP 500` al enviar un mensaje

### Causa

En este proyecto, ese error normalmente significa que Flask no pudo comunicarse correctamente con Dialogflow.

### Solucion

Revisa:

- las credenciales
- el acceso a internet
- el `PROJECT_ID` configurado en `app.py`
- los permisos de la cuenta de servicio

Tambien revisa la terminal donde se ejecuto Flask para ver el error real.

## 9. Error: el archivo HTML abre pero no conecta con el backend

### Causa

El frontend usa una URL fija para enviar mensajes:

```text
http://127.0.0.1:5000/chat
```

Eso significa que el navegador intenta conectarse al mismo equipo donde esta corriendo Flask.

### Solucion

1. Ejecuta backend y navegador en la misma maquina.
2. Si el backend corre en otra maquina, cambia la URL en `index.html` por la IP o dominio correctos.

Ejemplo:

```text
http://192.168.1.20:5000/chat
```

## 10. Error: problemas al activar el entorno virtual en PowerShell

### Causa

PowerShell puede bloquear scripts por politicas de ejecucion.

### Solucion

Ejecuta PowerShell como usuario normal y usa:

```bash
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Luego activa el entorno virtual:

```bash
.venv\Scripts\Activate.ps1
```

## 11. Error: caracteres raros o tildes mal mostradas

### Causa

La terminal o el editor pueden estar usando una codificacion distinta.

### Solucion

1. Guarda los archivos en UTF-8.
2. Usa un navegador moderno.
3. Si el problema aparece en terminal, prueba abrir una nueva sesion de PowerShell.

## 12. El proyecto funciona en tu PC pero no en otra

### Causas mas probables

- falta Python
- faltan librerias
- faltan credenciales
- el archivo JSON pertenece a otro proyecto
- no hay internet
- el puerto esta bloqueado
- el frontend apunta a una URL incorrecta

### Lista rapida de verificacion

Antes de probar en otra PC, confirma esto:

1. Existe `app.py`.
2. Existe `index.html`.
3. Existe `credencialesDialogFlow.json`.
4. Python responde con `python --version`.
5. Las dependencias estan instaladas.
6. El servidor inicia sin errores.
7. El navegador abre `http://127.0.0.1:5000`.
8. El chat responde al menos un mensaje.

## Comandos utiles

Instalar dependencias:

```bash
python -m pip install flask flask-cors google-cloud-dialogflow
```

Crear entorno virtual:

```bash
python -m venv .venv
```

Activarlo en PowerShell:

```bash
.venv\Scripts\Activate.ps1
```

Ejecutar el proyecto:

```bash
python app.py
```

## Recomendacion final

Si vas a mover este proyecto varias veces, conviene crear tambien un `requirements.txt` para instalar todo con un solo comando y reducir errores de configuracion.