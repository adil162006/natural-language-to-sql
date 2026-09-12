from pydantic import BaseModel

class SchemaUnderstanding(BaseModel):
    intent: str
    relevant_tables: list[str]
    is_ambiguous: bool
    clarification_question: str | None=None

class Clarification(BaseModel):
    is_ambiguous: bool
    clarification_question: str | None=None


class SQLGeneration(BaseModel):
    sql_query: str

class SQLReview(BaseModel):
    is_valid: bool
    feedback: str


class FinalResponse(BaseModel):
    response: str