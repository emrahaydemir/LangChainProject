from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from fastapi import FastAPI
from langserve import add_routes

load_dotenv()

model = ChatOpenAI(
    model="gpt-4", temperature=0.1
)  # model belirtme zorunlu degil, vermezsen default olani alir, temperature yaraticilik seviyesini ayarlar. arttikca alakasiz cevaplar artabilir. daha kesin cevaplar icin dusurulebilir


system_prompt = "Translate the following into {language}"  # sisteme prompt yapisini belirttik ve language degiskenini atadik.
prompt_template = ChatPromptTemplate.from_messages(  # yukaridaki message yapisinin template hali, daha moduler bir yapi.
    [("system", system_prompt), ("user", "{text}")]
)

parser = StrOutputParser()  # sadece response.content ciktisini verir. object dondurmez

chain = (
    prompt_template | model | parser
)  # inputu once prompt template e ver, sonucu modele ver, sonucu parser a gonder.

app = FastAPI(
    title="Translator", version="1.0.0", description="Translation Chat Bot"
)  # fast api ile hizli bir api yapisi olusturduk

add_routes(app, chain, path="/chain")  # domain/chain route unda app ve chain calistir

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000) # app in hangi host ve portta calisacagini ayarla
