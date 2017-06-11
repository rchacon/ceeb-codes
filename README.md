# CEEB Codes

A scraper and web application for high schools and college CEEB Codes.


## Usage

```
$ docker-compose up -d
```

Restore database:

```
$ docker exec -it ceebcodes_mongo_1 /bin/bash /tmp/backups/restore.sh
```


## Heroku Configuration

Gunicorn automatically honors the WEB_CONCURRENCY environment variable, if set.

```
$ heroku config:set WEB_CONCURRENCY=3
```


## JSON endpoints

GET /api/colleges

```
$ curl 'localhost:5000/api/colleges?state=CA&city=Alameda'
```

```json
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

```json
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
$ docker exec -it ceebcodes_app_1 /bin/bash
$ python -m ceeb.scraper [--save]
```


## Running tests

```
$ virtualenv -p python3 --no-site-packages .env
$ source .env/bin/activate
$ pip install -r requirements.txt
$ pip install -r tests/requirements.txt
$ python -m pytest tests/ --cov=ceeb --cov-report term-missing
```


## LICENSE

MIT
