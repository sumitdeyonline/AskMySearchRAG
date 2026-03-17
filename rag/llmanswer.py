from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

class RAG:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.model = ChatOpenAI(api_key=self.api_key,model="gpt-4o-mini")

    def generate(self, query, prompt):

        response = self.model.invoke(prompt)
        return response.content
        