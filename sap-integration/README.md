# SAP Integration

Utilities for connecting to SAP systems using Cloud Connector and BTP Destination Service.

## Environment Variables

```
SAP_DEST_TOKEN_URL      # OAuth2 token endpoint for the destination service
SAP_DEST_BASE_URL       # Base URL of the destination service instance
SAP_DEST_CLIENT_ID      # OAuth client id
SAP_DEST_CLIENT_SECRET  # OAuth client secret
SAP_DEST_NAME           # Name of the destination containing SAP system details
```

## Example Usage

```python
from sap_integration.sap_tool import sap_sales_order_tool

# LangChain agent can call the tool
result = sap_sales_order_tool.run("5000000001")
print(result)
```

The tool obtains a token via OAuth2, retrieves the destination configuration
and then calls `API_SALES_ORDER_SRV` to fetch a sales order. If the
destination is of type **OnPremise**, proxy settings returned from the
configuration are used for the request to route via the SAP Cloud Connector.
