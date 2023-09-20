from flask import Blueprint

blueprint = Blueprint('hello_blueprint', __name__)

@blueprint.route('/hello', methods=["GET"])
def hello():
    return "HELLO WORLD"
