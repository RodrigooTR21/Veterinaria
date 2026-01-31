#!/usr/bin/env bash
# Exit script on first error
set -e

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --no-input
