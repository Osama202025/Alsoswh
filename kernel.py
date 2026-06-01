import os
import importlib
from groq import Groq

class BehemothKernel:
    def __init__(self):
        self.client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
        self.knowledge_base = "knowledge_matrix.json"
        
    def think(self, goal):
        print(f"--- [Kernel: Processing Goal -> {goal}] ---")
        prompt = f"بصفتك عقل اصطناعي إمبراطوري، حلل الهدف التالي: '{goal}'. اكتب خطوات تنفيذية برمجية مفصلة."
        
        response = self.client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
        )
        return response.choices[0].message.content

    def execute_plan(self, plan):
        # النواة تطلب من المُنَفذ (Executor) العمل
        print(f"--- [Kernel: Dispatching Plan to Executor] ---")
        # هنا سنقوم لاحقاً بربطه بـ executor.py
        pass

if __name__ == "__main__":
    brain = BehemothKernel()
    print(brain.think("بناء نظام أتمتة كامل لتحليل بيانات الأسواق العالمية"))
