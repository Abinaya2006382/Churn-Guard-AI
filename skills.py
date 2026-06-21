def analyze_customer(customer):

    return f"""
    Customer Analysis:

    Age: {customer['Age']}
    Tenure: {customer['Tenure']}
    Contract: {customer['Contract Length']}

    Analysis completed.
    """


def predict_churn_risk(probability):

    if probability > 0.7:
        risk = "HIGH"
    elif probability > 0.4:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    return f"""
    Churn Probability: {probability*100:.2f}%

    Risk Level: {risk}
    """


def recommend_strategy(risk):

    if risk == "HIGH":
        return """
        Recommended Actions:
        - Give discount offer
        - Provide loyalty benefits
        - Contact customer support
        """

    else:
        return """
        Customer is stable.
        Continue regular engagement.
        """