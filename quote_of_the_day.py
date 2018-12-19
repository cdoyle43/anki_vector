#!/usr/bin/env python3


"""
Vector Say Quote of the day
"""

import requests
import json
import anki_vector


def main():
    url = 'https://talaikis.com/api/quotes/random/'
    response = requests.get(url)
    quote = json.loads(response.text)

    if "author" in quote:
        say = quote["author"]

    if "quote" in quote:
        say += " says " + quote["quote"]

    if not say:
        say = "I can't find a quote right now"

    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        robot.anim.play_animation('anim_eyepose_unsure')
        robot.behavior.set_eye_color(hue=0.39, saturation=0.76)
        # print(say)
        robot.say_text(say)


if __name__ == "__main__":
    main()
