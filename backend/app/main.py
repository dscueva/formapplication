from fastapi import FastAPI, HTTPException
from app.models import FormData
from app.grpc_client import send_form_data

app = FastAPI(title="Form Submission API")

@app.post("/submit-form", summary="Submit a form")
async def submit_form(form: FormData):
    try:
        response = send_form_data(form)
        return {"status": "success", "data": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
