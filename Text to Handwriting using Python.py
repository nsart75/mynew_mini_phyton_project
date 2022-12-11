import cv2
import pywhatkit as kit 

hand_write = input("Enter Your text: ")

kit.text_to_handwriting(hand_write , save_to = "hand_write.png")


img = cv2.imread("hand_write.png")

cv2.imshow('python hand write' , img)

cv2.waitKey(5)

cv2.destroyWindow()



