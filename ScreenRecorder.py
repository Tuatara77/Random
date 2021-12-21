import cv2 #install with pip install opencv-python
import numpy as np
import pyautogui #MUST INSTALL PILLOW - pip install Pillow
from datetime import datetime

screen_size = pyautogui.size()
FPS = 20.0
filename = "Video"
filetyle = ".avi"
file = filename + filetype

fourcc = cv2.VideoWriter_fourcc(*"XVID")

##timelist = list(datetime.now().strftime("%D"))
##timelist[0:2], timelist[3:5] = timelist[3:5], timelist[0:2]
##date = ""
##for f in timelist:
##    date += f
##time = datetime.now().strftime(f'{date} at %H:%M:%S')
##
##filename = str(time)+".avi"
##
##out = cv2.VideoWriter(f"{time}.avi", fourcc, 20.0, (screen_size))

out = cv2.VideoWriter(file, fourcc, FPS, (screen_size))

while True:
    img = pyautogui.screenshot(region=(0, 0, screen_size[0], screen_size[1]))
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    out.write(frame)

    cv2.imshow("screenshot", frame)

    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()
out.release()

