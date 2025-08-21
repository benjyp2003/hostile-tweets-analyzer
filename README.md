# Hostile Tweets Analyzer API

A FastAPI-based application that analyzes and processes tweet data related to Iran. The API provides endpoints to retrieve processed and analyzed tweet data.

## Features

- FastAPI web framework for high-performance API
- MongoDB integration for data storage
- Tweet data processing and analysis using pandas and NLTK
- Docker containerization support
- OpenShift deployment ready

## Project Structure

```
├── app/
│   ├── main.py          # FastAPI application entry point
│   ├── manager.py       # Data processing manager
│   ├── fetcher.py       # Data fetching from MongoDB
│   └── processor.py     # Tweet analysis and processing
├── scripts/
│   ├── docker-run.bat   # Docker deployment script
│   └── open-shift-run.bat # OpenShift deployment script
├── data/
│   └── weapon_list.txt  # Reference data
├── Dockerfile           # Container configuration
└── requirements.txt     # Python dependencies
```

## API Endpoints

- `GET /` - Welcome message and API information
- `GET /get_analyzed_data` - Returns processed and analyzed tweet data

## Requirements

- Python 3.11+
- MongoDB (for data storage)
- Dependencies listed in `requirements.txt`

## Installation & Setup

### Local Development

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

### Docker Deployment

Run the Docker script:
```bash
scripts\docker-run.bat
```

This will:
- Build the Docker image
- Stop any existing container
- Run the application on port 8000

### OpenShift Deployment

For OpenShift Sandbox deployment:
```bash
scripts\open-shift-run.bat
```

This script handles:
- Resource cleanup
- Application deployment with appropriate resource limits
- Service exposure

## Usage

Once running, the API will be available at:
- Local: `http://localhost:8000`
- OpenShift: Check the route URL after deployment

Visit the root endpoint for API information and use `/get_analyzed_data` to retrieve processed tweet data.

