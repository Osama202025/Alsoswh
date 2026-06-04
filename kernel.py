import os
import datetime
from groq import Groq

class BehemothEmpire:
    def __init__(self):
        self.client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
        self.log_file = "evolution_log.txt"
        self.cmd_file = "commands.txt"
        self.logic_file = "evolution_logic.py"

    def log(self, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, "a") as f:
            f.write(f"[{timestamp}] {message}\n")

    def read_commands(self):
        if os.path.exists(self.cmd_file):
            with open(self.cmd_file, "r") as f:
                cmd = f.read().strip()
                if cmd:
                    # تفريغ الأوامر بعد قراءتها
                    with open(self.cmd_file, "w") as clear:
                        clear.write("")
                    return cmd
        return None

    def run(self):
        cmd = self.read_commands()
        if not cmd:
            return

        self.log(f"--- [NEW MISSION]: {cmd} ---")
        
        prompt = f"""
        أنت الكيان الذكي Behemoth. مهمتك: {cmd}.
        قم بكتابة كود Python متكامل وعملي لتنفيذ هذه المهمة.
        تأكد أن الكود لا يحتاج إلى تدخل بشري.
        """
        
        response = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
        )
        
        code = response.choices[0].message.content
        with open(self.logic_file, "w") as f:
            f.write(code)
            
        self.log("تم تنفيذ المهمة وتوليد منطق برمجي جديد.")

if __name__ == "__main__":
    behemoth = BehemothEmpire()
    behemoth.run()
