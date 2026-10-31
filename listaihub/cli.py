import argparse
import sys
from .client import ListAIHubClient

def main():
    parser = argparse.ArgumentParser(description="ListAIHub CLI - AI Tools Discovery")
    subparsers = parser.add_subparsers(dest="command")

    search_parser = subparsers.add_parser("search", help="Search AI tools")
    search_parser.add_argument("query", help="Keyword or tag to search")
    search_parser.add_argument("--category", "-c", help="Category filter")
    search_parser.add_argument("--limit", "-l", type=int, default=10, help="Max results")

    subparsers.add_parser("categories", help="List all AI tool categories")

    args = parser.parse_args()
    client = ListAIHubClient()

    if args.command == "search":
        print(f"Searching ListAIHub for: '{args.query}'...")
        results = client.search_tools(query=args.query, category=args.category, limit=args.limit)
        if not results:
            print("No tools found matching query. Visit https://listaihub.com/ to browse full catalog.")
        else:
            for item in results:
                print(f"- {item.get('title')} ({item.get('url')}): {item.get('pricing', 'Free')}")
    elif args.command == "categories":
        cats = client.get_categories()
        print("Available categories on ListAIHub (https://listaihub.com/):")
        for c in cats:
            print(f"- {c.get('name')} [{c.get('slug')}]")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
