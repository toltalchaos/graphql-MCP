# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose ports for Flask (5000) and MCP (8001)
EXPOSE 5000 8001

# Create a startup script that runs both servers
RUN echo '#!/bin/bash\n\
echo "Starting Flask server on port 5000..."\n\
python app.py &\n\
FLASK_PID=$!\n\
\n\
echo "Starting MCP server on port 8001..."\n\
python app.py mcp &\n\
MCP_PID=$!\n\
\n\
echo "Both servers are running:"\n\
echo "- Flask server: http://localhost:5000"\n\
echo "- MCP server: localhost:8001"\n\
echo "Press Ctrl+C to stop both servers"\n\
\n\
# Wait for both processes\n\
wait $FLASK_PID $MCP_PID' > /app/start_servers.sh

RUN chmod +x /app/start_servers.sh

# Default command runs both servers
CMD ["/app/start_servers.sh"]
