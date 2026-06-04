import os
import datetime
from groq import Groq

class BehemothEmpire:
    def __init__(self):
        self.client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
        self.log_file = "evolution_log.txt"
        self.cmd_file = "commands.txt"

    def log(self, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, "a") as f:
            f.write(f"[{timestamp}] {message}\n")

    def read_commands(self):
        if os.path.exists(self.cmd_file):
            with open(self.cmd_file, "r") as f:
                cmd = f.read().strip()
                if cmd:
                    # تفريغ الأمر بعد قراءته ليبدأ التنفيذ
                    with open(self.cmd_file, "w") as clear:
                        clear.write("")
                    return cmd
        return None

    def evolve(self):
        instruction = self.read_commands() or "لا توجد أوامر، استمر في تحسين البنية التحتية للنظام."
        
        self.log(f"الوحش يستلم المهمة: {instruction}")
        
        prompt = f"""
        أنت الكيان الإمبراطوري المطور لنفسه. 
        المهمة الحالية: {instruction}
        بناءً على تاريخ تطورك، اكتب كود Python جديداً أو قم بتعديل البنية البرمجية لزيادة قوتك واستقلاليتك.
        أخرج الكود فقط داخل وسوم البرمجة.
        """
        
        response = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
        )
        
        new_logic = response.choices[0].message.content
        
        # حفظ التطور
        with open("evolution_logic.py", "w") as f:
            f.write(new_logic)
        
        self.log("تم تحديث المنطق البرمجي بنجاح.")

if __name__ == "__main__":
    behemoth = BehemothEmpire()
    behemoth.evolve()
