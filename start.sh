#!/bin/bash
echo "Starting the application..."
docker-compose up -d
echo "Application started. Check logs with: docker-compose logs -f"
