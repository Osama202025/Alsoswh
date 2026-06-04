بالتأكيد، يمكنني مساعدتك في كتابة ملف بايثون يقوم بإنشاء تقرير عن حالة النظام الحالية. سنقوم بإنشاء ملف بايثون يحتوي على الكود التالي، وسنجعله يخزن التقرير في مجلد agents.

```python
import os
from datetime import datetime

def get_number_of_files(directory):
    """
    إرجاع عدد الملفات في المجلد المحدد
    """
    return len([name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))])

def get_last_task_status():
    """
    للحصول على حالة آخر مهمة، سنفترض أن هناك ملف يحتوي على معلومات 마지막 مهمة
    هذا الملف يسمى "last_task_status.txt" ويكون فيه نص يحتوي على حالة المهمة
    """
    try:
        with open("last_task_status.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        return "لم تتم إضافة حالة المهمة"

def generate_report():
    """
    إنشاء تقرير عن حالة النظام الحالية
    """
    current_date = datetime.now().strftime("%Y-%m-%d")
    directory = os.path.dirname(os.path.abspath(__file__))
    number_of_files = get_number_of_files(directory)
    last_task_status = get_last_task_status()

    report = f"تقرير حالة النظام ({current_date}):\n"
    report += f"عدد الملفات في المجلد: {number_of_files}\n"
    report += f"حالة آخر مهمة: {last_task_status}\n"

    return report

def save_report(report):
    """
    حفظ التقرير في ملف باسم "system_report.txt" في مجلد agents
    """
    directory = os.path.dirname(os.path.abspath(__file__))
    report_file_path = os.path.join(directory, "system_report.txt")
    with open(report_file_path, "w") as file:
        file.write(report)

if __name__ == "__main__":
    report = generate_report()
    save_report(report)
    print("تم إنشاء تقرير حالة النظام بنجاح.")
```

هذا الكود سوف ينشئ تقريرًا يحتوي على تاريخ اليوم وعدد الملفات في المجلد الحالي (مجلد agents) وحالة آخر مهمة مسجلة في الملف `last_task_status.txt`. بعد إنشاء التقرير، سيتم حفظه في ملف باسم `system_report.txt` في مجلد agents.

لتشغيل هذا البرنامج، يجب أن تقوم بتمكين chạy Python على ملف الكود الموجود في مجلد agents. يمكنك القيام بذلك من خلال فتح 터미널 أو سطر الأوامر، والانتقال إلى مجلد agents، ثم كتابة الأمر التالي:
```bash
python filename.py
```
استبدل `filename.py` بأسم الملف الذي حفظت فيه الكود. بعد ذلك، سترى التقرير المحفوظ في ملف `system_report.txt`ภายใน مجلد agents، ورسالة في Terminal تشير إلى نجاح إنشاء التقرير.

يرجى ملاحظة أن هذا الكود يفترض أن الملف `last_task_status.txt` يحتوي على حالة آخر مهمة مسجلة، إذا لم يكن هذا الملف موجودًا، سيتم عرض رسالة بذلك في التقرير.