from langchain_core.runnables import RunnableLambda
def make_upper(text):
    return text.upper()
upper_lambda = RunnableLambda(make_upper)
result = upper_lambda.invoke("hello world")
print(result)  # Output: "HELLO WORLD"

# ------------ runnable lambda in chain------------
from langchain_core.output_parsers import StrOutputParser

add_exclamation = RunnableLambda(lambda x: x + "!!!")

chain = add_exclamation | StrOutputParser()

print(chain.invoke("Hello"))  # Output: "Hello!!!"