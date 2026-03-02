import streamlit as st
from openai import OpenAI
import random

# 1. Налаштування сторінки
st.set_page_config(page_title="UR AI Helper (Qwen)", page_icon="🤖")

# Стилізація інтерфейсу (CSS)
st.markdown("""
    <style>
    .stApp { background-color: #f0f2f5; }
    .chat-header { 
        background: white; 
        padding: 20px; 
        text-align: center; 
        font-size: 1.8rem; 
        font-weight: bold; 
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        color: #1a1a1a;
        margin-bottom: 20px;
    }
    </style>
    <div class="chat-header">🤖 Помічник Юр (Qwen AI)</div>
    """, unsafe_allow_html=True)

# 2. Налаштування OpenRouter (Ключ має бути у Secrets)
if "OPENROUTER_API_KEY" in st.secrets:
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=st.secrets["OPENROUTER_API_KEY"],
    )
else:
    st.error("❌ Помилка: OPENROUTER_API_KEY не знайдено у Secrets!")
    st.stop()

# 3. База знань та Цитати
QUOTES = [
    "RP — це не гра в перемогу, це гра в історію.",
    "Повага до RP інших — основа сильного сервера.",
    "Не шукай легких шляхів — шукай цікавих історій."
]

SYSTEM_PROMPT = """
Ти — штучний інтелект Юр, помічник сервера 'UKRAINE RP' у грі Emergency Hamburg.
Твоє завдання: допомагати гравцям з правилами.
Твоя база знань:
- Пункт 1 Стаття 1: RP-образи. Заборонено ображати гравців. Покарання через суд: штраф до 8 000€.
Якщо питання НЕ стосується RP або сервера UKRAINE RP, відповідай дослівно: 
'Я не знаю відповіді, так як я відповідаю на питання, лише пов'язані з правилами Сервера UKRAINE RP'.
"""

# 4. Логіка чату
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Вітаю! Я Юр на базі Qwen. Чим можу допомогти гравцеві UKRAINE RP?"}
    ]

# Відображення повідомлень
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Поле вводу
if prompt := st.chat_input("Запитай щось про правила..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        placeholder = st.empty()
        placeholder.markdown("* /me Думаю (Qwen AI)...*")
        
        try:
            # Використовуємо модель Qwen 2.5 72B (вона дуже розумна)
            response = client.chat.completions.create(
                model="qwen/qwen3-next-80b-a3b-instruct:free", 
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    *st.session_state.messages
                ],
                extra_headers={
                    "HTTP-Referer": "https://streamlit.io", # Обов'язково для OpenRouter
                    "X-Title": "Ukraine RP Assistant",
                }
            )
            answer = response.choices[0].message.content
            placeholder.markdown(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})
        except Exception as e:
            placeholder.error(f"Помилка Qwen API: {e}")

# Нижня частина
st.markdown("---")
st.markdown(f"<div style='text-align: center; color: #666;'>— {random.choice(QUOTES)}</div>", unsafe_allow_html=True)
