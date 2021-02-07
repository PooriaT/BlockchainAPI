# Blockchain API build on Django Rest Framework

Implement API via Django and Djano rest framework
that:
1. allows user to register and login via API
2. allows authenticated user to search address or transaction of ETH BTC or BCH (you can use blockchain.info API to check transactions and addresses)
3. All searches should be logged and user should be able to see his past searches and mark and address as 'mine'
4. All views, serializers and logic must have tests (we prefer numpy)

Bonus:

a. index past searches with elastic search and have an suggestion endpoint for the search box

b. wrap your application in docker with gunicorn and nginx server in reverse proxy

c. make some minimal frontend for the search / search history / my addresses functionality (login is not required, we will set the access token manually in the localStorage using chrome dev tools)
There is no need to write tests for the frontend!
d. describe your API with apiary


## Installation

### Creating Virtual Environment

```bash
mkdir myproject
cd myproject
python3 -m venv venv
```

### Installing the required libraries

Then installing the Django and Django Rest Framework library:

```bash
pip install django
pip install djangorestframework
```
In addition, in this project **requests** library is used.

```bash
pip install reqests
```

To build the Database, it requires to do the `migrations`:

```bash
python manage.py makemigrations <paymentapi>
python manage.py migrate
```

Then create the superuser:

```bash
python manage.py createsuperuser
```


## Applied Bitaps API inside the implemented API:

I am using Bitcoin Developer Center API for retrieving the blocks info.

https://api.bitaps.com/{currency}/v1/blockchain/
**currency**: btc, eth, bch

**Transactions**:  /transaction/{hash}

**Address state**: /address/state/{address}

**Address transactions**:  /address/transactions/{address}

For more information, visit the below link:
https://developer.bitaps.com/blockchain


## Running the application

After installing prerequisites, now you are ready to run the application.
To run it in developer mode, use the below command:

```bash
python manage.py runserver
```

To **regsiter** new user: <url>/register/

To **Login**: <url>/api-auth/login/

To **logout**: <url>/api-auth/logout/

To search for new cryptocurrencies blocks based on available address: <url>/address/

To search for new cryptocurrencies blocks based on available hash: <url>/transaction/

To query your address-based searches: <url>/address/history/

To query your hash-based searched: <url>/transaction/history/

## Test

To run the test case, use the below command:

```bash
python manage.py test
```
### Coverage test

To test the coverage test, first we should install below package:

```bash
pip install coverage
```

After that we can run the below command to create the coverage report:

```bash
coverage run --source='.' manage.py test paymentapi
```

After creating the report, there are two ways to show the report, one on the command line and the other is in HTML format.

#### Command line report

```bash
coverage report -m
```

#### HTML report

```bash
coverage html -d <dir-name>
```

## Documentation

A simple document for this API was build by **Apiary**:
https://blockchain14.docs.apiary.io/


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
