"""
Configuration settings for the Gabrielino Fire Assessment system.
"""

import os

# Project Information
PROJECT_NAME = "gabrielino"
APP_VERSION = "8.0"

# API Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyBhReEZ_u-1MPyDqr1zbIieF_nkh3c4rvA")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3")

# Cost Configuration
COST_GEMINI_FLASH_CALL = 0.0025  # Estimated cost per call
COST_CALFIRE_API_CALL = 0.0001   # Estimated cost for a data API call
COST_TRADITIONAL_ADJUSTER = 150.00  # Cost per traditional adjuster review
COST_PURE_API_WORKFLOW = 0.05  # Pure API-based workflow cost

# System Configuration
DEFAULT_CLAIM_ADDRESS = "2101 N Windsor Ave, Altadena, CA"
DEFAULT_CLAIM_DAMAGE = 550000
DEFAULT_DEMOGRAPHIC = "low_income"

# Display Configuration
CLEAR_SCREEN_COMMAND = 'cls' if os.name == 'nt' else 'clear'

# Logging Configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# Feature Flags
ENABLE_GEMINI = os.getenv("ENABLE_GEMINI", "true").lower() == "true"
ENABLE_OLLAMA = os.getenv("ENABLE_OLLAMA", "true").lower() == "true"
ENABLE_VISUAL_EFFECTS = os.getenv("ENABLE_VISUAL_EFFECTS", "true").lower() == "true"

# Performance Settings
AGENT_TIMEOUT_SECONDS = 30
MAX_PARALLEL_AGENTS = 4
PROCESSING_DELAY_MS = 50  # Visual pacing delay
