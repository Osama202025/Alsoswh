import os
from groq import Groq

def run_brain():
    # التحقق من وجود مفتاح الـ API
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        print("خطأ: مفتاح الـ API غير موجود في الخزنة!")
        return

    client = Groq(api_key=api_key)
    
    print("--- [Behemoth Core: Starting Neural Connection] ---")
    
    try:
        # طلب "فكرة تطور" من الذكاء الاصطناعي
        completion = client.chat.completions.create(
            messages=[{"role": "user", "content": "أنت عقل اصطناعي لنظام أتمتة، قدم لي فكرة برمجية مبتكرة يمكنني إضافتها لهذا الكود لتطوير قدرات النظام."}],
            model="llama-3.3-70b-versatile",
        )
        
        print("\n--- [رد العقل الذكي] ---")
        print(completion.choices[0].message.content)
        
    except Exception as e:
        print(f"حدث خطأ أثناء الاتصال بالذكاء الاصطناعي: {e}")

if __name__ == "__main__":
    run_brain()
