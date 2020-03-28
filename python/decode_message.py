import os

intro = """
MISSION
=============
You have found a secret message.
Puzzled, you quickly try to...

  _____                             _     _   _            __  __
 |  __ \                           | |   | | | |          |  \/  |
 | |  | | ___  ___ _ __ _   _ _ __ | |_  | |_| |__   ___  | \  / | ___  ___ ___  __ _  __ _  ___
 | |  | |/ _ \/ __| '__| | | | '_ \| __| | __| '_ \ / _ \ | |\/| |/ _ \/ __/ __|/ _` |/ _` |/ _ \
 | |__| |  __/ (__| |  | |_| | |_) | |_  | |_| | | |  __/ | |  | |  __/\__ \__ \ (_| | (_| |  __/
 |_____/ \___|\___|_|   \__, | .__/ \__|  \__|_| |_|\___| |_|  |_|\___||___/___/\__,_|\__, |\___|
                         __/ | |                                                       __/ |
                        |___/|_|                                                      |___/

"""
print(intro)

cypher = "qGBH71VNT03FC874IYI00BKEqjO0A19O6W07W6S327W158PqWRN91JVS30AV8854W004EGCqJ9648pX5W1i7W6B555Az11925HqX6m313T9E35Y0V67RCC05AXCqq5R7478Hc567HKW08T6GqAD2t4p8AL2u80X3S71W6Dq3L2287Z997C3F64KjLhYq2O2976J182W8U7323JqNFB18NMAa52FDP7343Bq"

message = ""

# Encrypt
for letter in cypher:
    if letter in "0123456789":
        message += " "

    elif letter == letter.upper():
        message += "#"

    elif letter == "q":
        message += "\n"

print(message)
