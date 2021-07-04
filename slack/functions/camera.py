import sys
import cv2
def test():
    
    sys.stderr.write("***start***\n")

    cc = cv2.VideoCapture(0)

    rr, img = cc.read()
    cv2.imwrite('test01.jpg',img)

    sys.stderr.write("***done***")
    
if __name__ == '__main__':
    test()