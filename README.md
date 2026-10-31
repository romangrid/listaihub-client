# ListAIHub Client (Python SDK & Agent CLI)

[![PyPI version](https://img.shields.io/badge/pypi-v1.0.0-blue.svg)](https://pypi.org/project/listaihub-client/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![API Documentation](https://img.shields.io/badge/API-OpenAPI_3.0-green.svg)](https://listaihub.com/agent/openapi.json)
[![Platform](https://img.shields.io/badge/Platform-ListAIHub.com-teal.svg)](https://listaihub.com/en/developers)

Official Python SDK and Agent Client for **[ListAIHub](https://listaihub.com/)** — the premier curated directory of artificial intelligence tools, autonomous agents, and productivity models.

Built specifically for autonomous AI agents, LLM tool-calling pipelines, and developers who need programmatic access to directory listings, category taxonomies, and developer token endpoints.

- 🌐 **Web Platform**: [https://listaihub.com/](https://listaihub.com/)
- 📘 **Developer Portal**: [https://listaihub.com/en/developers](https://listaihub.com/en/developers)
- 🤖 **Agent OpenAPI Spec**: [https://listaihub.com/agent/openapi.json](https://listaihub.com/agent/openapi.json)

---

## Features

- **Agent-Ready OpenAPI Integration**: Query categorized tools, pricing models, and ratings via standardized endpoints compatible with LangChain, LlamaIndex, and AutoGen.
- **Developer Token Authentication**: Seamless authentication against [ListAIHub Developers](https://listaihub.com/en/developers) using bearer tokens.
- **Multilingual Directory Discovery**: Full support for English, Spanish, Ukrainian, Arabic (RTL), and German localized taxonomy trees.
- **Automated Tool Submission**: Programmatically submit new AI tools and models directly to the verification queue.
- **Zero-Latency Search**: High-speed keyword and tag search across 1,000+ indexed AI applications.

---

## Installation

```bash
pip install listaihub-client
```

Or install directly from source:

```bash
git clone https://github.com/romangrid/listaihub-client.git
cd listaihub-client
pip install -e .
```

---

## Quickstart

### 1. Initialize Client

```python
from listaihub import ListAIHubClient

# Initialize client (public endpoints do not require an API key)
client = ListAIHubClient(api_key="your_developer_token_optional")

# Search AI tools in the directory
tools = client.search_tools(query="seo audit", category="marketing")
for tool in tools:
    print(f"Tool: {tool['title']} | URL: {tool['url']} | Pricing: {tool['pricing']}")
```

### 2. Fetch Category Taxonomy

```python
categories = client.get_categories()
print(f"Discovered {len(categories)} categories on ListAIHub:")
for cat in categories:
    print(f"- {cat['name']} ({cat['slug']}): {cat['tool_count']} tools")
```

### 3. Agent Tool Call Definition (OpenAPI)

For LangChain or custom autonomous agents, load the OpenAPI specification directly from [ListAIHub Agent Endpoint](https://listaihub.com/agent/openapi.json):

```python
import requests

spec = requests.get("https://listaihub.com/agent/openapi.json").json()
print("Available Agent Tools:", [path for path in spec.get("paths", {})])
```

---

## CLI Usage

```bash
# Search tools from terminal
listaihub search "image generation" --limit 5

# Inspect specific tool details
listaihub inspect --slug "midjourney"

# Validate developer token
listaihub auth verify --token "YOUR_LISTAIHUB_KEY"
```

---

## Documentation & Ecosystem

- **Main Directory**: [https://listaihub.com/](https://listaihub.com/)
- **Submit Your AI Tool**: [https://listaihub.com/submit](https://listaihub.com/submit)
- **Developer Portal**: [https://listaihub.com/en/developers](https://listaihub.com/en/developers)
- **OpenAPI Schema**: [https://listaihub.com/agent/openapi.json](https://listaihub.com/agent/openapi.json)

---

## License

This project is open-source under the [MIT License](LICENSE).
