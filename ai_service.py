import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def create_simple_tasks(description):
    if not client.api_key:
        return ["Error: The api key from openai is not configured."]
    
    try:
        prompt = f"""Divide the following task into a list of 3 to 5 minitasks. 

Task: {description}

Answer's format:
- Task 1 
- Task 2 
- Task 3
- etc

Respond only with the list of minitaks, one by line, starting each line with a - """
        params = {
            "model": "gpt-5",
            "messages": [
                {"role": "system", "content": "You are an assistent expert in tasks management that helps dividing complex tasks in simple steps."},
                {"role": "user", "content": prompt}
            ],
            "max_completion_tokens": 300,
            "verbosity": "medium",
            "reasoning_effort": "minimal"
        }

        response = client.chat.completions.create(**params)
        content = response.choices[0].message.content.strip()

        subtasks = []

        for line in content.split("\n"):
            line = line.strip()
            if line and line.startswith("-"):
                subtask = line[1:].strip()
                if subtask:
                    subtasks.append(subtask)
        return subtasks if subtasks else ["Error: Couldn't generate the subtasks."]

    except Exception:
        return ["Error: Connection with OpenAI was not successful"]