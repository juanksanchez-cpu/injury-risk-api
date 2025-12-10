
# API Predicción Riesgo de Lesión Deportiva

## Descripción
API FastAPI que predice probabilidad de lesión en 28 días para deportistas juveniles.

## Endpoints
- GET / --> estado
- POST /predict --> predicción

## Ejemplo
POST /predict
{
  "edad": 16,
  "sexo": 1,
  "estatura_cm": 160,
  "peso_kg": 55,
  "horas_entrenamiento_semanal": 8,
  "intensidad_entrenamiento": 4,
  "tipo_disciplina": 1,
  "antecedentes_lesiones_previas": 1,
  "tiempo_desde_ultima_lesion_dias": 120,
  "fatiga_autoreportada": 3,
  "sueno_horas": 7,
  "dolor_actual": 2,
  "flexibilidad": 4,
  "fuerza_muscular": 4,
  "estabilidad_equilibrio": 5
}
