from google.adk.agents.llm_agent import Agent


prediction_agent = Agent(
    name="prediction_agent",
    instruction="""
    You predict customer churn risk.
    Use machine learning results.
    Provide churn probability and risk level.
    """
)