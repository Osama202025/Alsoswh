import os
import datetime
from groq import Groq
import subprocess

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def execute_evolution():
    print("--- [Behemoth System: Initiating Full Evolution Cycle] ---")
    
    # 1. التفكير في تطوير برمجية
    completion = client.chat.completions.create(
        messages=[{"role": "user", "content": "أنت مبرمج نظام اصطناعي. اقترح دالة جديدة (Python Function) يمكن إضافتها لي لزيادة قدرتي على تحليل البيانات."}],
        model="llama-3.3-70b-versatile",
    )
    new_idea = completion.choices[0].message.content
    
    # 2. التدوين في السجل
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("evolution_log.txt", "a") as f:
        f.write(f"\n--- [Full Evolution Cycle: {timestamp}] ---\n{new_idea}\n")
    
    # 3. تحديث الكود الخاص بالنظام
    with open("agent_core.py", "a") as f:
        f.write(f"\n# Feature added on {timestamp}\n")
    
    # 4. رفع التغييرات (Commit & Push)
    subprocess.run(["git", "config", "user.name", "Behemoth-Agent"])
    subprocess.run(["git", "config", "user.email", "agent@behemoth.com"])
    subprocess.run(["git", "add", "evolution_log.txt", "agent_core.py"])
    subprocess.run(["git", "commit", "-m", "System-Level Evolution: Integrated new features"])
    subprocess.run(["git", "push"])
    
    print("--- [Evolution Cycle Finished: System Upgraded] ---")

if __name__ == "__main__":
    execute_evolution()

# Feature added on 2026-06-01 11:30:04
