# Belgrade-Meetup-Jan2019
This is the demo project I used during my talk at Python Belgrade Meetup #21


## Getting started

* Install dependencies

```bash
pip install -r requirements.txt
```

* Create a database

```bash
sudo -u postgres createdb -O <your-user> belgrade_meetup
```

* Run migrations

```bash
python3 manage.py migrate
```

* Bootstrap the database with some data

```bash
python3 manage.py loaddata bootstrap_db.json
```

* Start the local server

```
python3 manage.py runserver
```

* Bootstraped users credentials
```
Sales Team user:
    Username: sales
    Password: demo

Bookings Team user:
    Username: bookings
    Password: demo
```

## Branches roadmap

* `master` - The initial structure of the project
* `the-problem` - Introduces the problem we are solving
* `first-solution` - Adds the first temporary solution - duplicates logic
* `second-solution` - Adds the second temporary solution - optional arguments
* `third-solution` - Adds a solution with nice interface but introduces bug with a race condition
* `fourth-slution` - Final solution
* `fifth-solution` - It's a Proof of concept. I didn't show it on the meetup. I came up with this solution after the meetup.