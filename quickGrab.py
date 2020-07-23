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

ingredient_count = {'shrimp': 5,
                    'rice': 10,
                    'nori': 10,
                    'roe': 10,
                    'salmon': 5,
                    'unagi': 5}

sushi_sums = {3147: 'caliroll',
              2859: 'onigiri',
              2865: 'gunkan'}

empty_seat_sums = {1: 10325,
                   2: 11409,
                   3: 12148,
                   4: 12375,
                   5: 11724,
                   6: 10382}


# TODO: Organize the methods into other files, this is a mess.
# TODO: Write docstrings for each function


def screen_grab():
    """

    :return:
    """
    box = (x_pad1, y_pad1, x_pad2, y_pad2)
    im = ImageGrab.grab(box)
    # im.show()
    return im


def left_click_down():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    # print('LMB DOWN')


def left_click_up():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(.1)
    # print('LMB UP')


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
    t_exit = (588, 338)

    menu_rice = (544, 297)
    buy_rice = (544, 297)

    delivery_norm = (493, 293)

    plate_1 = (91, 211)
    plate_2 = (178, 208)
    plate_3 = (280, 201)
    plate_4 = (382, 203)
    plate_5 = (486, 208)
    plate_6 = (583, 211)


def clear_tables():
    # TODO: Maybe replace with a for loop of plate coordinates (looks cleaner, although no idea if its more efficient)
    mouse_position(Coordinates.plate_1)
    left_click()
    time.sleep(.2)

    mouse_position(Coordinates.plate_2)
    left_click()
    time.sleep(.2)

    mouse_position(Coordinates.plate_3)
    left_click()
    time.sleep(.2)

    mouse_position(Coordinates.plate_4)
    left_click()
    time.sleep(.3)

    mouse_position(Coordinates.plate_5)
    left_click()
    time.sleep(.4)

    mouse_position(Coordinates.plate_6)
    left_click()
    time.sleep(.5)


def make_food(food):
    if food == 'caliroll':
        make_caliroll()
    if food == 'onigiri':
        make_onigiri()
    if food == 'gunkan':
        make_gunkan()


def make_caliroll():
    print('Making Caliroll')
    ingredient_count['rice'] -= 1
    ingredient_count['nori'] -= 1
    ingredient_count['roe'] -= 1
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
    ingredient_count['rice'] -= 2
    ingredient_count['nori'] -= 1
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
    ingredient_count['rice'] -= 1
    ingredient_count['nori'] -= 1
    ingredient_count['roe'] -= 2
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
    current_colour = (0, 0, 0)
    original_colour = (0, 0, 0)
    coord = (0, 0)

    food_list = ('nori', 'roe', 'salmon', 'shrimp', 'unagi')
    if food in food_list:
        mouse_position(Coordinates.phone)
        time.sleep(.1)
        left_click()
        mouse_position(Coordinates.menu_toppings)
        time.sleep(.1)
        left_click()
        image = screen_grab()
        # Get coordinates of specified food and RGB colours to compare to
        if food == 'nori':
            coord = Coordinates.t_nori
            current_colour = image.getpixel(coord)
            original_colour = (109, 123, 127)
        elif food == 'roe':
            coord = Coordinates.t_roe
            current_colour = image.getpixel(coord)
            original_colour = (127, 61, 0)
        elif food == 'salmon':
            coord = Coordinates.t_salmon
            current_colour = image.getpixel(coord)
            original_colour = (127, 71, 47)
        elif food == 'shrimp':
            coord = Coordinates.t_shrimp
            current_colour = image.getpixel(coord)
            original_colour = (127, 127, 127)
        elif food == 'unagi':
            coord = Coordinates.t_unagi
            current_colour = image.getpixel(coord)
            original_colour = (94, 49, 8)

    elif food == 'rice':
        mouse_position(Coordinates.phone)
        time.sleep(.1)
        left_click()
        mouse_position(Coordinates.menu_rice)
        time.sleep(.1)
        left_click()
        image = screen_grab()

        coord = Coordinates.buy_rice
        current_colour = image.getpixel(coord)
        original_colour = (117, 117, 117)

    if current_colour != original_colour:
        print('Purchasing ', food)
        mouse_position(coord)
        left_click()
        time.sleep(.1)
        mouse_position(Coordinates.delivery_norm)
        left_click()
        if food == 'nori' or 'roe' or 'rice':
            ingredient_count[food] += 10
        else:
            ingredient_count[food] += 5
    else:
        print('Cannot purchase ', food)
        mouse_position(Coordinates.t_exit)
        left_click()


def check_food():
    for ingredient, count in ingredient_count.items():
        if count < 4:
            print('Attempting to buy ', ingredient)
            buy_food(ingredient)
    time.sleep(5)


def check_seat(seat):
    box = (0, 0, 0, 0)
    if seat == 1:
        box = (420, 353, 420 + 51, 353 + 28)
    if seat == 2:
        box = (521, 353, 521 + 51, 353 + 28)
    if seat == 3:
        box = (622, 353, 622 + 51, 353 + 28)
    if seat == 4:
        box = (723, 353, 723 + 51, 353 + 28)
    if seat == 5:
        box = (824, 353, 824 + 51, 353 + 28)
    if seat == 6:
        box = (925, 353, 925 + 51, 353 + 28)

    image = ImageOps.grayscale(ImageGrab.grab(box))
    # image.show()
    pixel_array = array(image.getcolors())
    pixel_array = pixel_array.sum()
    # print(pixel_array)
    return pixel_array


'''
nori (109, 123, 127)
roe (127, 61, 0)
salmon (127, 71, 47)
shrimp (127, 127, 127)
unagi (94, 49, 8)
rice (117, 117, 117)

bounding boxes
seat 1 = 420, 353 420+28, 353+51
seat 2 = 521, 353 521+28, 353+51
seat 3 = 622, 353 622+28, 353+51
seat 4 = 723, 353 723+28, 353+51
seat 5 = 824, 353 824+28, 353+51
seat 6 = 925, 353 925+28, 353+51

caliroll = 3147
onigiri = 2859
gunkan = 2865

empty seat 1 = 10325
empty seat 2 = 11409
empty seat 3 = 12148
empty seat 4 = 12375
empty seat 5 = 11724
empty seat 6 = 10382


'''


def sushi_go():
    check_food()
    for i in range(1, 7):
        seat_sum = check_seat(i)
        # If seat is not empty
        if seat_sum != empty_seat_sums.get(i):
            # If the array is in the sushi dictionary
            if seat_sum in sushi_sums:
                print('Seat', i, 'wants', sushi_sums[seat_sum])
                make_food(sushi_sums[seat_sum])
            else:
                print('Sushi type at seat', i, 'not found in dictionary')
    clear_tables()
    # Wait until orders reach the customer
    time.sleep(8)


def main():
    start_game()
    while True:
        sushi_go()


if __name__ == '__main__':
    main()
