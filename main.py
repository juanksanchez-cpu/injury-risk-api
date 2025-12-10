from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(title='API Predicción Riesgo de Lesión Deportiva')

model = joblib.load('model.pkl')

class InputFeatures(BaseModel):
    edad: float
    sexo: int
    estatura_cm: float
    peso_kg: float
    horas_entrenamiento_semanal: float
    intensidad_entrenamiento: int
    tipo_disciplina: int
    antecedentes_lesiones_previas: int
    tiempo_desde_ultima_lesion_dias: float
    fatiga_autoreportada: float
    sueno_horas: float
    dolor_actual: float
    flexibilidad: int
    fuerza_muscular: int
    estabilidad_equilibrio: int

@app.get('/')
def home():
    return {'status':'up','service':'injury-risk-api'}

@app.post('/predict')
def predict(features: InputFeatures):
    ordered = ["edad", "sexo", "estatura_cm", "peso_kg", "horas_entrenamiento_semanal", "intensidad_entrenamiento", "tipo_disciplina", "antecedentes_lesiones_previas", "tiempo_desde_ultima_lesion_dias", "fatiga_autoreportada", "sueno_horas", "dolor_actual", "flexibilidad", "fuerza_muscular", "estabilidad_equilibrio"]
    # Build input array in the correct order
    x = np.array([
        features.edad, features.sexo, features.estatura_cm, features.peso_kg,
        features.horas_entrenamiento_semanal, features.intensidad_entrenamiento,
        features.tipo_disciplina, features.antecedentes_lesiones_previas,
        features.tiempo_desde_ultima_lesion_dias, features.fatiga_autoreportada,
        features.sueno_horas, features.dolor_actual, features.flexibilidad,
        features.fuerza_muscular, features.estabilidad_equilibrio
    ]).reshape(1, -1)
    prob = float(model.predict_proba(x)[0][1])
    pred = int(model.predict(x)[0])
    return {'prediccion_binaria': pred, 'probabilidad': prob}
