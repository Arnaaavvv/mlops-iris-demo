# mlops-iris-demo

A simple end-to-end MLOps demo for training, retraining, and serving an Iris flower classification model using Python, Flask, and Jenkins.

## Overview

This project demonstrates a basic ML pipeline:

- Train a classification model on the Iris dataset
- Save the trained model as a pickle file
- Serve predictions through a Flask REST API
- Retrain the model automatically using a script
- Deploy the new model via a Jenkins pipeline

## Project Structure

- `train_model.py` — trains the initial model and saves `iris_model.pkl`
- `retrain.py` — retrains the model and overwrites `iris_model.pkl`
- `app.py` — Flask API that exposes `/predict`
- `requirements.txt` — Python dependencies
- `Jenkinsfile` — CI/CD pipeline for retraining and deployment
- `iris_model.pkl` — serialized trained model
- `ml_api.log` — prediction logs created by the API

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Arnaaavvv/mlops-iris-demo.git
   cd mlops-iris-demo
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Train the Model

Run the training script:

```bash
python train_model.py
```

This downloads the Iris dataset, compares candidate models using PyCaret, selects the best one, and saves it as:

```bash
iris_model.pkl
```

## Start the API

```bash
python app.py
```

The API will run on:

```bash
http://0.0.0.0:5000
```

## Predict Endpoint

Send a POST request to:

```bash
http://localhost:5000/predict
```

Example request body:

```json
{
  "features": [5.1, 3.5, 1.4, 0.2]
}
```

Example response:

```json
{
  "prediction": "setosa"
}
```

## Retraining

To retrain the model manually:

```bash
python retrain.py
```

This script reloads the Iris dataset, evaluates models again, and saves a fresh version of the trained model.

## Jenkins Pipeline

The repository includes a Jenkins pipeline in `Jenkinsfile` that:

- creates a virtual environment
- installs dependencies
- runs retraining
- copies the model into a deployment location
- restarts the API service
- archives the model artifact

## Notes

This project is intended as a lightweight demonstration of MLOps concepts such as:

- model training
- artifact persistence
- REST-based inference
- automated retraining
- deployment automation

It is intentionally simple and suitable for learning or prototyping.

## License

This project is provided for educational and demonstration purposes.
