# ToDo_App
To-Do App using Flask and GraphQL Welcome to the To-Do App! This application allows users to manage their tasks efficiently using a web interface. It is built using Flask for the backend and GraphQL for querying and mutating data.
##Table of Contents
  1.[Project Description](#project-description)
  2. [Features](#features)
  3. [Tech Stack](#tech-stack)
  4. [Installation](#installation)
  5. [Usage](#usage)
  6. [API Documentation](#api-documentation)
  7. [Contributing](#contributing)
##Project Description
  My project is a simple ToDo application built using Flask for the backend and GraphQL for managing the API. The frontend is a basic HTML template that displays a list of tasks, allowing users to add, edit, and delete tasks. This application demonstrates CRUD operations and integrates GraphQL to provide a flexible and efficient way to query and mutate data.
##Features
  -Add new task 
  - View all tasks
  - Update existing tasks
  - Delete tasks
  - Filter tasks by status (completed or pending)
##Tech Stack
  -**Frontend Framework:** Html, CSS
  - **Backend Framework:** Flask
  - **API Query Language:** GraphQL
  - **Other Libraries:** Flask-GraphQL, Ariadne
## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**
    ```sh
    git clone https://github.com/PriyaWaghela35/ToDo_App
    ```
2. **Create a virtual environment:**
    ```sh
    python -m venv venv
    ```
3. **Activate the virtual environment:**
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On MacOS/Linux:
        ```sh
        source venv/bin/activate
        ```
4. **Install dependencies:**
    ```sh
    pip install flask flask-grapghql graphene
    ```
5.**Run the application:**
    ```sh
    python app.run
    ```

The application should now be running on `http://127.0.0.1:5000/`.

## Usage

To interact with the GraphQL API, you can use tools like [GraphiQL](https://github.com/graphql/graphiql)

### Example Queries

- **Fetch all tasks:**
    ```graphql
    {
      allTasks {
        id
        title
        description
        completed
      }
    }
    ```

- **Add a new task:**
    ```graphql
    mutation {
      addTask(title: "New Task", description: "Task description") {
        id
        title
        description
        completed
      }
    }
    ```

- **Update a task:**
    ```graphql
    mutation {
      updateTask(id: 1, title: "Updated Task", description: "Updated description", completed: true) {
        id
        title
        description
        completed
      }
    }
    ```

- **Delete a task:**
    ```graphql
    mutation {
      deleteTask(id: 1) {
        id
      }
    }
    ```

## API Documentation

### Endpoints

- **GraphQL Endpoint:**
    You can query and mutate tasks using this endpoint.


## Contact

- **Author:** Priya Waghela
- **Email:** priyawaghela352gmail.com
- **GitHub:** https://github.com/PriyaWaghela35
