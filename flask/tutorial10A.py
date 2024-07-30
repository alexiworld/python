from flask import Flask, render_template
from tutorial10B import blueprint

app = Flask(__name__)
app.register_blueprint(blueprint, utl_prefix="")

@app.route('/')
def home():
    return "<h1>Test</h1>";

if __name__ == "__main__":
    app.run(debug=True)