from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ('Arial', 20, 'italic')

class QuizInterface():

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(width=500, height=600, background=THEME_COLOR, padx=20, pady=20)

        self.label_score = Label(text="Score: 0", background=THEME_COLOR, fg="white")
        self.label_score.grid(column=1, row=0)

        self.canvas_question = Canvas(width=300, height=250, background="white")
        self.canvas_question.grid(column=0, row=1, columnspan=2, pady=50)
        self.question_text = self.canvas_question.create_text(150, 125, text="question", font=FONT, width=280)

        false_icon = PhotoImage(file="images/false.png")
        true_icon = PhotoImage(file="images/true.png")
        self.button_false = Button(image=false_icon, command=self.true_pressed, highlightthickness=0)
        self.button_false.grid(column=1, row=2)
        self.button_true = Button(image=true_icon, command=self.false_pressed, highlightthickness=0)
        self.button_true.grid(column=0, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            next_question = self.quiz.next_question()
            self.canvas_question.itemconfig(self.question_text, text=next_question)
        else:
            self.canvas_question.itemconfig(self.question_text, text=f"You have reached the end of the quiz. Your final score is: {self.quiz.score}/10")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right == True:
            self.canvas_question.config(background="green")
            self.label_score.config(text=f"Score: {self.quiz.score}")
        if is_right == False:
            self.canvas_question.config(background="red")
        self.window.after(1000, self.change_bckg_normal)

    def change_bckg_normal(self):
        self.canvas_question.config(background="white")
        self.get_next_question()
