
COLOUR_TO_HEX = {"aquamarine1": "#7fffd4", "green1": "#00ff00", "magenta": "#ff00ff", "MediumSpringGreen": "#00fa9a",
                  "purple1": "#9b30ff", "red1": "#ff0000", "SeaGreen1": "#54ff9f", "SkyBlue1": "#87ceff",
                  "VioletRed1": "#ff3e96", "yellow1": "#ffff00", "gray63": "#a1a1a1"}

colour_name = input("Enter colour name: ")
while colour_name != "":
    if colour_name in COLOUR_TO_HEX:
        print("\n", colour_name, "in hex is", COLOUR_TO_HEX[colour_name])
    else:
        print("Invalid short state")
    colour = input("Enter short state: ")
