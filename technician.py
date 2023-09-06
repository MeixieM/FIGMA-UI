
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame_technician")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1024x600")
window.configure(bg = "#E5E5E5")

canvas = Canvas(
    window,
    bg = "#E5E5E5",
    height = 600,
    width = 1024,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1024.0,
    100.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    31.0,
    10.0,
    282.0,
    86.97332763671875,
    fill="#D3F9D8",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    64.0,
    47.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    64.0,
    47.0,
    image=image_image_2
)

canvas.create_text(
    97.0,
    27.0,
    anchor="nw",
    text="MACHINE",
    fill="#343A40",
    font=("Roboto Medium", 14 * -1)
)

canvas.create_text(
    97.0,
    44.0,
    anchor="nw",
    text="ONLINE",
    fill="#343A40",
    font=("Roboto Medium", 24 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=872.0,
    y=119.0,
    width=122.0,
    height=42.0
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    728.0,
    48.0,
    image=image_image_3
)

canvas.create_rectangle(
    31.0,
    181.0,
    506.0,
    581.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    522.0,
    181.0,
    994.0,
    581.0,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    769.0,
    39.0,
    anchor="nw",
    text="Alex Fernan F. Mercado",
    fill="#339AF0",
    font=("Roboto Bold", 20 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=326.0,
    y=115.0,
    width=372.0,
    height=51.0
)
window.resizable(False, False)
window.mainloop()
