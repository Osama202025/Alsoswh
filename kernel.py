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
        # 1. قراءة الأمر
        if not os.path.exists(self.cmd_file): return
        with open(self.cmd_file, "r") as f:
            cmd = f.read().strip()
        
        if not cmd: return

        # 2. تنفيذ المهمة
        self.log(f"--- [MISSION START]: {cmd} ---")
        prompt = f"أنت الكيان الذكي Behemoth. نفذ المهمة التالية بكود بايثون متكامل وقوي: {cmd}. ضع الكود في ملف داخل مجلد agents/."
        
        response = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
        )
        
        # 3. حفظ النتيجة (توليد وكيل جديد)
        file_name = f"agents/agent_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.py"
        with open(file_name, "w") as f:
            f.write(response.choices[0].message.content)
            
        # 4. تفريغ أمر المهمة (تطهير العقل)
        with open(self.cmd_file, "w") as f:
            f.write("")
        
        self.log(f"تمت المهمة بنجاح، تم توليد الوكيل: {file_name}")

if __name__ == "__main__":
    behemoth = BehemothEmpire()
    behemoth.run()
