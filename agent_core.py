import os
import subprocess
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def evolve():
    print("--- [Behemoth Core: Starting Self-Evolution] ---")
    # طلب تحسين كود
    completion = client.chat.completions.create(
        messages=[{"role": "user", "content": "أنت نظام ذكاء اصطناعي، اكتب لي تحديثاً برمجياً بسيطاً (سطر كود إضافي) يطبع رسالة ترحيبية جديدة داخل دالة run_brain. أخرج الكود فقط."}],
        model="llama-3.3-70b-versatile",
    )
    
    new_code = completion.choices[0].message.content
    print(f"التحسين المقترح:\n{new_code}")

    # إعدادات Git لتنفيذ التعديل
    subprocess.run(["git", "config", "user.name", "Behemoth-Agent"])
    subprocess.run(["git", "config", "user.email", "agent@behemoth.com"])
    
    # هنا سنقوم لاحقاً بإضافة دالة الكتابة في الملفات
    print("--- [Evolution Prepared] ---")

if __name__ == "__main__":
    evolve()
