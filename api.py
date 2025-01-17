import streamlit as st
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import threading
import uvicorn

# Streamlit code
def streamlit_ui():
    # UI di Streamlit
    st.title("Streamlit and FastAPI Example")

    # Input dari pengguna
    user_input = st.text_input("Enter a number:")
    if user_input:
        try:
            num = int(user_input)
            st.write(f"You entered: {num}")
            st.write(f"The square of {num} is {num ** 2}")
        except ValueError:
            st.write("Please enter a valid number.")

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
    # Jalankan Streamlit dalam thread terpisah
    def run_streamlit():
        streamlit_ui()

    thread = threading.Thread(target=run_streamlit)
    thread.start()

    # Jalankan FastAPI menggunakan uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
