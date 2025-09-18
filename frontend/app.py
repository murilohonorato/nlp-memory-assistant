# frontend/app.py
import streamlit as st
import requests

st.set_page_config(page_title="Memory Assistant - Protótipo")
st.title("🧠 NLP Memory Assistant - Protótipo")

# Entrada do usuário
user_id = st.text_input("User ID", value="u_test")
message = st.text_input("Mensagem")

if st.button("Enviar"):
    if not message.strip():
        st.warning("Digite uma mensagem antes de enviar!")
    else:
        try:
            res = requests.post(
                "http://localhost:8000/chat",
                json={"user_id": user_id, "message": message},
                timeout=10
            )
            res.raise_for_status()
            data = res.json()
            
            # Mostrar resposta
            st.markdown("**Assistente:**")
            st.write(data["reply"])
            
            # Mostrar memórias usadas (ainda vazio na Semana 1)
            st.markdown("**Memórias usadas:**")
            st.write(data.get("mem_used", []))
        except Exception as e:
            st.error(f"Erro ao conectar com o backend: {e}")
