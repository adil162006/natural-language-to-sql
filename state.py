from typing import TypedDict,Annotated
from langgraph.graph.message import add_messages
from schema import schema_dict

class State(TypedDict):
    user_input: str
    schema: dict
    relevant_tables: list[str]
    schema_context: dict
    sql_query: str
    review: dict
    final_response: str
    messages: Annotated[list, add_messages]
