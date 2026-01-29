from flask import Flask , render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "red"

@app.route('/grey')
def indexxx():
    return "redfghkl;"

if __name__ == "__main__":
    app.run()

