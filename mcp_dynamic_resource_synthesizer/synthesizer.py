"""Core MCP Dynamic Resource Synthesizer implementation."""
import json
from typing import Dict, List, Optional, Any, Callable


class VirtualResource:
    def __init__(self, uri: str, name: str, mime_type: str = "application/json", data: Any = None):
        self.uri = uri
        self.name = name
        self.mime_type = mime_type
        self.data = data


class MCPDynamicResourceSynthesizer:
    def __init__(self):
        self.resources: Dict[str, VirtualResource] = {}

    def register_resource(self, uri: str, name: str, mime_type: str = "application/json", data: Any = None) -> VirtualResource:
        res = VirtualResource(uri, name, mime_type, data)
        self.resources[uri] = res
        return res

    def list_resources(self) -> List[Dict[str, str]]:
        return [
            {"uri": r.uri, "name": r.name, "mimeType": r.mime_type}
            for r in self.resources.values()
        ]

    def read_resource(self, uri: str) -> Optional[Dict[str, Any]]:
        res = self.resources.get(uri)
        if not res:
            return None
        text_content = json.dumps(res.data) if isinstance(res.data, (dict, list)) else str(res.data)
        return {
            "uri": res.uri,
            "mimeType": res.mime_type,
            "text": text_content
        }

    def update_resource(self, uri: str, new_data: Any) -> bool:
        if uri in self.resources:
            self.resources[uri].data = new_data
            return True
        return False
