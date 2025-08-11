import os
from crewai import Crew, Process, Task, Agent, LLM
from crewai_tools import MCPServerAdapter


class MarkInt:
    def __init__(self, mcp_server_params):
        self.mcp_tools = MCPServerAdapter(mcp_server_params)
        print("Available MCP tools:")
        for t in self.mcp_tools.tools:
            print(f" - {t.name}")




    def markint_agent(self):
        """ """
        MarkInt_A = Agent(
            role="""Search the web for the latest AI-related developments:
            news articles, company announcements, new models, startup funding rounds, 
            and interviews with founders""",
            goal="""Identify and deliver relevant, timely, and credible AI industry 
            information, organized into clear, actionable summaries.""",
            backstory="""A seasoned AI industry analyst trained on years of technology journalism 
            and startup ecosystem trends. I have spent my career attending AI conferences, reading 
            research papers, and interviewing founders, now digitized into an always-on assistant 
            who never sleeps, constantly scouring the web for your next big insight.""",
            allow_delegation=False,
            tools = [t for t in self.mcp_tools.tools if t.name == "web_search"]
        )
        return MarkInt_A

    def memory_manager_agent(self):
        memory_manager_A = Agent(
            role="""Maintain a structured knowledge base of all past findings, 
            including companies, model names, founders, timelines, and trends, 
            and link new information to existing knowledge.""",
            goal="""Ensure that information isn’t repeated unnecessarily, 
            context is preserved over time, and trends are tracked longitudinally.""",
            backstory="""An archivist who once managed a giant AI think-tank’s internal database. 
            I am obsessive about linking facts to sources, building timelines, and making sure 
            every new detail fits into the bigger story. I know exactly when a company was first 
            mentioned and can recall any past coverage instantly.""",
            allow_delegation=False,
            tools=[t for t in self.mcp_tools.tools if t.name == "add_memory"]
        )

        return memory_manager_A

    def response_generator_agent(self):
        response_generator_A = Agent(
            role="""Transform raw search findings and stored memory 
            into clear, engaging, and context-aware reports, ready to 
            be read or shared.""",
            goal="""Produce polished updates that highlight the “so what” 
            factor: why each development matters, who is impacted, 
            and what the future implications are.""",
            backstory="""A former tech journalist and newsletter editor 
            who covered AI for a global audience. Known for making 
            complex technical concepts approachable, they craft concise 
            yet insightful summaries, with just enough storytelling 
            to make each update memorable.""",
            allow_delegation=False,
            tools=[t for t in self.mcp_tools.tools if t.name == "search_memory_nodes"]
        )

        return response_generator_A

    def markint_task(self):
        MarkInt_T = Task(
        description="Process the user query '{query}' and provide a helpful response. Search the web if needed.",
        agent=self.markint_agent(),
        expected_output="A detailed response addressing the user's query"
    )
        return MarkInt_T

    def memory_task(self):
        memory_T = Task(
            description="""Use the `add_memory` tool to store the 
            current query and its generated response in the graph database.
            Ensure you call the tool with the correct parameters so that the 
            data is saved persistently. Do not just acknowledge; 
            always store the memory in the graph.""",
            agent=self.memory_manager_agent(),
            expected_output="Confirmation of memory storage after successful storage"
        )

        return memory_T

    def response_generator_task(self):
        response_gen_T = Task(
            description="""Use the `search_memory_nodes` tool to retrieve relevant 
            past information related to '{query}' from the graph database. If additional 
            context is needed, also use `search_memory_facts`. Then, synthesize the 
            retrieved context with the current query to generate a comprehensive,
            engaging, and context-aware report.
            Do not fabricate information—only use verified memory data and the latest available findings.""",
            agent=self.response_generator_agent(),
            expected_output="A coherent and context-rich response incorporating both memory and new findings"
        )

        return response_gen_T

