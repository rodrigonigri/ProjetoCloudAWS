def string2ascii(string):
    import pyfiglet
    font = "slant"
    result = pyfiglet.figlet_format(string, font=font)
    return result
