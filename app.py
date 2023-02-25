from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
  return "<p>Hello, World!</p>"


if __name__ == "__main__":
  # print("i am inside the main")
  app.run(host='0.0.0.0', debug=True)
