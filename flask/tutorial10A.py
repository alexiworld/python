from flask import Flask, render_template
from tutorial10B import blueprint
from admin.tutorial10C import admin

app = Flask(__name__)
app.register_blueprint(blueprint, url_prefix="/bp") 
app.register_blueprint(admin, url_prefix="/admin") 
# To learn more https://flask.palletsprojects.com/en/3.0.x/blueprints/
print(app.url_map)

@app.route('/')
def home():
    return "<h1>Test</h1>";

if __name__ == "__main__":
    app.run(debug=True)