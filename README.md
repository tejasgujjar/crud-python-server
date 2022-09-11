# crud-python-server

```
$ cd crud-python-server

$ virtual env
$ source env/bin/activate

$ pip install -r requirements.txt

$ flask run
```

Go to http://127.0.0.1:5000

## APIs
APIs for CRUD operations on a user
### GET
- Get list of all users `/users`
- Get single user `/users/<email>`

### POST
- Create a new user `/users`
```
{
    "email": "tejas@gmail",
    "password": "12344",
    "firstname": "test",
    "lastname": "gujjar"
}
```

### PUT
- Update an existing user `/users/<email>`
```
{
    "password": "12344",
    "firstname": "test",
    "lastname": "gujjar"
}
```

### DELETE
- Delete an existing user `/users/<email>`