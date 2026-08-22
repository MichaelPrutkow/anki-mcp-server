from typing import Annotated, Any

from mcp.server import MCPServer
from pydantic import BaseModel, Field

import anki_mcp.constants as myConsts
from anki_mcp.anki import invoke

mcp = MCPServer("anki")


@mcp.tool(title="List Decks", annotations=myConsts.READ_ONLY)
def list_decks() -> dict[str, int]:
    """
    Gets the complete list of deck names and their IDs for the current user.

    Returns:
        List of all Decknames
    """
    return invoke("deckNamesAndIds")


@mcp.tool(title="Model/Field Names (internal)", annotations=myConsts.READ_ONLY)
def describe_note_type(name: str | None = None) -> list[str]:
    """
    Gets the complete list of model names for the current user, if the name is None.
    Otherwise gets the complete list of field names for the provided model name.

    Args:
        name: modelName

    Returns:
        List of model names for the current user or list of field names for the provided model name.
    """
    if name is None:
        return invoke("modelNames")
    return invoke("modelFieldNames", modelName=name)


@mcp.tool(title="Create a new Deck", annotations=myConsts.ADDS_IF_MISSING)
def create_deck(
    name: Annotated[str, Field(description="Deck, '::' creates Subdecks")],
) -> int:
    """
    Create a new empty deck. Will not overwrite a deck that exists with the same name.

    Args:
        Deck Name
    Returns:
        DeckID of the new deck
    """
    return invoke("createDeck", deck=name)


class SearchResult(BaseModel):
    query: str
    total_found: int
    note_ids: list[int]
    notes: list[dict[str, Any]] = []


@mcp.tool(title="Search for Notes", annotations=myConsts.READ_ONLY)
def search_notes(
    query: Annotated[str, Field(description=myConsts.ANKI_SEARCH_RULES)],
    limit: Annotated[int, Field(ge=1, le=100)] = 25,
    with_fields: bool = False,
) -> SearchResult:
    """
    Finds notes in the Anki collection.

    - total_found is the number of matches for the whole query
    - note_ids is capped at limit.

    A total_found of 0 usually means the query was malformed
    rather than that the collection is empty.

    Set with_field=True to also get field contents, tags and note type. This is
    considerably more expensive, so leave it off unless the content is needed
    """
    ids: list[int] = invoke("findNotes", query=query)
    selected = ids[:limit]

    notes: list[dict[str, Any]] = []
    if with_fields and selected:
        notes = invoke("notesInfo", notes=selected)

    return SearchResult(
        query=query, total_found=len(ids), note_ids=selected, notes=notes
    )


if __name__ == "__main__":
    # mcp.run(transport="stdio")
    res = create_deck("Test::TestSub")
    print(f"deck creatio successfull, new Deck has ID: {res}")
