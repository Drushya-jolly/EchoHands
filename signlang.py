import cv2 as cv
import mediapipe as mp
import math

cap = cv.VideoCapture(0)

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic
holistic = mp_holistic.Holistic(min_detection_confidence=0.7)
fingertip = [4, 8, 12, 16, 20]

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


def Cc(list):
    cnt = 0
    for i in range(0, 5):
        if (abs(list[fingertip[i]][2] - list[fingertip[i] - 2][2]) < 40):
            cnt = cnt + 1
    if cnt == 5:
        len1 = math.hypot(list[4][1] - list[8][1], list[4][2] - list[8][2])
        len2 = math.hypot(list[4][1] - list[12][1], list[4][2] - list[12][2])
        len3 = math.hypot(list[4][1] - list[16][1], list[4][2] - list[16][2])
        len4 = math.hypot(list[4][1] - list[20][1], list[4][2] - list[20][2])
        if (len1 > 80 and len2 > 80 and len3 > 80 and len4 > 80):
            return True

    return False

def Dd(list):
    if(list[8][2] < list[6][2] and abs(list[8][2] - list[6][2]) > 40):
        len1 = math.hypot(list[4][1] - list[12][1], list[4][2] - list[12][2])
        len2 = math.hypot(list[4][1] - list[16][1], list[4][2] - list[16][2])
        len3 = math.hypot(list[4][1] - list[20][1], list[4][2] - list[20][2])
        if len1 < 30 and len2 < 30 and len3 < 30:
            return True

    return False

def Ee(list, hand_type):
    len1 = math.hypot(list[3][1] - list[8][1], list[3][2] - list[8][2])
    len2 = math.hypot(list[4][1] - list[12][1], list[4][2] - list[12][2])
    if len1 > 30 and len2 > 30 and list[12][2] < list[9][2]:
        if hand_type == 'Right':
            if list[3][1] > list[6][1]:
                if (list[8][2] > list[6][2] and list[12][2] > list[10][2] and list[16][2] > list[14][2] and list[20][2] > list[18][2]
                and list[4][1] > list[18][1]):
                    return True

        elif hand_type == 'Left':
            if list[3][1] < list[6][1]:
                if (list[8][2] > list[6][2] and list[12][2] > list[10][2] and list[16][2] > list[14][2] and list[20][2] > list[18][2]
                and list[4][1] < list[18][1]):
                    return True

    return False

def Ff(list):
    if (list[12][2] < list[9][2] and list[16][2] < list[13][2] and list[20][2] < list[17][2] and list[12][2] < list[10][2]):
        if abs(list[8][1] - list[5][1]) < 40:
            len1 = math.hypot(list[4][1] - list[8][1], list[4][2] - list[8][2])
            len2 = math.hypot(list[4][1] - list[12][1], list[4][2] - list[12][2])
            if len1 < 60 and len2 > 50:
                return True

    return False

def Gg(list, hand_type):
    if (abs(list[4][2] - list[6][2]) < 50):
        if (hand_type == 'Right'):
            if list[8][1] > list[5][1]:
                if (list[12][1] < list[10][1] and list[16][1] < list[14][1] and list[20][1] < list[18][1] and list[6][2] < list[10][2]):
                    return True

        elif (hand_type == 'Left'):
            if list[8][1] < list[5][1]:
                if (list[12][1] > list[10][1] and list[16][1] > list[14][1] and list[20][1] > list[18][1] and list[6][2] < list[10][2]):
                    return True
    return False

def Hh(list, hand_type):
    if(list[4][2] > list[6][2] and list[4][2] < list[14][2]):
        if (hand_type == 'Right'):
            if list[8][1] > list[5][1] and list[12][1] > list[9][1]:
                if (list[16][1] < list[14][1] and list[20][1] < list[18][1] and list[10][2] < list[14][2]):
                    return True

        elif (hand_type == 'Left'):
           if list[8][1] < list[5][1]:
               if (list[16][1] > list[14][1] and list[20][1] > list[18][1] and list[10][2] < list[14][2]):
                    return True

    return False

def Ii(list, hand_type):
    len = math.hypot(list[4][1] - list[17][1], list[4][2] - list[17][2])
    if list[9][2] > list[10][2] and len < 100:
        if(hand_type == 'Right'):
            if list[4][1] > list[18][1]:
                if(list[20][2] < list[18][2]):
                    if(list[4][2] < list[2][2] and list[5][2] < list[8][2] and list[9][2] < list[12][2] and list[13][2] < list[16][2]):
                        return True

        elif(hand_type == 'Left'):
            if list[4][1] < list[18][1]:
                if (list[20][2] < list[18][2]):
                    if (list[4][2] < list[2][2] and list[5][2] < list[8][2] and list[9][2] < list[12][2] and list[13][2] < list[16][2]):
                        return True

    return False

def Jj(list, hand_type):
    len = math.hypot(list[4][1] - list[6][1], list[4][2] - list[6][2])
    if len < 50:
        if (hand_type == 'Right'):
            if list[4][1] < list[20][1] and abs(list[10][2] - list[20][2]) < 50:
                if (list[20][2] < list[18][2]):
                    if (list[4][2] < list[2][2] and list[5][2] < list[8][2] and list[9][2] < list[12][2] and list[13][2] <
                            list[16][2]):
                        return True

        elif (hand_type == 'Left'):
            if list[4][1] > list[20][1] and abs(list[10][2] - list[20][2]) < 50:
                if (list[20][2] < list[18][2]):
                    if (list[4][2] < list[2][2] and list[5][2] < list[8][2] and list[9][2] < list[12][2] and list[13][2] <
                            list[16][2]):
                        return True

    return False

def Kk(list, hand_type):
    len = math.hypot(list[4][1] - list[10][1], list[4][2] - list[10][2])
    if len < 50 and list[8][2] < list[12][2] and abs(list[8][1] - list[12][1]) < 50 and list[8][2] < list[6][2] and list[12][2] < list[10][2] and list[14][2] < list[16][2] and list[18][2] < list[20][2]:
        if (hand_type == 'Right'):
            if (list[4][1] > list[20][1]):
                return True

        elif (hand_type == 'Left'):
            if (list[4][1] < list[20][1]):
                return True

    return False

def Ll(list, hand_type):
    if abs(list[4][2] - list[2][2]) < 50 and abs(list[8][1] - list[5][1]) < 50 and list[8][2] < list[6][2] and abs(list[4][1] - list[10][1] > 50) and abs(list[9][2] - list[10][2]) < 20:
        if (hand_type == 'Right'):
            if (list[4][1] > list[20][1] and list[9][2] < list[12][2] and list[13][2] < list[16][2] and list[17][2] < list[20][2]):
                return True

        elif (hand_type == 'Left'):
            if (list[4][1] < list[20][1] and list[9][2] < list[12][2] and list[13][2] < list[16][2] and list[17][2] < list[20][2]):
                return True

    return False

def Mm(list, hand_type):
    if list[4][2] < list[18][2] and abs(list[4][2] - list[6][2]) < 50:
        len1 = math.hypot(list[4][1] - list[18][1], list[4][2] - list[18][2])
        len2 = math.hypot(list[4][1] - list[14][1], list[4][2] - list[14][2])
        if len1 < 40 and len2 < 60:
            if hand_type == 'Right':
                if (list[8][2] > list[6][2] and list[12][2] > list[10][2] and list[16][2] > list[14][2] and list[20][2] >
                        list[18][2]):
                    if (list[4][1] < list[14][1]):
                        return True

            elif hand_type == 'Left':
                if (list[8][2] > list[6][2] and list[12][2] > list[10][2] and list[16][2] > list[14][2] and list[20][2] >
                        list[18][2]):
                    if (list[4][1] > list[14][1]):
                        return True

    return False

def Nn(list, hand_type):
    if list[4][2] < list[14][2] and abs(list[4][2] - list[10][2]) < 50:
        len1 = math.hypot(list[4][1] - list[14][1], list[4][2] - list[14][2])
        len2 = math.hypot(list[4][1] - list[10][1], list[4][2] - list[10][2])
        if len1 < 40 and len2 < 60:
            if hand_type == 'Right':
                if (list[8][2] > list[6][2] and list[12][2] > list[10][2] and list[16][2] > list[14][2] and list[20][2] >
                        list[18][2]):
                    if (list[4][1] < list[10][1]):
                        return True

            elif hand_type == 'Left':
                if (list[8][2] > list[6][2] and list[12][2] > list[10][2] and list[16][2] > list[14][2] and list[20][2] >
                        list[18][2]):
                    if (list[4][1] > list[10][1]):
                        return True

    return False

def Oo(list, hand_type):
    len1 = math.hypot(list[4][1] - list[8][1], list[4][2] - list[8][2])
    len2 = math.hypot(list[4][1] - list[12][1], list[4][2] - list[12][2])
    len3 = math.hypot(list[4][1] - list[16][1], list[4][2] - list[16][2])
    len4 = math.hypot(list[4][1] - list[7][1], list[4][2] - list[7][2])
    len5 = math.hypot(list[4][1] - list[11][1], list[4][2] - list[11][2])
    len6 = math.hypot(list[4][1] - list[15][1], list[4][2] - list[15][2])
    if (len1 < 60 and len2 < 40 and len3 < 60 and abs(list[4][1] - list[3][1]) < 30
            and abs(list[8][2] - list[12][2]) < 30 and abs(list[12][2] - list[16][2] < 30) and abs(list[16][2] - list[20][2] < 30)
            and len4 > 20 and len5 > 20 and len6 > 20):
        if hand_type == 'Right':
            if list[4][1] > list[20][1]:
                return True

        elif hand_type == 'Left':
            if list[4][1] < list[20][1]:
                return True

    return False

def Pp(list, hand_type):
    len = math.hypot(list[4][1] - list[10][1], list[4][2] - list[10][2])
    if (len < 60 and list[8][2] < list[12][2] and abs(list[8][1] - list[12][1]) < 60 and abs(list[8][2] - list[6][2]) < 40 and
    list[10][2] < list[12][2] and list[14][2] < list[16][2] and list[18][2] < list[20][2] and abs(list[9][2] - list[10][2]) > 30):
        if (hand_type == 'Right'):
            if (list[4][1] > list[20][1]):
                return True

        elif (hand_type == 'Left'):
            if (list[4][1] < list[20][1]):
                return True

    return False

def Qq(list, hand_type):
    if(list[4][1] < list[2][1] and list[8][1] < list[5][1]):
        if (hand_type == 'Right'):
            if list[8][1] < list[5][1]:
                if (list[12][1] > list[10][1] and list[16][1] > list[14][1] and list[20][1] > list[18][1] and list[6][1] < list[10][1]):
                    return True

        elif (hand_type == 'Left'):
            if list[8][1] > list[5][1]:
                if (list[12][1] < list[10][1] and list[16][1] < list[14][1] and list[20][1] < list[18][1] and list[6][1] > list[10][1]):
                    return True

    return False


def Rr(list,hand_type):
    if(list[2][1] > list[18][1]):
        if(hand_type == 'Right'):
            if (abs(list[6][2] - list[10][2]) < 30 and abs(list[7][2] - list[11][2]) < 30 and list[8][2] < list[5][2] and list[12][2] < list[9][2] and list[12][1] > list[8][1]):
                if (list[4][2] < list[2][2] and list[16][2] > list[14][2] and list[20][2] > list[18][1]):
                    return True

    if (list[2][1] < list[18][1]):
        if (hand_type == 'Left'):
            if (abs(list[6][2] - list[10][2]) < 30 and abs(list[7][2] - list[11][2]) < 30 and list[8][2] < list[5][2] and list[12][2] < list[9][2] and list[12][1] < list[8][1]):
                if (list[4][2] < list[2][2] and list[16][2] > list[14][2] and list[20][2] > list[18][1]):
                    return True

    return False

def Ss(list, hand_type):
    len = math.hypot(list[4][1] - list[15][1], list[4][2] - list[15][2])
    if list[9][2] > list[10][2] and len < 30:
        if(hand_type == 'Right'):
            if list[4][1] > list[18][1]:
                if(list[20][2] > list[18][2]):
                    if(list[4][2] < list[2][2] and list[5][2] < list[8][2] and list[9][2] < list[12][2] and list[13][2] < list[16][2]):
                        return True

        elif(hand_type == 'Left'):
            if list[4][1] < list[18][1]:
                if (list[20][2] > list[18][2]):
                    if (list[4][2] < list[2][2] and list[5][2] < list[8][2] and list[9][2] < list[12][2] and list[13][2] < list[16][2]):
                        return True

    return False

def Uu(list, hand_type):
    len = math.hypot(list[8][1] - list[12][1], list[8][2] - list[12][2])
    if(list[8][2] < list[6][2] and list[12][2] < list[10][2] and abs(list[4][2] - list[14][2]) < 50 and len < 50):
        if (hand_type == 'Right'):
            if(list[2][1] > list[18][1]):
                if(list[16][2] > list[14][2] and list[20][2] > list[18][2]):
                    return True

        elif (hand_type == 'Left'):
            if(list[2][1] < list[18][1]):
                if(list[16][2] > list[14][2] and list[20][2] > list[18][2]):
                    return True
    return False

def Vv(list, hand_type):
    len = math.hypot(list[8][1] - list[12][1], list[8][2] - list[12][2])
    if(list[8][2] < list[6][2] and list[12][2] < list[10][2] and abs(list[4][2] - list[14][2]) < 50 and len > 100):
        if (hand_type == 'Right'):
            if(list[2][1] > list[18][1]):
                if(list[16][2] > list[14][2] and list[20][2] > list[18][2]):
                    return True

        elif (hand_type == 'Left'):
            if(list[2][1] < list[18][1]):
                if(list[16][2] > list[14][2] and list[20][2] > list[18][2]):
                    return True
    return False

def Ww(list, hand_type):
    len1 = math.hypot(list[8][1] - list[12][1], list[8][2] - list[12][2])
    len2 = math.hypot(list[12][1] - list[16][1], list[12][2] - list[16][2])
    if(list[8][2] < list[6][2] and list[12][2] < list[10][2] and abs(list[4][2] - list[19][2]) < 30 and len1 > 50 and len2 > 50):
        if (hand_type == 'Right'):
            if(list[5][1] > list[18][1]):
                return True

        elif (hand_type == 'Left'):
            if(list[5][1] < list[18][1]):
                return True

    return False

def Xx(list, hand_type):
    if(list[8][2] > list[6][2] and list[6][2] < list[5][2] and abs(list[4][2] - list[14][2]) < 50 and abs(list[8][2] - list[7][2]) < 40):
        if (hand_type == 'Right'):
            if(list[2][1] > list[18][1]):
                if(list[12][2] > list[10][2] and list[16][2] > list[14][2] and list[20][2] > list[18][2]):
                    return True

        elif (hand_type == 'Left'):
            if(list[2][1] < list[18][1]):
                if(list[12][2] > list[10][2] and list[16][2] > list[14][2] and list[20][2] > list[18][2]):
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
        #if(abs(list[2][2] - list[4][2]) < 30):
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


def again(list,hand_type):
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


while cap.isOpened():
    ret, frame = cap.read()
    img = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    results = holistic.process(img)

    list = []

    if results.right_hand_landmarks and results.left_hand_landmarks:
        mp_drawing.draw_landmarks(frame, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
        mp_drawing.draw_landmarks(frame, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
        for id, lm in enumerate(results.right_hand_landmarks.landmark):
            h, w, c = frame.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            list.append([id, cx, cy])

        for id, lm in enumerate(results.left_hand_landmarks.landmark):
            h, w, c = frame.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            list.append([id + 21, cx, cy])

        if results.pose_landmarks:
            mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)
            for id, lm in enumerate(results.pose_landmarks.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                list.append([id + 42, cx, cy])

        if which(list):
            # print("Which?")
            cv.putText(frame, "Which?", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

        elif house(list):
            # print("House")
            cv.putText(frame, "!House!", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

        elif angry(list):
            # print("!!Angry!!")
            cv.putText(frame, "!!Angry!!", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

        elif cry(list):
            # print("Cry")
            cv.putText(frame, "!!Cry!!", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

        elif sad(list):
            # print("Sad")
            cv.putText(frame, "!!Sad!!", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

        elif list[9][2] < list[25][2]:
            if again(list, 'Right'):
                # print("Again")
                cv.putText(frame, "Again!!", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

        elif list[9][2] > list[25][2]:
            if again(list, 'Left'):
                # print("Again")
                cv.putText(frame, "Again!!", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

    elif results.right_hand_landmarks or results.left_hand_landmarks:
        if results.right_hand_landmarks:
            cnt = 1
            mp_drawing.draw_landmarks(frame, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
            for id, lm in enumerate(results.right_hand_landmarks.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                list.append([id, cx, cy])

        elif results.left_hand_landmarks:
            cnt = 2
            mp_drawing.draw_landmarks(frame, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
            for id, lm in enumerate(results.left_hand_landmarks.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                list.append([id, cx, cy])

        if love_you(list):
            # print("I love you")
            cv.putText(frame, "I love you!", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

        # elif okay(list):
        #     # print("Okay")
        #     cv.putText(frame, "Okay!", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

        elif no(list):
            # print("No!")
            cv.putText(frame, "No!", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

        elif yes(list):
            # print("Yes!")
            cv.putText(frame, "Yes!", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)


        elif Cc(list):
            # print("Cc")
            cv.putText(frame, "Cc", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

        elif Dd(list):
            # print("Dd")
            cv.putText(frame, "Dd", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

        elif Ff(list):
            cv.putText(frame, "Ff", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

        elif cnt == 1:

            if bathroom(list, 'Right'):
                # print("Bathroom")
                cv.putText(frame, "Bathroom...", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)
                cv.putText(frame, "Tt", (500, 400), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

            elif stop(list, 'Right'):
                # print("Stop!")
                cv.putText(frame, "Stop!", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

            elif Aa(list, 'Right'):
                # print("Aa")
                cv.putText(frame, "Aa", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

            elif Bb(list, 'Right'):
                # print("Bb")
                cv.putText(frame, "Bb", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

            elif Ee(list, 'Right'):
                # print("Ee")
                cv.putText(frame, "Ee", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

            elif Gg(list, 'Right'):
                # print("Gg")
                cv.putText(frame, "Gg", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

            elif Hh(list, 'Right'):
                # print("Hh")
                cv.putText(frame, "Hh", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

            elif Ii(list, 'Right'):
                # print("Ii")
                cv.putText(frame, "Ii", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

            elif Jj(list, 'Right'):
                # print("Jj")
                cv.putText(frame, "Jj", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

            elif Kk(list, 'Right'):
                # print("Kk")
                cv.putText(frame, "Kk", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

            elif Ll(list, 'Right'):
                # print("Ll")
                cv.putText(frame, "Ll", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

            elif Mm(list, 'Right'):
                # print("Ll")
                cv.putText(frame, "Mm", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

            elif Nn(list, 'Right'):
                # print("Ll")
                cv.putText(frame, "Nn", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

            elif Oo(list, 'Right'):
                # print("Ll")
                cv.putText(frame, "Oo", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

            elif Pp(list, 'Right'):
                # print("Pp")
                cv.putText(frame, "Pp", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

            elif Qq(list, 'Right'):
                # print("Pp")
                cv.putText(frame, "Qq", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

            elif Rr(list, 'Right'):
                # print("Pp")
                cv.putText(frame, "Rr", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

            elif Ss(list, 'Right'):
                # print("Pp")
                cv.putText(frame, "Ss", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

            elif Uu(list, 'Right'):
                # print("Pp")
                cv.putText(frame, "Uu", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

            elif Vv(list, 'Right'):
                # print("Pp")
                cv.putText(frame, "Vv", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

            elif Ww(list, 'Right'):
                # print("Pp")
                cv.putText(frame, "Ww", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

            elif Xx(list, 'Right'):
                # print("Pp")
                cv.putText(frame, "Xx", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

            elif Yy(list, 'Right'):
                # print("Pp")
                cv.putText(frame, "Yy", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

        elif cnt == 2:

            if bathroom(list, 'Left'):
                # print("Bathroom")
                cv.putText(frame, "Bathroom...", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)
                cv.putText(frame, "Tt", (500, 400), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

            elif stop(list, 'Left'):
                # print("Stop!")
                cv.putText(frame, "Stop!", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

            elif Aa(list, 'Left'):
                # print("Aa")
                cv.putText(frame, "Aa", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

            elif Bb(list, 'Left'):
                # print("Bb")
                cv.putText(frame, "Bb", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

            elif Ee(list, 'Left'):
                # print("Ee")
                cv.putText(frame, "Ee", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

            elif Gg(list, 'Left'):
                # print("Gg")
                cv.putText(frame, "Gg", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

            elif Hh(list, 'Left'):
                # print("Hh")
                cv.putText(frame, "Hh", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

            elif Ii(list, 'Left'):
                # print("Ii")
                cv.putText(frame, "Ii", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

            elif Jj(list, 'Left'):
                # print("Jj")
                cv.putText(frame, "Jj", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

            elif Kk(list, 'Left'):
                # print("Kk")
                cv.putText(frame, "Kk", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

            elif Ll(list, 'Left'):
                # print("Ll")
                cv.putText(frame, "Ll", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

            elif Mm(list, 'Left'):
                # print("Ll")
                cv.putText(frame, "Mm", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

            elif Nn(list, 'Left'):
                # print("Ll")
                cv.putText(frame, "Nn", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

            elif Oo(list, 'Left'):
                # print("Ll")
                cv.putText(frame, "Oo", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

            elif Pp(list, 'Left'):
                # print("Pp")
                cv.putText(frame, "Pp", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

            elif Qq(list, 'Left'):
                # print("Pp")
                cv.putText(frame, "Qq", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

            elif Rr(list, 'Left'):
                # print("Pp")
                cv.putText(frame, "Rr", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

            elif Ss(list, 'Left'):
                # print("Pp")
                cv.putText(frame, "Ss", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

            elif Uu(list, 'Left'):
                # print("Pp")
                cv.putText(frame, "Uu", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

            elif Vv(list, 'Left'):
                # print("Pp")
                cv.putText(frame, "Vv", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

            elif Ww(list, 'Left'):
                # print("Pp")
                cv.putText(frame, "Ww", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

            elif Xx(list, 'Left'):
                # print("Pp")
                cv.putText(frame, "Xx", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

            elif Yy(list, 'Left'):
                # print("Pp")
                cv.putText(frame, "Yy", (80, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 6)

    cv.imshow('frame', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
