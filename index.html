import streamlit as st
import google.generativeai as genai
import random

# 1. Налаштування сторінки
st.set_page_config(page_title="UR AI Helper", page_icon="🤖")

# Стилізація під ваш HTML-код
st.markdown("""
    <style>
    .stApp { background-color: #f0f2f5; }
    .chat-header { 
        background: white; 
        padding: 20px; 
        text-align: center; 
        font-size: 1.5rem; 
        font-weight: bold; 
        border-radius: 15px 15px 0 0;
        border-bottom: 1px solid #eee;
        color: #1a1a1a;
    }
    .disclaimer { 
        font-size: 0.8rem; 
        color: #999; 
        text-align: center; 
        margin-top: 10px; 
    }
    </style>
    <div class="chat-header">Привіт! Я Юр! Чим можу тобі допомогти?</div>
    """, unsafe_allow_html=True)

# 2. База знань та цитати
QUOTES = [
    "RP — це не гра в перемогу, це гра в історію.",
    "RP — це мистецтво жити іншим життям.",
    "Повага до RP інших — основа сильного сервера.",
    "Кожен персонаж — це шанс зробити світ гри живішим.",
    "Не шукай легких шляхів — шукай цікавих історій."
]

RULES_CONTEXT = """
Ти штучний інтелект, який має допомагати гравцям з правилами та з RP-термінами. 
Твоя база знань: 
Пункт 1 "Повага, антибулінг та особистий простір". 
Пункт 1 стаття 1: RP-образи. Поважай інших гравців і уникай RP-образів. 
Покарання: штраф до 8 000€ (через суд). 
Якщо питання не про RP або сервер UKRAINE RP в Emergency Hamburg, відповідай, що не знаєш відповіді.
"""

# 3. Налаштування API
if "GOOGLE_API_KEY" not in st.secrets:
    st.error("Помилка: GOOGLE_API_KEY не знайдено в Secrets!")
    st.stop()

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

# 4. Логіка чату
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Вітаю! Я твій РП-помічник. Запитуй про правила чи конституцію сервера UKRAINE RP!"}
    ]

# Відображення повідомлень
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Поле вводу
if prompt := st.chat_input("Напишіть питання..."):
    # Додаємо повідомлення користувача
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Відповідь ШІ
    with st.chat_message("assistant"):
        placeholder = st.empty()
        placeholder.markdown("* /me Думаю...*") # Ефект "Думаю" як у вашому HTML
        
        try:
            full_prompt = f"{RULES_CONTEXT}\n\nКористувач: {prompt}"
            response = model.generate_content(full_prompt)
            
            answer = response.text
            placeholder.markdown(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})
        except Exception as e:
            placeholder.error(f"Виникла помилка: {e}")

# 5. Нижня частина (Цитата та Дисклеймер)
st.markdown(f"<div style='font-style: italic; text-align: center; padding: 10px; color: #555;'>— {random.choice(QUOTES)}</div>", unsafe_allow_html=True)
st.markdown("<div class='disclaimer'>ШІ може робити помилки. Перевіряйте важливу інформацію у адміністрації UKRAINE RP.</div>", unsafe_allow_html=True)
