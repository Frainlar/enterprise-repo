import os
from dataclasses import dataclass
from typing import Optional, Dict

import requests
from langchain.tools import Tool


def _get_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


@dataclass
class SAPDestinationConfig:
    """Configuration for accessing SAP BTP Destination Service."""

    token_url: str
    destination_url: str
    client_id: str
    client_secret: str
    destination_name: str

    @classmethod
    def from_env(cls) -> "SAPDestinationConfig":
        return cls(
            token_url=_get_env("SAP_DEST_TOKEN_URL"),
            destination_url=_get_env("SAP_DEST_BASE_URL"),
            client_id=_get_env("SAP_DEST_CLIENT_ID"),
            client_secret=_get_env("SAP_DEST_CLIENT_SECRET"),
            destination_name=_get_env("SAP_DEST_NAME"),
        )


class SAPDestinationClient:
    """Helper for calling SAP OData APIs via BTP Destination Service."""

    def __init__(self, config: Optional[SAPDestinationConfig] = None) -> None:
        self.config = config or SAPDestinationConfig.from_env()

    def _get_oauth_token(self) -> str:
        resp = requests.post(
            self.config.token_url,
            data={"grant_type": "client_credentials"},
            auth=(self.config.client_id, self.config.client_secret),
        )
        resp.raise_for_status()
        return resp.json()["access_token"]

    def _get_destination(self) -> Dict:
        token = self._get_oauth_token()
        headers = {"Authorization": f"Bearer {token}"}
        url = f"{self.config.destination_url}/destination-configuration/v1/destinations/{self.config.destination_name}"
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()
        return resp.json()

    def _prepare_request(self, path: str) -> Dict:
        dest = self._get_destination()
        cfg = dest["destinationConfiguration"]
        auth_token = dest["authTokens"][0]["value"]
        base_url = cfg["URL"].rstrip("/")
        full_url = f"{base_url}/{path.lstrip('/') }"
        headers = {
            "Authorization": f"Bearer {auth_token}",
            "Accept": "application/json",
        }
        proxies = None
        if dest.get("proxyType") == "OnPremise":
            host = cfg.get("ProxyHost")
            port = cfg.get("ProxyPort")
            if host and port:
                proxy_url = f"http://{host}:{port}"
                proxies = {"http": proxy_url, "https": proxy_url}
        return {"url": full_url, "headers": headers, "proxies": proxies}

    def fetch_sales_order(self, order_id: str) -> Dict:
        """Fetch details for an SAP sales order via API_SALES_ORDER_SRV."""
        req = self._prepare_request(f"API_SALES_ORDER_SRV/A_SalesOrder('{order_id}')")
        resp = requests.get(req["url"], headers=req["headers"], proxies=req["proxies"])
        resp.raise_for_status()
        return resp.json()


def get_sales_order(order_id: str) -> Dict:
    client = SAPDestinationClient()
    return client.fetch_sales_order(order_id)


sap_sales_order_tool = Tool(
    name="sap_sales_order",
    description="Fetch SAP Sales Order details using OData.",
    func=get_sales_order,
)
