# My Python Application

This is a simple Python application with a CI/CD pipeline set up using Travis CI.

## Features

- Greets a user.
- Includes unit tests.
- Automatically tested with Travis CI on push.

## Setup and Running

1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/my-python-app.git](https://github.com/YOUR_USERNAME/my-python-app.git)
   cd my-python-app
   ```
2. Create a virtual environment (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python myapp/main.py
   ```
5. Run tests:
   ```bash
   pytest tests/
   ```

## CI/CD with Travis CI

This project uses Travis CI for continuous integration.
- `.travis.yml` defines the build process.
- Tests are run on every push to the repository.
- Email notifications are sent on build completion.