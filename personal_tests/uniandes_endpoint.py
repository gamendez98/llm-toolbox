import os
from typing import cast
from dotenv import load_dotenv
from openai.lib.azure import AzureOpenAI
from openai.types.chat import ChatCompletionMessageParam

load_dotenv()


def main():
    model_name = "gpt-4-32k-rfmanrique"
    deployment_name = "gpt"
    messages = [{
        'content': "Don't make assumptions about what values to plug into functions. Ask for clarification if a user request is ambiguous.",
        'role': 'system'}, {'content': 'Turn off wifi', 'role': 'user'}]
    openai_tools = [{'function': {'description': 'Enable / Disable wifi', 'name': 'set_wifi_status', 'parameters': {
        'properties': {'on': {'description': 'If we want to turn on wifi', 'type': 'boolean'}}, 'required': ['on'],
        'type': 'object'}}, 'type': 'function'}]
    azure_api_key = os.getenv("AZURE_OPENAI_API_KEY", "EMPTY")
    openai_client = AzureOpenAI(
        azure_endpoint="https://invuniandesai-2.openai.azure.com/",
        api_version="2024-12-01-preview",
        api_key=azure_api_key
    )
    print(
        openai_client.chat.completions.create(
            model=deployment_name,
            messages=cast(list[ChatCompletionMessageParam], messages),
            tools=openai_tools,
        )
    )


if __name__ == "__main__":
    main()
