from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Dummy data for paintings
paintings = [
    {"id": 1, "name": "Sunset Bliss", "category": "Nature", "price": 200, "image": "static/images/sunset.jpg"},
    {"id": 2, "name": "City Lights", "category": "Urban", "price": 250, "image": "static/images/city.jpg"},
    {"id": 3, "name": "Ocean Breeze", "category": "Nature", "price": 300, "image": "static/images/ocean.jpg"}
]

cart = []

@app.route('/')
def home():
    return render_template('index.html', paintings=paintings)

@app.route('/category/<category>')
def category(category):
    filtered_paintings = [p for p in paintings if p['category'].lower() == category.lower()]
    return render_template('category.html', paintings=filtered_paintings)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    painting_id = request.json.get('id')
    painting = next((p for p in paintings if p['id'] == painting_id), None)
    if painting:
        cart.append(painting)
        return jsonify({"message": "Painting added to cart!", "cart": cart})
    return jsonify({"message": "Painting not found!"}), 404

@app.route('/cart')
def view_cart():
    return render_template('cart.html', cart=cart)

@app.route('/ar_view/<int:painting_id>')
def ar_view(painting_id):
    painting = next((p for p in paintings if p['id'] == painting_id), None)
    if not painting:
        return "Painting not found", 404
    return render_template('ar_view.html', painting=painting)

@app.route('/remove_from_cart', methods=['POST'])
def remove_from_cart():
    painting_id = request.json.get('id')
    global cart
    cart = [item for item in cart if item['id'] != painting_id]
    return jsonify({"message": "Item removed from cart!", "cart": cart})


if __name__ == '__main__':
    app.run(debug=True)
