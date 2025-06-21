# ✈️ FlyOrDie.ai

> Should you even board this plane? Let AI roast it before the clouds do.

## 🔥 What It Does
Predicts how safe (or sketchy) a flight is based on:
- Aircraft age
- Weather conditions
- Maintenance history
- Airline delays
- Route performance

## 🧠 Tech Stack
- Frontend: React + Tailwind CSS
- Backend: Flask
- ML: scikit-learn (Random Forest)
- Data Sources: OpenSky API, FAA, Weather APIs

## 🚀 How to Run

### Backend
```bash
cd backend
pip install -r ../requirements.txt
python train_model.py
python app.py
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## 🙃 Sample Output
```json
{
  "risk": 2,
  "roast": "💀 You may land or you may trend on Twitter. Choose wisely."
}
```
