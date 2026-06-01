
import random

# رسائل ترحيب عشوائية
messages = [
    "مرحبا، يسعدني مساعدتك!",
    "أهلاً بك، هل يمكنني مساعدتك في أمر ما؟",
    "مرحباً بك، كيف يمكنني مساعدتك اليوم؟",
    "أهلاً بك، يسعدني أن أتحدث معك!",
    "مرحباً، كيف يمكنني خدمتك؟"
]

def print_welcome_message():
    # طباعة رسالة ترحيب عشوائية
    print(random.choice(messages))

def main():
    print_welcome_message()
    # باقي الكود هنا...

if __name__ == "__main__":
    main()
