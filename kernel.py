import os
import datetime
from groq import Groq

class BehemothEmpire:
    def __init__(self):
        self.client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
        # تحديد المسار المطلق للملفات
        self.base_path = os.getcwd()
        self.log_file = os.path.join(self.base_path, "evolution_log.txt")
        self.cmd_file = os.path.join(self.base_path, "commands.txt")

    def log(self, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, "a") as f:
            f.write(f"[{timestamp}] {message}\n")

    def read_commands(self):
        if os.path.exists(self.cmd_file):
            with open(self.cmd_file, "r") as f:
                cmd = f.read().strip()
                if cmd:
                    # تفريغ الملف
                    with open(self.cmd_file, "w") as clear:
                        clear.write("")
                    return cmd
        return None

    def evolve(self):
        instruction = self.read_commands()
        if not instruction:
            self.log("لا توجد أوامر في commands.txt. النظام في وضع الخمول.")
            return

        self.log(f"الوحش استلم المهمة: {instruction}")
        
        try:
            prompt = f"المهمة: {instruction}. اكتب كود Python لتنفيذها."
            response = self.client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama-3.3-70b-versatile",
            )
            new_logic = response.choices[0].message.content
            
            with open(os.path.join(self.base_path, "evolution_logic.py"), "w") as f:
                f.write(new_logic)
            self.log("تم تحديث المنطق البرمجي.")
        except Exception as e:
            self.log(f"خطأ في التنفيذ: {str(e)}")

if __name__ == "__main__":
    behemoth = BehemothEmpire()
    behemoth.evolve()
