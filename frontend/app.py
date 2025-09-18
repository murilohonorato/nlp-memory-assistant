# frontend/app.py
import streamlit as st
import requests

st.set_page_config(page_title="Memory Assistant - Protótipo")
st.title("Memory Assistant - Protótipo")

user_id = st.text_input("User ID", value="u_test")
msg = st.text_input("Mensagem")

if st.button("Enviar"):
    try:
        res = requests.post("http://localhost:8000/chat", json={"user_id": user_id, "message": msg}, timeout=10)
        res.raise_for_status()
        data = res.json()
        st.markdown("**Assistente:**")
        st.write(data["reply"])
        st.markdown("**Memórias usadas:**")
        st.write(data.get("mem_used", []))
    except Exception as e:
        st.error("Erro ao chamar backend: " + str(e))

