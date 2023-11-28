import taskingai
import os
# Load TaskingAI API Key from environment variable
model_id = os.environ.get("MODEL_ID")
print(taskingai.Config.API_KEY, taskingai.Config.HOST, model_id)

from taskingai.inference import *
# choose an available chat_completion model from your project

# function call
function = Function(
    name="plus_a_and_b",
    description="Sum up a and b and return the result",
    parameters={
        "type": "object",
        "properties": {
            "a": {
                "type": "integer",
                "description": "The first number"
            },
            "b": {
                "type": "integer",
                "description": "The second number"
            }
        },
        "required": ["a", "b"]
    },
)
chat_completion = taskingai.inference.chat_completion(
    model_id=model_id,
    messages=[
        SystemMessage("You are a professional assistant."),
        UserMessage("What is the result of 112 plus 22?"),
        AssistantMessage(
            function_call=FunctionCall(name="plus_a_and_b", arguments={"a": 112, "b": 22}),
        ),
        FunctionMessage(
            name="plus_a_and_b",
            content="144"
        )
    ],
    functions=[function]
)


print(chat_completion.message)