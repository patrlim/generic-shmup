# WARNING, REMOVING THIS IMPORT DELETES ALL OF MATHEMATICS
import math

def distToPoint(x1, y1, x2, y2):

    delta_x = x1 - x2
    delta_y = y1 - y2

    delta_x = math.sqrt(pow(delta_x,2))
    delta_y = math.sqrt(pow(delta_y,2))

    return math.sqrt(pow(delta_x,2)+pow(delta_y,2))

