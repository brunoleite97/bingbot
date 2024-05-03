import pyautogui
import time
import random
from faker import Faker

fake = Faker()

keywords = [fake.word() for _ in range(1000)]

for keyword in keywords:

    pyautogui.hotkey('winleft')
    pyautogui.write('Microsoft Edge')
    pyautogui.press('enter')
    time.sleep(5)
    
    pyautogui.write(keyword)
    pyautogui.press('enter')
    time.sleep(random.randint(10, 30))
    
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(2)

print("Pesquisas concluídas.")
