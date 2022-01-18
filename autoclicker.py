import tkinter as tk
from tkinter import END
import mouse

hotkey = "Insert"


title = "Autoclicker"
windowx = 150
windowy = 400
startposx = 200
startposy = 540


def click(event=None):
    mouse.click()
    clickcount['state'] = "normal"
    count = int(clickcount.get("1.0", END))
    count += 1
    clickcount.delete("1.0", END)
    clickcount.insert(END, chars=str(count))
    clickcount['state'] = "disabled"


window = tk.Tk()
window.title(title)
window.geometry(f"{windowx}x{windowy}+{startposx}+{startposy}")


clicktext = tk.Label(window, width=8, height=1, text="Click Count")
clicktext.place(x=7, y=10)
clickcount = tk.Text(window, width=8, height=1)
clickcount.place(x=80, y=10)
clickcount.insert(END, chars="0")
clickcount['state'] = "disabled"

# ratetext = tk.Label(window, width=8, height=1, text="Clicks/s")
# ratetext.place(x=7, y=35)
# clickrate = tk.Entry(window, width=10)
# clickrate.place(x=80, y=35)

window.bind(f"<{hotkey}>", click)


window.mainloop()