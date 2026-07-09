# 🌤️ Basic Weather App

A Python-based Weather Application that fetches and displays real-time weather information for a user-specified location using a weather API. This project was developed as part of the **Python Programming Internship at Oasis Infobyte (OIBSIP)**.

## 📌 Project Overview

The Basic Weather App allows users to check current weather conditions by entering a city name. The application retrieves weather data from an API and displays useful information such as temperature, humidity, wind speed, and weather conditions.

## ✨ Features

* Search weather by city name
* Real-time weather updates
* Temperature display
* Humidity information
* Weather condition details
* User-friendly interface
* Error handling for invalid locations

## 🛠️ Technologies Used

* Python 3
* Weather API
* Requests Library
* JSON Data Handling

## 📂 Project Structure

```text
Basic_Weather_App/
│
├── weather_app.py
├── requirements.txt
├── README.md
└── screenshots/
```

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/Nandni-Babbar/OIBSIP.git
```

### 2. Navigate to the Project Folder

```bash
cd OIBSIP/NandniBabbar_Task3
```

### 3. Install Required Dependencies

```bash
pip install requests
```

> If your project uses any additional libraries (such as `Pillow` or `tkintermapview`), install those as well.

### 4. Add Your API Key

Open `Weather_App.py` and replace:

```python
API_KEY = "YOUR_API_KEY"
```

with your actual Weather API key.

### 5. Run the Application

```bash
python Weather_App.py
```
## 📖 Sample Output

```text
Enter City Name: Mumbai

Weather Details
------------------
Temperature : 29°C
Humidity    : 78%
Condition   : Clear Sky
Wind Speed  : 12 km/h
```

## 🎯 Learning Outcomes

Through this project, I learned:

* API integration using Python
* Working with JSON data
* User input handling
* Error and exception handling
* Real-time data retrieval
* Building practical applications
