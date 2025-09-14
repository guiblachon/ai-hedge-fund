"""
Railway entry point for the AI Hedge Fund FastAPI application.
This file imports the FastAPI app from the backend directory.
"""
import sys
import os
from pathlib import Path

# Add the app directory to Python path
app_dir = Path(__file__).parent / "app"
sys.path.insert(0, str(app_dir))

# Import the FastAPI app from the backend
from app.backend.main import app

# This is the app that Railway will run
__all__ = ["app"]
