"""A module for file uploads"""
from flask import Blueprint, request, jsonify, current_app
from werkzeug.utils import secure_filename
import os
from app.utils import allowed_file

upload_bp = Blueprint('upload', __name__, url_prefix='/upload')

@upload_bp.route('/upload', methods=['POST'])
def upload_file():
    """Uploads a file to the application's file system"""
    if 'file' not in request.files:
        return jsonify({"message": "No file part"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        return jsonify({"message": "File uploaded successfully", "file_path": file_path}), 200
    
    return jsonify({"message": "Invalid file type"}), 400


@upload_bp.route('/upload/multiple', methods=['POST'])
def upload_multiple_files():
    if 'files' not in request.files:
        return jsonify({"message": "No file part"}), 400

    files = request.files.getlist('files')
    file_paths = []
    
    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            file_paths.append(file_path)
    
    return jsonify({"message": "Files uploaded successfully", "file_paths": file_paths}), 200