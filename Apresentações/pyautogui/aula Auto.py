import pyautogui
from time import sleep

# while True:
#     print(pyautogui.position())
#     sleep(2)

# pyautogui.moveTo(0, 0) #MOVE PARA POSICAO
# pyautogui.moveTo(1920, 1080) #MOVE PARA POSICAO
# pyautogui.moveTo(960, 540) #MOVE PARA POSICAO

# pyautogui.moveRel(0, -100)

# pyautogui.click()
# pyautogui.leftClick()
# pyautogui.rightClick()
# pyautogui.tripleClick(0, 0)

# pyautogui.hotkey('ctrl', 'shift', 'esc')
# pyautogui.hotkey('win')
# pyautogui.keyDown('win')
# pyautogui.keyDown('win')
# pyautogui.keyDown('win')
# pyautogui.keyDown('win')



# pyautogui.press('win')
# pyautogui.write('bloco de notas', interval=0.1)
# pyautogui.press('enter')
# print(pyautogui.KEYBOARD_KEYS(pyautogui.press('enter')))
#
# with pyautogui.hold('win'):
#     pyautogui.press(['A', 'B'], interval= 0.5)
#     pyautogui.press('A',presses=3, interval= 0.5)

# pyautogui.dragTo(0, 0, button='left', duration=2)
# pyautogui.dragRel(-500, 0, button='left', duration=2)


# pyautogui.hotkey("alt", "tab")
# # sleep(3)
# pyautogui.moveTo(162, 219)
# pyautogui.dragTo(977, 273, duration=2)
# pyautogui.dragRel(-177, 273, duration=2)
# pyautogui.dragRel(-177, -273, duration=2)
# pyautogui.dragRel(-177, -273, duration=2)
# pyautogui.dragRel(177, -273, duration=2)
# pyautogui.dragRel(977, 273, duration=2)


# pyautogui.alert(text='Cauan',title='Alerta', button='a')


# var = pyautogui.prompt(text='ALE', title='alerta', default='')

# pyautogui.confirm(text='Cauan', title='Alerta')

# pyautogui.password(text='Cauan', title='Cauan', default='', mask='*')

sleep(1)
x = pyautogui.locateOnScreen('Capturar.PNG')
print(x)
pyautogui.moveTo(x)
