#!/usr/bin/env bash

docker-compose run --rm app sh -c "python manage.py test"