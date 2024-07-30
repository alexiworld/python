from flask import Blueprint, render_template

blueprint = Blueprint("blueprint", __name__, static_folder='static', template_folder='templates')

@blueprint.route('/home')
@blueprint.route('/')
def home():
    return render_template("tutorial10/home.html")

@blueprint.route('/test')
def test():
    return "<h1>BP Test</h1>"
