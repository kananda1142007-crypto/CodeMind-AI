
import ollama

def review_code(code, previous_memory=""):

    prompt = f"""
You are CodeMind AI, an expert Java code reviewer.

Previous developer memory:
{previous_memory}

Review the following Java code.

Explain:
1. Bugs and errors
2. Code quality issues
3. Improvements
4. Corrected code

Java code:
{code}
"""

    response = ollama.chat(
        model="llama3.2:latest",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"]
