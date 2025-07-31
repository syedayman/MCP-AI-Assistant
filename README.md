# AI Assistant using MCP Servers

A conversational AI assistant that leverages the Model Context Protocol (MCP) to connect any LLM with various external tools and services. The assistant in this project can interact with web browsers through Playwright and search Airbnb listings, with the flexibility to add more MCP servers as needed. It uses the [mcp-use](https://github.com/mcp-use) library and LangChain to connect any LLM to any MCP server and build custom agents that have tool access and also maintains context across conversations for more natural interactions in a simple command-line interface.

## Usage
1. Clone the repository
2. Install uv package manager using `pip install uv`
3. Navigate to project directory and create and activate a virtual environment with uv
```
uv venv
.venv\Scripts\activate 
```
4. Install dependencies with `uv sync`
5. Set up environment variables (OPENAI_API_KEY)
6. Run the application using `uv run app.py`
