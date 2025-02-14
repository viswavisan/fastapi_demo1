from fastapi import FastAPI

app = FastAPI()
@app.get('/main')
def credit_decision():
    return 'working fine'