import cv2
from cvzone.HandTrackingModule import HandDetector
import gestures as gs
import numpy as np
cimport numpy as np
import pyautogui

cpdef list landmark_xyposition(list hand1, int landmarkId):
    return hand1['lmList'][landmarkId][0:2]

cdef object detector, camera, instance
cdef int screen_weight, screen_height, camera_weight, camera_height
cdef np.ndarray frame, img
cdef list hands, hand1, lmposition_12, fingers1

cdef int run():
    detector = HandDetector(maxHands=1, detectionCon=0.9)
    camera = cv2.VideoCapture(0)
    camera_height = 480
    camera_weight = 640
    screen_weight, screen_height = pyautogui.size()
    camera.set(3, camera_weight)
    camera.set(4, camera_height)
    while True:
        check, frame = camera.read()
        img = cv2.flip(frame, 1)
        hands, img = detector.findHands(img, flipType=False)
        fingers1 = detector.fingersUp(hand1)
        instance = gs.gestures(fingers1, hand1, detector)
        if hands:
            hand1 = hands[0]
            lmposition_12 = landmark_xyposition(hand1=hand1, landmarkId=12)
            pyautogui.moveTo(screen_weight*lmposition_12[0]/camera_weight, screen_height*lmposition_12[1]/camera_height)
            instance = gs.gestures(fingers1, hand1, detector)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        cv2.imshow("Visor", img)