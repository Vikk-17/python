# Get the position of the mouse:

#! python3
import pyautogui
print("Press Ctrl+C to quit")


def getMousePos():
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = f'X: {str(x).rjust(4)} and Y: {str(y).rjust(4)}'
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print("\nDone.")

getMousePos()
