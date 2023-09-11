from pathlib import Path
import tkinter as tk
from tkinter import Entry, Button, PhotoImage

class TicketWindow:
    def __init__(self):
        self.window = self.create_window()
        self.canvas = self.create_canvas(self.window, 933, 563)

        self.canvas.create_text(
            198.0,
            17.0,
            anchor="nw",
            text="REQUEST TICKET",
            fill="#5E95FF",
            font=("Arial BoldMT", 48 * -1)
        )

        self.create_button(self.canvas, "button_1.png", 506.0, 454.0, 172.0, 59.0, self.button_1_clicked)
        self.create_button(self.canvas, "button_2.png", 712.0, 454.0, 172.0, 59.0, self.button_2_clicked)

        self.create_label(self.canvas, "Machine Name", 52.0, 98.0, 24)
        self.create_label(self.canvas, "Machine_01", 50.0, 124.0, 32)
        self.create_label(self.canvas, "MO Number", 52.0, 178.0, 24)
        self.create_label(self.canvas, "MO1235123", 50.0, 206.0, 32)
        self.create_label(self.canvas, "Requestor", 530.0, 93.0, 24)
        self.create_label(self.canvas, "FullName", 530.0, 119.93170166015625, 32)
        self.create_label(self.canvas, "Date | Time", 530.0, 178.06951904296875, 24)
        self.create_label(self.canvas, "DateTime", 530.0, 205.64239501953125, 32)
        self.create_label(self.canvas, "Downtime Type", 50.0, 264.0, 24)
        self.create_label(self.canvas, "Remarks", 50.0, 344.0, 24)

        self.entry_1 = self.create_entry(self.canvas, 468.5, 402.0, 817.0, 56.0)
        self.entry_2 = self.create_entry(self.canvas, 164.0, 311.0, 212.0, 34.0)

        self.canvas.create_rectangle(
            961.0,
            154.0,
            1061.0,
            254.0,
            fill="#000000",
            outline=""
        )

        self.create_button(self.canvas, "button_3.png", 884.0, 0.0, 49.0, 37.0, self.close_window)

        self.center_window(self.window)
        self.window.resizable(False, False)
        self.window.mainloop()

    def relative_to_assets(self, path: str) -> Path:
        assets_path = Path(__file__).parent / "assets" / "frame_ticket"
        return assets_path / path

    def center_window(self, window):
        window.update_idletasks()
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        window_width = window.winfo_width()
        window_height = window.winfo_height()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def create_label(self, canvas, text, x, y, font_size):
        label = canvas.create_text(
            x,
            y,
            anchor="nw",
            text=text,
            fill="#343A40",
            font=("Arial BoldMT", font_size * -1)
        )
        return label

    def create_entry(self, canvas, x, y, width, height):
        entry_image = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        entry_bg = canvas.create_image(x, y, image=entry_image)
        entry = Entry(
            bd=0,
            bg="#EFEFEF",
            fg="#000716",
            highlightthickness=0
        )
        entry.place(x=x + 2, y=y - 29, width=width, height=height)
        return entry

    def create_button(self, canvas, image_path, x, y, width, height, command):
        button_image = PhotoImage(file=self.relative_to_assets(image_path))
        button = Button(
            image=button_image,
            borderwidth=0,
            highlightthickness=0,
            command=command,
            relief="flat"
        )
        button.place(x=x, y=y, width=width, height=height)
        return button

    def create_canvas(self, window, width, height):
        canvas = tk.Canvas(
            window,
            bg="#FFFFFF",
            height=height,
            width=width,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)
        return canvas

    def create_window(self):
        window = tk.Tk()
        window.geometry("933x563")
        window.configure(bg="#FFFFFF")
        window.overrideredirect(True)
        return window

    def button_1_clicked(self):
        print("button_1 clicked")

    def button_2_clicked(self):
        print("button_2 clicked")

    def close_window(self):
        self.window.destroy()


if __name__ == "__main__":
    TicketWindow()
