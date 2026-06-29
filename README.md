# AI Document Summarizer

An intelligent document summarization tool powered by AI. Upload documents in various formats and get concise, coherent summaries automatically.

## Features

✨ **Multi-Format Support**
- PDF files
- Text files (.txt)
- Word documents (.docx)
- Markdown files (.md)

🤖 **AI-Powered Summarization**
- Uses state-of-the-art language models
- Customizable summary length
- Preserves key information and context

🌐 **Web Interface**
- Clean, user-friendly dashboard
- Real-time processing
- Download summaries as text files

⚡ **REST API**
- Programmatic access to summarization
- Easy integration with other applications

## Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yagnasri2005/doc-summarizer.git
   cd doc-summarizer
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your API key (if using cloud models):
   ```
   OPENAI_API_KEY=your_api_key_here
   # OR for Hugging Face:
   HUGGINGFACE_API_KEY=your_token_here
   ```

### Running the Application

**Start the server:**
```bash
python app.py
```

**Access the web interface:**
Open your browser and go to `http://localhost:5000`

## Usage

### Web Interface
1. Navigate to http://localhost:5000
2. Click "Choose File" and select a document
3. Adjust summary length preference (short/medium/long)
4. Click "Summarize"
5. Download or copy the summary

### API Usage

**Summarize a document:**
```bash
curl -X POST -F "file=@document.pdf" http://localhost:5000/api/summarize
```

**Response:**
```json
{
  "success": true,
  "summary": "This document discusses...",
  "original_length": 5000,
  "summary_length": 250,
  "processing_time": 2.5
}
```

## Configuration

Edit `config.py` to customize:
- Summary length ratios
- Maximum file size
- Supported file formats
- Model selection
- API endpoints

## Supported Summarization Models

### Option 1: OpenAI (Recommended)
- Most accurate summaries
- Requires API key (paid)
- Setup: https://platform.openai.com/api-keys

### Option 2: Hugging Face (Free)
- No cost
- Good quality
- Setup: https://huggingface.co/settings/tokens

### Option 3: Local Model (Ollama)
- Completely free and offline
- Requires local setup
- Setup: https://ollama.ai

## Project Structure

```
doc-summarizer/
├── app.py                 # Main Flask application
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── .env.example           # Example environment variables
├── static/
│   ├── css/
│   │   └── style.css      # Styling
│   └── js/
│       └── script.js      # Frontend logic
├── templates/
│   ├── index.html         # Main page
│   ├── results.html       # Results page
│   └── about.html         # About page
└── utils/
    ├── document_parser.py # Document parsing logic
    └── summarizer.py      # Summarization logic
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Web interface |
| POST | `/api/summarize` | Summarize a document |
| GET | `/api/health` | Health check |
| GET | `/api/config` | Get current configuration |

## Troubleshooting

**Issue: "ModuleNotFoundError: No module named 'flask'"**
- Solution: Run `pip install -r requirements.txt`

**Issue: "API key not found"**
- Solution: Check your `.env` file and ensure the API key is set correctly

**Issue: File upload fails**
- Solution: Check file size (default max: 50MB) and format compatibility

**Issue: Summarization is slow**
- Solution: Consider using a faster model or reducing file size

## Development

### Running Tests
```bash
pytest tests/
```

### Code Style
```bash
black . --line-length 88
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues, questions, or suggestions:
- Open an Issue on GitHub
- Check existing issues for solutions
- Review the documentation

## Roadmap

- [ ] Support for audio/video transcription summaries
- [ ] Multi-language support
- [ ] Batch processing for multiple documents
- [ ] Advanced customization options
- [ ] Mobile app
- [ ] Browser extension

## Acknowledgments

Built with:
- [Flask](https://flask.palletsprojects.com/)
- [Transformers](https://huggingface.co/transformers/)
- [PyPDF2](https://github.com/py-pdf/PyPDF2)
- [python-docx](https://python-docx.readthedocs.io/)

---

**Made with ❤️ by Your Name**
