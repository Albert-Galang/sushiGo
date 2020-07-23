import os
import time

from numpy import *
import win32api
import win32con
from PIL import ImageGrab, ImageOps

x_pad1 = 392
y_pad1 = 298

x_pad2 = 1028
y_pad2 = 778

play_coordinates = (314, 203)

continue_coordinates = (310, 384)

skip_coordinates = (580, 450)

goal_coordinates = (319, 374)

# TODO: Organize the methods into other files, this is a mess.


def screen_grab():
    box = (x_pad1, y_pad1, x_pad2, y_pad2)
    im = ImageGrab.grab(box)
    im.show()
    return im


def left_click_down():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    print('LMB DOWN')


def left_click_up():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(.1)
    print('LMB UP')


def left_click():
    left_click_down()
    left_click_up()


def mouse_position(cord):
    win32api.SetCursorPos((x_pad1 + cord[0], y_pad1 + cord[1]))


def get_coordinates():
    x, y = win32api.GetCursorPos()
    x = x - x_pad1
    y = y - y_pad1

    print(x, y)
    return x, y


def start_game():
    # Press play
    mouse_position(play_coordinates)
    left_click()
    time.sleep(.1)

    # Press continue
    mouse_position(continue_coordinates)
    left_click()
    time.sleep(.1)

    # Press skip
    mouse_position(skip_coordinates)
    left_click()
    time.sleep(.1)

    # Press continue on the goal screen
    mouse_position(goal_coordinates)
    left_click()
    time.sleep(.1)


class Coordinates:
    f_shrimp = (35, 330)
    f_rice = (95, 330)
    f_nori = (35, 395)
    f_roe = (95, 395)
    f_salmon = (35, 445)
    f_unagi = (95, 445)

    mat = (245, 381)
    phone = (579, 381)
    menu_toppings = (533, 273)

    t_shrimp = (488, 222)
    t_nori = (498, 267)
    t_roe = (575, 277)
    t_salmon = (490, 333)
    t_unagi = (573, 225)

    menu_rice = (544, 297)
    buy_rice = (544, 297)

    delivery_norm = (493, 293)

    plate_1 = (91, 211)
    plate_2 = (194, 211)
    plate_3 = (296, 211)
    plate_4 = (397, 211)
    plate_5 = (499, 211)
    plate_6 = (600, 211)


def clear_tables():
    # TODO: Maybe replace with a for loop of plate coordinates (looks cleaner, although no idea if its more efficient)
    mouse_position(Coordinates.plate_1)
    left_click()

    mouse_position(Coordinates.plate_2)
    left_click()

    mouse_position(Coordinates.plate_3)
    left_click()

    mouse_position(Coordinates.plate_4)
    left_click()

    mouse_position(Coordinates.plate_5)
    left_click()

    mouse_position(Coordinates.plate_6)
    left_click()

    time.sleep(2)


def make_caliroll():
    print('Making Caliroll')
    mouse_position(Coordinates.f_rice)
    left_click()
    time.sleep(.05)
    mouse_position(Coordinates.f_nori)
    left_click()
    time.sleep(.05)
    mouse_position(Coordinates.f_roe)
    left_click()
    time.sleep(.05)
    mouse_position(Coordinates.mat)
    left_click()
    time.sleep(2)


def make_onigiri():
    print('Making Onigiri')
    mouse_position(Coordinates.f_rice)
    left_click()
    time.sleep(.05)
    mouse_position(Coordinates.f_rice)
    left_click()
    time.sleep(.05)
    mouse_position(Coordinates.f_nori)
    left_click()
    time.sleep(.05)
    mouse_position(Coordinates.mat)
    left_click()
    time.sleep(2)


def make_gunkan():
    print('Making Gunkan')
    mouse_position(Coordinates.f_rice)
    left_click()
    time.sleep(.05)
    mouse_position(Coordinates.f_nori)
    left_click()
    time.sleep(.05)
    mouse_position(Coordinates.f_roe)
    left_click()
    time.sleep(.05)
    mouse_position(Coordinates.f_roe)
    left_click()
    time.sleep(.05)
    mouse_position(Coordinates.mat)
    left_click()
    time.sleep(2)


def buy_food(food):

    mouse_position(Coordinates.phone)

    mouse_position(Coordinates.menu_toppings)

    mouse_position(Coordinates.t_shrimp)
    mouse_position(Coordinates.t_nori)
    mouse_position(Coordinates.t_roe)
    mouse_position(Coordinates.t_salmon)
    mouse_position(Coordinates.t_unagi)
    #mouse_position(Coordinates.t_exit)

    mouse_position(Coordinates.menu_rice)
    mouse_position(Coordinates.buy_rice)

    mouse_position(Coordinates.delivery_norm)


def main():
    pass


if __name__ == '__main__':
    main()


