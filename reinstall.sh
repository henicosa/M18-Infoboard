#!/bin/bash
echo "Reinstalling the application..."
docker-compose down -v
docker-compose pull
docker-compose build --no-cache
docker-compose up -d
echo "Application reinstalled and started"
