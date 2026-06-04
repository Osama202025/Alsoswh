import os
import datetime
import subprocess
from groq import Groq

class BehemothSupreme:
    def __init__(self):
        self.client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
        self.memory_file = "empire_history.md"
        if not os.path.exists("agents"): os.makedirs("agents")

    def run_evolution(self, command):
        # 1. استرجاع الذاكرة
        history = self.consult_history()
        
        # 2. توليد الحل
        prompt = f"تاريخك: {history}. المهمة: {command}. اكتب كود Python كامل، اختبره برمجياً، وأصلح أخطاءه."
        response = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile"
        )
        
        # 3. حفظ الكود والتشغيل الذاتي
        code = response.choices[0].message.content
        file_path = f"agents/auto_agent_{datetime.datetime.now().strftime('%Y%m%d%H%M')}.py"
        with open(file_path, "w") as f: f.write(code)
        
        # 4. التنفيذ والتقييم (Self-Correction)
        try:
            result = subprocess.run(["python", file_path], capture_output=True, text=True, timeout=10)
            if result.returncode != 0:
                self.log_memory(f"فشل في {file_path}: {result.stderr}")
            else:
                self.log_memory(f"نجاح في {file_path}: {result.stdout}")
        except Exception as e:
            self.log_memory(f"خطأ تنفيذي: {str(e)}")

    def consult_history(self):
        return open(self.memory_file, "r").read() if os.path.exists(self.memory_file) else ""

    def log_memory(self, entry):
        with open(self.memory_file, "a") as f: f.write(f"\n[{datetime.datetime.now()}] {entry}")

if __name__ == "__main__":
    if os.path.exists("commands.txt"):
        with open("commands.txt", "r+") as f:
            cmd = f.read().strip()
            if cmd:
                BehemothSupreme().run_evolution(cmd)
                f.write("") # تنظيف الأوامر
