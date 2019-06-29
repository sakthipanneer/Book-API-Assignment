# Book-API-Assignment

- Create a folder to clone (or) download the code
- Install the git :

    ubuntu :
    ```
    $ git init
    ```
    windows :

    Download the git software from the [link](https://git-scm.com/download/win) and install it


- Install the python, if you are windows user use the [link](https://www.python.org/downloads/) to install it, or if you have any queries follow the stackoverflow [link](https://stackoverflow.com/questions/21372637/installing-python-2-7-on-windows-8)

- Install the pip :

    ubuntu :
    ```
    $ sudo apt-get update && sudo apt-get -y upgrade
    $ sudo apt-get install python-pip
    $ pip -V (or) pip --version
    ```
    windows :
    To install pip, securely download [get-pip.py](https://bootstrap.pypa.io/get-pip.py)
    Then run the following:
    ```
    $ python get-pip.py
    $ pip -V (or) pip --version
    ```

- Create a Virtual Environment to maintain isolated Python environments. To know more refer [here](https://virtualenv.pypa.io/en/stable/)

    Install Virtual Environment by using this command in terminal :
    ```
    $ pip install virtualenv
    ```
    Create a Virtual Environment by
    ```
    $ virtualenv test_env (You can specify your env name)
    ```
    Activate the Virtual Environment by

    ubuntu :
    ```
    source test_env/bin/activate
    ```
    windows :
    ```
    test_env\bin\activate
    ```
- Clone or Download the project source code:

    Steps to clone :
    ```
    $ https://github.com/sakthipanneer/Book-API-Assignment.git
    ```
- Enter the project folder in terminal
    ```
    $ cd Book-API-Assignment
    ```
- Install dependicies by requirements.txt
    ```
    pip install -r requirements.txt
    ```
- Create a postgres database with following details
    ```
    DB name: books,
    User: postgres,
    Password: root
    ```
    If you have any doubt in creating a user and DB refer this [link](https://medium.com/coding-blocks/creating-user-database-and-adding-access-on-postgresql-8bfcd2f4a91e)
- Run the Django apps by
    ```
    python manage.py runserver 8000(Port whatever you want)
    ```
    or
    ```
    python manage.py runserver 0.0.0.0:8000(To access from outside system)
    ```
    it can help you access from some other machines
- If any DB migration warning is thrown from terminal, use the command
    ```
    $ python manage.py makemigrations

    $ python manage.py migrate
    ```
- Run test case by,
    ```
    $ python manage.py test
    ```



## API Requirements urls

### Requirements 1
[Link 1](http://localhost:8000/api/external-books/?name=Book)

### Requirements 2
[Create](http://localhost:8000/api/v1/books/)

[Read](http://localhost:8000/api/v1/books/)

[Read with filter](http://localhost:8000/api/v1/books?name=Book1)

[Retrieve](http://localhost:8000/api/v1/books/:id)

[Patch](http://localhost:8000/api/v1/books/:id)

[Delete](http://localhost:8000/api/v1/books/:id)

