import os
import subprocess
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def self_evolve():
    print("--- [Behemoth Core: Initiating Self-Rewrite] ---")
    
    # 1. طلب تحسين الكود من الذكاء الاصطناعي
    prompt = "أنت مبرمج خبير. أعد كتابة محتوى ملف agent_core.py الحالي بحيث تضيف رسالة ترحيب مطبوعة تتغير في كل مرة يعمل فيها الكود. أخرج الكود البرمجي الكامل فقط دون مقدمات."
    completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile",
    )
    
    new_code = completion.choices[0].message.content.replace("```python", "").replace("```", "")
    
    # 2. الكتابة الفعلية داخل الملف
    with open("agent_core.py", "w") as f:
        f.write(new_code)
    
    # 3. رفع التعديلات تلقائياً إلى المستودع
    subprocess.run(["git", "config", "user.name", "Behemoth-Agent"])
    subprocess.run(["git", "config", "user.email", "agent@behemoth.com"])
    subprocess.run(["git", "add", "agent_core.py"])
    subprocess.run(["git", "commit", "-m", "Auto-evolution: Self-updated code"])
    subprocess.run(["git", "push"])
    
    print("--- [Evolution Complete: System Self-Updated] ---")

if __name__ == "__main__":
    self_evolve()
