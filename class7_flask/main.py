from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hello")
@app.route("/hello/<user>")
def index(user = None):
	return render_template("hello.html")


if __name__ == "__main__":
	app.run(debug=False)