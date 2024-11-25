"""A module that handles the documents of the application"""

from flask import Blueprint, redirect, render_template, url_for


document_bp = Blueprint('documents', __name__, url_prefix='/documents')


@document_bp.route('/terms-of-service', methods=['GET', 'POST'])
def terms_of_service():
    """Handles the terms of service for the whole app"""
    return render_template('terms_of_service.html')

@document_bp.route('/privacy-policy', methods=['GET', 'POST'])
def privacy_policy():
    """Handles the privacy policy for the whole app"""
    return render_template('privacy_policy.html')

@document_bp.route('/contact-us')
def contact_us():
    """Handles the app's contact info"""
    return render_template('contact_us.html')