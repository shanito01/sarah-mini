from fastapi import FastAPI

app = FastAPI(title="Sarah Mini API")

@app.get("/")
def root():
    return {"message": "Sarah Mini API"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/checkins")
def list_checkins():
    return [
        {"id": 1, "mood": "bien", "activity": "caminata", "note": "Ejemplo ficticio"},
        {"id": 2, "mood": "cansado", "activity": "descanso", "note": "Solo datos de demostración"}
    ]
