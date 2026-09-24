from pathlib import Path

project_root = Path(__file__).resolve().parent.parent

master_schema = project_root/"schema"/"master.sql"


with open(master_schema, 'r', encoding="utf-8") as schema_file:
    schema_content = schema_file.read()

print(schema_content)
