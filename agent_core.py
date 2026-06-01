import datetime
from groq import Groq
import os

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def think():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"--- [Behemoth Core: Thinking at {now}] ---")
    
    completion = client.chat.completions.create(
        messages=[{"role": "user", "content": "أعطني حكمة قصيرة جداً عن التطور."}],
        model="llama-3.3-70b-versatile",
    )
    print(f"الرد: {completion.choices[0].message.content}")

if __name__ == "__main__":
    think()
