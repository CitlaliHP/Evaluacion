
from flask import Flask
from controllers.data_controller import data_blueprint

app = Flask(__name__)
app.secret_key = 'clave-secreta'
app.register_blueprint(data_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
