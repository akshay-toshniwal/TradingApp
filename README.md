# Trading Project Setup

This repository contains the Trading Project. Follow the steps below to set up the project on your local machine.

## Prerequisites

- Python 3.x
- pip
- virtualenv (optional, but recommended)

### Install virtualenv if not already installed
  ```
  pip install virtualenv
```
### Create a virtual environment (replace 'venv' with your preferred name)
```
  virtualenv venv
```
### Activate the virtual environment

  #### On Windows:
```
  venv\Scripts\activate
```
  #### On macOS and Linux:
```
  source venv/bin/activate
```
## Getting Started

1. Clone the repository:

   ```
   git clone https://github.com/akshay-toshniwal/TradingProject.git
   cd TradingProject
   ```   

2. To start with project
    ```
    cd TradingProject/
    ```

3. Create media directory
    ```
    mkdir media
    ```

4. Install Django and project dependencies:

   ```
   pip install -r requirements.txt
   ```

5. Migrate the database:

   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Run the development server:

   ```
   python manage.py runserver
   ```

7. Access the application in your web browser at http://localhost:8000/
