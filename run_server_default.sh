#!/usr/bin/ bash
CURRENT_DIR=`pwd`
SECRET_KEY=`poetry run python get_random_secret_key.py`
docker run --rm -p 8001:8000 -e SECRET_KEY=$SECRET_KEY --name dd-server-default -v $CURRENT_DIR/db:/opt/app/db dd/server:latest