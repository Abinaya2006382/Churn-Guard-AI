class CustomerDataServer:

    def get_customer_data(self):

        customer = {

            "Customer_ID": 101,
            "Age": 30,
            "Tenure": 5,
            "Monthly_Charges": 6000,
            "Contract": "Monthly"

        }

        return customer



server = CustomerDataServer()


data = server.get_customer_data()


print("==============================")
print("Customer Data MCP Server")
print("==============================")


for key,value in data.items():

    print(
        key,":",value
    )