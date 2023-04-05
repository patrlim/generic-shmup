# WARNING, REMOVING THIS IMPORT DELETES ALL OF MATHEMATICS
import math
import arcade

def distToPoint(x1, y1, x2, y2):

    delta_x = x1 - x2
    delta_y = y1 - y2

    delta_x = math.sqrt(pow(delta_x,2))
    delta_y = math.sqrt(pow(delta_y,2))

    return math.sqrt(pow(delta_x,2)+pow(delta_y,2))

def gfssf(fs,screenwidth):
    if fs:
        return arcade.get_display_size()[0] / screenwidth
    else:
        return 1

