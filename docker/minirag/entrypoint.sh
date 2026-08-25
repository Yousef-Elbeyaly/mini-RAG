#!/bin/bash
set -e

echo "Running DataBase Migration..."
export PYTHONPATH=/app

cd /app/models/db_schemes/minirag
alembic upgrade head
cd /app

echo "Starting FastAPI Server..."
exec uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4