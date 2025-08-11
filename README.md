# MarkInt_Agent
A multi-agent system for tracking AI news, company updates, model launches, funding, and founder stories. Uses web search + Neo4j knowledge graph to store, link, and visualise facts over time, delivering context-aware reports with CrewAI and MCP tools.


# MarkInt – AI Industry Intelligence Agent

MarkInt is a multi-agent AI system for tracking and reporting on the latest developments in the AI industry.  
It continuously searches for news, startup updates, model launches, funding rounds, and founder stories, storing them in a Neo4j-powered knowledge graph for context-aware, longitudinal insights.

## 🚀 Features
- **Web Search Agent** – Finds credible and timely AI-related news and announcements.  
- **Memory Manager Agent** – Stores and links facts in a Neo4j graph database for future reference.  
- **Response Generator Agent** – Produces polished, context-rich reports from past and present data.  
- **Knowledge Graph Integration** – Organises and connects AI developments for trend analysis.  
- **CrewAI & MCP Tools** – Orchestrates tasks with multi-agent collaboration and external tools.

## 🛠 Tech Stack
- **Python**  
- **CrewAI** for multi-agent orchestration  
- **MCP (Model Context Protocol)** for tool integration  
- **Neo4j AuraDB** for graph storage  
- **OpenAI GPT-4o-mini** for LLM reasoning  
- **Linkup API** for web search

## 📂 Project Structure
- `mcp_server.py` — MCP server providing web search  
- `markint.py` — Agents and tasks for MarkInt  
- `main.py` — Entry point for running the multi-agent system  

## 💡 Usage

Simply run the system and type your query, such as:

- "Latest funding news for AI startups"  
- "What new AI models were launched this month?"  
- "Founders of top AI startups in Europe"

MarkInt will then:

- Search the web for updates.  
- Store results in the Neo4j knowledge graph.  
- Generate a context-aware report.

Type `quit` to exit.

## 📜 License

MIT License – free to use and modify.

Clone the repository:  
   ```bash
   git clone https://github.com/rileena-sanyal/MarkInt_Agent.git
   cd MarkInt_Agent
   
