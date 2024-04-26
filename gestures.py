from cvzone.HandTrackingModule import HandDetector

class gestures():
    def __init__(self, position, hands, detector: HandDetector):
        self.position = tuple(position)
        self.hands = hands
        self.detector = detector
    
    
    def distance(self, lm1, lm2):
        landmark1 = self.hands['lmList'][lm1][0:2]
        landmark2 = self.hands['lmList'][lm2][0:2]
        lenght, info, flip = self.detector.findDistance(landmark1, landmark2)
        del info, flip
        return lenght
    
    def toroclick(self):
        if self.position == (0,0,0,0,1) and gestures.distance(self,4, 8)<20:
            return True
        return False
    
    def o(self):
        if self.position == (1,0,1,1,1) and gestures.distance(self, 4, 8)<20:
            return True
        return False
    
    def double_toroclick(self):
        if self.position == (1,1,0,0,1) and gestures.distance(self,4,8)>40 and gestures.distance(self, 12,16)<20 and gestures.distance(self,12,4)<20 and gestures.distance(self,16,4)<20:
            return True
        return False
        
    def peace_click(self):
        if self.position == (1,1,1,0,0) and gestures.distance(self, 8,12)<25 and gestures.distance(self, 4,16)<20:
            return True
        return False