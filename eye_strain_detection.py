from scipy.spatial import distance
from imutils import face_utils
import imutils
import dlib
import cv2
import time

def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

THRESH = 0.20
DROWSY_FRAME_CHECK = 10
SLEEP_FRAME_CHECK = 20

detect = dlib.get_frontal_face_detector()
predict = dlib.shape_predictor('./shape_predictor_68_face_landmarks.dat')

cap = cv2.VideoCapture(0)

(lstart, lend) = face_utils.FACIAL_LANDMARKS_68_IDXS['left_eye']
(rstart, rend) = face_utils.FACIAL_LANDMARKS_68_IDXS['right_eye']

flag = 0
prev = False
blinked = 0

start_time = time.perf_counter()

while True:
    ret, frame = cap.read()
    frame = imutils.resize(frame, width = 450)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    subjects = detect(gray, 0)
    for subject in subjects:
        shape = predict(gray, subject)
        shape = face_utils.shape_to_np(shape)
        leftEye = shape[lstart: lend]
        rightEye = shape[rstart: rend]
        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)
        ear = (leftEAR + rightEAR) / 2.0
        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)
        cv2.drawContours(frame, [leftEyeHull], -1, (0, 0, 255), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 0, 255), 1)
        if ear <= THRESH and prev == False:
            flag += 1
            print(flag)
            if flag >= 3:
                prev = True
            if flag >= DROWSY_FRAME_CHECK:
                # prev = True
                print('\n\n\nDROWSYYYY\n\n\n')
            if flag >= SLEEP_FRAME_CHECK:
                print('\n\n\nPLEASE GO SLEEP\n\n\n')
        else:
            if prev:
                blinked += 1
                print('You have blinked ' + str(blinked) + ' times!')
                after_blink_time = time.perf_counter() - start_time
                if blinked > int(after_blink_time) * 0.5:
                    print('Dude your eyes are stressed')
            prev = False
            flag = 0
            
    cv2.imshow('Frame', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()