# Detecting Anomalies in Servo Motors Using Machine Learning
## Course: Autonomous Robots

### Project Members:
- Sahar Tuvyahu
- Yehonatan Baruchson
- Guy Gur-Arieh
- Harel Gilad
## Introduction
The project aims to detect anomalies in servo motors that could indicate a breakdown using a machine learning model. This is critical for applications where servo motor failure could have significant consequences, such as in airplane wing control surfaces.

## Objectives
Detect anomalies in servo motors to predict potential failures.
Use a machine learning model for accurate and efficient anomaly detection.

## Motivation
Servo motors are widely used in critical applications, and their failure can lead to serious issues. By detecting anomalies early, maintenance can be performed proactively to prevent failures.

## Servo Motors
Types:

- 180° Servo: Typically used for precise angular control. Only 180° servos were used in this project.
- 360° Servo: Used for continuous rotation.
## Applications:

- Robotics
- Remote control vehicles
- Automated machinery
- Aerospace control surfaces
- and more

## Project Overview
Controlling the Servo:

- Implemented using the Arduino IDE.
- Controlled the servo motors in a pendulum motion using ESP32.

Audio Recording:

- Recorded audio of the servo motors in both normal and faulty conditions.
- Induced faults by adding saltwater to simulate deterioration.

Data Preparation:

- Changed the audio file type to a suitable format for processing.
- Divided the data into training (80%), validation (10%), and testing (10%) sets.

Model Training:

Chose Convolutional Neural Network (CNN) for its advantages:
- Automatic Feature Extraction: Efficient for audio data.
- Efficiency: Fewer parameters, reduced overfitting, faster computation.
- Performance: Higher accuracy, robust to input variations.
- Real-Time Deployment: Suitable for embedded systems like ESP32, low latency. This is crucial because the model is intended to be deployed on the servos themselves, allowing for real-time anomaly detection and immediate action.
## Model Evaluation
- Achieved excellent results with minimal false positives.
- The model is effective in detecting subtle anomalies in servo motor operation.
## Results
- Training Set: 80%
- Validation Set: 10%
- Test Set: 10%
- Performance: Only 6 false positives, demonstrating high accuracy and reliability.
## Conclusion
The project successfully developed a machine learning model to detect anomalies in servo motors, which can be deployed in real-time systems like the ESP32 to prevent failures in critical applications.


## Usage:

1. you can use the our model called: **model_30_06_2024.pt**

2. you can also train your own model with your own data, using our Implementation:

Clone the repository to your local machine:
```bash
git clone https://github.com/s4646/ServoAnomalyDetection.git
```
Inside the working directory, create the folder:
```bash
./data
``` 
Inside data, for each type of audio file (good and bad) add: ./data/0 ./data/1
```bash
./data/0
./data/1
``` 
Add your audio recordings to a new folder called original inside each lable:
```bash
 ./data/0/original - faulty recordings of the servo
 ./data/0/original - good recordings of the servo
``` 
run the  files:
```bash
data_preprocessing.py
``` 
We used an iPhone to record the servo, so we converted the audio type from .m4a to .wav
```bash
train.ipynb
```
Note:
- Inside the documents folder there is a detailed presentation showing the entire project process with pictures
