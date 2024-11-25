from flask import Blueprint, request, jsonify
from models import db
from models.product import Product


product_bp = Blueprint('product_service', __name__, url_prefix='/product')

# CRUD for Products

@product_bp.route('/create', methods=['POST'])
def create():
    """Adds a new product to the business"""
    data = request.json
    new_product = Product(
        name=data['name'],
        description=data.get('description', ''),
        price=data['price'],
        quantity=data['quantity']
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"message": "Product added successfully"}), 201

@product_bp.route('/products/<int:id>', methods=['PUT'])
def update(id):
    """Updates the products' credentials"""
    data = request.json
    product = Product.query.get_or_404(id)
    product.name = data['name']
    product.description = data.get('description', product.description)
    product.price = data['price']
    product.quantity = data['quantity']
    db.session.commit()
    return jsonify({"message": "Product updated successfully"}), 200

@product_bp.route('/products/<int:id>', methods=['DELETE'])
def delete(id):
    """Deletes an existing product"""
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted successfully"}), 200

@product_bp.route('/products', methods=['GET'])
def get():
    """Gets all the products in the business."""
    products = Product.query.all()
    return jsonify([{
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'quantity': product.quantity,
        'created_at': product.created_at,
        'updated_at': product.updated_at
    } for product in products]), 200

@product_bp.route('/buy/<int:id>', methods=['POST'])
def buy(id):
    """Handles the buying of a product."""
    data = request.json
    product = Product.query.get_or_404(id)
    
    if product.quantity < data['quantity']:
        return jsonify({"message": "Not enough stock"}), 400
    
    # Process payment logic (simplified)
    total_cost = product.price * data['quantity']
    
    # Update stock
    product.quantity -= data['quantity']
    db.session.commit()
    
    return jsonify(
        {"message": f"Bought {data['quantity']} {product.name}(s) for ${total_cost}"}), 200