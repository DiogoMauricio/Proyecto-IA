import os

from flask import Flask, jsonify, request
from flask_cors import CORS
from google.cloud import dialogflow_v2 as dialogflow


# Configura la ruta al archivo JSON de credenciales de Google Cloud.
# Reemplaza este valor con la ruta real en tu entorno.
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credencialesDialogFlow.json"

# Completa estos valores con tu configuracion de Dialogflow.
PROJECT_ID = "impresi-n3d-chatbot-ggdo"
SESSION_ID = "chatbot_IA__id"
LANGUAGE_CODE = "es"


# Inicializa la aplicacion Flask y habilita CORS para el frontend.
app = Flask(__name__)
CORS(app)


@app.route("/chat", methods=["POST"])
def chat():
    # Obtiene el texto y también busca si viene un archivo en el paquete
    mensaje = request.form.get("mensaje", "").strip()
    archivo = request.files.get("archivo")

    # Si el alumno sube un .stl sin escribir texto, le inventamos un mensaje interno para que Dialogflow lo entienda
    if not mensaje and archivo:
        mensaje = "He enviado un archivo adjunto"

    # Ahora el portero solo bloquea si no hay NI mensaje NI archivo
    if not mensaje:
        return jsonify({"error": "Debes enviar un mensaje valido."}), 400

        # (A partir de aquí, deja el resto de tu código tal como estaba, creando el session_client, etc.)
    try:
        # Crea el cliente de sesiones de Dialogflow.
        session_client = dialogflow.SessionsClient()

        # Construye la ruta de sesion usando el proyecto y la sesion definidos.
        session = session_client.session_path(PROJECT_ID, SESSION_ID)

        # Prepara el texto del usuario para que Dialogflow lo procese.
        text_input = dialogflow.TextInput(text=mensaje, language_code=LANGUAGE_CODE)
        query_input = dialogflow.QueryInput(text=text_input)

        # Envia el mensaje a Dialogflow y recibe la respuesta del agente.
        response = session_client.detect_intent(
            request={"session": session, "query_input": query_input}
        )

        # Extrae el texto final que el bot debe devolver al frontend.
        fulfillment_text = response.query_result.fulfillment_text

        return jsonify({"respuesta": fulfillment_text})
    except Exception:
        # Devuelve un error amigable si falla la comunicacion con Google Cloud.
        return jsonify({"error": "No se pudo procesar la solicitud en este momento."}), 500


if __name__ == "__main__":
    # Ejecuta el servidor Flask en modo debug sobre el puerto solicitado.
    app.run(debug=True, port=5000)