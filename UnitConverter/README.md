# 🔄 Unit Converter

A simple web-based unit converter built with **FastAPI (Python)** and **JavaScript**.
It allows users to convert values between different units of **length**, **weight**, and **temperature** in real time.
(project from roadmap.sh: https://roadmap.sh/projects/unit-converter)

---

## 🚀 Features

* Convert between multiple unit types:

  * Length (mm, cm, m, km, in, ft, yd, mi)
  * Weight (mg, g, kg, oz, lb)
  * Temperature (C, F, K)
* Real-time conversion (no button required)
* Dynamic UI (units update based on selected category)
* Simple and responsive interface
* Backend API built with FastAPI

---

## 🛠️ Tech Stack

* **Backend:** Python + FastAPI
* **Frontend:** HTML, CSS, JavaScript
* **Templating:** Jinja2

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/henriquefrassetto/python-learning-projects.git
cd python-learning-projects/UnitConverter
```

Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
```

Install dependencies:

```bash
pip install fastapi uvicorn
```

---

## ▶️ Running the App

Start the server:

```bash
uvicorn main:app --reload
```

Then open your browser:

```
http://127.0.0.1:8000
```

---

## 📡 API Endpoints

### Length Conversion

```
/length_conversion?conversion_from=m&conversion_to=ft&input_value=10
```

### Weight Conversion

```
/weight_conversion?conversion_from=kg&conversion_to=lb&input_value=5
```

### Temperature Conversion

```
/temperature_conversion?conversion_from=C&conversion_to=F&input_value=25
```

---

## 🧠 How It Works

* The frontend captures user input and sends requests to the backend using `fetch()`.
* The backend processes the conversion and returns the result as JSON.
* The UI updates automatically whenever the input or units change.

---

## 📌 Future Improvements

* Add more unit categories (speed, pressure, energy)
* Improve UI/UX design
* Add input validation and error handling
* Create a unified `/convert` endpoint
* Deploy the app online

---

## 📄 License

This project is open-source and available under the MIT License.
