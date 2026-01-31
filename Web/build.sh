#!/usr/bin/env bash
# Exit script on first error
set -e

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Collect static files with verbose output to debug issues
python manage.py collectstatic --no-input --verbosity 2

# Verify static files were collected
ls -la staticfiles/
