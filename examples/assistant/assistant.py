import taskingai
from taskingai.assistant import Assistant

# Load TaskingAI API Key fron environment variable

# choose an available chat_completion model from your project
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

print(f"created assistant: {assistant}\n")


# get assistant
assistant_id: str = assistant.assistant_id
assistant: Assistant = taskingai.assistant.get_assistant(
    assistant_id=assistant_id
)

print(f"got assistant: {assistant}\n")


# update assistant
assistant: Assistant = taskingai.assistant.update_assistant(
    assistant_id=assistant_id,
    name="My New Assistant",
    description="This is my new assistant",
)

print(f"updated assistant: {assistant}\n")


# delete assistant
taskingai.assistant.delete_assistant(assistant_id=assistant_id)
print(f"deleted assistant: {assistant_id}\n")

# list assistants
assistants = taskingai.assistant.list_assistants()
assistant_ids = [assistant.assistant_id for assistant in assistants]
print(f"list assistants: {assistants}\n")
print(f"f{assistant_id} in {assistant_ids}: {assistant_id in assistant_ids}\n")






