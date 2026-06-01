import os
from groq import Groq

# إعداد العقل ليقرأ المفتاح من الخزنة
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def think():
    print("--- [Behemoth Core: Thinking Phase] ---")
    completion = client.chat.completions.create(
        messages=[{"role": "user", "content": "أنت عقل اصطناعي، أعطني فكرة برمجية لتطوير نفسك."}],
        model="llama3-8b-8192",
    )
    print("الرد:")
    print(completion.choices[0].message.content)

if __name__ == "__main__":
    think()
