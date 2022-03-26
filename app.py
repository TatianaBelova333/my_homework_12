from flask import Flask, send_from_directory
from main.views import main_blueprint
from loader.views import post_loader_blueprint


app = Flask(__name__)


app.register_blueprint(main_blueprint)
app.register_blueprint(post_loader_blueprint, url_prefix='/post')


if __name__ == "__main__":
    app.run(debug=True)