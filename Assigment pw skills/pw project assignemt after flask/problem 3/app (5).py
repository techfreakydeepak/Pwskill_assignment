from flask import Flask, render_template, redirect, url_for
from flask_dance.contrib.google import make_google_blueprint, google
from flask_dance.contrib.facebook import make_facebook_blueprint, facebook

app = Flask(__name__)
app.secret_key = 'your-secret-key'  

# Google OAuth2 blueprint
google_blueprint = make_google_blueprint(
    client_id='your-google-client-id',  
    client_secret='your-google-client-secret', 
    scope=['profile', 'email']
)
app.register_blueprint(google_blueprint, url_prefix='/login')

#Facebook OAuth2 blueprint
facebook_blueprint = make_facebook_blueprint(
    client_id='your-facebook-app-id', 
    client_secret='your-facebook-app-secret',  
)
app.register_blueprint(facebook_blueprint, url_prefix='/login')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def index():
    if not google.authorized and not facebook.authorized:
        return redirect(url_for('google.login'))  
    return 'You are logged in!'

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000)