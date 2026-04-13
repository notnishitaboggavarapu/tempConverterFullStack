# 🌡️ Temperature Converter (Full Stack App)

A simple full-stack web application that converts temperature between Celsius and Fahrenheit using **React (Frontend)** and **FastAPI (Backend)**.

---

## 🚀 Tech Stack

### Frontend
- React.js
- JavaScript
- HTML / CSS
- Fetch API

### Backend
- FastAPI (Python)
- Pydantic (Data Validation)
- Uvicorn (Server)

---

## 📌 Features

- Convert Celsius → Fahrenheit
- Convert Fahrenheit → Celsius
- Real-time API communication between frontend and backend
- Input validation using Pydantic
- CORS enabled for cross-origin requests
- Clean and simple UI

---

## 📁 Project Structure

```

pythonProject1/
│
├── backend/
│   ├── main.py
│   ├── venv/
│
├── frontend/
│   ├── src/
│   │   ├── App.js
│   │   ├── index.js
│   ├── package.json
│
└── README.md

````

---

## ⚙️ How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/temperature-converter.git
cd temperature-converter
````

---

### 2️⃣ Run Backend (FastAPI)

```bash
cd backend
pip install fastapi uvicorn
uvicorn main: app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

### 3️⃣ Run Frontend (React)

```bash
cd frontend
npm install
npm start
```

Frontend runs at:

```
http://localhost:3000
```

---

## 🔗 API Endpoint

### ➤ Convert Temperature

```
POST /convert
```

### Request Body

```json
{
  "value": 100,
  "from_unit": "C",
  "to_unit": "F"
}
```

### Response

```json
{
  "result": 212.0,
  "unit": "F"
}
```

---

## 🧠 What I Learned

* Building REST APIs using FastAPI
* Creating schemas using Pydantic
* Connecting frontend and backend using Fetch API
* Handling CORS errors
* Full-stack project structure

---

## 🎯 Future Improvements

* Add Kelvin conversion
* Improve UI design (Tailwind / Material UI)
* Add loading and error states
* Deploy frontend (Vercel) and backend (Render)
* Add history of conversions

---

## 👩‍💻 Author

**Nishita Boggavarapu**
Aspiring Full Stack Developer 🚀


# 🚀 Next Step (Important)

After adding this:

```bash
git add README.md
git commit -m "added professional README"
git push


Just say 👍
