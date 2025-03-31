from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2 as cv
import mediapipe as mp
import numpy as np
import math
import base64
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize MediaPipe
mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic
holistic = mp_holistic.Holistic(min_detection_confidence=0.7)
fingertip = [4, 8, 12, 16, 20]

# Define sign detection functions
def Aa(list, hand_type):
    len = math.hypot(list[4][1] - list[6][1], list[4][2] - list[6][2])
    if len < 70 and list[4][2] < list[7][2] and abs(list[4][2] - list[3][2]) > 20:
        if hand_type == 'Right':
            if list[3][1] > list[6][1]:
                if (list[8][2] > list[6][2] and list[12][2] > list[10][2] and list[16][2] > list[14][2] and
                list[20][2] > list[18][2] and list[4][1] > list[18][1]):
                    return True

        elif hand_type == 'Left':
            if list[3][1] < list[6][1]:
                if (list[8][2] > list[6][2] and list[12][2] > list[10][2] and list[16][2] > list[14][2] and
                list[20][2] > list[18][2] and list[4][1] < list[18][1]):
                    return True

    return False


def Bb(list, hand_type):
    len1 = math.hypot(list[8][1] - list[11][1], list[8][2] - list[11][2])
    if len1 < 30:
        if hand_type == 'Right':
            if (list[8][2] < list[6][2] and list[12][2] < list[10][2] and list[16][2] < list[14][2] and
            list[20][2] < list[18][2] and list[4][1] < list[5][1]):
                return True

        if hand_type == 'Left':
            if (list[8][2] < list[6][2] and list[12][2] < list[10][2] and list[16][2] < list[14][2] and
            list[20][2] < list[18][2] and list[4][1] > list[5][1]):
                return True

    return False

def Yy(list, hand_type):
    len = math.hypot(list[4][1] - list[6][1], list[4][2] - list[6][2])
    if(list[4][2] < list[2][2] and list[20][2] < list [17][2] and len > 30):
        if(hand_type == 'Right'):
            if (list[4][1] > list[18][1]):
                if(list[8][2] > list[6][2] and list[12][2] > list[10][2] and list[16][2] > list[14][2]):
                    return True

        elif (hand_type == 'Left'):
            if (list[4][1] < list[18][1]):
                if (list[8][2] > list[6][2] and list[12][2] > list[10][2] and list[16][2] > list[14][2]):
                    return True

    return False

def which(list):
    if ((list[4][2] < list[3][2] and list[3][2] < list[2][2]) and (list[5][1] < list[6][1] and
                                                                   list[9][1] < list[10][1] and list[13][1] < list[14][
                                                                       1] and list[17][1] < list[18][1]) and
            (list[25][2] < list[24][2] and list[24][2] < list[23][2]) and (list[26][1] > list[27][1] and
                                                                           list[30][1] > list[31][1] and list[34][1] >
                                                                           list[35][1] and list[38][1] > list[39][1])):
        if (list[8][1] < list[6][1] and list[12][1] < list[10][1] and list[16][1] < list[14][1] and list[20][1] <
            list[18][1]) and (
                list[29][1] > list[27][1] and list[33][1] > list[31][1] and list[37][1] > list[35][1] and list[41][1] >
                list[39][1]):
            return True

    return False

def stop(list, hand_type):
    if abs(list[8][2] - list[6][2]) > 50:
        if hand_type == 'Right':
            if list[4][1] > list[5][1]:
                cnt = 0
                for i in range(0, 5):
                    if (list[fingertip[i]][2] < list[fingertip[i] - 2][2]):
                        cnt = cnt + 1
                if cnt == 5:
                    len = math.hypot(list[4][1] - list[8][1], list[4][2] - list[8][2])
                    if len > 100:
                        return True

        elif hand_type == 'Left':
            if list[4][1] < list[5][1]:
                cnt = 0
                for i in range(0, 5):
                    if (list[fingertip[i]][2] < list[fingertip[i] - 2][2]):
                        cnt = cnt + 1
                if cnt == 5:
                    len = math.hypot(list[4][1] - list[8][1], list[4][2] - list[8][2])
                    if len > 100:
                        return True

    return False

def love_you(list):
    if abs(list[8][2] - list[6][2]) > 50:
        if (list[4][2] < list[2][2] and list[8][2] < list[6][2] and list[20][2] < list[18][2]):
            if (list[12][2] > list[10][2] and list[16][2] > list[14][2]):
                return True

    return False

def okay(list):
    if (list[12][2] < list[9][2] and list[16][2] < list[13][2] and list[20][2] < list[17][2]):
        len = math.hypot(list[4][1] - list[8][1], list[4][2] - list[8][2])
        if len < 60:
            return True

    return False

def no(list):
    if (list[16][2] > list[14][2] and list[20][2] > list[18][2] and abs(list[6][2] - list[7][2]) < 20):
        len1 = math.hypot(list[4][1] - list[8][1], list[4][2] - list[8][2])
        len2 = math.hypot(list[4][1] - list[12][1], list[4][2] - list[12][2])
        len3 = math.hypot(list[5][1] - list[6][1], list[5][2] - list[6][2])
        len4 = math.hypot(list[9][1] - list[10][1], list[9][2] - list[10][2])
        if len1 < 60 and len2 < 60 and len3 < 20 and len4 < 20:
            return True

    return False

def bathroom(list, hand_type):
    if list[4][2] < list[6][2]:
        len1 = math.hypot(list[4][1] - list[10][1], list[4][2] - list[10][2])
        len2 = math.hypot(list[4][1] - list[6][1], list[4][2] - list[6][2])
        if len1 < 50 and len2 < 50:
            if hand_type == 'Right':
                if (list[8][2] > list[6][2] and list[12][2] > list[10][2] and list[16][2] > list[14][2] and list[20][2] >
                        list[18][2]):
                    if (list[4][1] < list[6][1]):
                        return True

            elif hand_type == 'Left':
                if (list[8][2] > list[6][2] and list[12][2] > list[10][2] and list[16][2] > list[14][2] and list[20][2] >
                        list[18][2]):
                    if (list[4][1] > list[6][1]):
                        return True
    return False

def yes(list):
    if (list[2][2] > list[5][2] and list[5][2] < list[6][2] and list[9][2] < list[10][2] and list[13][2] < list[14][2]
            and list[17][2] < list[18][2] and list[8][2] < list[12][2] and list[12][2] < list[10][2]):
        len1 = math.hypot(list[10][1] - list[0][1], list[10][2] - list[0][2])
        len2 = math.hypot(list[4][1] - list[6][1], list[4][2] - list[6][2])
        if len1 < 100 and len2 < 60:
            return True
    return False

def house(list):
    len1 = math.hypot(list[4][1] - list[25][1], list[4][2] - list[25][2])
    len2 = math.hypot(list[8][1] - list[29][1], list[8][2] - list[29][2])
    len3 = math.hypot(list[12][1] - list[33][1], list[12][2] - list[33][2])
    len4 = math.hypot(list[16][1] - list[37][1], list[16][2] - list[37][2])
    len5 = math.hypot(list[20][1] - list[41][1], list[20][2] - list[41][2])
    len6 = math.hypot(list[0][1] - list[21][1], list[0][2] - list[21][2])

    if len1 > 30 and len2 < 20 and len3 < 20 and len4 < 20 and len5 < 50 and len6 > 50:
        return True

    return False

def angry(list):
    if (list[3][1] < list[19][1] and list[24][1] > list[40][1]):
        len1 = math.hypot(list[8][1] - list[6][1], list[8][2] - list[6][2])
        len2 = math.hypot(list[12][1] - list[10][1], list[12][2] - list[10][2])
        len3 = math.hypot(list[16][1] - list[14][1], list[16][2] - list[14][2])
        len4 = math.hypot(list[20][1] - list[18][1], list[20][2] - list[18][2])
        len5 = math.hypot(list[29][1] - list[27][1], list[29][2] - list[27][2])
        len6 = math.hypot(list[33][1] - list[31][1], list[33][2] - list[31][2])
        len7 = math.hypot(list[37][1] - list[35][1], list[37][2] - list[35][2])
        len8 = math.hypot(list[41][1] - list[39][1], list[41][2] - list[39][2])
        len9 = math.hypot(list[4][1] - list[5][1], list[4][2] - list[5][2])
        len10 = math.hypot(list[25][1] - list[26][1], list[25][2] - list[26][2])
        if len1 < 40 and len2 < 40 and len3 < 40 and len4 < 40 and len5 < 40 and len6 < 40 and len7 < 40 and len8 < 40 and len9 < 60 and len10 < 60:
            return True
    return False

def cry(list):
    if (list[12][2] > list[10][2] and list[16][2] > list[14][2] and list[20][2] > list[18][2] and list[33][2] >
            list[31][2] and list[37][2] > list[35][2] and list[41][2] > list[39][2]):
        if (list[3][1] < list[19][1] and list[24][1] > list[40][1]):
            len1 = math.hypot(list[8][1] - list[47][1], list[8][2] - list[47][2])
            len2 = math.hypot(list[29][1] - list[44][1], list[29][2] - list[44][2])
            len3 = math.hypot(list[4][1] - list[10][1], list[4][2] - list[10][2])
            len4 = math.hypot(list[25][1] - list[31][1], list[25][2] - list[31][2])
            if len1 < 30 and len2 < 30 and len3 < 40 and len4 < 40:
                return True
    return False

def again(list, hand_type):
    if(hand_type == 'Right'):
        if abs(list[21][2] - list[25][2]) < 30 and abs(list[21][2] - list[29][2]) < 30 and abs(list[21][2] - list[33][2]) < 30 and abs(list[21][2] - list[37][2]) < 30 and abs(list[21][2] - list[41][2] < 30):
            len = math.hypot(list[30][1] - list[12][1], list[30][2] - list[12][2])
            if len < 50:
                if list[5][2] < list[7][2] and list[9][2] < list[11][2] and list[13][2] < list[15][2] and list[17][2] < list[19][2]:
                    return True
    elif(hand_type == 'Left'):
        if abs(list[0][2] - list[4][2]) < 30 and abs(list[0][2] - list[8][2]) < 30 and abs(list[0][2] - list[12][2]) < 30 and abs(list[0][2] - list[16][2]) < 30 and abs(list[0][2] - list[20][2] < 30):
            len = math.hypot(list[9][1] - list[33][1], list[9][2] - list[33][2])
            if len < 50:
                if list[26][2] < list[28][2] and list[30][2] < list[32][2] and list[34][2] < list[36][2] and list[38][2] < list[40][2]:
                    return True
    return False

def sad(list):
    if (list[3][1] < list[19][1] and list[24][1] > list[40][1]):
        len1 = math.hypot(list[8][1] - list[6][1], list[8][2] - list[6][2])
        len2 = math.hypot(list[12][1] - list[10][1], list[12][2] - list[10][2])
        len3 = math.hypot(list[16][1] - list[14][1], list[16][2] - list[14][2])
        len4 = math.hypot(list[20][1] - list[18][1], list[20][2] - list[18][2])
        len5 = math.hypot(list[29][1] - list[27][1], list[29][2] - list[27][2])
        len6 = math.hypot(list[33][1] - list[31][1], list[33][2] - list[31][2])
        len7 = math.hypot(list[37][1] - list[35][1], list[37][2] - list[35][2])
        len8 = math.hypot(list[41][1] - list[39][1], list[41][2] - list[39][2])
        if len1 > 30 and len2 > 30 and len3 > 30 and len4 > 30 and len5 > 30 and len6 > 30 and len7 > 30 and len8 > 30:
            if (list[4][2] < list[2][2] and list[8][2] < list[6][2] and list[12][2] < list[10][2] and list[16][2] <
                    list[14][2] and list[20][2] < list[18][2] and
                    list[25][2] < list[23][2] and list[29][2] < list[27][2] and list[33][2] < list[31][2] and list[37][
                        2] < list[35][2] and list[41][2] < list[39][2]):
                return True

    return False

# I noticed Cc was being called in the original but not defined, adding a stub
def Cc(list):
    return False

# I noticed Dd was being called in the original but not defined, adding a stub
def Dd(list):
    return False

# I noticed Ee was being called in the original but not defined, adding a stub
def Ee(list, hand_type):
    return False

# I noticed Ff was being called in the original but not defined, adding a stub
def Ff(list):
    return False

@app.route('/detect', methods=['POST'])
def detect_sign():
    try:
        # Get the image from the request
        if 'image' not in request.files:
            return jsonify({"error": "No image provided"}), 400
        
        # Read the image
        file = request.files['image']
        image_data = file.read()
        
        # Convert to OpenCV format
        nparr = np.frombuffer(image_data, np.uint8)
        frame = cv.imdecode(nparr, cv.IMREAD_COLOR)
        
        if frame is None:
            return jsonify({"error": "Could not decode image"}), 400
        
        # Process the frame similar to the main loop in your original code
        img = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        results = holistic.process(img)
        
        list = []
        detected_sign = "No sign detected"
        
        # Process right and left hands if both are detected
        if results.right_hand_landmarks and results.left_hand_landmarks:
            # Extract landmarks for right hand
            for id, lm in enumerate(results.right_hand_landmarks.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                list.append([id, cx, cy])
            
            # Extract landmarks for left hand
            for id, lm in enumerate(results.left_hand_landmarks.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                list.append([id + 21, cx, cy])
            
            # Extract pose landmarks if available
            if results.pose_landmarks:
                for id, lm in enumerate(results.pose_landmarks.landmark):
                    h, w, c = frame.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    list.append([id + 42, cx, cy])
            
            # Check for two-hand signs
            if which(list):
                detected_sign = "Which?"
            elif house(list):
                detected_sign = "House"
            elif angry(list):
                detected_sign = "Angry"
            elif cry(list):
                detected_sign = "Cry"
            elif sad(list):
                detected_sign = "Sad"
            elif list[9][2] < list[25][2] and again(list, 'Right'):
                detected_sign = "Again"
            elif list[9][2] > list[25][2] and again(list, 'Left'):
                detected_sign = "Again"
            
        # Process single hand
        elif results.right_hand_landmarks or results.left_hand_landmarks:
            if results.right_hand_landmarks:
                hand_type = 'Right'
                # Extract landmarks for right hand
                for id, lm in enumerate(results.right_hand_landmarks.landmark):
                    h, w, c = frame.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    list.append([id, cx, cy])
            
            elif results.left_hand_landmarks:
                hand_type = 'Left'
                # Extract landmarks for left hand
                for id, lm in enumerate(results.left_hand_landmarks.landmark):
                    h, w, c = frame.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    list.append([id, cx, cy])
            
            # Check for single-hand signs
            if love_you(list):
                detected_sign = "I love you"
            elif no(list):
                detected_sign = "No"
            elif yes(list):
                detected_sign = "Yes"
            elif Cc(list):
                detected_sign = "C"
            elif Dd(list):
                detected_sign = "D"
            elif Ff(list):
                detected_sign = "F"
            elif hand_type == 'Right':
                if bathroom(list, 'Right'):
                    detected_sign = "Bathroom"
                elif stop(list, 'Right'):
                    detected_sign = "Stop"
                elif Aa(list, 'Right'):
                    detected_sign = "A"
                elif Bb(list, 'Right'):
                    detected_sign = "B"
                elif Ee(list, 'Right'):
                    detected_sign = "E"
                elif Yy(list, 'Right'):
                    detected_sign = "Y"
            elif hand_type == 'Left':
                if bathroom(list, 'Left'):
                    detected_sign = "Bathroom"
                elif stop(list, 'Left'):
                    detected_sign = "Stop"
                elif Aa(list, 'Left'):
                    detected_sign = "A"
                elif Bb(list, 'Left'):
                    detected_sign = "B"
                elif Ee(list, 'Left'):
                    detected_sign = "E"
                elif Yy(list, 'Left'):
                    detected_sign = "Y"
        
        return jsonify({"sign": detected_sign})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
