import streamlit as st

# 1. Preparando a "mochila" (Session State)
if "passo" not in st.session_state:
    st.session_state.passo = 1
if "escolha_salva" not in st.session_state:
    st.session_state.escolha_salva = ""

st.title("Quiz Interativo 🎤✨")

# --- PÁGINA 1 ---
if st.session_state.passo == 1:
    st.write("## Pergunta 1: O que você mais gosta?")
    
    # Criamos o rádio. 
    res = st.radio("Escolha uma opção:", ["Animes", "Jogos", "Programar"], index=None)
    
    if res:
        st.session_state.escolha_salva = res # Salva o que ele escolheu
        st.write(f"Que legal que você gosta de {res}!")

        if st.button("Proxima"):
            st.session_state.passo = 2
            st.rerun()

# --- PÁGINA 2 ---
elif st.session_state.passo == 2:
    st.write("## Pergunta 2: Escreva seu nome: ")
    nome = st.text_input("Me chamo: ")
    
    if nome:
        st.session_state.nome_salvo = nome
        # Aqui pegamos o que foi salvo lá na página 1
        escolha_anterior = st.session_state.escolha_salva
        st.write(f"Muito prazer, {nome}! Vi que você gosta de {escolha_anterior}!")
    
    if st.button("proxima"):
        st.session_state.passo = 3
        st.rerun()

#--- Pagina 3 ---
elif st.session_state.passo == 3:
    st.write("## Quantos anos você tem?")
    idade = st.text_input("Tenho: ")

    if idade:
        nome = st.session_state.nome_salvo
        gosto = st.session_state.escolha_salva
        st.write(f"Ei {nome}, agora sei que você gosta de {gosto} e que tem {idade} anos de idade!")

        if st.button("Retornar"):
            st.session_state.passo = 1
            st.rerun()
