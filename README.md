# CEEB Codes

A scraper and web application for high schools and college CEEB Codes.


## Configure MongoDB

```
$ export MONGO_URI=<MONGO_URI>
```

Default URI is `mongodb://localhost:27017/schools`.


## Run web application

```
$ python app.py
```

`GET /api/colleges`

```
$ curl 'localhost:5000/api/colleges?state=CA&city=Syracuse'
```

`GET /api/highschools`

```
$ curl 'localhost:5000/api/highschools?state=CA&city=Syracuse'
```

## Run scraper

Binary backups and JSON backups can be found in `backups/`

```
$ python scraper.py
```

## LICENSE

Copyright 2016 Raul Chacon
