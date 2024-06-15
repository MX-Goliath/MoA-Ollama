# MoA-Ollama
Mixture of Agents (MoA) using ollama and python

This project implements the concept of a Mixture of Agents (MoA), where several preliminary agents generate basic responses to a given prompt, and one final agent combines these responses to generate the final answer. The project also includes a console chat with the bot, which maintains the dialogue history.

## Requirements

- Python 3.x
- `ollama` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/moa-chatbot.git
    cd moa-chatbot
    ```

2. Install the `ollama` library:
    ```sh
    pip install ollama
    ```

## Usage

To start the console chat, run:
```sh
python moa_chatbot.py
```

### Code Structure

- `agent_1(prompt)`: The first preliminary agent that generates a basic response to the given prompt.
- `agent_2(prompt)`: The second preliminary agent that generates a basic response to the given prompt.
- `agent_3(prompt)`: The third preliminary agent that generates a basic response to the given prompt.
- `final_agent(prompt, responses)`: The final agent that combines the responses from the preliminary agents and generates the final response.
- `mixture_of_agents_with_history(history, prompt)`: The main function that orchestrates the agents' work and maintains the dialogue history.
- `chat()`: The function to start the console chat.

### Example

```sh
You: Why is the sky blue?
Bot: The sky is blue due to the scattering of light in the atmosphere. Shorter blue light waves scatter more than longer red light waves, making the sky appear blue.
```

### Exiting

To exit the chat, type `exit` or `quit`.


