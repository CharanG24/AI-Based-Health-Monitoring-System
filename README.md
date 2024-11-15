# AI-Based-Health-Monitoring-System

An AI-driven health monitoring platform that tracks vital signs and detects potential health anomalies in real-time. This system uses machine learning to predict anomalies based on health metrics like heart rate, temperature, and blood pressure. Built with Python, TensorFlow, Keras, Flask, SQL, and Docker, it provides a RESTful API for easy integration and data management.

Features

- Real-time Anomaly Detection: Uses a TensorFlow/Keras model to detect anomalies in health metrics.
- Database Integration: Stores health metrics and anomaly detection results in a MySQL database.
- RESTful API: Provides endpoints for data input and anomaly detection.
- Dockerized: Easily deployable and scalable across different environments with Docker.

Prerequisites

- Docker
- Docker Compose
- Python 3.8 or higher

Usage

Running with Docker:
1. Build the Docker image:
   $ docker build -t health_monitor .

2. Run the app with Docker Compose:
   $ docker-compose up
   This will start both the Flask API and the MySQL database.

API Endpoints:
- POST /predict: Submit health metrics to get an anomaly prediction.
  Request Body (JSON):
  {
    "name": "John Doe",
    "heart_rate": 80,
    "temperature": 98.6,
    "blood_pressure": 120
  }
  Response:
  {
    "anomaly_detected": true
  }


