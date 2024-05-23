import tkinter as tk
import ttkbootstrap as tb
from tkinter import messagebox

root = tb.Window(themename="solar")

class QuizSystem:
    def __init__(self, master):
        self.master = master
        master.title("Quiz System")
        master.geometry("500x600")

        self.frame_name = tb.Frame(master, padding=10)
        self.frame_name.pack(fill=tk.X)

        self.frame_class = tb.Frame(master, padding=10)
        self.frame_class.pack(fill=tk.X)

        self.frame_questions = tb.Frame(master, padding=10)
        self.frame_questions.pack(fill=tk.X)

        self.frame_submit = tb.Frame(master, padding=10)
        self.frame_submit.pack(fill=tk.X)

        self.label_name = tb.Label(self.frame_name, text="Nama:")
        self.label_name.pack(side=tk.LEFT, padx=5)
        self.entry_name = tb.Entry(self.frame_name)
        self.entry_name.pack(side=tk.LEFT, padx=5)

        self.label_class = tb.Label(self.frame_class, text="Kelas:")
        self.label_class.pack(side=tk.LEFT, padx=7)
        self.entry_class = tb.Entry(self.frame_class)
        self.entry_class.pack(side=tk.LEFT, padx=7)

        self.questions = [
            {"text": "4 + (2 - 9) =", "answer": "-3"},
            {"text": "201 - (21 * 2) =", "answer": "159"},
            {"text": "21 * 21 =", "answer": "441"},
            {"text": "2 * 189 =", "answer": "378"},
            {"text": "3 * 72 =", "answer": "216"}
        ]

        self.labels = []
        self.entries = []

        for i, question in enumerate(self.questions):
            label = tb.Label(self.frame_questions, text=question["text"])
            label.pack(pady=5)
            self.labels.append(label)

            entry = tb.Entry(self.frame_questions)
            entry.pack(pady=9)
            self.entries.append(entry)

        self.submit = tb.Button(self.frame_submit, text="Submit", command=self.check)
        self.submit.pack(pady=10)

    def check(self):
        answers = [entry.get() for entry in self.entries]

        nilai = 0
        for i, answer in enumerate(answers):
            if answer == self.questions[i]["answer"]:
                self.labels[i].config(text=f"Benar! {self.questions[i]['text']} {answer}")
                nilai += 1
            else:
                self.labels[i].config(text=f"Salah! {self.questions[i]['text']} {self.questions[i]['answer']}")

        name = self.entry_name.get()
        class_name = self.entry_class.get()
        score = f"{nilai} dari {len(self.questions)}"
        messagebox.showinfo("Hasil Quiz", f"Nama: {name}\nKelas : {class_name}\nNilai  : {score}")

quiz_system = QuizSystem(root)
root.mainloop()
