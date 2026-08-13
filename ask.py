from dotenv import load_dotenv
import anthropic

load_dotenv()

client = anthropic.Anthropic()

question = input("ask away...")

while(question!="quit"):
    try:
        resp = client.messages.create(model="claude-haiku-4-5-20251001", max_tokens=1024, messages=[{"role": "user", "content": question}])
        content = resp.content
        text = content[0].text
        print(text)
    except anthropic.APIStatusError as e:
        print("Something went wrong\n Status Code:", e.status_code, "Error:",e.type)
    except Exception as e:
        print("Something went wrong: ", e)    
    question = input("ask away...")

