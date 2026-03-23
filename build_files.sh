#!/bin/bash

# Install dependencies, allowing installation in a managed environment
pip install --break-system-packages -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Apply database migrations
python manage.py migrate

# Create the superuser (if it doesn't exist)
python manage.py create_superuser
