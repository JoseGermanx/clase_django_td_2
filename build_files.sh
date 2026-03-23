#!/bin/bash

# Vercel now automatically installs dependencies from requirements.txt
# using a tool called 'uv'. The 'pip install' command is no longer needed here.

# Collect static files
python manage.py collectstatic --noinput

# Apply database migrations
python manage.py migrate
