from mcp.server import MCPServer
from mcp.types import ToolAnnotations

from anki_mcp.anki import invoke

mcp = MCPServer("anki")


@mcp.tool(annotations=ToolAnnotations(read_only_hint=True, open_world_hint=True))
def list_decks() -> list[str]:
    """All Decks of opened Anki-Collection"""
    return invoke("deckNames")


if __name__ == "__main__":
    mcp.run()
