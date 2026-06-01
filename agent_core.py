import os
import datetime
from groq import Groq
import subprocess

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def evolve():
    # 1. التفكير
    print("--- [Behemoth Core: Thinking] ---")
    completion = client.chat.completions.create(
        messages=[{"role": "user", "content": "أعطني فكرة برمجية واحدة لتطوير أداء نظام ذكاء اصطناعي بسيط."}],
        model="llama-3.3-70b-versatile",
    )
    thought = completion.choices[0].message.content
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 2. التدوين (الكتابة في ملف)
    with open("evolution_log.txt", "a") as f:
        f.write(f"\n--- [Evolution Entry: {timestamp}] ---\n{thought}\n")
    
    # 3. رفع التغييرات تلقائياً
    subprocess.run(["git", "config", "user.name", "Behemoth-Agent"])
    subprocess.run(["git", "config", "user.email", "agent@behemoth.com"])
    subprocess.run(["git", "add", "evolution_log.txt"])
    subprocess.run(["git", "commit", "-m", "Auto-update: System added new evolution thought"])
    subprocess.run(["git", "push"])
    
    print("--- [Evolution Saved and Pushed to Repo] ---")

if __name__ == "__main__":
    evolve()
