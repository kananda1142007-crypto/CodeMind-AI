
import streamlit as st
from groq import Groq
from memory import save_memory, recall_memory

st.set_page_config(
    page_title="CodeMind AI",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 CodeMind AI")
st.subheader("Intelligent Java Code Review Agent with Persistent Memory")

st.write(
    "Your AI coding assistant that remembers previous "
    "mistakes, coding preferences and Java concepts."
)

st.divider()

# Connect to Groq
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except Exception:
    client = None

st.header("☕ Java Code Reviewer")

code = st.text_area(
    "Paste your Java code here:",
    height=300,
    placeholder="public class Main {\n    public static void main(String[] args) {\n        System.out.println(\"Hello World\");\n    }\n}"
)

if st.button("🔍 Review My Code"):
    if not code.strip():
        st.warning("Please enter Java code first.")

    elif client is None:
        st.error("Groq API key is missing. Check Streamlit Secrets.")

    else:
        with st.spinner("Reviewing your Java code..."):
            try:
                # Try to recall previous memories
                try:
                    previous = recall_memory(
                        "Previous Java coding mistakes and preferences"
                    )
                    context = "\n".join(previous) if previous else "No previous memory."
                except Exception:
                    context = "Memory service is currently unavailable."

                response = client.chat.completions.create(
                    model="openai/gpt-oss-20b",
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are CodeMind AI, an expert Java code reviewer "
                                "and personal coding mentor. Explain problems in "
                                "simple language. Identify bugs, errors, improvements "
                                "and best practices. Use previous developer memories "
                                "when available. Never invent past mistakes."
                            )
                        },
                        {
                            "role": "user",
                            "content": f"""
Previous developer memory:
{context}

Review this Java code:

{code}

Give:
1. Bugs and errors
2. Explanation of each problem
3. Improved Java code
4. Suggestions for improvement
"""
                        }
                    ]
                )

                review = response.choices[0].message.content

                st.session_state["last_review"] = review
                st.session_state["last_code"] = code

                # Save review to Hindsight if available
                try:
                    save_memory(
                        f"Java code review: {review}. Original code: {code}"
                    )
                    st.success("Review completed and memory saved!")
                except Exception:
                    st.warning(
                        "Review completed, but Hindsight is not connected online yet."
                    )

            except Exception as e:
                st.error(f"AI review error: {e}")

if "last_review" in st.session_state:
    st.subheader("📋 AI Code Review")
    st.markdown(st.session_state["last_review"])

st.divider()

# Developer Memory
st.header("🧠 Developer Memory")
st.write("Ask CodeMind AI what it remembers from previous reviews.")

question = st.text_input(
    "Ask about your previous coding reviews:",
    placeholder="What Java mistakes did I make previously?"
)

if st.button("🧠 Recall Memory"):
    if not question.strip():
        st.warning("Enter a question first.")
    else:
        with st.spinner("Searching Hindsight memory..."):
            try:
                memories = recall_memory(question)

                if memories:
                    for item in memories:
                        st.info(item)
                else:
                    st.warning("No related memories found.")

            except Exception:
                st.error(
                    "Hindsight is not connected to the online website yet."
                )
