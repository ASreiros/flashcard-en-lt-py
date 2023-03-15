from tkinter import *
from data import Data

BACKGROUND_COLOR = "#B1DDC6"
ANSWER_COLOR = "white"
CARD_COLOR = "#8EC3B0"
SHADOW_1 = "#332E33"
SHADOW_2 = "#332E33"
SHADOW_3 = "#665C66"
SHADOW_4 = "#807380"
SHADOW_5 = "#998A99"
TIME = 5
FONT_NAME = "Ariel"
LANGUAGE = "English"
TRANSLATE = "Lietuvių"


def count_down(count):
	if count > 0:
		label_time.config(text=count, bg=CARD_COLOR)
		window.after(1000, count_down, count - 1)
	else:
		show_answer()


def show_word():
	dictionary.flag = False
	canvas.itemconfig(card, fill=CARD_COLOR)
	word = dictionary.get_word()
	label_language.config(text=LANGUAGE, bg=CARD_COLOR, fg=ANSWER_COLOR)
	label_warning.config(bg=CARD_COLOR, fg=ANSWER_COLOR, text=f"Correct answers: {dictionary.correct} / {dictionary.tries}")
	if word != "|EXIT|":
		label_word.config(text=word, bg=CARD_COLOR, fg=ANSWER_COLOR)
		count_down(TIME)
	else:
		label_word.config(text="")
		label_warning.config(text="No more new words in dictionary")


def show_answer():
	dictionary.flag = True
	canvas.itemconfig(card, fill=ANSWER_COLOR)
	label_time.config(text="", bg=ANSWER_COLOR)
	label_language.config(text=TRANSLATE, bg=ANSWER_COLOR, fg=CARD_COLOR)
	label_word.config(text=dictionary.translate, bg=ANSWER_COLOR, fg=CARD_COLOR)
	label_warning.config(bg=ANSWER_COLOR, fg=CARD_COLOR, text=f"Correct answers: {dictionary.correct} / {dictionary.tries}")


def press_right():
	if dictionary.flag:
		dictionary.correct_word()
		show_word()
	else:
		label_warning.config(text="Wait until translation is shown")


def press_wrong():
	if dictionary.flag:
		show_word()
	else:
		label_warning.config(text="Wait until translation is shown")


def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
	points = [x1 + radius, y1,
			  x1 + radius, y1,
			  x2 - radius, y1,
			  x2 - radius, y1,
			  x2, y1,
			  x2, y1 + radius,
			  x2, y1 + radius,
			  x2, y2 - radius,
			  x2, y2 - radius,
			  x2, y2,
			  x2 - radius, y2,
			  x2 - radius, y2,
			  x1 + radius, y2,
			  x1 + radius, y2,
			  x1, y2,
			  x1, y2 - radius,
			  x1, y2 - radius,
			  x1, y1 + radius,
			  x1, y1 + radius,
			  x1, y1]

	return canvas.create_polygon(points, **kwargs, smooth=True)


dictionary = Data()
window = Tk()
window.title("Flash cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=710, height=700, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.pack()

card_shadow = round_rectangle(10, 10, 710, 510, radius=100, fill=SHADOW_4)
card = round_rectangle(0, 0, 700, 500, radius=100, fill=CARD_COLOR)

image_right = PhotoImage(file="images/right.png")
button_right = Button(image=image_right, highlightthickness=0, bg=CARD_COLOR, command=press_right)
button_right.place(x=500, y=520)

image_wrong = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=image_wrong, highlightthickness=0, bg=CARD_COLOR, command=press_wrong)
button_wrong.place(x=100, y=520)

label_time = Label(text="", font=(FONT_NAME, 40, "italic"), fg="white", bg=CARD_COLOR)
label_time.place(x=350, y=40, anchor="center")

label_language = Label(text="language", font=(FONT_NAME, 40, "italic"), fg="white", bg=CARD_COLOR)
label_language.place(x=350, y=100, anchor="center")

label_word = Label(text="", font=(FONT_NAME, 80, "italic"), fg="white", bg=CARD_COLOR)
label_word.place(x=350, y=250, anchor="center")

label_warning = Label(text="", font=(FONT_NAME, 20, "italic"), bg=CARD_COLOR)
label_warning.place(x=350, y=480, anchor="center")


show_word()
window.mainloop()

