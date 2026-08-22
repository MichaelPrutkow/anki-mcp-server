from mcp.types import ToolAnnotations

READ_ONLY = ToolAnnotations(
    read_only_hint=True,
    destructive_hint=False,
    idempotent_hint=True,
    open_world_hint=False,
)

# creates new, calling twice does not overwrites, but creates multiples
ADDS_NEW = ToolAnnotations(
    read_only_hint=False,
    destructive_hint=False,
    idempotent_hint=False,
    open_world_hint=False,
)

# creates only if missing, second call changes nothing
ADDS_IF_MISSING = ToolAnnotations(
    read_only_hint=False,
    destructive_hint=False,
    idempotent_hint=True,
    open_world_hint=False,
)

# Overwrites or deletes existing, calling multiple times doesn't affect state
OVERWRITES = ToolAnnotations(
    read_only_hint=False,
    destructive_hint=True,
    idempotent_hint=True,
    open_world_hint=False,
)

ANKI_SEARCH_RULES = """ MUST follow Anki's strict search syntax:
1. BASIC LOGIC:
- Space = AND (e.g., 'dog cat' -> contains both)
- 'or' = OR (e.g., 'dog or cat')
- '-' = NOT (e.g., '-cat' -> without cat)
- '(...)' = Grouping (e.g., 'dog (cat or mouse)')
- '\"...\"' = Exact phrase/spaces (e.g., '\"a dog\"')
- '*' = Wildcard (e.g., 'd*g' -> dog, dug, dg...)

2. FIELDS & METADATA:
- 'deck:Name' or 'deck:Name::Subdeck' (e.g, 'deck:\"French Words\"')
- 'tag:Name' (e.g, 'tag:animal', 'tag:none' for no tags)
- 'note:Name' (Filter by Note Type, e.g., 'note:Basic')
- 'FieldName:Text' (e.g., 'Front:dog') CRITICAL: Field searches require EXACT matches! Use wildcards for partial matches (e.g., `Front:*dog*`).
- `FieldName:` (Empty field) / `FieldName:_*` (Non-empty field)
            
3. CARD STATES:
- `is:new` (New cards)
- `is:due` (Waiting to be studied)
- `is:learn` (In learning)
- `is:review` (Reviews/lapsed)
- `is:suspended` (Suspended cards)

4. General
- 'prop:lapses>3', 'prop:ivl>=21' (numeric comparisons)
- 'added:7', 'edited:7' (within the last N days)
- '\' escapes a literal '*', '_', '"' or ':'
- Tags are hierarchical: 'tag:mcp::batch::*' matches all subtags
"""
