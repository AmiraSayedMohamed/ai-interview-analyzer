#!/usr/bin/env python3
"""
FastAPI Server Runner
Run this script to start the AI Interview Analyzer backend server.
"""

import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "main:app", 
        host="127.0.0.1", 
        port=8000, 
        reload=True,
        log_level="info"
    )
