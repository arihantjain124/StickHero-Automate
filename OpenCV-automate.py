from ppadb.client import Client as AdbClient
import cv2
import time
client = AdbClient(host="127.0.0.1", port=5037)
devices = client.devices()
device = devices[0]
# dev = client.device(device[0])
x = 450
black = [0, 0, 0]
while (True):
    p1 = 0
    p2 = 0
    p3 = 0
    p4 = 0
    flag = 0
    s = "input touchscreen swipe 170 187 170 187"  # + delay in milliseconds
    result = device.screencap()
    with open("image.png", "wb") as fp:
        fp.write(result)
    img = cv2.imread("image.png")
    imgw = int(img.shape[1])
    imgh = int(img.shape[0])
    img = img[imgh - x - 1:imgh - x, :]
    img = img.reshape(imgw, 3)
    line = [list(i) for i in img]
    pixels = (len(line))
    print(pixels)
    for i in range(pixels):
        if line[i] == black and flag == 0:
            if p1 == 0:
                p1 = i
            else:
                p3 = i
            flag = 1
            continue
        if line[i] != black and flag == 1:
            if p2 == 0:
                p2 = i
            else:
                p4 = i
            flag = 0
            continue
    print(p1, p2, p3, p4)
    distance = p3 - p2
    red = (p4 - p3) / 2 + distance
    print(red)
    i = int(red*0.98)
    s = s+" "+str(i)
    device.shell(s)
    print(i)
    time.sleep(3.5)
