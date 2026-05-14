import streamlit as st

if "passo" not in st.session_state:
    st.session_state.passo = 1

st.title("Quiz Interativo🎤✨")

if st.session_state.passo == 1:
    st.write("## Pergunta 1: O que você mais gosta?")
    escolha = st.radio("Escolha uma opção:", ["Animes", "Jogos","Programar"], key="pergunta1", index=None)
    if escolha:
        st.write(f"✨Que legal que você gosta de {escolha}!")

        if st.button("Proxima"):
            st.session_state.passo = 2
            st.rerun()

elif st.session_state.passo == 2:
    st.write("### Parabens voce conseguiu chegar na proxima tela")
    if st.button("Reiniciar"):
        st.session_state.passo = 1
        st.rerun()
        
