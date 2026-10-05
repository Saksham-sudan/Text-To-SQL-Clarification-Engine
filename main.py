from utils.chat_module import chat_func

input_prompt = None

while input_prompt != "exit":
    input_prompt = input("Query> ")
    response = chat_func(input_prompt)