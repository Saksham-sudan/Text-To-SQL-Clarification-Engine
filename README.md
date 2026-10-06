# Text-To-SQL Clarification Engine

A **GenAI**-based intelligent clarification engine that converts **natural language** to accurate **SQL** queries and asks clarifying questions if the current context is not enough to generate a valid query.

## Installation

- First, clone this repo.
- Open your terminal and run `pip install -r requirements.txt`.
- Create a **.env** file in the root folder.
- Add a `GEMINI_API_KEY=""` variable to the `.env` file.
- Go to **Google AI Studio** to get a Gemini API key and paste it into the variable.
    - *Note:* You can change the model name in the `chat_module` depending on which model you prefer to use.

## System Structure

The clarification system is divided into the following components:
- **Loader module:** A basic script to load the database schema.
- **Clarification module:** The heart of the system. This is where the magic happens, transforming the tool from a basic Text-to-SQL script into a powerful, context-dependent clarification engine.
- **Chat module:** A call point to the external API (Gemini) to provide the brains for the whole system.
- **main.py:** Serves as the entry point for the CLI script. Run it to get started.

## Future Scope
- Make a basic web interface.
- Add Retrieval-Augmented Generation (RAG).
- Add an option for custom database input.
- Add an option to change the inference model dynamically.
- Add a "bad day protocol" throughout the whole system for error handling.
- Add token and context constraints.