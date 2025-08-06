import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

course_content = """
An operating system (OS) is system software that manages computer hardware, software resources, 
and provides common services for computer programs. Time-sharing operating systems schedule tasks 
for efficient use of the system and may include accounting for resource usage. Operating systems 
perform tasks such as managing memory, processes, software and hardware, and facilitating user interaction 
through graphical interfaces or command-line tools. Examples include Windows, macOS, Linux, and Unix.
"""

payload = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a teacher's assistant. Create a study guide."},
        {"role": "user", "content": course_content}
    ]
)

study_guide = payload['choices'][0]['message']['content']

print("Course Review: ", study_guide)