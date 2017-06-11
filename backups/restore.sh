#! /bin/bash

# docker exec -it ceebcodes_mongo_1 /bin/bash /tmp/backups/restore.sh

mongorestore  --collection colleges --db schools /tmp/backups/dump/schools/colleges.bson
mongorestore  --collection highschools --db schools /tmp/backups/dump/schools/highschools.bson
