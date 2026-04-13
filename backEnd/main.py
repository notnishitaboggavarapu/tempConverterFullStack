from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)
class TempRequest(BaseModel):
    value: float
    from_unit: str
    to_unit: str
    
@app.post("/convert")
def convert_temperature(data: TempRequest):
    value = data.value   # or data.value (based on your model)
    from_unit = data.from_unit.upper()
    to_unit = data.to_unit.upper()

    if from_unit == "C" and to_unit == "F":
        result = (value * 9/5) + 32
    elif from_unit == "F" and to_unit == "C":
        result = (value - 32) * 5/9
    elif from_unit == to_unit:
        result = value
    else:
        return {"error": "Invalid conversion"}

    return {
        "result": round(result, 2),
        "unit": to_unit
    }
