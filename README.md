# Med Consultation API

The Med Consultation API is a Django Rest Framework (DRF) based platform designed for online medical consultations, appointment scheduling, and patient management.

## Table of Contents
1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Project Structure](#project-structure)
4. [Installation](#installation)
5. [Environment Variables](#environment-variables)
6. [Running the Application](#running-the-application)
7. [API Documentation](#api-documentation)
8. [Best Practices Followed](#best-practices-followed)
9. [Contributing](#contributing)
10. [License](#license)

---

## Features
- User authentication and authorization using Django Rest Framework's Token Authentication
- Role-based access control (Doctors, Patients, Admin)
- Appointment scheduling and management
- Patient record management
- Secure APIs with Token-based authentication
- Comprehensive error handling and input validation

## Technologies Used
- **Programming Language:** Python
- **Framework:** Django, Django Rest Framework (DRF)
- **Database:** PostgreSQL
- **Authentication:** Token Authentication
- **Containerization:** Docker
- **Testing:** Pytest
- **Documentation:** DRF's built-in API documentation and Swagger/OpenAPI

## Project Structure
```plaintext
med-consultation-api/
├── app/
│   ├── manage.py               # Entry point of the Django project
│   ├── settings/                # Configuration and environment settings
│   ├── models/                  # Database models
│   ├── views/                   # API view logic
│   ├── urls.py                  # URL routing
│   ├── serializers/             # DRF serializers for request and response validation
│   ├── utils/                   # Utility functions
├── tests/                       # Test cases for the application
├── Dockerfile                   # Docker configuration
├── requirements.txt             # Python dependencies
├── .env.example                 # Example environment variables file
└── README.md                    # Project documentation
```

## Installation
### Prerequisites
- Python 3.9+
- PostgreSQL
- Docker (Optional for containerized deployment)

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/themusharraf/med-consultation-api.git
    cd med-consultation-api
    ```
2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Environment Variables
Create a `.env` file in the project root by copying `.env.example`:
```bash
cp .env.example .env
```
Fill in the required environment variables:
```plaintext
DATABASE_URL=postgresql://user:password@localhost:5432/medconsultation
SECRET_KEY=your_django_secret_key
DEBUG=True
ALLOWED_HOSTS=*
```

## Running the Application
### Locally
```bash
python manage.py migrate
python manage.py runserver
```

## API Documentation
Once the application is running, visit:
- DRF's Browsable API: [http://localhost:8000/api/](http://localhost:8000/api/)
- Swagger/OpenAPI: [http://localhost:8000/docs](http://localhost:8000/docs) (if configured)

## Best Practices Followed
1. **Modular Architecture:** Organized code into views, serializers, and models.
2. **Database Migrations:** Use of Django's migration system.
3. **Environment Variables:** Secure and configurable environment settings.
4. **Secure Authentication:** Token-based authentication for API security.
5. **Data Validation:** Use of DRF serializers for request and response validation.
6. **Exception Handling:** Comprehensive error handling for better API responses.
7. **Testing:** Unit and integration tests using Pytest.
8. **Logging:** Standard logging practices for monitoring and debugging.
9. **Documentation:** Auto-generated API documentation with Swagger and DRF.
10. **Containerization:** Dockerized application for consistency across environments.

## Contributing
Contributions are welcome! Follow these steps:
1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.


