"""Unit tests for mcp-dynamic-resource-synthesizer."""
import unittest
from mcp_dynamic_resource_synthesizer.synthesizer import MCPDynamicResourceSynthesizer


class TestMCPDynamicResourceSynthesizer(unittest.TestCase):
    def test_register_and_read(self):
        synth = MCPDynamicResourceSynthesizer()
        synth.register_resource("test://a", "Test A", data={"k": "v"})
        lst = synth.list_resources()
        self.assertEqual(len(lst), 1)
        self.assertEqual(lst[0]["uri"], "test://a")

        data = synth.read_resource("test://a")
        self.assertIsNotNone(data)
        self.assertIn('"k": "v"', data["text"])

    def test_update_resource(self):
        synth = MCPDynamicResourceSynthesizer()
        synth.register_resource("test://b", "Test B", data="init")
        synth.update_resource("test://b", "updated")
        data = synth.read_resource("test://b")
        self.assertEqual(data["text"], "updated")
