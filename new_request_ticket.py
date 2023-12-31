from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame_ticket")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def center_window(window):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")


window = Tk()

window.geometry("933x563")
window.configure(bg = "#FFFFFF")
window.overrideredirect(True)


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 563,
    width = 933,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    198.0,
    17.0,
    anchor="nw",
    text="REQUEST TICKET",
    fill="#5E95FF",
    font=("Arial BoldMT", 48 * -1)
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
    x=506.0,
    y=454.0,
    width=172.0,
    height=59.0
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
    x=712.0,
    y=454.0,
    width=172.0,
    height=59.0
)

canvas.create_text(
    52.0,
    98.0,
    anchor="nw",
    text="Machine Name",
    fill="#343A40",
    font=("Arial BoldMT", 24 * -1)
)

canvas.create_text(
    50.0,
    124.0,
    anchor="nw",
    text="Machine_01",
    fill="#868E96",
    font=("ArialMT", 32 * -1)
)

canvas.create_text(
    52.0,
    178.0,
    anchor="nw",
    text="MO Number",
    fill="#343A40",
    font=("Arial BoldMT", 24 * -1)
)

canvas.create_text(
    50.0,
    206.0,
    anchor="nw",
    text="MO1235123",
    fill="#868E96",
    font=("ArialMT", 32 * -1)
)

canvas.create_text(
    530.0,
    93.0,
    anchor="nw",
    text="Requestor",
    fill="#343A40",
    font=("Arial BoldMT", 24 * -1)
)

canvas.create_text(
    530.0,
    119.93170166015625,
    anchor="nw",
    text="FullName",
    fill="#868E96",
    font=("ArialMT", 32 * -1)
)

canvas.create_text(
    530.0,
    178.06951904296875,
    anchor="nw",
    text="Date | Time",
    fill="#343A40",
    font=("Arial BoldMT", 24 * -1)
)

canvas.create_text(
    530.0,
    205.64239501953125,
    anchor="nw",
    text="DateTime",
    fill="#868E96",
    font=("ArialMT", 32 * -1)
)

canvas.create_text(
    50.0,
    264.0,
    anchor="nw",
    text="Downtime Type",
    fill="#343A40",
    font=("Arial BoldMT", 24 * -1)
)

canvas.create_text(
    50.0,
    344.0,
    anchor="nw",
    text="Remarks",
    fill="#343A40",
    font=("Arial BoldMT", 24 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    468.5,
    402.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#EFEFEF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=60.0,
    y=373.0,
    width=817.0,
    height=56.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    164.0,
    311.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#EFEFEF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=58.0,
    y=293.0,
    width=212.0,
    height=34.0
)

canvas.create_rectangle(
    961.0,
    154.0,
    1061.0,
    254.0,
    fill="#000000",
    outline="")

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: window.destroy(),
    relief="flat"
)
button_3.place(
    x=884.0,
    y=0.0,
    width=49.0,
    height=37.0
)

center_window(window)
window.resizable(False, False)
window.mainloop()
