# FastAPI Project

This is a FastAPI project that includes user authentication (sign-up, log-in, and fetching user details) with JWT-based authentication and MongoDB as the database. This project follows best practices in folder structure and code organization.

## Why This Structure is Best Practice

### Separation of Concerns

Each component (models, schemas, services, endpoints) is separated, making the codebase more maintainable and understandable. This modular approach ensures that changes in one part of the application do not affect others, reducing the risk of introducing bugs.

### Scalability

The directory structure supports scaling by organizing the code into distinct functional areas. As the application grows, new features and modules can be added without cluttering the existing codebase.

### Versioning

API versioning is incorporated, allowing for future expansions and backward compatibility. This is essential for maintaining and updating APIs without disrupting existing clients.

### Security

Security configurations and mechanisms (like JWT handling) are isolated in a dedicated module. This makes it easier to manage and update security policies without affecting other parts of the application.

### Configuration Management

Centralized configuration settings using environment variables for better manageability. This allows for easy changes in configuration without modifying the codebase, supporting different environments like development, testing, and production.

## Table of Contents
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Environment Variables](#environment-variables)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

```plaintext
fastAPI-structure/
│
├── app/
│   ├── api/
│   │   └── v1/
│   │       └── endpoints/
│   │           └── users.py
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   ├── db/
│   │   └── database.py
│   ├── models/
│   │   └── user.py
│   ├── schemas/
│   │   └── user.py
│   ├── services/
│   │   └── user.py
│   └── main.py
│
├── mongodb_data/
│
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation

### Prerequisites

- Python 3.9 or higher
- MongoDB 6.0 or higher

### Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/fastapi_project.git
    cd fastapi_project
    ```

2. Create and activate a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up MongoDB:
    Ensure MongoDB is installed and running on your local machine. If not, install it using Homebrew:

    ```sh
    /opt/homebrew/bin/brew tap mongodb/brew
    /opt/homebrew/bin/brew install mongodb-community@6.0
    ```

    Start MongoDB service:
    ```sh
    /opt/homebrew/bin/brew services start mongodb/brew/mongodb-community@6.0
    ```

5. Configure environment variables:
    Create a `.env` file in the root directory and add the following environment variables:
    ```env
    MONGODB_URI="mongodb://localhost:27017"
    SECRET_KEY="your_secret_key"
    ALGORITHM="HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    ```

## Running the Application

To run the FastAPI application, use the following command:

```sh
uvicorn app.main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

## API Endpoints

### POST /api/v1/signup
Sign up a new user.

#### Request Body
```json
{
  "username": "string",
  "email": "string",
  "password": "string"
}
```

#### Response
```json
{
  "username": "string",
  "email": "string",
  "id": "string"
}
```

### POST /api/v1/login
Log in a user and get a JWT token.

#### Request Body
```json
{
  "username": "string",
  "password": "string"
}
```

#### Response
```json
{
  "access_token": "string",
  "token_type": "bearer"
}
```

### GET /api/v1/users/me
Get details of the currently authenticated user.

#### Headers
```http
Authorization: Bearer <JWT token>
```

#### Response
```json
{
  "username": "string",
  "email": "string",
  "id": "string"
}
```

## Environment Variables

The project uses environment variables for configuration. These are set in the `.env` file in the root directory.

- `MONGODB_URI`: URI for connecting to MongoDB.
- `SECRET_KEY`: Secret key for JWT encoding and decoding.
- `ALGORITHM`: Algorithm used for JWT.
- `ACCESS_TOKEN_EXPIRE_MINUTES`: Expiration time for access tokens in minutes.

## Dependencies

- `fastapi==0.95.2`
- `uvicorn==0.30.1`
- `pydantic==1.10.7`
- `pydantic-settings==2.3.4`
- `python-dotenv==1.0.1`
- `motor==3.2.0`
- `passlib==1.7.4`
- `python-jose==3.3.0`
- `bcrypt==4.0.1`
- `email-validator==2.0.0`
- `python-multipart==0.0.5`

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

This README provides a detailed overview of the project, including installation instructions, project structure, API endpoints, and other necessary details to help users understand and use the project.