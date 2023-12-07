from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample in-memory database for demonstration
todos = [
    {
        "id": 1,
        "title": "Example 1",
        "createdAt": "2023-08-27",
        "updatedAt": "2023-10-30",
        "description": "This is example 1.",
        "completed": False
    },
    {
        "id": 2,
        "title": "Example 2",
        "createdAt": "2023-09-19",
        "updatedAt": "2023-12-01",
        "description": "This is example 2.",
        "completed": True
    },
]

# Start page
@app.route('/')
def start_page():
    return 'This is start page.\nAdd /todos to see my works'

# Route to get all todo datas with optional query parameters as GET method
@app.route('/todos', methods=['GET'])
def get_todos():
    completed_param = request.args.get('completed')
    category_param = request.args.get('category')

    # Filtering logic based on query parameters
    filtered_todos = todos
    if completed_param is not None:
        filtered_todos = [todo for todo in filtered_todos if todo["completed"] == (completed_param.lower() == 'true')]
    if category_param is not None:
        filtered_todos = [todo for todo in filtered_todos if category_param.lower() in todo["category"].lower()]

    return jsonify(filtered_todos)

# Route to create a new todo data as POST method
@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()

    # Validation with error code
    if "title" not in data or "createdAt" not in data or "updatedAt" not in data or "description" not in data:
        return jsonify({"error": "Invalid request format"}), 400

    new_todo = {
        "id": len(todos) + 1,
        "title": data["title"],
        "createdAt": data["createdAt"],
        "updatedAt": data["updatedAt"],
        "description": data["description"],
        "completed": False,
    }
    todos.append(new_todo)

    return jsonify(new_todo), 201

# Route to get a specific todo data by ID as GET method
@app.route('/todos/<int:id>', methods=['GET'])
def get_todo(id):
    todo = next((todo for todo in todos if todo["id"] == id), None)
    if todo is None:
        return jsonify({"error": "Todo not found"}), 404

    return jsonify(todo)

# Route to update a specific todo data by ID as PATCH/PUT method
@app.route('/todos/<int:id>', methods=['PATCH', 'PUT'])
def update_todo(id):
    todo = next((todo for todo in todos if todo["id"] == id), None)
    if todo is None:
        return jsonify({"error": "Todo not found"}), 404

    data = request.get_json()
    # Validation
    if "title" in data:
        todo["title"] = data["title"]
    if "description" in data:
        todo["description"] = data["description"]
    if "completed" in data:
        todo["completed"] = data["completed"]

    return jsonify(todo)

# Route to delete a specific todo data by ID as DELETE method
@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    global todos
    todos = [todo for todo in todos if todo["id"] != id]
    return jsonify({"message": "Todo deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)


