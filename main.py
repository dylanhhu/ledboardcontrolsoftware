import neopixel
import board
from random import randrange
from time import sleep

# definitions of functions
def rgb_to_grb_and_brightness(rgb, userbrightness):
    r, g, b = rgb
    ledpower = r * g * b  # 255 255 255 would be 16,581,375

    if ledpower >= 3375000:  # this is 150 150 150
        brightness = 0.3 * userbrightness
    else:
        brightness = 0.6 * userbrightness

    return (int(g * brightness), int(r * brightness), int(b * brightness))

settings_file = open("settings.txt", "rt")

brightness_value_ = settings_file.readline()
brightness_value_ = brightness_value_.replace("brightness = ", "")
brightness_value_ = brightness_value_.replace("\n", "")
brightness_value = float(brightness_value_)
brightness_value = brightness_value / 100

color1_ = settings_file.readline()
color2_ = settings_file.readline()
color3_ = settings_file.readline()

color1_ = color1_.replace("color1 = ", "")
color1_ = color1_.replace("\n", "")
color2_ = color2_.replace("color2 = ", "")
color2_ = color2_.replace("\n", "")
color3_ = color3_.replace("color3 = ", "")
color3_ = color3_.replace("\n", "")

color1 = int(color1_)
color2 = int(color2_)
color3 = int(color3_)

color_value = (color1, color2, color3)

mode_ = settings_file.readline()
mode_ = mode_.replace("mode = ", "")
mode_ = mode_.replace("\n", "")
mode = mode_

delay_ = settings_file.readline()
delay_ = delay_.replace("delayrainbow = ", "")
delay_ = delay_.replace("\n", "")
delay = int(delay_)

print(color_value)
print(brightness_value)
print(mode)
print(delay)

boardleds = neopixel.NeoPixel(board.D4, 117)

for x in range(0, 10):
    if mode == "rainbow":
        while True:
            for pixel in range(0, 117):
                boardleds[pixel] = (int(randrange(0, 255) * brightness_value), int(randrange(0, 255) * brightness_value), int(randrange(0, 255) * brightness_value))
            sleep(float(delay)/1000)
    elif mode == "setcolor":
        while True:
            for pixel in range(0, 117):
                boardleds[pixel] = rgb_to_grb_and_brightness(color_value, brightness_value)
    else:
        mode = "rainbow"
        