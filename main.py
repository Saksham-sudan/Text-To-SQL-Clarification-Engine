from utils.chat_module import call_func
from utils.clarification_module import MasterModel

data_model = MasterModel

def text_to_sql():
    last_id = None
    input_prompt = None
    print("type 'exit' to exit\n")
    while True:
        input_prompt = input("USER PROMPT: ")
        if input_prompt == 'exit':
            print("-------THANK YOU-------")
            break
        print("-----PROCESSING-----")
        print("\n")
        call_response = call_func(input_prompt, last_id)#type:ignore
        chat_response = data_model.model_validate_json(call_response.output_text)#type:ignore
        if chat_response.is_ambiguous == True:
            print(f"SYSTEM RESPONSE: {chat_response.clarifying_question}\n")
        else:
            print(f"QUERY> {chat_response.final_response}\n")
        last_id = call_response.id#type:ignore

text_to_sql()
