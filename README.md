# anki-mcp

An MCP server that lets Claude create and maintain Anki flashcards.

## Requirements

- Anki with the AnkiConnect add-on (code `2055492159`), restart Anki after installing
- Anki must be running while you use this server

## Install

### Claude Desktop, one click
Download `anki-mcp.mcpb` from the latest release and double-click it.

### Terminal
Add to claude_desktop_config.json:
{"mcpServers": {"anki": {"command": "uvx", "args": ["anki-mcp"]}}}

## Tools
<TODO>

## Prompt
<TODO>

## Design decisions
<TODO>

## Safety
This server writes to your real collection. undo_batch removes a batch, but make a backup first.

## License
MIT