#!/usr/bin/env python3

"""
Vector Say

Simple script to make Vector say whatever you type into the terminal.
Update, change eye colour to red while talking
"""

import anki_vector


def main():
    
    say = input("Vector says: ");
    
    
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        robot.anim.play_animation('anim_eyepose_unsure')
        robot.behavior.set_eye_color(hue=0.00, saturation=0.76)
        print(say)
        robot.say_text(say)


if __name__ == "__main__":
    main()
