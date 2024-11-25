from flask import Blueprint, request, jsonify
from models import db
from models.service import Service

service_bp = Blueprint('service', __name__, url_prefix='/service')

# CRUD for Services

@service_bp.route('/services', methods=['POST'])
def add_service():
    data = request.json
    new_service = Service(
        name=data['name'],
        description=data.get('description', ''),
        price=data['price'],
        duration=data['duration']
    )
    db.session.add(new_service)
    db.session.commit()
    return jsonify({"message": "Service added successfully"}), 201

@service_bp.route('/services/<int:id>', methods=['PUT'])
def update_service(id):
    data = request.json
    service = Service.query.get_or_404(id)
    service.name = data['name']
    service.description = data.get('description', service.description)
    service.price = data['price']
    service.duration = data['duration']
    db.session.commit()
    return jsonify({"message": "Service updated successfully"}), 200

@service_bp.route('/services/<int:id>', methods=['DELETE'])
def delete_service(id):
    service = Service.query.get_or_404(id)
    db.session.delete(service)
    db.session.commit()
    return jsonify({"message": "Service deleted successfully"}), 200

@service_bp.route('/services', methods=['GET'])
def get_services():
    services = Service.query.all()
    return jsonify([{
        'id': service.id,
        'name': service.name,
        'description': service.description,
        'price': service.price,
        'duration': service.duration,
        'created_at': service.created_at,
        'updated_at': service.updated_at
    } for service in services]), 200
