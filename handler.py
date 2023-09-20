from flask import Blueprint, request, jsonify
from grocery.repository import data
import json

blueprint = Blueprint('my_blueprint', __name__)
grocery_data = data.main()

@blueprint.route("/get", methods=["GET"])
def get():
    return jsonify(grocery_data)


@blueprint.route("/post", methods=["POST"])
def post():
    sku = request.form.get('SKU')
    name = request.form.get('Name')
    description = request.form.get('Description')
    price = request.form.get('Price')
    quantity = request.form.get('Quantity')
    expiration_date = request.form.get('Expiration Date')

    grocery_data.append({'SKU': sku, 'Name': name, 'Description': description, 'Price': price, 'Quantity': quantity, 'Expiration Date': expiration_date})
    #return f"SKU = {sku}, Quant = {quantity}"
    return grocery_data

@blueprint.route("/delete/<sku>", methods=["DELETE"])
def delete(sku):
    deleted = False
    for item in range(len(grocery_data)):   
        #return item['SKU'] == sku 
        #return f"{item['SKU']} y {sku}"
        if grocery_data[item]['SKU'] == sku:
            del grocery_data[item]
            deleted = True
            break
       
        
    if deleted:
        return f"Borrado y queda {grocery_data}"
    else:
        return "No borrado"
    #return f"{grocery_data} y {sku}"
    #return "nada"
