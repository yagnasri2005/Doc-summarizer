"""Configuration settings for Document Summarizer."""
import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Base configuration."""
    
    # Flask settings
    DEBUG = True
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    
    # File upload settings
    UPLOAD_FOLDER = 'temp_uploads'
    MAX_FILE_SIZE_MB = 50
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'docx', 'md'}
    
    # Summarization settings
    DEFAULT_MODEL = os.getenv('SUMMARIZER_MODEL', 'huggingface')  # 'openai', 'huggingface', 'local'
    DEFAULT_LENGTH = 'medium'
    
    SUMMARY_LENGTHS = {
        'short': {'ratio': 0.2, 'min_words': 50, 'max_words': 100},
        'medium': {'ratio': 0.3, 'min_words': 100, 'max_words': 200},
        'long': {'ratio': 0.5, 'min_words': 200, 'max_words': 500}
    }
    
    # API Keys
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    HUGGINGFACE_API_KEY = os.getenv('HUGGINGFACE_API_KEY')
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    
    # Model settings
    HUGGINGFACE_MODEL = os.getenv('HUGGINGFACE_MODEL', 'facebook/bart-large-cnn')
    OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo')
    
    # API endpoints
    OPENAI_API_BASE = os.getenv('OPENAI_API_BASE', 'https://api.openai.com/v1')
    
    # Processing settings
    MAX_INPUT_LENGTH = 4096  # Max tokens for processing
    MIN_SUMMARY_LENGTH = 50   # Minimum summary length in words
