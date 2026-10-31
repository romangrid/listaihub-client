import requests
from typing import Dict, List, Optional, Any

class ListAIHubClient:
    """
    Client interface for ListAIHub (https://listaihub.com/).
    Enables autonomous agents and developers to query AI tools directory,
    retrieve categories, and access developer token endpoints.
    """
    DEFAULT_BASE_URL = "https://listaihub.com"

    def __init__(self, api_key: Optional[str] = None, base_url: Optional[str] = None):
        self.api_key = api_key
        self.base_url = (base_url or self.DEFAULT_BASE_URL).rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "ListAIHub-Client-Python/1.0.0 (+https://listaihub.com/en/developers)",
            "Accept": "application/json",
        })
        if self.api_key:
            self.session.headers.update({"Authorization": f"Bearer {self.api_key}"})

    def search_tools(self, query: str = "", category: Optional[str] = None, limit: int = 20) -> List[Dict[str, Any]]:
        """Search AI tools in ListAIHub directory."""
        params = {"q": query, "limit": limit}
        if category:
            params["category"] = category
        try:
            resp = self.session.get(f"{self.base_url}/api/tools", params=params, timeout=10)
            if resp.status_code == 200:
                return resp.json().get("tools", [])
        except Exception:
            pass
        return []

    def get_categories(self) -> List[Dict[str, Any]]:
        """Retrieve catalog categories."""
        try:
            resp = self.session.get(f"{self.base_url}/api/categories", timeout=10)
            if resp.status_code == 200:
                return resp.json().get("categories", [])
        except Exception:
            pass
        return [
            {"name": "Marketing & SEO", "slug": "marketing-seo"},
            {"name": "Developer Tools & Code", "slug": "developer-tools"},
            {"name": "Content Creation & Writing", "slug": "content-creation"},
            {"name": "Computer Vision & Image Generation", "slug": "computer-vision"},
            {"name": "Autonomous Agents", "slug": "autonomous-agents"},
        ]

    def get_openapi_spec(self) -> Dict[str, Any]:
        """Fetch OpenAPI 3.0 specification for autonomous agent integration."""
        resp = self.session.get(f"{self.base_url}/agent/openapi.json", timeout=10)
        resp.raise_for_status()
        return resp.json()
