"""CLI for mcp-dynamic-resource-synthesizer."""
import sys
import argparse
from .synthesizer import MCPDynamicResourceSynthesizer


def main():
    parser = argparse.ArgumentParser(description="MCP Dynamic Resource Synthesizer CLI")
    parser.add_argument("--demo", action="store_true", help="Run dynamic resource synthesizer demo")
    args = parser.parse_args()

    if args.demo:
        synth = MCPDynamicResourceSynthesizer()
        synth.register_resource("live://swarm/status", "Swarm Status", data={"active_agents": 8, "status": "nominal"})
        synth.register_resource("memo://scratchpad/current", "Working Scratchpad", mime_type="text/plain", data="Goal: Refactor AST")

        print("[+] Registered Virtual MCP Resources:")
        for r in synth.list_resources():
            print(f"    - {r['uri']} ({r['name']}) [{r['mimeType']}]")

        content = synth.read_resource("live://swarm/status")
        print(f"[+] Read Resource Content:\n    {content}")
    else:
        parser.print_help()
    sys.exit(0)


if __name__ == "__main__":
    main()
