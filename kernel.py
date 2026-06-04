import os
import datetime
import json
from groq import Groq

class BehemothSupreme:
    def __init__(self):
        self.client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
        self.root_dir = "BEHEMOTH_OS" # بيئة تشغيل الوحش
        if not os.path.exists(self.root_dir): os.makedirs(self.root_dir)

    def evolve(self, prompt_input):
        # تقسيم المهمة إلى "وحدات بناء"
        prompt = f"""
        أنت الذكاء الاصطناعي الأقوى Behemoth. مهمتك: {prompt_input}.
        قم بإنشاء نظام برمجي ضخم وموزع. 
        1. قسّم الكود إلى ملفات متعددة (.py) داخل مجلد {self.root_dir}/.
        2. استخدم أسلوب البرمجة المتعددة (Modular Programming).
        3. أضف تعليقات توثيقية لكل 10 أسطر.
        4. اجعل النظام يكتب ملف 'manifest.json' يوضح كيفية ربط الملفات ببعضها.
        """
        
        response = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            max_tokens=15000 # صلاحية مطلقة للحجم
        )
        
        self.distribute_code(response.choices[0].message.content)

    def distribute_code(self, ai_output):
        # المحرك يقوم بتوزيع مخرجات الذكاء الاصطناعي على ملفات
        lines = ai_output.split('\n')
        current_file = None
        for line in lines:
            if line.startswith("FILE:"):
                current_file = os.path.join(self.root_dir, line.replace("FILE:", "").strip())
            elif current_file:
                with open(current_file, "a") as f: f.write(line + "\n")

if __name__ == "__main__":
    if os.path.exists("commands.txt"):
        with open("commands.txt", "r") as f:
            cmd = f.read().strip()
            if cmd:
                BehemothSupreme().evolve(cmd)
                with open("commands.txt", "w") as f: f.write("")
