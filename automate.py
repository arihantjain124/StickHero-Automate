from ppadb.client import Client as AdbClient
import cv2
import time
client = AdbClient(host="127.0.0.1", port=5037)
devices = client.devices()
device = devices[0]
# dev = client.device(device[0])
while (True):
    s = "input touchscreen swipe 170 187 170 187"  # + delay in milliseconds
    result = device.screencap()
    with open("screen.png", "wb") as fp:
        fp.write(result)
    img = cv2.imread("screen.png")
    imgh = int(img.shape[0]) * 3 // 4
    x = int(img.shape[0] / 120)
    imgw = int(img.shape[1] / 4.32)
    img = img[imgh + x - 1:imgh + x, imgw:]
    line = img.shape[1]
    for i in range(line):
        if img[0][i][2] > 200 and img[0][i][1] < 50 and img[0][i][0] < 50:
            break
    if i < 800:
        i = i+12
        s = s+" "+str(i)
        device.shell(s)
        print(i)
    # cv2.imshow("img", img)
    # cv2.waitKey(1)
    time.sleep(4)
