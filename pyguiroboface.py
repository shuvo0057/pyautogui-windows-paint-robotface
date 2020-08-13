import pyautogui
import time

time.sleep(5)

# first square
pyautogui.click(1744, 71)
pyautogui.moveTo(1773, 216)

pyautogui.dragTo(1773, 216, 2, pyautogui.easeInBounce)
pyautogui.dragTo(1773, 804, 2, pyautogui.easeInBounce)
pyautogui.dragTo(1093, 804, 2, pyautogui.easeInBounce)
pyautogui.dragTo(1093, 216, 2, pyautogui.easeInBounce)
pyautogui.dragTo(1773, 216, 2, pyautogui.easeInBounce)


# second square
pyautogui.click(1664, 71)

pyautogui.moveTo(1725, 264, 0.8)

pyautogui.dragTo(1725, 264, 1.5, pyautogui.easeInOutQuad)
pyautogui.dragTo(1725, 766, 1.5, pyautogui.easeInOutQuad)
pyautogui.dragTo(1139, 766, 1.5, pyautogui.easeInOutQuad)
pyautogui.dragTo(1139, 264, 1.5, pyautogui.easeInOutQuad)
pyautogui.dragTo(1725, 264, 1.5, pyautogui.easeInOutQuad)


# change colour for eyes
pyautogui.click(1596, 69)

# left eye
pyautogui.click(1182, 305)
distance = 200


while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.1)
    distance = distance - 5
    pyautogui.dragRel(0, distance, duration=0.1)

    pyautogui.dragRel(-distance, 0, duration=0.1)
    distance = distance - 5

    pyautogui.dragRel(0, -distance, duration=0.1)


# right eye
pyautogui.click(1502, 305)
distance = 200


while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.1)
    distance = distance - 5
    pyautogui.dragRel(0, distance, duration=0.1)

    pyautogui.dragRel(-distance, 0, duration=0.1)
    distance = distance - 5

    pyautogui.dragRel(0, -distance, duration=0.1)


# mouth

pyautogui.click(1636, 73)

wait = 2

pyautogui.click(1396, 671)
distance = 80


while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.1)
    distance = distance - 4
    pyautogui.dragRel(0, distance, duration=0.1)

    pyautogui.dragRel(-distance, 0, duration=0.1)
    distance = distance - 4

    pyautogui.dragRel(0, -distance, duration=0.1)

# eyeball colour

wait = 1
pyautogui.click(1412, 94)
wait = 1

# eyeball 1
pyautogui.click(1221, 329)
distance = 50


while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.1)
    distance = distance - 4
    pyautogui.dragRel(0, distance, duration=0.1)

    pyautogui.dragRel(-distance, 0, duration=0.1)
    distance = distance - 4

    pyautogui.dragRel(0, -distance, duration=0.1)

# eyeball 2
pyautogui.click(1315, 331)
distance = 50


while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.1)
    distance = distance - 4
    pyautogui.dragRel(0, distance, duration=0.1)

    pyautogui.dragRel(-distance, 0, duration=0.1)
    distance = distance - 4

    pyautogui.dragRel(0, -distance, duration=0.1)

# eyeball 3
pyautogui.click(1533, 326)
distance = 50


while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.1)
    distance = distance - 4
    pyautogui.dragRel(0, distance, duration=0.1)

    pyautogui.dragRel(-distance, 0, duration=0.1)
    distance = distance - 4

    pyautogui.dragRel(0, -distance, duration=0.1)


# eyeball 4

pyautogui.click(1623, 327)
distance = 50

while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.1)
    distance = distance - 4
    pyautogui.dragRel(0, distance, duration=0.1)

    pyautogui.dragRel(-distance, 0, duration=0.1)
    distance = distance - 4

    pyautogui.dragRel(0, -distance, duration=0.1)


pyautogui.click(1182, 83)

pyautogui.click(1209, 953)

pyautogui.write('FUCK EVERYTHING!', interval=0.25)
pyautogui.hotkey('ctrl', 'A')
pyautogui.click(1087, 109)

pyautogui.press('enter')
pyautogui.click(1427, 951)
pyautogui.hotkey('ctrl', 'A')
pyautogui.click(1418, 68)
#update incoming
#Version 1.0
#Day 1
