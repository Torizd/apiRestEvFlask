from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

# Datos de ejemplo en formato JSON
data = [
    {"id": 1, "name": "Item 1", "value": "Value 1"},
    {"id": 2, "name": "Item 2", "value": "Value 2"},
    {"id": 3, "name": "Item 3", "value": "Value 3"}
]

# Ruta GET
@app.route('/get', methods=['GET'])
def get_items():
    return jsonify(data)

# Ruta POST
@app.route('/post', methods=['POST'])
def add_item():
    new_item = request.json
    data.append(new_item)
    return jsonify(new_item), 201

# Ruta PUT
@app.route('/put/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    updated_item = request.json
    for item in data:
        if item['id'] == item_id:
            item.update(updated_item)
            return jsonify(item)
    return jsonify({"message": "Item not found"}), 404

# Ruta DELETE
@app.route('/delete/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global data
    data = [item for item in data if item['id'] != item_id]
    return jsonify({"message": "Item deleted"}), 200

# Ruta para crear una cookie
@app.route('/cookie', methods=['GET'])
def set_cookie():
    resp = make_response("Cookie is set")
    resp.set_cookie('username', 'DiegoToriz')
    resp.set_cookie('career', 'Cibernetica')
    return resp

# Ruta para leer las cookies
@app.route('/getcookies', methods=['GET'])
def get_cookies():
    username = request.cookies.get('username')
    career = request.cookies.get('career')
    return jsonify({"username": username, "career": career})

if __name__ == '__main__':
    app.run(port=3000)
