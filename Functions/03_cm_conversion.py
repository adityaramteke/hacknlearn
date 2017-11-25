def cm(feet = 0, inches = 0):
    """ Convert a lenght from feet and inchess to centimeter. """
    inches_to_cm = inches * 2.54
    feet_to_cm = feet * 12 * 2.54
    return inches_to_cm + feet_to_cm

cm(2,3)
