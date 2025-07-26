import tkinter as tk
from tkinter import messagebox

# قاعدة بيانات بسيطة للأسئلة
questions = {
    "ما هو عاصمة الجزائر؟": "الجزائر",
    "ما هو حاصل 7 × 8؟": "56",
    "من هو مكتشف قانون الجاذبية؟": "نيوتن",
    "ما هي وحدة قياس التيار الكهربائي؟": "أمبير"
}

# الدالة للتحقق من الإجابة
def check_answer():
    user_answer = entry.get()
    correct = questions[current_question]
    if user_answer.strip().lower() == correct.strip().lower():
        messagebox.showinfo("نتيجة", "إجابة صحيحة ✅")
    else:
        messagebox.showwarning("نتيجة", f"إجابة خاطئة ❌. الإجابة الصحيحة: {correct}")
    next_question()

# عرض السؤال التالي
def next_question():
    global current_question
    current_question = random.choice(list(questions.keys()))
    question_label.config(text=current_question)
    entry.delete(0, tk.END)

# واجهة التطبيق
import random
app = tk.Tk()
app.title("EduBot - مساعد الدراسة")

question_label = tk.Label(app, text="", font=("Arial", 16))
question_label.pack(pady=20)

entry = tk.Entry(app, font=("Arial", 14))
entry.pack(pady=10)

submit_button = tk.Button(app, text="تحقق", command=check_answer)
submit_button.pack(pady=10)

# أول سؤال
current_question = random.choice(list(questions.keys()))
question_label.config(text=current_question)

app.mainloop()
