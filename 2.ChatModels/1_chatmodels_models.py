from langchain_openai import ChatOpenAI
from dotenv import load_dotenv     # used to load environment variables from .env file
load_dotenv()   
# Create an instance of the ChatOpenAI class
chat_model=ChatOpenAI(model="gpt-3.5-turbo-instruct",temprature=0,max_completion_tokens=10)   # about temperature, see the end of this file for details

response = chat_model.invoke("What is the capital of France?")
print(response.content)

'''temperature is a parameter that controls the randomness of a language model's output. It affects how creative or deterministic the responses are.

• Lower values (0.0 - 0.3) → More deterministic and predictable.
• Higher values (0.7 - 1.5) → More random, creative, and diverse.

Use Case                                   Recommended Temperature
-------------------------------------------------------------------
Factual answers (math, code, facts)         0.0 - 0.3
Balanced response (general QA, explanations) 0.5 - 0.7
Creative writing, storytelling, jokes       0.9 - 1.2
Maximum randomness (wild ideas, brainstorming) 1.5+

'''

'''
max_completion_tokens is a parameter that limits the maximum number of tokens in the generated response. It helps control the length of the output and can prevent excessively long responses.
'''  




# paid api