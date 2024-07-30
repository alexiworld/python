from flask import Blueprint

admin = Blueprint("admin", __name__, static_folder='static', template_folder='templates')

@admin.route('/home')
@admin.route('/')
def home():
    return "<h1>Admin Home</h1>"

@admin.route('/test')
def test():
    return "<h1>Admin Test</h1>"
