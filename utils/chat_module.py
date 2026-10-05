from google import genai
from utils.loader_module import load_schema
from utils.data_model import MasterModel

client = genai.Client()
schema = load_schema("master.sql")
data_model = MasterModel


persona_block = "You are an expert PostgreSQL Database Administrator. Your job is to translate human questions into SQL, or ask clarifying questions if the human is being vague. Never guess. If you are unsure, you must ask for clarification."
rules_block = "Write strictly in PostgreSQL. You are in READ-ONLY mode. You are strictly forbidden from writing INSERT, UPDATE, DELETE, or DROP commands. Do not wrap your SQL in markdown formatting (like ```sql). Output only the raw query."
schema_block = f"Here is the database schema you must use:\n--- BEGIN SCHEMA ---\n{schema}\n--- END SCHEMA ---"
clarification_block ="If the user asks for 'status', check if multiple tables have a status column. If they do, ask the user which one they mean. If the user asks a time-based question (like 'last week') but doesn't specify if they mean 'Order Date' or 'Shipped Date', you must ask them to clarify."
system_prompt = f"{persona_block}\n\n{rules_block}\n\n{schema_block}\n\n{clarification_block}"

def chat_func(input_prompt: str):
    last_id: str | None = None
    while True:
        response = client.interactions.create(
            model = 'gemini-3.1-flash-lite',
            system_instruction= system_prompt,
            input = input_prompt,
            previous_interaction_id = last_id,
            response_format={
                "mime_type": "application/json",
                "schema": data_model.model_json_schema()
            },
            generation_config={
            "temperature": 0.0
            },
        )

        last_id = response.id #type:ignore
        call_response = data_model.model_validate_json(response.output_text) # type:ignore
        return call_response