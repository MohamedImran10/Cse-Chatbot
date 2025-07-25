# CSE Chatbot - Dockerized

A Flask-based chatbot application for Computer Science and Engineering queries, powered by Google's Gemini AI.

## 🐳 Docker Setup

### Prerequisites
- Docker installed on your system
- Docker Compose (usually included with Docker Desktop)

### Quick Start with Docker

1. **Clone the repository and navigate to the project directory**
   ```bash
   cd /path/to/cse-chatbot
   ```

2. **Create environment file**
   ```bash
   cp .env.example .env
   ```
   Then edit `.env` file and add your Gemini API key:
   ```
   GEMINI_API_KEY=your_actual_api_key_here
   SECRET_KEY=your_secret_key_here
   ```

3. **Build and run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

4. **Access the application**
   Open your browser and go to: `http://localhost:5000`

### Alternative Docker Commands

#### Build the Docker image manually:
```bash
docker build -t cse-chatbot .
```

#### Run the container manually:
```bash
docker run -p 5000:5000 --env-file .env cse-chatbot
```

#### Run in detached mode:
```bash
docker-compose up -d
```

#### Stop the application:
```bash
docker-compose down
```

#### View logs:
```bash
docker-compose logs -f
```

### Production Deployment

For production deployment, consider:

1. **Use a reverse proxy** (nginx, traefik)
2. **Enable HTTPS**
3. **Use a production WSGI server** like Gunicorn:

Create a `Dockerfile.prod`:
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install gunicorn
RUN pip install gunicorn

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN useradd --create-home --shell /bin/bash app && chown -R app:app /app
USER app

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "run:app"]
```

## 📁 Project Structure

```
cse-chatbot/
├── Dockerfile              # Docker image configuration
├── docker-compose.yml      # Docker Compose configuration
├── .dockerignore           # Files to ignore in Docker build
├── .env.example            # Environment variables template
├── requirements.txt        # Python dependencies
├── run.py                 # Flask application entry point
└── app/
    ├── __init__.py
    ├── chatbot.py         # Chatbot logic
    ├── config.py          # Application configuration
    ├── responses.json     # Predefined responses
    ├── static/            # CSS and JS files
    └── templates/         # HTML templates
```

## 🔧 Environment Variables

- `GEMINI_API_KEY`: Your Google Gemini AI API key (required)
- `SECRET_KEY`: Flask secret key for sessions
- `FLASK_ENV`: Environment (development/production)
- `PORT`: Port number (default: 5000)

## 🚀 Features

- Interactive chat interface
- CSE-specific knowledge base
- Google Gemini AI integration
- Responsive web design
- Dockerized for easy deployment

## 📝 Development

To run in development mode:

```bash
# Without Docker
pip install -r requirements.txt
python run.py

# With Docker (development)
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up
```

## 🛠️ Troubleshooting

1. **Port already in use**: Change the port in `docker-compose.yml`
2. **API key issues**: Ensure your `.env` file has the correct Gemini API key
3. **Build failures**: Try `docker-compose down && docker-compose up --build`

## 📄 License

[Add your license information here]
