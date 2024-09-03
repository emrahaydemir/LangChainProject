from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model='gpt-4', temperature=0.1) #model belirtme zorunlu degil, vermezsen default olani alir, temperature yaraticilik seviyesini ayarlar. arttikca alakasiz cevaplar artabilir. daha kesin cevaplar icin dusurulebilir

message=[
    SystemMessage(content='Translate the following from English to Spanish'), #sisteme verilen mesaj. sisteme uzmanlik alani belirtilebilir'
    HumanMessage(content='Hi')
]

if __name__ == '__main__':
    response = model.invoke(message)
    print(response.content)