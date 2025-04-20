from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0,
)

if __name__ == "__main__":
    res = llm.invoke("Que es la musica?")
    print(res.content)
