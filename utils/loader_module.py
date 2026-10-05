from pathlib import Path

def load_schema(file_name: str):
    project_root = Path(__file__).resolve().parent.parent
    schema_file = project_root/"schema"/file_name
    with open(schema_file, 'r', encoding="utf-8") as f:
        if f:
            schema_content = f.read()
            return schema_content.strip()