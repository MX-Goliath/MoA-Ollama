# Mixture of Agents (MoA) Chatbot

This project implements the concept of a Mixture of Agents (MoA), where several preliminary agents generate basic responses to a given prompt, and one final agent combines these responses to generate the final answer. The project also includes a console chat with the bot, which maintains the dialogue history.

## Features

- **Model Listing**: Retrieve and display a list of available models from `ollama`.
- **Multi-Agent Response Generation**: Generate responses from multiple agents and combine them into a final unified response.
- **Interactive CLI**: Command-line interface for user interaction, including prompts and model selection.

## Requirements

- Python 3.7+
- `ollama` library
- `typer` library
- `InquirerPy` library

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/MX-Goliath/MoA-Ollama.git
    cd MoA-Ollama
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```sh
    pip install ollama typer InquirerPy
    ```

## Usage

1. **Run the application**:
    ```sh
    python main.py
    ```

2. **Follow the prompts**:
    - Select a model from the list of available models.
    - Enter your prompts when asked. Type 'exit' to quit the application.

3. **Interaction Flow**:
    - The application will generate responses using multiple agents.
    - A final unified response will be generated based on the preliminary responses.
    - The conversation history will be maintained throughout the session.


