import pyautogui as pg

pg.hotkey("Win", "r")
pg.typewrite("shell:RecycleBinFolder\n")
pg.hotkey("Ctrl", "e")
pg.hotkey("shift", "f10")

for i in range(3):
    pg.hotkey("down")
for i in range(3):
    pg.hotkey("Enter")

pg.hotkey("Alt", "f4")