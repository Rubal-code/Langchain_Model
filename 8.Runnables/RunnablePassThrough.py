# RunnablePassThrough is a simple Runnable that just passes its input through to its output. It can be used as a placeholder or for testing purposes.

from langchain_groq import ChatGroq
from langchain_core.runnables import RunnablePassthrough,RunnableSequence,RunnableParallel
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser   
from dotenv import load_dotenv

load_dotenv()

prompt1= PromptTemplate(
    template="Generate a tweet about {topic}",  
    input_variables=["topic"]
)
model=ChatGroq(
    model="llama-3.3-70b-versatile"
)
parser=StrOutputParser()
prompt2= PromptTemplate(
    template="Generate a Linkedin post about {topic}",
    input_variables=["topic"]
)
joke_gen_chain = RunnableSequence(prompt1, model, parser)


parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': RunnableSequence(prompt2, model, parser)
})
final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

print(final_chain.invoke({'topic':'cricket'}))