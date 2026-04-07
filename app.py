import streamlit as st
import wikipedia

# ==============================
# 🎨 UI
# ==============================
st.set_page_config(page_title="AI Chatbot (Smart Free)", page_icon="🤖")

st.title("🤖 AI Chatbot (Smart FREE)")
st.markdown("Built by **Kuldeep Singh** 🚀")

# ==============================
# 🧠 FUNCTION
# ==============================
def get_answer(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        return result
    except wikipedia.exceptions.DisambiguationError as e:
        return f"⚠ Be more specific. Options: {e.options[:3]}"
    except wikipedia.exceptions.PageError:
        return "❌ Sorry, I couldn't find information."
    except:
        return "⚠ Something went wrong."

# ==============================
# 💬 MEMORY
# ==============================
if "messages" not in st.session_state:
    st.session_state.messages = []

# ==============================
# DISPLAY CHAT
# ==============================
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ==============================
# INPUT
# ==============================
user_input = st.chat_input("Ask anything...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Searching... 🔍"):
            answer = get_answer(user_input)
            st.write(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})