# TaskingAI-client

The official TaskingAI Python client.

For more information, see the docs at [TaskingAI Documentation](https://docs.tasking.ai/)

## Prerequisites

The TaskingAI client is compatible with Python 3.8 and above.

## Installation

Use `pip` to install the TaskingAI Python client.

```shell
# Install the latest version
pip install taskingai

# Install a specific version
pip install taskingai==0.2.2
```

## Usage

### Initialization

Before you can use the TaskingAI SDK, you must have your TaskingAI project set up and running. For community version, visit [TaskingAI Community](https://www.github.com/taskingai/taskingai) to get started. For cloud version, visit [TaskingAI Cloud](https://www.tasking.ai) to sign up first.

You need to initialize the TaskingAI Python client with an API key you obtain from the TaskingAI console. You can set the API key as an environment variable or pass it directly to the `init` function.

#### Using environment variables (Recommended)

Set it as an environment variable on your local system, and the SDK will automatically load the key without passing the `api_key` parameter in the `init` function.

```shell
export TASKINGAI_API_KEY=$YOUR_API_KEY
```

When you run your Python script, the SDK will automatically pick up the API key from the environment variable.

```python
import taskingai
# taskingai.init()
# No need to initialize the SDK with the API key
```

#### Passing the API key directly

You can also specify an API key to the SDK by passing it as a parameter to the init function:

```python
import taskingai
taskingai.init(api_key="YOUR_API_KEY")
```

If you use community version, you can set the base URL to the TaskingAI server by passing it to the `init` function:

```python
import taskingai
taskingai.init(api_key="YOUR_API_KEY", host="http://localhost:8080")
```

### Assistants

The Assistant system in TaskingAI represents a sophisticated framework designed to create and manage AI agents with customizable functionalities.

Here is an example of how to create, update, and delete an assistant:

```python
import taskingai

# Initialize your API key if you haven't already set it in the environment
taskingai.init(api_key="YOUR_API_KEY")

# Create an assistant
asst = taskingai.assistant.create_assistant(
    model_id="YOUR_MODEL_ID",
    memory={"type": "naive"},
    system_prompt_template=["You are a professional assistant."],
)
print(f"Assistant created: {asst.assistant_id}")

# Get details about the assistant
assistant_details = taskingai.assistant.get_assistant(assistant_id=asst.assistant_id)
print(f"Assistant details: {assistant_details}")

# Update the assistant's description
taskingai.assistant.update_assistant(
    assistant_id=asst.assistant_id,
    description="Updated description"
)
print(f"Assistant updated.")

# Delete the assistant when done
taskingai.assistant.delete_assistant(assistant_id=asst.assistant_id)
print("Assistant deleted successfully.")
```

### Retrieval

TaskingAI offers comprehensive tools for the retrieval system, ranging from straightforward to intricate setups. Here is an example of how to create, add, retrieve, and delete a record in a collection:

```python
import taskingai

# Create a collection for storing and retrieving data
coll = taskingai.retrieval.create_collection(
    embedding_model_id="YOUR_EMBEDDING_MODEL_ID",
    capacity=1000
)
print(f"Collection created: {coll.collection_id}")

# Add a record to the collection
record = taskingai.retrieval.create_record(
    collection_id=coll.collection_id,
    type="text",
    content="Machine learning is ...",
    text_splitter={"type": "token", "chunk_size": 200, "chunk_overlap": 20}
)
print(f"Record added to collection: {record.record_id}")

# Retrieve the record from the collection
retrieved_record = taskingai.retrieval.get_record(
    collection_id=coll.collection_id,
    record_id=record.record_id
)
print(f"Record retrieved: {retrieved_record.content}")

# Delete the record
taskingai.retrieval.delete_record(
    collection_id=coll.collection_id,
    record_id=record.record_id
)
print("Record deleted.")

# Delete the collection
taskingai.retrieval.delete_collection(collection_id=coll.collection_id)
print("Collection deleted.")
```

## Contributing

We welcome contributions of all kinds. Please read our [Contributing Guidelines](./CONTRIBUTING.md) for more information on how to get started.
