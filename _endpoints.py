
def prompt_claude(message: str, model="claude-3-5-sonnet-20241022", image=None):
    """
    A prompt helper function that sends a message to anthropic
    and returns only the text response.

    Example models: claude-3-5-sonnet-20240620 or claude-3-opus-20240229
    """
    from anthropic import Anthropic

    # convert message in the right format if necessary
    if image is None:
        message = [{"role": "user", "content": message}]
    else:
        message = [{
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": message
                },
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/png",
                        "data": image
                    }
                }
            ]
        }]

    # setup connection to the LLM
    client = Anthropic()

    message = client.messages.create(
        messages=message,
        model=model,
        max_tokens=10,
    )

    # extract answer
    return message.content[0].text


def prompt_chatgpt(message: str, model="gpt-4o-2024-08-06", image=None):
    """A prompt helper function that sends a message to openAI
    and returns only the text response.
    """
    # convert message in the right format if necessary
    import openai
    import warnings

    if image is None:
        message = [{"role": "user", "content": message}]
    else:
        message = [{"role": "user", "content": [{
                    "type": "text",
                    "text": message,
                },{
                    "type": "image_url",
                    "image_url": {"url": "data:image/png;base64," + image}
                }]}]

    # setup connection to the LLM
    client = openai.OpenAI()

    # submit prompt
    response = client.chat.completions.create(
        model=model,
        messages=message,
        max_tokens=10,
    )

    # extract answer
    return response.choices[0].message.content


def prompt_gemini(request, model="gemini-1.5-flash-001", image=None):
    """Send a prompt to Google Gemini and return the response"""
    from google import generativeai as genai
    import os
    import base64
    
    genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
    client = genai.GenerativeModel(model)
    
    if image is not None:
        response = client.generate_content([image, request])
    else:
        response = client.generate_content(request)
        
    return response.text


def prompt_gh_models(message: str, model: str, image=None):
    """
    A helper function that sends a message to the Azure VLM endpoints
    with optional image input and returns the text response.
    """
    import os
    import base64
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import (
        UserMessage,
        TextContentItem,
        ImageContentItem,
        ImageUrl,
        ImageDetailLevel,
    )
    from azure.core.credentials import AzureKeyCredential

    # Azure setup
    token = os.environ["GITHUB_TOKEN"]
    endpoint = "https://models.inference.ai.azure.com"

    # Initialize the client
    client = ChatCompletionsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(token),
    )

    # Build the message with optional image
    content_items = [TextContentItem(text=message)]
    if image:
        content_items.append(
            ImageContentItem(image_url={"url": "data:image/png;base64," + image})
        )

    # Submit the request
    response = client.complete(
        messages=[
            UserMessage(content=content_items)
        ],
        model=model,
        max_tokens=10,
    )

    # Extract and return the response
    return response.choices[0].message.content

