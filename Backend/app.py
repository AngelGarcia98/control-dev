import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()



from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite peticiones desde el frontend

@app.route("/contacto", methods=["POST"])
@app.route("/contacto", methods=["POST"])
def contacto():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No se recibieron datos"}), 400

    nombre = data.get("nombre")
    empresa = data.get("empresa")
    correo = data.get("correo")
    telefono = data.get("telefono")
    mensaje = data.get("mensaje")

    if not nombre or not correo or not mensaje:
        return jsonify({"error": "Faltan campos obligatorios"}), 400

    # 📧 ENVIAR CORREO AQUÍ
    msg = EmailMessage()
    msg["Subject"] = "📩 Nuevo mensaje desde Control Dev"
    msg["From"] = os.getenv("EMAIL_USER")
    msg["To"] = os.getenv("EMAIL_TO")

    msg.set_content(f"""
Nombre: {nombre}
Empresa: {empresa}
Correo: {correo}
Teléfono: {telefono}

Mensaje:
{mensaje}
""")

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS"))
            smtp.send_message(msg)
    except Exception as e:
        print("❌ Error al enviar correo:", e)
        return jsonify({"error": "Error al enviar el correo"}), 500

    # 👆 AQUÍ TERMINA EL ENVÍO DE CORREO

    return jsonify({"message": "Mensaje recibido correctamente"}), 200


if __name__ == "__main__":
    app.run(debug=True)
