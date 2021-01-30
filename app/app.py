from flask import Flask, render_template
from controllers.place_controller import places_blueprint

app = Flask(__name__)

app.register_blueprint(places_blueprint)

if __name__ == '__main__':
    app.run(debug=True)



@app.route('/')
def home():
    return render_template("index.html", title="Home")


