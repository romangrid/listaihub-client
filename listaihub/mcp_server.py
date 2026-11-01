#!/usr/bin/env python3
"""
Model Context Protocol (MCP) server for ListAIHub directory.
Allows AI models and agents to search AI tools, query categories, and fetch OpenAPI specifications.
Reference: https://listaihub.com/en/developers
"""

import sys
import json
import logging
from .client import ListAIHubClient

logging.basicConfig(level=logging.INFO, stream=sys.stderr)

TOOLS = [
    {
        "name": "search_ai_tools",
        "description": "Searches ListAIHub curated catalog of artificial intelligence tools, models, and agents.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Keyword search query (e.g., 'seo', 'coding assistant', 'transcription')"
                },
                "category": {
                    "type": "string",
                    "description": "Optional category filter slug (e.g., 'developer-tools', 'marketing-seo')"
                }
            },
            "required": ["query"]
        }
    },
    {
        "name": "get_categories",
        "description": "Retrieves the structured catalog categories available on ListAIHub.",
        "inputSchema": {
            "type": "object",
            "properties": {}
        }
    },
    {
        "name": "get_openapi_spec",
        "description": "Fetches the full OpenAPI 3.0 specification from ListAIHub for machine-readable agent tool discovery.",
        "inputSchema": {
            "type": "object",
            "properties": {}
        }
    }
]

def handle_request(req):
    method = req.get("method")
    req_id = req.get("id")
    
    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {"listChanged": False}},
                "serverInfo": {"name": "listaihub-mcp", "version": "1.1.0"}
            }
        }
    elif method == "notifications/initialized":
        return None
    elif method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {"tools": TOOLS}
        }
    elif method == "tools/call":
        params = req.get("params", {})
        tool_name = params.get("name")
        args = params.get("arguments", {})
        
        client = ListAIHubClient()
        if tool_name == "search_ai_tools":
            q = args.get("query", "")
            cat = args.get("category")
            res = client.search_tools(q, category=cat)
        elif tool_name == "get_categories":
            res = client.get_categories()
        elif tool_name == "get_openapi_spec":
            res = client.get_openapi_spec()
        else:
            res = {"error": f"Unknown tool: {tool_name}"}
            
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "content": [
                    {
                        "type": "text",
                        "text": json.dumps(res, indent=2, ensure_ascii=False)
                    }
                ]
            }
        }
    else:
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {"code": -32601, "message": f"Method {method} not found"}
        }

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_request(req)
            if resp is not None:
                sys.stdout.write(json.dumps(resp) + "\n")
                sys.stdout.flush()
        except Exception as e:
            logging.error(f"Error handling request: {e}")

if __name__ == "__main__":
    main()
