from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatOpenAI(
    model="gpt-4", temperature=0.1
)  # model belirtme zorunlu degil, vermezsen default olani alir, temperature yaraticilik seviyesini ayarlar. arttikca alakasiz cevaplar artabilir. daha kesin cevaplar icin dusurulebilir


system_prompt = "Translate the following into {language}"
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_prompt), ("user", "{text}")]
)

parser = StrOutputParser()  # sadece response.content ciktisini verir. object dondurmez

chain = prompt_template | model | parser # inputu once prompt template e ver, sonucu modele ver, sonucu parser a gonder.

if __name__ == "__main__":
    print(chain.invoke({"language": "italian", "text": "Hello World!"}))
