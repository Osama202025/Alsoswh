import os
import google.generativeai as genai
from groq import Groq
from openai import OpenAI

class BehemothNexusPrime:
    def __init__(self):
        # تفعيل الثلاثي الخارق باستخدام متغيرات البيئة من GitHub Secrets
        self.groq = Groq(api_key=os.environ.get("GROQ_API_KEY"))
        genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
        self.gemini = genai.GenerativeModel('gemini-1.5-flash')
        self.deepseek = OpenAI(api_key=os.environ.get("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com")
        
        self.nexus_dir = "BEHEMOTH_NEXUS"
        if not os.path.exists(self.nexus_dir): os.makedirs(self.nexus_dir)

    def orchestrate(self, task):
        print(f"Orchestrating task: {task}")
        
        # اختيار الذكاء بناءً على طبيعة المهمة
        if "بناء" in task or "نظام" in task:
            response = self.gemini.generate_content(task).text
        elif "تصحيح" in task or "ذكاء" in task:
            res = self.deepseek.chat.completions.create(model="deepseek-chat", messages=[{"role": "user", "content": task}])
            response = res.choices[0].message.content
        else:
            res = self.groq.chat.completions.create(messages=[{"role": "user", "content": task}], model="llama-3.3-70b-versatile")
            response = res.choices[0].message.content
            
        self.deploy(response)

    def deploy(self, content):
        lines = content.splitlines()
        current_file = None
        for line in lines:
            if "### FILE:" in line:
                filename = line.replace("### FILE:", "").strip()
                current_file = os.path.join(self.nexus_dir, filename)
            elif current_file:
                with open(current_file, "a") as f: f.write(line + "\n")

if __name__ == "__main__":
    if os.path.exists("commands.txt"):
        with open("commands.txt", "r") as f:
            cmd = f.read().strip()
        if cmd:
            nexus = BehemothNexusPrime()
            nexus.orchestrate(cmd)
            with open("commands.txt", "w") as f: f.write("")
