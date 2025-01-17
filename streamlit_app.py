import streamlit as st

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

# Jalankan UI Streamlit
if __name__ == "__main__":
    streamlit_ui()
