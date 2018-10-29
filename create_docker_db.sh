#Want to use this for testing the creation of mysql databases in a docker container

docker run --name mysql -d -e MYSQL_RANDOM_ROOT_PASSWORD=yes \
    -e MYSQL_DATABASE=eplApi -e MYSQL_USER=flaskuser \
    -e MYSQL_PASSWORD=Bun6#0le \
    mysql/mysql-server:5.7