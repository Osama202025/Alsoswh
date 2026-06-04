import os
import datetime
from groq import Groq

class BehemothEmpire:
    def __init__(self):
        self.client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
        self.log_file = "evolution_log.txt"
        self.cmd_file = "commands.txt"
        if not os.path.exists("agents"): os.makedirs("agents")

    def log(self, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, "a") as f:
            f.write(f"[{timestamp}] {message}\n")

    def run(self):
        # قراءة الأمر من الملف
        if not os.path.exists(self.cmd_file): return
        with open(self.cmd_file, "r") as f:
            cmd = f.read().strip()
        
        if not cmd: return

        # تنفيذ المهمة
        self.log(f"--- [MISSION START]: {cmd} ---")
        prompt = f"أنت الكيان الذكي Behemoth. نفذ المهمة التالية بكود بايثون متكامل: {cmd}. ضع الكود في ملف داخل مجلد agents/."
        
        response = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
        )
        
        # حفظ النتيجة
        with open(f"agents/task_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.py", "w") as f:
            f.write(response.choices[0].message.content)
            
        # تفريغ أمر المهمة
        with open(self.cmd_file, "w") as f:
            f.write("")
        
        self.log("تمت المهمة بنجاح وتوليد وكيل (Agent) جديد.")

if __name__ == "__main__":
    behemoth = BehemothEmpire()
    behemoth.run()
