import subprocess
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn

# FastAPI code (API Endpoint)
app = FastAPI()

@app.get("/api")
def get_api_data():
    """
    API yang mengembalikan data dalam format JSON.
    """
    data = {"message": "This is an API response!"}
    return JSONResponse(content=data)

@app.get("/api/square/{number}")
def get_square(number: int):
    """
    API untuk menghitung kuadrat dari angka yang diberikan.
    """
    result = number ** 2
    return JSONResponse(content={"number": number, "square": result})

if __name__ == "__main__":
    # Jalankan Streamlit dalam subprocess terpisah
    subprocess.Popen(["streamlit", "run", "streamlit_app.py"])

    # Jalankan FastAPI menggunakan uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
