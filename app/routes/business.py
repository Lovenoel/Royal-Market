"""A module that handles the business operations."""
from flask import Blueprint, render_template, redirect, url_for, flash
from models.business import Business, db
from flask_login import login_required, current_user
from forms.BusinessProfileForm import BusinessProfileForm

business_bp = Blueprint('business', __name__, url_prefix='/business')

@business_bp.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    """Handles the business dashboard operations"""
    if current_user.is_admin:
        businesses = Business.query.filter_by(owner_id=current_user.id).all()
        return render_template('business_dashboard.html', businesses=businesses)
    else:
        return redirect(url_for('home'))
    

@business_bp.route('/create', methods=['GET', 'POST'])
def create():
    """Adds a new business."""
    if not current_user.is_authenticated:
        flash('You need to log in to add a business.', 'danger')
        return redirect(url_for('auth.login'))
    # if current_user.is_authenticated and current_user.is_admin:
    #     return redirect(url_for('business.dashboard'))
    form = BusinessProfileForm()
    if form.validate_on_submit():
        print('Form fully validated.')
        business = Business.query.filter_by(email=form.email.data).first()
        if business:
            print(f'Business found: {business}')
        new_business = Business(
            name = form.name.data,
            email = form.email.data,
            owner_id = current_user.id,
            description = form.description.data,
            location = form.location.data,
            online_available = form.online_available.data,
            offline_available = form.offline_available.data
        )
        db.session.add(new_business)
        db.session.commit()
        flash('Your business has been created','success')
        return redirect(url_for('business.dashboard'))
    return render_template(
        'create_business.html',
        form=form)


@business_bp.route('/manage', methods=['GET', 'POST'])
def manage():
    """Handles business management."""