from pathlib import Path
import re

schema = Path("./db_reference.dbml").read_text()

schema_dict = {}

table_pattern = r"Table\s+(\w+)\s*\{(.*?)\}"

for table_name, table_content in re.findall(
    table_pattern,
    schema,
    re.DOTALL
):
    columns = {}

    for line in table_content.splitlines():
        line = line.strip()

        if not line or line.startswith("Note:"):
            continue

        match = re.match(
           r"(\w+)\s+([\w(),]+)(?:\s+\[(.*?)\])?",
            line
        )

        if match:
            column_name = match.group(1)
            column_type = match.group(2)
            constraints = match.group(3)

            columns[column_name] = {
                "type": column_type,
                "constraints": constraints
            }

    schema_dict[table_name] = columns

print(schema_dict)