from pydantic import BaseModel, Field, model_validator

class MasterModel(BaseModel):
    """this object acts as a routing engine to either clarify an ambiguous database request or output a final, valid PostgreSQL query."""

    reasoning_summary : str = Field(
        description= "step-by-step map the user's natural language request to the provided schema's tables, columns, and semantic comments.explicitly state any missing information or overlapping concepts you encounters before populating any other fields."
    )

    is_ambiguous: bool = Field(
        description= f"evaluate your own {reasoning_summary!r}. If you find multiple valid join paths, semantic collisions, or missing temporal bounds. you must set this boolean to True. If the request perfectly maps to the schema, you must set this to False."
    )

    clarifying_question : str | None = Field(
        default= None,
        description= "If is_ambiguous = True Then only Generate a concise, user-friendly phrase explaining this database path. Do not use SQL syntax in this field. else None"
    )

    system_memory : str | None = Field(
        default= None,
        description= "If is_ambiguous = True then only Provide the exact table and column reference in 'table.column' format. This must exactly match an entity in the provided DDL schema, make use of this in the next cycle of reasoning, at least two, but no more than four, mutually exclusive interpretations of the user's intent. else None"
    )

    final_response : str | None = Field(
        default= None,
        description= "If is_ambiguous = False then only this field must contain only the raw executable PostgreSQL. you are forbiden from write markdown code fences, explanations, or trailing semicolons for this field"
    )

    @model_validator(mode='after')
    def validator_func(self):
        return self