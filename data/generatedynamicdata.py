from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
load_dotenv()
llm = ChatOpenAI()

topics = ["AI", "Machine Learning", "Deep Learning", "NLP","Supervised Learning","Neural Networks","Transformers","Computer Vision","AI Ethics","AI in Healthcare","AI in Finance"]

for topic in topics:
    text = llm.invoke(f"Write a 200 word explanation about {topic}")
    
    with open(f"{topic}.txt","w") as f:
        f.write(text.content)