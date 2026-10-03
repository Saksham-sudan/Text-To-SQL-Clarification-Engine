from pathlib import Path

class SchemaError(Exception):
    """Base exception classs for schema related errors"""
    pass

class SchemaNotFoundError(SchemaError):
    def __init__(self, path: Path):
        self.path = path
        super().__init__(f"Schema not found at:{path}")

class SchemaFileEmptyError(SchemaError):
    def __init__(self) -> None:
        super().__init__("Schema File empty")

def load_schema(file_name: str):
    project_root = Path(__file__).resolve().parent.parent
    schema_file = project_root/"schema"/file_name
    if schema_file.exists():
        try:
            with open(schema_file, 'r', encoding="utf-8") as f:
                if f:
                    schema_content = f.read()
                    return schema_content.strip()
                else:
                    raise SchemaFileEmptyError
        except PermissionError as e:
            print(e)
    else:
        raise SchemaNotFoundError(schema_file)