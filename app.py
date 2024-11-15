# app.py
from flask import Flask, request, jsonify
from model.anomaly_model import create_anomaly_detection_model, load_trained_model
from database.models import init_db, PatientData, session
from utils.preprocess import preprocess_data

app = Flask(__name__)
init_db()  # Initialize the database

# Load the trained model (assumes it's saved as 'trained_model.h5')
model = load_trained_model('model/trained_model.h5')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    heart_rate = data['heart_rate']
    temperature = data['temperature']
    blood_pressure = data['blood_pressure']

    # Preprocess data and make a prediction
    metrics = preprocess_data([heart_rate, temperature, blood_pressure])
    prediction = model.predict(metrics)[0][0] > 0.5  # Anomaly if result > 0.5

    # Save the prediction result to the database
    patient = PatientData(
        name=data['name'],
        heart_rate=heart_rate,
        temperature=temperature,
        blood_pressure=blood_pressure,
        anomaly=int(prediction)
    )
    session.add(patient)
    session.commit()

    return jsonify({'anomaly_detected': bool(prediction)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
