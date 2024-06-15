# Chatbot with Multiple Agent Responses

This project is a chatbot application built with Python. It uses the `ollama` library to interact with different models, generate responses, and provide a final unified response based on multiple preliminary responses. The application uses `typer` for command-line interface creation and `InquirerPy` for model selection prompts.

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
    git clone https://github.com/yourusername/yourrepository.git
    cd yourrepository
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

## Code Overview

- `get_models()`: Retrieves a list of available models from `ollama`.
- `agent(prompt, model, chat_history)`: Generates a response from a single agent.
- `final_agent(prompt, responses, model, chat_history)`: Combines preliminary responses into a final unified response.
- `main()`: Main function to run the interactive CLI.

## Example

```sh
$ python main.py
Select a model: 
> model1
  model2
  model3
Enter your prompt (type 'exit' to quit): Hello, how are you?
Response from agent 1: ...
Response from agent 2: ...
Response from agent 3: ...
Final unified response: ...
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## Contact

For any questions or suggestions, please open an issue on the GitHub repository.

---

Feel free to customize this README further to suit your project's specific details and needs.
