# Flask + MCP Server Setup

This project runs a Flask GraphQL server and an MCP (Model Context Protocol) server on different ports.

## 🐳 Docker Setup (Recommended) --desktop with MCP enabled

### Quick Start with Docker Compose
```bash
# Build and run both servers in a container
docker-compose up --build

# Run in background
docker-compose up -d --build

# Stop the services
docker-compose down
```

### Manual Docker Build
```bash
# Build the image
docker build -t flask-mcp-app .

# Run the container
docker run -p 5000:5000 -p 8001:8001 flask-mcp-app
```

## 🐍 Local Development Setup

### Prerequisites
```bash
pip install -r requirements.txt
```

### Option 1: Run Both Servers Together
```bash
python run_servers.py
```
This will start:
- Flask server on port 5000 (http://localhost:5000)
- MCP server on port 8001

### Option 2: Run Servers Separately

**Flask server only:**
```bash
python run_servers.py flask
# or directly:
python app.py
```

**MCP server only:**
```bash
python run_servers.py mcp
# or directly:
python app.py mcp
```

## 🌐 Accessing the Services

- **Flask GraphQL Server**: http://localhost:5000
  - GraphQL endpoint: http://localhost:5000/graphql
  - Schema info: http://localhost:5000/schema_info

- **MCP Server**: localhost:8001
  - This is the MCP protocol server for AI tool integration

## 📝 GraphQL Usage

You can test the GraphQL endpoint with a query like:
```graphql
query {
  resolveHello(name: "World") {
    greeting
  }
}
```

## 🛑 Stopping the Servers

**Docker:**
```bash
docker-compose down
```

**Local Development:**
- If running both servers together, press `Ctrl+C` to stop both
- If running separately, press `Ctrl+C` in each terminal

## 📁 Project Structure

```
├── app.py                 # Main application with Flask + MCP
├── run_servers.py         # Script to run both servers
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose configuration
├── .dockerignore         # Files to ignore in Docker build
└── README.md            # This file
```
