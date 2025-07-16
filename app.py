from fastapi import FastAPI, Request
import mysql.connector
from gemini_integration import get_gemini_response

app = FastAPI()

@app.post("/get-context/")
async def get_context(request: Request):
    try:
        data = await request.json()
        prompt = data.get("prompt", "")

        if not prompt:
            return {"status": "error", "message": "Prompt is required"}

        # Gemini API call
        gemini_response = get_gemini_response(prompt)

        # DB Connection
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # <-- change this to your real MySQL password
            database="mcp_db"
        )
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO responses (prompt, response) VALUES (%s, %s)",
            (prompt, gemini_response)
        )
        db.commit()
        db.close()

        return {"status": "success", "response": gemini_response}

    except Exception as e:
        import traceback
        traceback.print_exc()  # Print full error stack trace in terminal
        return {"status": "error", "message": str(e)}
