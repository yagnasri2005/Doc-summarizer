"""Main Flask application for Document Summarizer."""
import os
from flask import Flask, render_template, request, jsonify, send_file
from werkzeug.utils import secure_filename
from datetime import datetime
import traceback

from config import Config
from utils.document_parser import DocumentParser
from utils.summarizer import DocumentSummarizer

app = Flask(__name__)
app.config.from_object(Config)

# Initialize components
parser = DocumentParser()
summarizer = DocumentSummarizer()


@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')


@app.route('/api/health')
def health():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    })


@app.route('/api/config')
def get_config():
    """Get current configuration."""
    return jsonify({
        'max_file_size_mb': Config.MAX_FILE_SIZE_MB,
        'supported_formats': Config.ALLOWED_EXTENSIONS,
        'summary_lengths': Config.SUMMARY_LENGTHS,
        'default_model': Config.DEFAULT_MODEL
    })


@app.route('/api/summarize', methods=['POST'])
def summarize():
    """Summarize an uploaded document."""
    try:
        # Validate request
        if 'file' not in request.files:
            return jsonify({'success': False, 'error': 'No file provided'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'success': False, 'error': 'No file selected'}), 400
        
        # Validate file extension
        if not allowed_file(file.filename):
            return jsonify({
                'success': False,
                'error': f'File type not supported. Allowed: {", ".join(Config.ALLOWED_EXTENSIONS)}'
            }), 400
        
        # Get parameters
        summary_length = request.form.get('length', 'medium')
        if summary_length not in Config.SUMMARY_LENGTHS:
            summary_length = 'medium'
        
        # Save file temporarily
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        file.save(filepath)
        
        # Parse document
        text = parser.parse(filepath)
        if not text:
            return jsonify({
                'success': False,
                'error': 'Could not extract text from document'
            }), 400
        
        original_length = len(text.split())
        
        # Generate summary
        summary = summarizer.summarize(
            text,
            length=summary_length
        )
        
        summary_length_words = len(summary.split())
        
        # Clean up
        try:
            os.remove(filepath)
        except:
            pass
        
        return jsonify({
            'success': True,
            'summary': summary,
            'original_length': original_length,
            'summary_length': summary_length_words,
            'compression_ratio': round((1 - summary_length_words / original_length) * 100, 2),
            'timestamp': datetime.now().isoformat()
        }), 200
        
    except Exception as e:
        print(f"Error in summarize endpoint: {str(e)}")
        print(traceback.format_exc())
        return jsonify({
            'success': False,
            'error': f'Processing error: {str(e)}'
        }), 500


@app.route('/api/summarize-text', methods=['POST'])
def summarize_text():
    """Summarize plain text input."""
    try:
        data = request.get_json()
        
        if not data or 'text' not in data:
            return jsonify({'success': False, 'error': 'No text provided'}), 400
        
        text = data.get('text', '').strip()
        summary_length = data.get('length', 'medium')
        
        if not text:
            return jsonify({'success': False, 'error': 'Text cannot be empty'}), 400
        
        if summary_length not in Config.SUMMARY_LENGTHS:
            summary_length = 'medium'
        
        # Generate summary
        summary = summarizer.summarize(text, length=summary_length)
        
        return jsonify({
            'success': True,
            'summary': summary,
            'original_length': len(text.split()),
            'summary_length': len(summary.split()),
            'compression_ratio': round((1 - len(summary.split()) / len(text.split())) * 100, 2)
        }), 200
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Processing error: {str(e)}'
        }), 500


def allowed_file(filename):
    """Check if file extension is allowed."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Endpoint not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
