from agents import Agent, Runner, AsyncOpenAI, set_default_openai_client, OpenAIChatCompletionsModel, set_tracing_disabled
from dotenv import load_dotenv
import os

# Import environment variables from a .env file to securely access sensitive data
load_dotenv()

# Fetch the Gemini API key stored in the environment variables
gemini_api_key = os.getenv("GEMINI-API-KEY")

# Display the API key for debugging (remove this in production to avoid exposing sensitive info)
print("gemini_api_key", gemini_api_key)

# Initialize a client to make OpenAI-compatible requests to the Gemini API
external_client = AsyncOpenAI(
        api_key = gemini_api_key,  # Pass the Gemini API key for authentication
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"  # Point to Gemini's OpenAI-compatible API endpoint
)

# Configure the Gemini client as the default for all OpenAI-style API interactions
set_default_openai_client(external_client)

# Turn off internal tracing to reduce unnecessary logs and simplify output
set_tracing_disabled(True)

# Set up a chat model that uses the Gemini model, styled like an OpenAI model
model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",  # Specify the Gemini 2.0 Flash model for processing
    openai_client=external_client  # Link to the Gemini client configured earlier
)

# Define the main function to execute the AI assistant
def main():
    # Create an AI agent with a name, role description, and the Gemini model
    agent = Agent(name="Assistant", instructions="You are a helpful assistant.", model=model)

    # Run the agent synchronously to answer a question about the capital of Pakistan
    result = Runner.run_sync(agent, "Hello, What is the capital of Pakistan?")

    # Output the agent's final response (e.g., the answer provided by the model)
    print(result.final_output)