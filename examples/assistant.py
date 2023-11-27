import taskingai
from taskingai.assistant import Assistant

# Load TaskingAI API Key fron environment variable

model_id = "Gk1145Bl"


# create an assistant
assistant: Assistant = taskingai.assistant.create_assistant(
    model_id=model_id,
    name="My Assistant",
    description="This is my assistant",
    system_prompt_template=["You are a professional assistant speaking {{language}}."],
    tools=[],
    retrievals=[],
    metadata={"foo": "bar"},
)

print(f"created assistant: {assistant}")


# get assistant
assistant_id: str = assistant.assistant_id
assistant: Assistant = taskingai.assistant.get_assistant(
    assistant_id=assistant_id
)

print(f"got assistant: {assistant}")








