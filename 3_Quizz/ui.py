import time
from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quize")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 10))
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150,125,width=280,text="Some Question Text",fill=THEME_COLOR,font=("Times New Roman",15))
        self.canvas.config(bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2,padx=20,pady=20)

        true_image = PhotoImage(file="images/true.png")
        self.correct_buttton = Button(image=true_image,command=self.true_pressed)
        self.correct_buttton.grid(column=1, row=2, padx=20, pady=20)

        false_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=false_image, command=self.false_pressed)
        self.wrong_button.grid(column=0, row=2, padx=20, pady=20)
        self.get_next_question()



        self.window.mainloop()
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score : {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text=f"You've reached the end of the quiz.\nYour final score was: {self.quiz.score}/{self.quiz.question_number}")

            self.correct_buttton.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))


    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)












