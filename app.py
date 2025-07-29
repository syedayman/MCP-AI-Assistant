import asyncio
import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from mcp_use import MCPClient, MCPAgent

async def run_memory_chat():
    """ Run a chat using MCPAgent's built in conversation memory. """

    load_dotenv()
    #os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    config_file = "mcp_config.json"
    print("Initializing MCP server...")

    client = MCPClient.from_config_file(config_file)
    #llm = ChatOpenAI(model="gpt-4o")
    llm = ChatGroq(model="qwen-qwq-32b")
    
    agent = MCPAgent(
        llm=llm,
        client=client,
        max_steps=15,
        memory_enabled=True,
    )

    print("\n ~~~~~ Chat with any MCP server ~~~~~")
    print("Type 'exit' to end the chat")
    print("Type 'clear' to clear conversation history")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    try:
        while True:
            user_input = input("\nYou: ")                       # get user input

            if user_input.lower() in ["exit", "quit"]:          # check for exit
                print("Exiting...")
                break

            if user_input.lower() == "clear":                   # check for clear history
                agent.clear_conversation_history()
                print("Conversation history cleared.")
                break

            print("\nAssistant: ", end="", flush=True)           # print assistant response

            try:
                response = await agent.run(user_input)           # run the agent with user input
                print(response)                                  # automatic memory handling   

            except Exception as e:
                print(f"\nError: {e}")

    finally:                                                     # clean up
        if client and client.sessions:
            await client.close_all_sessions()

if __name__ == "__main__":
    asyncio.run(run_memory_chat())


