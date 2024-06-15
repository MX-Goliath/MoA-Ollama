import subprocess
import ollama
import typer
from typing import List, Dict, Any
from InquirerPy import inquirer

app = typer.Typer()

def get_models() -> List[str]:
    result = subprocess.run(['ollama', 'list'], capture_output=True, text=True)
    models = []
    for line in result.stdout.splitlines()[1:]:  # Пропускаем заголовок
        parts = line.split()
        if len(parts) >= 1:
            models.append(parts[0])
    return models

def agent(prompt: str, model: str, chat_history: List[Dict[str, Any]]) -> str:
    response = ollama.chat(model=model, messages=chat_history + [
        {'role': 'user', 'content': prompt},
    ])
    return response['message']['content']

def final_agent(prompt: str, responses: List[str], model: str, chat_history: List[Dict[str, Any]]):
    combined_prompt = f"Original prompt: {prompt}\n\nResponses from preliminary agents:\n1. {responses[0]}\n2. {responses[1]}\n3. {responses[2]}\n\nGenerate one final response considering these inputs. Don't mention agents. Your answer should be unified and succinct."
    response = ollama.chat(model=model, messages=chat_history + [
        {'role': 'user', 'content': combined_prompt},
    ],
    stream=True
    )
    final_response = ""
    for chunk in response:
        print(chunk['message']['content'], end='', flush=True)
        final_response += chunk['message']['content']
    print('\n')
    return final_response

def main():
    models = get_models()
    selected_model = inquirer.select(
        message="Select a model:",
        choices=models,
    ).execute()

    chat_history = []

    while True:
        prompt = typer.prompt("Enter your prompt (type 'exit' to quit)")
        if prompt.lower() == 'exit':
            break

        chat_history.append({'role': 'user', 'content': prompt})

        responses = []
        for _ in range(3):
            response = agent(prompt, selected_model, chat_history)
            responses.append(response)
        
        final_response = final_agent(prompt, responses, selected_model, chat_history)
        chat_history.append({'role': 'assistant', 'content': final_response})

if __name__ == "__main__":
    typer.run(main)
