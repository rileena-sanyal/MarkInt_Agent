from dotenv import load_dotenv
from markint import MarkInt
import opik
from crewai import LLM, Crew
from opik.integrations.crewai import track_crewai

load_dotenv()
llm = LLM(model="openai/gpt-4o-mini")
opik.configure(use_local=False)
track_crewai(project_name="MarkInt")
mcp_server_params = [
    {
        "url": "http://localhost:8000/sse",
        "transport": "sse"
    },
    {
    "url": "http://localhost:8080/sse",
    "transport": "sse"
    }
  ]

markInt = MarkInt(mcp_server_params)

crew = Crew(
        agents=[markInt.markint_agent(), markInt.memory_manager_agent(), markInt.response_generator_agent()],
        tasks=[markInt.markint_task(), markInt.memory_task(), markInt.response_generator_task()],
        verbose=False
    )

print("Please type 'quit' if you want to quit")
while True:
    query = input("User: ")
    if query.strip() == "quit":
        break
    result = crew.kickoff(inputs={"query": query})
    print("Narrator: ", result)