from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
CARD_COLOR = "#8EC3B0"
SHADOW_1 = "#332E33"
SHADOW_2 = "#332E33"
SHADOW_3 = "#665C66"
SHADOW_4 = "#807380"
SHADOW_5 = "#998A99"


window = Tk()
window.title("Flash cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.pack()

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


card_shadow5 = round_rectangle(10, 10, 710, 510, radius=20, fill=SHADOW_3)
card = round_rectangle(0, 0, 700, 500, radius=20, fill=CARD_COLOR)


window.mainloop()

