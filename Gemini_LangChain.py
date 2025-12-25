from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

from dotenv import load_dotenv


# Load API key from .env
load_dotenv()

#first Create the model

llm= ChatGoogleGenerativeAI(

    model ="gemini-2.5-flash-lite"
)


#  second step is to create the prompt template

prompt = PromptTemplate.from_template(
  "Explain {topic} in simple terms."

)




# third step is to Create a chain

# chain= LLMChain(
#
#     llm= llm,
#     prompt= prompt
#
# )
chain = prompt | llm


# fourth step is to run the chain

response = chain.invoke({"topic": "LangChain chains"})
print(response.content)




