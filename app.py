from agents.data_agent import data_agent
from agents.prediction_agent import prediction_agent
from agents.recommendation_agent import recommendation_agent
from mcp_server import server
from skills import (
    analyze_customer,
    predict_churn_risk,
    recommend_strategy
)


print("================================")
print("ChurnGuard AI Started")
print("================================")


customer = {
    "Age":30,
    "Tenure":5,
    "Contract Length":"Monthly"
}


print(data_agent.name)

print(
    analyze_customer(customer)
)


print(
    predict_churn_risk(0.81)
)


print(
    recommend_strategy("HIGH")
)


print("================================")
print("AI Retention System Ready")
customer_data = server.get_customer_data()

print("\nMCP Customer Data:")
print(customer_data)