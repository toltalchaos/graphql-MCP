#!/usr/bin/env python3
"""
Script to run Flask and MCP servers on different ports
"""
import subprocess
import sys
import time
import signal
import os

def run_flask():
    """Run Flask server on port 5000"""
    print("Starting Flask server on port 5000...")
    return subprocess.Popen([sys.executable, "app.py"])

def run_mcp():
    """Run MCP server on port 8001"""
    print("Starting MCP server on port 8001...")
    return subprocess.Popen([sys.executable, "app.py", "mcp"])

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == "flask":
            # Run only Flask server
            run_flask()
        elif sys.argv[1] == "mcp":
            # Run only MCP server
            run_mcp()
        else:
            print("Usage: python run_servers.py [flask|mcp]")
            sys.exit(1)
    else:
        # Run both servers
        flask_process = run_flask()
        time.sleep(2)  # Give Flask time to start
        mcp_process = run_mcp()
        
        print("\nBoth servers are running:")
        print("- Flask server: http://localhost:5000")
        print("- MCP server: localhost:8001")
        print("\nPress Ctrl+C to stop both servers")
        
        try:
            # Wait for both processes
            flask_process.wait()
            mcp_process.wait()
        except KeyboardInterrupt:
            print("\nShutting down servers...")
            flask_process.terminate()
            mcp_process.terminate()
            flask_process.wait()
            mcp_process.wait()

if __name__ == "__main__":
    main()
