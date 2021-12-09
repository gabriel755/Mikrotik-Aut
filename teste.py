import pyautogui

user = "bruno.najanet"
password = "9jjH2dtB"
sw1 = "10.250.250.4"
sw2 = "10.250.250.6"
sw2 = "10.250.250.8"
sw4 = "10.250.250.12"
sw5 = "10.250.250.15"
sw6 = "10.250.250.19"
sw7 = "10.250.250.21"
sw8 = "10.250.250.23"
sw9 = "10.250.250.24"
sw10 = "10.250.250.25"
sw11 = "10.250.250.28"
sw12 = "10.199.199.100"
sw13 = "10.250.250.34"

# --------------- SW1
pyautogui.PAUSE = 3.5
pyautogui.press("winleft")
pyautogui.write("powershell")
pyautogui.press("enter")
pyautogui.write("ssh "+ user + "@" + sw1)
pyautogui.press("enter")
pyautogui.write("yes")
pyautogui.press("enter")
pyautogui.write(password)
pyautogui.press("enter")
pyautogui.write("quit")
pyautogui.press("enter")

# ------------ SW2
pyautogui.PAUSE = 3.5
pyautogui.write("ssh "+ user + "@" + sw2)
pyautogui.press("enter")
pyautogui.write("yes")
pyautogui.press("enter")
pyautogui.write(password)
pyautogui.press("enter")
pyautogui.write("quit")
pyautogui.press("enter")

# ----------- SW 2
pyautogui.PAUSE = 3.5
pyautogui.write("ssh "+ user + "@" + sw3)
pyautogui.press("enter")
pyautogui.write("yes")
pyautogui.press("enter")
pyautogui.write(password)
pyautogui.press("enter")
pyautogui.write("quit")
pyautogui.press("enter")

# ------ SW 4
pyautogui.PAUSE = 3.5
pyautogui.write("ssh "+ user + "@" + sw4)
pyautogui.press("enter")
pyautogui.write("yes")
pyautogui.press("enter")
pyautogui.write(password)
pyautogui.press("enter")
pyautogui.write("quit")
pyautogui.press("enter")

# ----------- SW 5 
pyautogui.PAUSE = 3.5
pyautogui.write("ssh "+ user + "@" + sw5)
pyautogui.press("enter")
pyautogui.write("yes")
pyautogui.press("enter")
pyautogui.write(password)
pyautogui.press("enter")
pyautogui.write("quit")
pyautogui.press("enter")

# ---------- SW 6
pyautogui.PAUSE = 3.5
pyautogui.write("ssh "+ user + "@" + sw6)
pyautogui.press("enter")
pyautogui.write("yes")
pyautogui.press("enter")
pyautogui.write(password)
pyautogui.press("enter")
pyautogui.write("quit")
pyautogui.press("enter")

pyautogui.PAUSE = 3.5
pyautogui.write("ssh "+ user + "@" + sw7)
pyautogui.press("enter")
pyautogui.write("yes")
pyautogui.press("enter")
pyautogui.write(password)
pyautogui.press("enter")
pyautogui.write("quit")
pyautogui.press("enter")

pyautogui.PAUSE = 3.5
pyautogui.write("ssh "+ user + "@" + sw8)
pyautogui.press("enter")
pyautogui.write("yes")
pyautogui.press("enter")
pyautogui.write(password)
pyautogui.press("enter")
pyautogui.write("quit")
pyautogui.press("enter")

pyautogui.PAUSE = 3.5
pyautogui.write("ssh "+ user + "@" + sw9)
pyautogui.press("enter")
pyautogui.write("yes")
pyautogui.press("enter")
pyautogui.write(password)
pyautogui.press("enter")
pyautogui.write("quit")
pyautogui.press("enter")

pyautogui.PAUSE = 3.5
pyautogui.write("ssh "+ user + "@" + sw10)
pyautogui.press("enter")
pyautogui.write("yes")
pyautogui.press("enter")
pyautogui.write(password)
pyautogui.press("enter")
pyautogui.write("quit")
pyautogui.press("enter")

pyautogui.PAUSE = 3.5
pyautogui.write("ssh "+ user + "@" + sw11)
pyautogui.press("enter")
pyautogui.write("yes")
pyautogui.press("enter")
pyautogui.write(password)
pyautogui.press("enter")
pyautogui.write("quit")
pyautogui.press("enter")


pyautogui.PAUSE = 3.5
pyautogui.write("ssh "+ user + "@" + sw12)
pyautogui.press("enter")
pyautogui.write("yes")
pyautogui.press("enter")
pyautogui.write(password)
pyautogui.press("enter")
pyautogui.write("quit")
pyautogui.press("enter")

pyautogui.PAUSE = 3.5
pyautogui.write("ssh "+ user + "@" + sw13)
pyautogui.press("enter")
pyautogui.write("yes")
pyautogui.press("enter")
pyautogui.write(password)
pyautogui.press("enter")
pyautogui.write("quit")
pyautogui.press("enter")
