import streamlit as st

st.title("📚 Teste A1 de Russo 🇷🇺")
st.subheader("Baseado no PDF do curso de russo do site https://timetospeakrussian.com/")

# Inicializa o estado do quiz para controlar o que aparece na tela
if "quiz_finalizado" not in st.session_state:
    st.session_state.quiz_finalizado = False
if "resultado_texto" not in st.session_state:
    st.session_state.resultado_texto = ""
if "resultado_sucesso" not in st.session_state:
    st.session_state.resultado_sucesso = False
if "respostas_salvas" not in st.session_state:
    st.session_state.respostas_salvas = {}

# Suas perguntas do arquivo QuizRussoA1.py
perguntas = [
    {
        "enunciado": "1. Сейчас сентябрь, это___",
        "opcoes": ["очень", "осень"],
        "correta": "осень",
        "chave": "p1",
    },
    {
        "enunciado": "2. Марина - очень красивая___",
        "opcoes": ["дедушка", "девушка"],
        "correta": "девушка",
        "chave": "p2"
    },
    {
        "enunciado": "3. Хайнц живёт в Германии, он___",
        "opcoes": ["немец", "немецкий"],
        "correta": "немец",
        "chave": "p3",
    },
    {
        "enunciado": "4. Вы хорошо___по-китайски?",
        "opcoes": ["помните", "понимаете"],
        "correta": "понимаете",
        "chave": "p4",
    },
    {
        "enunciado": "5. Я очень___выучить русский язык.",
        "opcoes": ["могу", "хочу"],
        "correta": "хочу",
        "chave": "p5",
        },
    {
        "enunciado": "6. Вам нравится говорить___?",
        "opcoes": ["по-русски", "русский язык"],
        "correta": "по-русски",
        "chave": "p6",
        },
    {
        "enunciado": "7. Тебе___позвонить домой сегодня.",
        "opcoes": ["должно", "нужно"],
        "correta": "нужно",
        "chave": "p7",
        },
    {
        "enunciado": "8. Им___заплатить за гостиницу на сайте.",
        "opcoes": ["надо", "рады"],
        "correta": "надо",
        "chave": "p8",
        },
    {
        "enunciado": "9. Зимой в России___",
        "opcoes": ["холодно", "холодный"],
        "correta": "холодно",
        "chave": "p9",
        },
    {
        "enunciado": "10. Тебе___нравится Москва?",
        "opcoes": ["много", "очень"],
        "correta": "очень",
        "chave": "p10",
        }
        
]

respostas_usuario = {}

# Mostra as perguntas na tela
for p in perguntas:
    st.write(f"### {p['enunciado']}")
    
    # Se o quiz acabou, os botões ficam desativados (disabled=True) e mostram o que o usuário marcou antes
    if st.session_state.quiz_finalizado:
        resposta_marcada = st.session_state.respostas_salvas.get(p["chave"])
        
        # Descobre qual era o índice da resposta para deixar ela marcada visualmente
        idx = p["opcoes"].index(resposta_marcada) if resposta_marcada in p["opcoes"] else None
        
        st.radio(
            "Sua resposta: ",
            p["opcoes"],
            index=idx,
            key=f"final_{p['chave']}",
            disabled=True
        )
        
        # Lógica de destaque da correção
        if resposta_marcada == p["correta"]:
            st.success(f"✨ Correto! Você acertou.")
        else:
            st.error(f"❌ Errado. Você marcou '{resposta_marcada}'. A resposta correta é: **{p['correta']}**")
            
    else:
        # Se o quiz está em andamento, mostra os botões normais para responder
        respostas_usuario[p['chave']] = st.radio(
            "Escolha a alternativa correta: ",
            p["opcoes"],
            index=None,
            key=p["chave"]
        )
        
    st.write("---")

nota_para_passar = 6  # Ajustei para 3 já que agora são 4 perguntas!
total_perguntas = len(perguntas)

# CASO 1: O quiz ainda NÃO foi finalizado (Mostra o botão de Finalizar)
if not st.session_state.quiz_finalizado:
    if st.button("Finalizar Quiz"):
        acertos = 0
        respondidas = 0
        
        for p in perguntas:
            resp = respostas_usuario[p['chave']]
            if resp is not None:
                respondidas += 1
                if resp == p["correta"]:
                    acertos += 1
                    
        if respondidas < total_perguntas:
            st.warning("⚠️ Por favor, responda a todas as perguntas antes de finalizar!")
        else:
            # Salva as respostas no session_state para usar no gabarito
            st.session_state.respostas_salvas = respostas_usuario.copy()
            st.session_state.quiz_finalizado = True
            st.session_state.resultado_sucesso = acertos >= nota_para_passar
            
            if st.session_state.resultado_sucesso:
                st.session_state.resultado_texto = f"🎉 Parabéns! Você acertou {acertos} de {total_perguntas}."
            else:
                st.session_state.resultado_texto = f"❌ Você acertou {acertos} de {total_perguntas}, continue praticando!"
            
            st.rerun()

# CASO 2: O quiz JÁ FOI finalizado (Mostra o resultado geral lá embaixo e o botão de refazer)
else:
    st.write("### Resultado Geral:")
    if st.session_state.resultado_sucesso:
        st.success(st.session_state.resultado_texto)
    else:
        st.error(st.session_state.resultado_texto)
        
    st.write("---")
    
    # Botão de refazer limpa o estado e recomeça tudo do zero
    if st.button("Refazer Quiz"):
        st.session_state.quiz_finalizado = False
        st.session_state.resultado_texto = ""
        st.session_state.respostas_salvas = {}
        st.rerun()
