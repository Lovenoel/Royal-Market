"""Checks for the file type"""
from app import app

def allowed_file(filename):
    """Checks and returns allowed files."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']