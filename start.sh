#!/usr/bin/env bash
set -e

echo "Installing dependencies..."
pip install -r backend/requirements.txt

echo "Starting FastAPI app..."
cd backend
uvicorn main:app --host 0.0.0.0 --port 10000
