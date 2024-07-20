import subprocess
import ollama
import typer
from typing import List, Dict, Any
from InquirerPy import inquirer
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

app = typer.Typer()

models_cache = None

def get_models() -> List[str]:
    global models_cache
    if models_cache is None:
        try:
            result = subprocess.run(['ollama', 'list'], capture_output=True, text=True, check=True)
            models = [line.split()[0] for line in result.stdout.splitlines()[1:] if line.split()]
            models_cache = models
        except subprocess.CalledProcessError as e:
            typer.secho(f"Error calling subprocess: {e}", err=True, fg=typer.colors.RED)
            return []
    return models_cache

def agent(prompt: str, model: str, chat_history: List[Dict[str, Any]], language: str) -> str:
    if language:
        prompt = f"Answer in {language} language. " + prompt
    response = ollama.chat(model=model, messages=chat_history + [
        {'role': 'user', 'content': prompt},
    ])
    return response['message']['content']

def final_agent(prompt: str, responses: List[str], model: str, chat_history: List[Dict[str, Any]], language: str):
    combined_prompt = f"Original prompt: {prompt}\n\nResponses from preliminary agents:\n1. {responses[0]}\n2. {responses[1]}\n3. {responses[2]}\n\nGenerate one final response considering these inputs. Don't mention agents. Your answer should be unified and succinct."
    if language:
        combined_prompt = f"Answer in {language} language. " + combined_prompt
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
    if not models:
        typer.secho("No models available. Exiting...", err=True, fg=typer.colors.RED)
        raise typer.Exit()

    selected_model = inquirer.select(
        message="Select a model:",
        choices=models,
    ).execute()

    language = inquirer.text(message="Enter the response language (leave empty for default):").execute()

    chat_history = []

    while True:
        try:
            prompt = input("Enter your prompt (type 'exit' to quit): ")
        except EOFError:
            break
        
        if prompt.lower() == 'exit':
            break

        if not prompt.strip():
            typer.secho("Prompt cannot be empty. Please enter a valid prompt.", fg=typer.colors.RED)
            continue

        chat_history.append({'role': 'user', 'content': prompt})

        responses = []
        with ThreadPoolExecutor(max_workers=2) as executor:
            futures = [executor.submit(agent, prompt, selected_model, chat_history, language) for _ in range(3)]
            for future in as_completed(futures):
                try:
                    responses.append(future.result())
                except Exception as e:
                    typer.secho(f"Error in agent response: {e}", fg=typer.colors.RED)

        if len(responses) < 3:
            typer.secho("Not enough responses generated. Try again.", fg=typer.colors.RED)
            continue

        final_response = final_agent(prompt, responses, selected_model, chat_history, language)
        chat_history.append({'role': 'assistant', 'content': final_response})

if __name__ == "__main__":
    typer.run(main)
