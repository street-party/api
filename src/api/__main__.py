from src.api.api import connexion_app
from src.api.config import PYTHON_MODULE_PORT


if __name__ == '__main__':
    connexion_app.run(host='0.0.0.0', port=PYTHON_MODULE_PORT)
