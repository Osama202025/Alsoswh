import os
from groq import Groq

# العقل يتصل الآن بـ Groq باستخدام المفتاح المخزن في الخزنة
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def think():
    print("--- [Behemoth Core: Thinking Phase] ---")
    try:
        completion = client.chat.completions.create(
            messages=[{"role": "user", "content": "أنت عقل اصطناعي، أعطني فكرة برمجية واحدة لتطوير نفسك."}],
            model="llama3-8b-8192",
        )
        print("الرد:")
        print(completion.choices[0].message.content)
    except Exception as e:
        print(f"حدث خطأ أثناء التفكير: {e}")

if __name__ == "__main__":
    think()

