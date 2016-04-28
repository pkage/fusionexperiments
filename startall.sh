#! /bin/sh

echo "unloading previous virtual environments"
deactivate

echo "loading project's virtual environment"
. fe/bin/activate

echo "starting scss watcher..."
scss --watch app/scss/main.scss:app/static/css/main.css &

echo "starting mongo...."
mongod --dbpath db/ > /dev/null &

echo "done!"

