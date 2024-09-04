from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatOpenAI(
    model="gpt-4", temperature=0.1
)  # model belirtme zorunlu degil, vermezsen default olani alir, temperature yaraticilik seviyesini ayarlar. arttikca alakasiz cevaplar artabilir. daha kesin cevaplar icin dusurulebilir

# message=[
#     SystemMessage(content='Translate the following from English to Spanish'), #sisteme verilen mesaj. sisteme uzmanlik alani belirtilebilir'
#     HumanMessage(content='Hi')
# ]


system_prompt = "Translate the following into {language}"  # sisteme prompt yapisini belirttik ve language degiskenini atadik.
prompt_template = ChatPromptTemplate.from_messages(  # yukaridaki message yapisinin template hali, daha moduler bir yapi.
    [("system", system_prompt), ("user", "{text}")]
)

parser = StrOutputParser()  # sadece response.content ciktisini verir. object dondurmez

chain = (
    prompt_template | model | parser
)  # inputu once prompt template e ver, sonucu modele ver, sonucu parser a gonder.

if __name__ == "__main__":
    print(
        chain.invoke({"language": "italian", "text": "Hi!"})
    )  # sisteme verilen promptaki language degiskenine italian degerini gonderdik. user prompt ise text degiskenine gonderildi
