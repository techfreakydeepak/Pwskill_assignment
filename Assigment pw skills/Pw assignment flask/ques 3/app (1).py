from flask import Flask

app = Flask(__name__)

@app.route("/user/<name>")
def display_dynamic(name):
    return f"Hello, {name}! :)"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)