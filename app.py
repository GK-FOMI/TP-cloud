import os
from flask import Flask

app = Flask(__name__)

# Route principale (/)
@app.route('/')
def home():
    # Récupère la variable d'environnement, ou met un texte par défaut si elle n'existe pas
    message = os.environ.get('APP_MESSAGE', 'Message par défaut')
    return f"Service Models Lab 2<br>Message: {message}"

# Route de santé (/health)
@app.route('/health')
def health():
    return "OK"

if __name__ == "__main__":
    # Le PaaS va fournir un port dynamique, on l'écoute
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)