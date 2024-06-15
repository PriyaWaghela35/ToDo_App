from flask import Flask, request, jsonify, render_template,render_template_string
from ariadne import QueryType, MutationType, make_executable_schema, graphql_sync, gql
from mutation import resolve_create_task, resolve_update_task, resolve_delete_task
from query import resolve_task, resolve_get_tasks

app = Flask(__name__)

@app.route("/graphql", methods=["GET"])
def graphql_todo():
    return render_template("todo.html")

@app.route('/')
def index():
    index_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset=utf-8/>
        <title>Todo App</title>
    </head>
    <body>
        <h1>Welcome to the Todo App</h1>
        <button onclick="location.href='/graphql'" type="button">Go to GraphQL Todo App</button>
    </body>
    </html>
    """
    return render_template_string(index_html)

if __name__ == "__main__":
    app.run(debug=True)
