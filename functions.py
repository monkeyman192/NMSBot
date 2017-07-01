# get record info for a given level from speedrun.com

import requests
from math import floor
from random import randrange

def HextoNMS(hex_str):
    # convert the hex representation of a colour to NMS code
    R = "{:.6f}".format(int(hex_str[:2], 16)/255)
    G = "{:.6f}".format(int(hex_str[2:4], 16)/255)
    B = "{:.6f}".format(int(hex_str[4:6], 16)/255)
    return R, G, B

def NMStoRGB(R, G, B, *A):
    # convert the NMS format to RGBA format
    R_out, G_out, B_out = [round(255*x) for x in [R, G, B]]
    if A:
        out = "R = {0}, G = {1}, B = {2}, A = {3}\n".format(R_out, G_out, B_out, A[0])
    else:
        out = "R = {0}, G = {1}, B = {2}\n".format(R_out, G_out, B_out)
    out += RGBtoHex(R_out, G_out, B_out)
    return out

def RGBtoNMS(R, G, B, *A):
    R_out, G_out, B_out = ["{:.6f}".format(x/255) for x in [R, G, B]]
    if A:
        return "R = {0}, G = {1}, B = {2}, A = {3:.6f}".format(R_out, G_out, B_out, A[0])
    else:
        return "R = {0}, G = {1}, B = {2}, A = 1.000000".format(R_out, G_out, B_out)

def RGBtoHex(R, G, B):
    hex_string = "{0:02X}{1:02X}{2:02X}".format(R, G, B)
    return "https://www.webpagefx.com/web-design/color-picker/{}".format(hex_string)

def NMS_colour_struct(R, G, B, *A):
    out = '```xml\n<Property value="Colour.xml">\n'
    if A:
        A = A[0]
    else:
        A = '1.000000'
    out += '  <Property name="R" value="{}" />\n'.format(R)
    out += '  <Property name="G" value="{}" />\n'.format(G)
    out += '  <Property name="B" value="{}" />\n'.format(B)
    out += '  <Property name="A" value="{}" />\n'.format(A)
    out += '</Property>```'
    return out
        

if __name__ == "__main__":
    print(NMStoRGB(0.3, 0.2, 0.1, 0.5))
    print(RGBtoNMS(35, 122, 240, 1))
    print(RGBtoHex(212, 255, 12))
    print(HextoNMS('034282'))
