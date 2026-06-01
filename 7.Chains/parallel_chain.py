from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

# Load environment variables
load_dotenv()

# Models
model_groq = ChatGroq(
    model="llama-3.3-70b-versatile"
)

model_google = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

# Output Parser
parser = StrOutputParser()

# Prompt 1: Generate Notes
prompt1 = PromptTemplate(
    template="""
Generate short and simple notes from the following text:

{text}
""",
    input_variables=["text"]
)

# Prompt 2: Generate Quiz
prompt2 = PromptTemplate(
    template="""
Generate 5 short question-answer pairs from the following text:

{text}
""",
    input_variables=["text"]
)

# Prompt 3: Merge Results
prompt3 = PromptTemplate(
    template="""
Merge the provided notes and quiz into a single well-formatted study document.

Notes:
{notes}

Quiz:
{quiz}
""",
    input_variables=["notes", "quiz"]
)

# Parallel Execution
parallel_chain = RunnableParallel(
    notes=prompt1 | model_groq | parser,
    quiz=prompt2 | model_google | parser
)

# Merge Chain
merge_chain = prompt3 | model_groq | parser

# Final Chain
chain = parallel_chain | merge_chain

# Sample Text
text = """
Support vector machines (SVMs) are a set of supervised learning methods used
for classification, regression and outlier detection.

The advantages of support vector machines are:

1. Effective in high dimensional spaces.
2. Effective even when dimensions exceed samples.
3. Memory efficient because they use support vectors.
4. Versatile due to different kernel functions.

The disadvantages of support vector machines include:

1. Choosing the correct kernel and regularization is crucial.
2. They do not directly provide probability estimates.
3. Training can be computationally expensive.
"""

# Run Chain
result = chain.invoke({
    "text": text
})

print("\n" + "=" * 80)
print("FINAL OUTPUT")
print("=" * 80)
print(result)

# Display Chain Graph
print("\n" + "=" * 80)
print("CHAIN GRAPH")
print("=" * 80)

try:
    chain.get_graph().print_ascii()
except Exception as e:
    print(f"Graph visualization error: {e}")