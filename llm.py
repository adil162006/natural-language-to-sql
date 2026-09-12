from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

# 1. Schema Understanding Node
schema_understanding_llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.0
)

# 2. Clarification Node (Can be combined with Schema node in your graph)
clarification_llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.1
)

# 3. SQL Generator Node
sql_generator_llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.0
)

# 4. SQL Reviewer Node
sql_reviewer_llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.0
)

# 5. Response Generator Node
response_generator_llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.3
)