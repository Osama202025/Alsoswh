import os
import subprocess
import sys

# التثبيت الذاتي للمكتبات المفقودة
def install_dependencies():
    packages = ["groq", "google-generativeai", "openai"]
    for package in packages:
        try:
            __import__(package.replace("-", "_"))
        except ImportError:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install_dependencies()

# الآن استيراد المكتبات بعد التأكد من وجودها
import google.generativeai as genai
from groq import Groq
from openai import OpenAI

class BehemothNexusPrime:
    def __init__(self):
        self.groq = Groq(api_key=os.environ.get("GROQ_API_KEY"))
        genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
        self.gemini = genai.GenerativeModel('gemini-1.5-flash')
        self.deepseek = OpenAI(api_key=os.environ.get("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com")
        self.nexus_dir = "BEHEMOTH_NEXUS"
        if not os.path.exists(self.nexus_dir): os.makedirs(self.nexus_dir)

    def orchestrate(self, task):
        # منطق اختيار الذكاء
        if "بناء" in task:
            response = self.gemini.generate_content(task).text
        elif "تصحيح" in task:
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
