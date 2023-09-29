from langchain.memory import ConversationBufferWindowMemory
import os
from langchain.llms import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


api_key = os.environ.get('OPEN_AI_KEY')

chain = LLMChain(
    llm=OpenAI(temperature=0), 
    verbose=True,
    prompt=PromptTemplate.from_template("{query}")
)

while True:
    query = input("Enter Your Query:")
    print(chain(query))