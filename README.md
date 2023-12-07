# itclub_assignment

## Introduction
This is IT Club assignment using Flask Flamework
<br>
<br>

## Development Period
* 07 Dec 2022
<br>

## Member
- Yeonjae Lim
<br>

## Development Environment
- `Python 3.11.3`
- **Framework** : Flask
- **Database** : in-memory
<br>

## Main Features
1. Retrieve Todos
   - Use the `/todos` endpoint to retrieve a list of todos.
   - Optional query parameters for filtering by completion status and category.
3. Create New Todo
   - Add a new todo using the `/todos` endpoint with a `POST` request.
   - Ensure proper validation of the request format.
3. Retrieve Specific Todo
   - Get details of a specific todo by providing its ID to the `/todos/<id>` endpoint.
4. Update Todo
   - Modify the details of a todo using the `/todos/<id>` endpoint with `PATCH` or `PUT` requests.
   - Supports updating title, description, and completion status.
4. Delete Todo
   - Remove a todo by specifying its ID through the `/todos/<id>` endpoint with a `DELETE` request.
<br>

## How to run
1. Go to [yeonjaelim.pythonanywhere.com](yeonjaelim.pythonanywhere.com)
2. Add `/todos` to see the current data (it include in-memory data for demonstraton purpose)
3. Add `/todos/<id>` to see the data of specific ID
<br>
<br>




