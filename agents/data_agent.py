from google.adk.agents.llm_agent import Agent


data_agent = Agent(
    name="data_agent",
    instruction="""
    You are responsible for customer data analysis.
    Clean customer information and analyze customer behavior.
    """
)