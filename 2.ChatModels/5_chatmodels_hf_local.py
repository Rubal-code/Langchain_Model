from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace
import os

os.environ['HF_HOME']='D:/huggingface_cache'  # Set the Hugging Face cache directory to a local path

llm=HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    model_kwargs={}, # keep empty if you don't want to pass any additional arguments to the model
    pipeline_kwargs={
        "temperature": 0.7,
        "max_new_tokens": 100
    }
)
model=ChatHuggingFace(llm=llm)
result=model.invoke("What is the capital of France?")
print(result.content)


# local can be also used for paid api as well, but here we are using it for free api