#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from hermes_python.hermes import Hermes

INTENT_HOW_ARE_YOU = "e_rosinska:how_are_you"
INTENT_GOOD = "e_rosinska:feeling_good"
INTENT_MOODY = "e_rosinska:feeling_moody"

def main():
    with Hermes("localhost:1883") as h:
        h.subscribe_intent(INTENT_HOW_ARE_YOU, how_are_you_callback) \
         .start()


def how_are_you_callback(hermes, intent_message):
    session_id = intent_message.session_id
    response = "Amazing. What about you?"
    hermes.publish_end_session(session_id, response)

def feeling_good_callback(hermes, intent_message):
    session_id = intent_message.session_id
    response = "Good for you."
    hermes.publish_end_session(session_id, response)

def feeling_moody_callback(hermes, intent_message):
    session_id = intent_message.session_id
    response = "Want to get wasted?"
    hermes.publish_end_session(session_id, response)
if __name__ == "__main__":
    main()
