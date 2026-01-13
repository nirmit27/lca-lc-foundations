"""
Settings and configuration
"""

import os
from dotenv import load_dotenv

load_dotenv()

# Gemini API
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GEMINI_API_MODEL = os.getenv("GEMINI_API_MODEL")

# Application
input_modes = ["List of ingredients 📝", "An image of your inventory 📸"]
