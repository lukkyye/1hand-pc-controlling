import cv2
from cvzone.HandTrackingModule import HandDetector
import gestures as gs
import pyautogui
import launch_functions

if __name__ == "__main__":
    detector = HandDetector(maxHands=1, detectionCon=0.9)
    camera = cv2.VideoCapture(0)
    cam_w, cam_h = (640, 480)
    screen_w, screen_h = pyautogui.size()
    camera.set(3, cam_w)
    camera.set(4, cam_h)
    while True:
        check, frame = camera.read()
        img = cv2.flip(frame, 1)
        hands, img = detector.findHands(img, flipType=False)
        if hands:
            hand1 = hands[0]
            positionlm8 = hand1['lmList'][12][0:2]
            poslm12_x, poslm12_y = tuple(positionlm8)
            pyautogui.moveTo(screen_w*poslm12_x/cam_w, screen_h*poslm12_y/cam_h)
            fingers1 = detector.fingersUp(hand1)
            instance = gs.gestures(fingers1, hand1, detector)
            if instance.peace_click():
                launch_functions.PEACECLICK
            if instance.toroclick():
                launch_functions.TOROCLICK
            if instance.double_toroclick():
                launch_functions.DOUBLE_TOROCLICK
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        cv2.imshow("Camera feed", img)
    

    cv2.destroyAllWindows()