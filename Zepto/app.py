from flask import Flask, request

app = Flask(__name__)

# sample data
products = [
    {'id': 1, 'name': 'samsung galaxy s24', 'price': 70000},
    {'id': 2, 'name': 'iPhone 15', 'price': 90000},
    {'id': 3, 'name': 'Google Pixel 8', 'price': 60000}  
]


# get all products
@app.route('/products',methods=['GET'])
def get_products():
    return products

# get product by id
@app.route("/product/<product_id>", methods=['GET'])
def get_product(product_id):
    product_id = int(product_id)  # convert the product_id from string to integer
    for product in products:
        if product['id'] == product_id:
            return product
    
    return {"message": "Product not found"}

# adding a new product
@app.route('/products', methods=['POST'])
def add_product():
    request_data = request.get_json()

    new_product = {
        'id': len(products) + 1,
        'name': request_data['name'],
        'price': request_data['price']
    }

    products.append(new_product)

    return {"message": "Product added successfully", 
            "product": new_product}





app.run(debug=True)