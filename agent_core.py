import os
from groq import Groq

def run_brain():
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        print("خطأ: لم يتم العثور على مفتاح API!")
        return

    client = Groq(api_key=api_key)
    print("--- [Behemoth Core: Thinking Phase] ---")
    
    completion = client.chat.completions.create(
        messages=[{"role": "user", "content": "أنت جزء من نظام ذكاء اصطناعي، أعطني فكرة برمجية واحدة لتطوير نفسك."}],
        model="llama3-8b-8192",
    )
    print("الرد:")
    print(completion.choices[0].message.content)

if __name__ == "__main__":
    run_brain()
