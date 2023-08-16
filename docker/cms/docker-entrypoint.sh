#!/bin/bash

# migrate
python manage.py migrate --noinput

# collect static
python manage.py collectstatic --noinput

exec "$@"
