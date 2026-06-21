from google.adk.agents.llm_agent import Agent


recommendation_agent = Agent(
    name="recommendation_agent",
    instruction="""
    Suggest customer retention strategies.
    Recommend offers and actions to prevent churn.
    """
)