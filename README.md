# CEEB Codes

A scraper and web application for high schools and college CEEB Codes.


## Installation

```
$ pip install -r requirements.txt
```


## Configure MongoDB

Binary backups and JSON backups can be found in `backups/`.

Restore the `colleges` collection.

```
$ mongorestore --host <HOST> --port <PORT> --username <USER> --password <PASSWORD> --collection colleges --db <DB> backups/dump/schools/colleges.bson
```

Restore the `highschools` collection.

```
$ mongorestore --host <HOST> --port <PORT> --username <USER> --password <PASSWORD> --collection highschools --db <DB> backups/dump/schools/highschools.bson
```

The scraper and web application use the environment variable `MONGO_URI` for connecting to mongo.

```
$ export MONGO_URI=<MONGO_URI>
```

If not set, the following URI will be used: `mongodb://localhost:27017/schools`.


## Heroku Configuration

Gunicorn automatically honors the WEB_CONCURRENCY environment variable, if set.

```
$ heroku config:set WEB_CONCURRENCY=3
```


## Running web application

```
$ python ceeb/app.py
```

GET /api/colleges

```
$ curl 'localhost:5000/api/colleges?state=CA&city=Alameda'
```

```
{
  "count": 1,
  "results": [
    {
      "address": {
        "city": "Alameda",
        "state": "CA"
      },
      "ceeb_code": "4118",
      "name": "Coll Alameda"
    }
  ]
}
```

GET /api/highschools

```
$ curl 'localhost:5000/api/highschools?state=NY&city=Liverpool'
```

```
{
  "count": 1,
  "results": [
    {
      "address": {
        "city": "Liverpool",
        "state": "NY"
      },
      "ceeb_code": "332850",
      "name": "Liverpool High School"
    }
  ]
}
```


## Swagger

GET /apidocs/index.html


## Running scraper

```
$ python scraper.py
```


## Running tests

```
$ pip install nose
$ nosetests
```


## LICENSE

MIT

