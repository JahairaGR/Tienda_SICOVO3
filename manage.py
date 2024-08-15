from app import inicializar_app
from config import config

# Cargar la configuración
configuracion = config['development']
app = inicializar_app(configuracion)

if __name__ == '__main__':
    # Ejecutar la aplicación con el servidor integrado de Flask
    app.run(host='127.0.0.1', port=5000)
