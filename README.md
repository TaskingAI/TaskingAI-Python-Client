# TaskingAI-client

The TaskingAI Python client for creating and managing AI-driven applications.

For more information, see the docs at [TaskingAI Documentation](https://docs.tasking.ai/)

## Installation

Install the latest released version using pip:

```shell
pip3 install taskingai
```

## Quickstart

Here's how you can quickly start building and managing AI-driven applications using the TaskingAI client.

### Assistants

Explore the ease of creating and customizing your own AI assistants with TaskingAI to enhance user interactions.

```python
import taskingai
from taskingai.assistant import *
from taskingai.assistant.memory import AssistantNaiveMemory

# Initialize your API key if you haven't already set it in the environment
taskingai.init(api_key="YOUR_API_KEY")

# Create an assistant
assistant = create_assistant(
    model_id="YOUR_MODEL_ID",
    memory=AssistantNaiveMemory(),
    system_prompt_template=["You are a professional assistant."],
)
print(f"Assistant created: {assistant.id}")

# Get details about the assistant
assistant_details = get_assistant(assistant_id=assistant.id)
print(f"Assistant details: {assistant_details}")

# Update the assistant's description
update_assistant(
    assistant_id=assistant.id,
    description="An updated description for my assistant."
)
print(f"Assistant updated.")

# Delete the assistant when done
delete_assistant(assistant_id=assistant.id)
print("Assistant deleted successfully.")
```

### Retrieval

Leverage TaskingAI's retrieval capabilities to store, manage, and extract information, making your applications smarter and more responsive.

```python
import taskingai
from taskingai.retrieval import *

# Create a collection for storing and retrieving data
collection = create_collection(
    embedding_model_id="YOUR_MODEL_ID",
    capacity=1000
)
print(f"Collection created: {collection.id}")

# Add a record to the collection
record = create_record(
    collection_id=collection.id,
    content="Example text for machine learning.",
    text_splitter=TokenTextSplitter(chunk_size=200, chunk_overlap=20),
)
print(f"Record added to collection: {record.id}")

# Retrieve the record from the collection
retrieved_record = get_record(
    collection_id=collection.id,
    record_id=record.id
)
print(f"Record retrieved: {retrieved_record.text}")

# Delete the record
delete_record(
    collection_id=collection.id,
    record_id=record.id
)
print("Record deleted.")

# Delete the collection
delete_collection(collection_id=collection.id)
print("Collection deleted.")
```

### Tools

Utilize TaskingAI's tools to create actions that enable your assistant to interact with external APIs and services, enriching the user experience.

```python
import taskingai
from taskingai.tool import *

# Define a schema for the tool action
NUMBERS_API_SCHEMA = {
    # Schema definition goes here
}

# Create a tool action based on the defined schema
actions = bulk_create_actions(
    schema=NUMBERS_API_SCHEMA,
    authentication=ActionAuthentication(type=ActionAuthenticationType.NONE)
)
action = actions[0]
print(f"Action created: {action.id}")

# Run the action for a test purpose
result = run_action(
    action_id=action.id,
    parameters={"number": 42}
)
print(f"Action result: {result}")

# Delete the action when done
delete_action(action_id=action.id)
print("Action deleted.")
```

## Contributing

We welcome contributions of all kinds. Please read our [Contributing Guidelines](./CONTRIBUTING.md) for more information on how to get started.
