#!/usr/bin/env python3
import os
import sys
import time

try:
    from PIL import Image
except ImportError:
    sys.exit("Cannot import from PIL: Do `pip3 install --user Pillow` to install")

import anki_vector
from anki_vector.util import degrees

def main():
    args = anki_vector.util.parse_command_args()




    with anki_vector.Robot(args.serial) as robot:
        # If necessary, move Vector's Head and Lift to make it easy to see his face

        # robot.say_text("Hello")

        robot.behavior.set_head_angle(degrees(45.0))
        robot.behavior.set_lift_height(0.0)

        current_directory = os.path.dirname(os.path.realpath(__file__))
        image_path = os.path.join(current_directory, "", "face_images", "cozmo_image.jpg")

        image_file = Image.open(image_path)

        screen_data = anki_vector.screen.convert_image_to_screen_data(image_file)
        robot.screen.set_screen_with_image_data(screen_data, 3.0)

        robot.say_text("Hello, Lead Tech, Here's the Dev Team.")





if __name__ == "__main__":
    main()