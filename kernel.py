import os
from google import genai # المكتبة الأحدث
from groq import Groq
from openai import OpenAI

class BehemothNexusPrime:
    def __init__(self):
        # تفعيل المحركات الأحدث
        self.client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))
        self.groq = Groq(api_key=os.environ.get("GROQ_API_KEY"))
        self.deepseek = OpenAI(api_key=os.environ.get("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com")
        
        self.nexus_dir = "BEHEMOTH_NEXUS"
        os.makedirs(self.nexus_dir, exist_ok=True)

    def orchestrate(self, task):
        # استخدام Gemini 2.0 Flash (الأحدث)
        response = self.client.models.generate_content(
            model='gemini-2.0-flash',
            contents=task
        )
        self.deploy(response.text)

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
