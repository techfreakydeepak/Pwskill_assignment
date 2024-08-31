from flask import Flask, jsonify

app = Flask(__name__)

#Custom error handling for 404
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Not found"}), 404

#Custom error handling for 500
@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Sample route
@app.route('/')
def index():
    return "Welcome to the Flask app!"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)