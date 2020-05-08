from pynput.mouse import Button, Controller  # Importa librería Mouse
import pythoncom, pyHook 


mouse = Controller()  

def BlockMouse():
    mouse.position = (0, 0) # el mouse se va a la posición 0,0 de la pantalla
    #mouse.press(Button.right)
    #mouse.release(Button.right)
    mouse.press(Button.left)
    mouse.release(Button.left)
    
k = pyHook.HookManager()
while(True):
    def e(event):
        return False
    k.KeyAll = e
    k.HookKeyboard()
    pythoncom.PumpMessages()
