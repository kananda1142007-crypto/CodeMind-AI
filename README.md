# 🧠 CodeMind AI

**An Intelligent Java Code Review Agent with Persistent Memory**

CodeMind AI is an AI-powered Java code review assistant that detects programming mistakes, explains errors, suggests improved code, and remembers previous coding mistakes using Hindsight memory.

## Features

- Java code review using local AI.
- Detects bugs and programming errors.
- Explains problems in simple language.
- Suggests improved Java code.
- Stores previous code reviews using Hindsight.
- Retrieves past coding mistakes and preferences.
- Uses previous memories to personalize future reviews.

## Technologies Used

- Python
- Streamlit
- Ollama
- Llama 3.2
- Hindsight Memory
- Docker

## Architecture

1. User enters Java code in the Streamlit interface.
2. CodeMind retrieves relevant developer memories from Hindsight.
3. Ollama (Llama 3.2) reviews the Java code using the retrieved context.
4. The AI generates bugs, explanations, corrected code, and suggestions.
5. The review is saved to Hindsight for future retrieval.

## Installation

### Prerequisites

- Python
- Docker Desktop
- Ollama
- Llama 3.2 model

### Setup

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd CodeMind-AI
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Download the AI model:

```bash
ollama pull llama3.2
```

Start the Hindsight API server using the project's configured local setup.

Run the application:

```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

## Project Structure

```text
CodeMind-AI/
├── app.py
├── config.py
├── memory.py
├── reviewer.py
├── requirements.txt
├── README.md
├── test_ai.py
└── test_memory.py
```

## Project Goal

To help Java developers and students improve their coding skills through intelligent code reviews and persistent AI memory.

## Developed For

Hindsight AI Agent Challenge.
