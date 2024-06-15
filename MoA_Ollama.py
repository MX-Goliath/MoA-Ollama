import ollama
default_model="llama3"
# Define preliminary agents
def agent_1(prompt, default_model):
    response = ollama.chat(model=default_model, messages=[
      {'role': 'user', 'content': prompt},
    ])
    return response['message']['content']

def agent_2(prompt, default_model):
    response = ollama.chat(model=default_model, messages=[
      {'role': 'user', 'content': prompt},
    ])
    return response['message']['content']

def agent_3(prompt, default_model):
    response = ollama.chat(model=default_model, messages=[
      {'role': 'user', 'content': prompt},
    ])
    return response['message']['content']

# Define the final agent
def final_agent(prompt, responses, default_model):
    combined_prompt = f"Original prompt: {prompt}\n\nResponses from preliminary agents:\n1. {responses[0]}\n2. {responses[1]}\n3. {responses[2]}\n\nGenerate one final response considering these inputs. Don't mention agents. Your answer should be unified and succinct. "
    response = ollama.chat(model=default_model, messages=[
      {'role': 'user', 'content': combined_prompt},
    ],
    stream=True
    )
    for chunk in response:
      print(chunk['message']['content'], end='', flush=True)
    print('\n')
    # return response['message']['content']

# Main function to orchestrate the MoA
def mixture_of_agents(prompt):
    responses = []
    responses.append(agent_1(prompt, default_model))
    responses.append(agent_2(prompt, default_model))
    responses.append(agent_3(prompt, default_model))
    
    final_response = final_agent(prompt, responses, default_model)
    return final_response

# Example usage
prompt = "why is the sky blue?"
final_answer = mixture_of_agents(prompt)

