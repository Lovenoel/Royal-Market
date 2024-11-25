"""The main application's entry point."""
from flask import (
    Flask, redirect, render_template, Response,
    request,
    url_for, make_response)
from models import login_Manager, db
from routes import bcrypt
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()

# The main app instance
app = Flask(__name__)

csrf.init_app(app)
# Import Configurations
from config import Config
app.config.from_object(Config)
bcrypt.init_app(app)
db.init_app(app)
login_Manager.init_app(app)
# login_Manager.login_view = 'auth.login'

# Import blueprints
from routes.auth import auth_bp as auth_bp
from routes.business import business_bp as business_bp
from services.services import service_bp as service_bp
from services.product import product_bp as product_bp
from routes.documents import document_bp as document_bp
#from routes.upload import upload_bp as upload_bp

# Register blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(business_bp, url_prefix='/business')
app.register_blueprint(service_bp, url_prefix='/service')
app.register_blueprint(product_bp, url_prefix='/product')
app.register_blueprint(document_bp, url_prefix='/documents')
#app.register_blueprint(upload_bp, url_prefix='/upload')

@app.route('/')
def home():
    """A route that returns the home route"""
    return render_template('index.html')

@app.errorhandler(401)
def unauthorized_error(error):
    return redirect(url_for('auth.login'))


# Routes to handle cookies
# Setting and storing cookies
@app.route('/set_cookie')
def set_cookie():
    """Sets cookies for storage"""
    response = make_response("Cookie is set!")
    response.set_cookie('user_id', value='12345', max_age=60*60*24)  # Expires in 1 day
    return response


# Retrieving Cookies
@app.route('/get_cookie')
def get_cookie():
    """ Retrieves/Gets Cookies """
    user_id = request.cookies.get('user_id')  # Get cookie value
    return f"The user ID is {user_id}" if user_id else "No cookie found."


# Deleting Cookies
@app.route('/delete_cookie')
def delete_cookie():
    """ Deletes cookies."""
    response = make_response("Cookie deleted!")
    response.set_cookie('user_id', '', expires=0)
    return response


@app.route('/track', methods=['POST'])
def track_user():
    """Tracks the cookies behaviour."""
    data = request.get_json()
    print(f"Element clicked: {data['element']} at {data['timestamp']}")
    return "Tracked", 200



if __name__ == '__main__':
    app.run(debug=True)