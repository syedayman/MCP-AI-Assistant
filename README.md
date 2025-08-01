# AI Assistant using MCP Servers

A conversational AI assistant that leverages the Model Context Protocol (MCP) to connect any LLM with various external tools and services. The assistant in this project can interact with web browsers through Playwright and search Airbnb listings, with the flexibility to add more MCP servers as needed. It uses the [mcp-use](https://github.com/mcp-use) library and LangChain to connect any LLM to any MCP server and build custom agents that have tool access and also maintains context across conversations for more natural interactions in a simple command-line interface.

AI Assistant interacting with Airbnb MCP Server to find hotels <img width="1919" height="1016" alt="Screenshot 2025-08-01 141729" src="https://github.com/user-attachments/assets/8c0e1585-4e12-40d1-b777-7f1afdb023d8" />

AI Assistant interacting with Playwright MCP Server for automated browsing <img width="1919" height="1018" alt="Screenshot 2025-08-01 141842" src="https://github.com/user-attachments/assets/2bbbeea1-1dea-4bb7-af1f-92b4f8f7528f" />

<img width="1919" height="1018" alt="Screenshot 2025-08-01 141816" src="https://github.com/user-attachments/assets/c22f3214-95b2-42c1-9575-b97943200e97" />




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
