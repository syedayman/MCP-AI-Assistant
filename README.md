# AI Assistant using MCP Servers

A conversational AI assistant that leverages the Model Context Protocol (MCP) to connect any LLM with various external tools and services. The assistant in this project can interact with web browsers through Playwright and search Airbnb listings, with the flexibility to add more MCP servers as needed. It uses the [mcp-use](https://github.com/mcp-use) library and LangChain to connect any LLM to any MCP server and build custom agents that have tool access and also maintains context across conversations for more natural interactions in a simple command-line interface.

## Usage

1. Install uv package manager using `pip install uv`
2. Clone the repository with `git clone https://github.com/syedayman/MCP-AI-Assistant.git`
3. Navigate to project directory `cd MCP-AI-Assistant`
4. Create and activate a virtual environment with uv
```
uv venv
.venv\Scripts\activate 
```
4. Install dependencies with `uv sync`
5. Set up environment variables in your `.env` file in this format
```OPENAI_API_KEY = your_api_key_here```
7. Run the application using `uv run app.py`
