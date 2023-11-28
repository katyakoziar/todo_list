# TODO LIST

This to-do list site will help you manage your life and time.

## How to install the project

1) Open the terminal and navigate to the folder where you want to clone the repository.
    ```
    cd path/to/your/directory
    ```

2) Use the git clone command to clone the repository.
   ```
   git clone repository_url
   ```
   
3) Go to the project directory.
   ```angular2html
   cd task_manager_project
   ```
   
4) Create and activate a virtual environment:
   ```angular2html
   python -m venv venv
   ```
   - for Windows:
   ```angular2html
   .\venv\Scripts\activate
   ```
   - for Linux/Mac:
   ```angular2html
   source venv/bin/activate
   ```
   
5) Use pip to install the requirements.
   ```angular2html
   pip install -r requirements.txt
   ```
   
6) Apply the migrations.
   ```angular2html
   python manage.py migrate
   ```
7) Use the following command to load prepared data from fixture
```angular2html
   python manage.py loaddata db_data.json
   ```
   
8) Run the Django development server.
   ```angular2html
   python manage.py runserver
   
Run the site from a local web server:  [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

