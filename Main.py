import ctypes
import json as jsond
import time
import binascii
import colorama
import pyautogui
import pydirectinput
import requests
from uuid import uuid4
import webbrowser
import platform
import subprocess
import datetime
import sys
import os
import os.path
import platform
import psutil
import requests
import threading
import socket
from termcolor import colored

colorama.init()


ctypes.windll.kernel32.SetConsoleTitleW("Warzone Auto Camo - Made by Flex#8888")
print("\n")

print('{:^127s}'.format(colored("_____ _     _______  __  _____ ___   ___  _     ____", 'red')))
print('{:^127s}'.format(colored("|  ___| |   | ____\ \/ / |_   _/ _ \ / _ \| |   / ___|", 'red')))
print('{:^127s}'.format(colored(" | |_  | |   |  _|  \  /    | || | | | | | | |   \___ \ ", 'red')))
print('{:^127s}'.format(colored(" |  _| | |___| |___ /  \    | || |_| | |_| | |___ ___) |", 'red')))
print('{:^127s}'.format(colored("|_|   |_____|_____/_/\_\   |_| \___/ \___/|_____|____/", 'red')))
print('{:^127s}'.format(colored("", 'cyan')))
print('{:^127s}'.format(colored("", 'cyan')))

print("\n")
print(colored('Welcome to Flex Tools (v1.0.0)!', 'red'))

print('{:^50s}'.format(colored("    #Follow the tutorial carefully before starting the program for the first time. ", 'white')))
print('{:^34s}'.format(colored("shorturl.at/hjC35", 'blue')))
print('{:^50s}'.format(colored("    #For technical support or other issues, please make a ticket on Discord. ", 'white')))
print('{:^47s}'.format(colored("https://discord.gg/kXFqzb6cFm", 'blue')))
print("\n")





costom_name = ("1")
print('\n')


def scroll_down():  # scroll down to camos
    pyautogui.scroll(-30)

    pyautogui.scroll(-30)

    pyautogui.scroll(-30)

    pyautogui.scroll(-30)

    pyautogui.scroll(-30)

    pyautogui.scroll(-30)


def camos():
    pydirectinput.click(x=521, y=200, )

    pydirectinput.click(x=417, y=1165, )

    scroll_down()

    pydirectinput.click(x=368, y=1198, )  # CAMO BEG

    pydirectinput.click(x=897, y=1156, )  # DAMSCUS

    pydirectinput.press('esc')  # Esc

    pydirectinput.press('esc')  # Esc

    pydirectinput.click(x=638, y=1344, )  # click save

    pydirectinput.click(x=1267, y=1014, )  # ENTER NAME

    pydirectinput.click(x=684, y=642, )  # ENTER NAME BLANK CLICK

    pydirectinput.click(x=670, y=646, )  # CLICK BLANK TEXT
    pydirectinput.write(costom_name)

    pydirectinput.click(x=1278, y=699, )  # ENTER NAME / OK

    pydirectinput.click(x=1269, y=1070, )  # save mod
    time.sleep(0.5)
    pydirectinput.press('esc')  # Esc

    pydirectinput.click(x=517, y=189, )  # CUSTOMIZE

    pydirectinput.click(x=455, y=1165, )  # click camouflage

    scroll_down()

    pydirectinput.click(x=385, y=1199, )  # click completiomist

    pydirectinput.click(x=1083, y=1160, )  # OBSIDISN

    pydirectinput.press('esc')  # Esc

    pydirectinput.press('esc')  # Esc

    pydirectinput.click(x=638, y=1350, )  # SAVE COSTOM MOD

    pydirectinput.click(x=1268, y=1124, )  # CREATE NEW MOD

    pydirectinput.press('esc')  # Esc

    pydirectinput.click(x=455, y=1165, )  # click camouflage

    scroll_down()

    pydirectinput.click(x=792, y=1177, )  # click Mastery

    pydirectinput.click(x=514, y=1145, )  # daimoned

    pydirectinput.press('esc')  # Esc

    pydirectinput.press('esc')  # Esc

    pydirectinput.click(x=638, y=1350, )  # SAVE COSTOM MOD

    pydirectinput.click(x=1268, y=1124, )  # CREATE NEW MOD

    pydirectinput.press('esc')  # Esc

    pydirectinput.click(x=455, y=1165, )

    scroll_down()

    pydirectinput.click(x=792, y=1177, )  # click Mastery

    pydirectinput.click(x=717, y=1155, )  # click dark matter

    pydirectinput.press('esc')  # Esc

    pydirectinput.press('esc')  # Esc

    pydirectinput.click(x=638, y=1350, )  # SAVE COSTOM MOD

    pydirectinput.click(x=1268, y=1124, )  # CREATE NEW MOD


def camos2():
    pydirectinput.click(x=521, y=200, )

    pydirectinput.click(x=417, y=1165, )

    scroll_down()

    pydirectinput.click(x=383, y=1194, )  # complet

    pydirectinput.click(x=519, y=1161, )  # gold

    pydirectinput.press('esc')  # Esc

    pydirectinput.press('esc')  # Esc

    pydirectinput.click(x=638, y=1344, )  # click save

    pydirectinput.click(x=1267, y=1014, )  # ENTER NAME

    pydirectinput.click(x=684, y=642, )  # ENTER NAME BLANK CLICK

    pydirectinput.click(x=670, y=646, )  # CLICK BLANK TEXT
    pydirectinput.write(costom_name)

    pydirectinput.click(x=1278, y=699, )  # ENTER NAME / OK

    pydirectinput.click(x=1269, y=1070, )  # save mod
    time.sleep(0.5)
    pydirectinput.press('esc')  # Esc

    pydirectinput.click(x=517, y=189, )  # CUSTOMIZE

    pydirectinput.click(x=455, y=1165, )  # click camouflage

    scroll_down()

    pydirectinput.click(x=375, y=1197, )  # complte

    pydirectinput.click(x=708, y=1162, )  # platinum

    pydirectinput.press('esc')  # Esc

    pydirectinput.press('esc')  # Esc

    pydirectinput.click(x=638, y=1350, )  # SAVE COSTOM MOD

    pydirectinput.click(x=1268, y=1124, )  # CREATE NEW MOD

    pydirectinput.press('esc')  # Esc

    pydirectinput.click(x=455, y=1165, )  # click camouflage

    scroll_down()

    pydirectinput.click(x=377, y=1197, )  # comlpte

    pydirectinput.click(x=896, y=1162, )  # damscus

    pydirectinput.press('esc')  # Esc

    pydirectinput.press('esc')  # Esc

    pydirectinput.click(x=638, y=1350, )  # SAVE COSTOM MOD

    pydirectinput.click(x=1268, y=1124, )  # CREATE NEW MOD

    pydirectinput.press('esc')  # Esc

    pydirectinput.click(x=455, y=1165, )

    scroll_down()

    pydirectinput.click(x=343, y=1197, )  # complte

    pydirectinput.click(x=1077, y=1158, )  # obsidian

    pydirectinput.press('esc')  # Esc

    pydirectinput.press('esc')  # Esc

    pydirectinput.click(x=638, y=1350, )  # SAVE COSTOM MOD

    pydirectinput.click(x=1268, y=1124, )  # CREATE NEW MOD


def camos3():
    pydirectinput.click(x=521, y=200, )

    pydirectinput.click(x=417, y=1165, )

    scroll_down()

    pydirectinput.click(x=368, y=1198, )  # CAMO BEG

    pydirectinput.click(x=897, y=1156, )  # DAMSCUS

    pydirectinput.press('esc')  # Esc

    pydirectinput.press('esc')  # Esc

    pydirectinput.click(x=638, y=1344, )  # click save

    pydirectinput.click(x=1267, y=1014, )  # ENTER NAME

    pydirectinput.click(x=684, y=642, )  # ENTER NAME BLANK CLICK

    pydirectinput.click(x=670, y=646, )  # CLICK BLANK TEXT
    pydirectinput.write(costom_name)

    pydirectinput.click(x=1278, y=699, )  # ENTER NAME / OK

    pydirectinput.click(x=1269, y=1070, )  # save mod
    time.sleep(0.5)
    pydirectinput.press('esc')  # Esc

    pydirectinput.click(x=517, y=189, )  # CUSTOMIZE

    pydirectinput.click(x=455, y=1165, )  # click camouflage

    scroll_down()

    pydirectinput.click(x=744, y=1189, )  # click mastery

    pydirectinput.click(x=523, y=1158, )  # daimond

    pydirectinput.press('esc')  # Esc

    pydirectinput.press('esc')  # Esc

    pydirectinput.click(x=638, y=1350, )  # SAVE COSTOM MOD

    pydirectinput.click(x=1268, y=1124, )  # CREATE NEW MOD

    pydirectinput.press('esc')  # Esc

    pydirectinput.click(x=455, y=1165, )  # click camouflage

    scroll_down()

    pydirectinput.click(x=792, y=1177, )  # click Mastery

    pydirectinput.click(x=711, y=1158, )  # dm ultra

    pydirectinput.press('esc')  # Esc

    pydirectinput.press('esc')  # Esc

    pydirectinput.click(x=638, y=1350, )  # SAVE COSTOM MOD

    pydirectinput.click(x=1268, y=1124, )  # CREATE NEW MOD

    pydirectinput.press('esc')  # Esc

    pydirectinput.click(x=455, y=1165, )

    scroll_down()

    pydirectinput.click(x=1144, y=1180, )  # click special

    pydirectinput.click(x=522, y=1156, )  # hot and cold

    pydirectinput.press('esc')  # Esc

    pydirectinput.press('esc')  # Esc

    pydirectinput.click(x=638, y=1350, )  # SAVE COSTOM MOD

    pydirectinput.click(x=1268, y=1124, )  # CREATE NEW MOD


def camos4():
    pydirectinput.click(x=521, y=200, )

    pydirectinput.click(x=417, y=1165, )

    scroll_down()

    pydirectinput.click(x=368, y=1198, )  # CAMO BEG

    pydirectinput.click(x=1077, y=1163, )  # ob camo

    pydirectinput.press('esc')  # Esc

    pydirectinput.press('esc')  # Esc

    pydirectinput.click(x=638, y=1344, )  # click save

    pydirectinput.click(x=1267, y=1014, )  # ENTER NAME

    pydirectinput.click(x=684, y=642, )  # ENTER NAME BLANK CLICK

    pydirectinput.click(x=670, y=646, )  # CLICK BLANK TEXT
    pydirectinput.write(costom_name)

    pydirectinput.click(x=1278, y=699, )  # ENTER NAME / OK

    pydirectinput.click(x=1269, y=1070, )  # save mod
    time.sleep(0.5)
    pydirectinput.press('esc')  # Esc

    pydirectinput.click(x=517, y=189, )  # CUSTOMIZE

    pydirectinput.click(x=455, y=1165, )  # click camouflage

    scroll_down()

    pydirectinput.click(x=1165, y=1191, )  # click special

    pydirectinput.click(x=520, y=1156, )  # hot and cold

    pydirectinput.press('esc')  # Esc

    pydirectinput.press('esc')  # Esc

    pydirectinput.click(x=638, y=1350, )  # SAVE COSTOM MOD

    pydirectinput.click(x=1268, y=1124, )  # CREATE NEW MOD

    pydirectinput.press('esc')  # Esc

    pydirectinput.click(x=455, y=1165, )  # click camouflage

    scroll_down()

    pydirectinput.click(x=1140, y=1184, )  # click specail

    pydirectinput.click(x=708, y=1169, )  # rainbow

    pydirectinput.press('esc')  # Esc

    pydirectinput.press('esc')  # Esc

    pydirectinput.click(x=638, y=1350, )  # SAVE COSTOM MOD

    pydirectinput.click(x=1268, y=1124, )  # CREATE NEW MOD

    pydirectinput.press('esc')  # Esc

    pydirectinput.click(x=455, y=1165, )

    scroll_down()

    pydirectinput.click(x=1144, y=1180, )  # click special

    pydirectinput.click(x=885, y=1166, )  # banded

    pydirectinput.press('esc')  # Esc

    pydirectinput.press('esc')  # Esc

    pydirectinput.click(x=638, y=1350, )  # SAVE COSTOM MOD

    pydirectinput.click(x=1268, y=1124, )  # CREATE NEW MOD


def scroll_gun():
    pydirectinput.tripleClick(x=1215, y=738, )

    pyautogui.scroll(-30)

    pyautogui.scroll(-30)

    pyautogui.scroll(-30)

    pyautogui.scroll(-30)

    pyautogui.scroll(-30)

    pyautogui.scroll(-30)

    pyautogui.scroll(-30)


def ESC():
    time.sleep(0.5)
    pydirectinput.press('esc')  # Esc
    time.sleep(0.8)
    pydirectinput.press('esc')  # Esc
    time.sleep(0.8)
    pydirectinput.click(x=431, y=353, )


def esc_scroll():
    pydirectinput.press('esc')  # Esc
    time.sleep(0.8)
    pydirectinput.press('esc')  # Esc
    time.sleep(0.8)
    pydirectinput.click(x=431, y=353, )

    scroll_gun()


def switch_tab():
    pydirectinput.press('esc')  # Esc
    time.sleep(0.8)
    pydirectinput.press('esc')  # Esc
    time.sleep(0.8)
    pydirectinput.click(x=431, y=353, )  # CLICK GUN
    time.sleep(0.5)
    pydirectinput.click(x=527, y=190, )  # CHANGES TABS TO OHTER GUNS CHANGE THIS FOR ALL


def switch_tab_shotgun():
    pydirectinput.press('esc')  # Esc
    time.sleep(0.8)
    pydirectinput.press('esc')  # Esc
    time.sleep(0.8)
    pydirectinput.click(x=431, y=353, )  # CLICK GUN
    time.sleep(0.5)
    pydirectinput.click(x=723, y=188, )  # CHANGES TABS TO OHTER GUNS CHANGE THIS FOR ALL


def switch_tab_LMG():
    pydirectinput.press('esc')  # Esc
    time.sleep(0.8)
    pydirectinput.press('esc')  # Esc
    time.sleep(0.8)
    pydirectinput.click(x=431, y=353, )  # CLICK GUN
    time.sleep(0.5)
    pydirectinput.click(x=913, y=189, )  # CHANGES TABS TO OHTER GUNS CHANGE THIS FOR ALL


def switch_tab_marksman():
    pydirectinput.press('esc')  # Esc
    time.sleep(0.8)
    pydirectinput.press('esc')  # Esc
    time.sleep(0.8)
    pydirectinput.click(x=431, y=353, )  # CLICK GUN
    time.sleep(0.5)
    pydirectinput.click(x=1311, y=186, )  # CHANGES TABS TO OHTER GUNS CHANGE THIS FOR ALL


def switch_tab_sniper():
    pydirectinput.press('esc')  # Esc
    time.sleep(0.8)
    pydirectinput.press('esc')  # Esc
    time.sleep(0.8)
    pydirectinput.click(x=431, y=353, )  # CLICK GUN
    time.sleep(0.5)
    pydirectinput.click(x=1518, y=188, )  # CHANGES TABS TO OHTER GUNS CHANGE THIS FOR ALL


def switch_to_pistol():
    pydirectinput.press('esc')
    time.sleep(1.3)
    pydirectinput.press('esc')

    pydirectinput.click(x=457, y=611, )

    pydirectinput.click(x=453, y=405, )


def ESC_pistol():
    pydirectinput.press('esc')  # Esc
    time.sleep(0.8)
    pydirectinput.press('esc')  # Esc
    time.sleep(0.8)
    pydirectinput.click(x=420, y=597, )


def ESC_pistol_SCROLL():
    pydirectinput.press('esc')  # Esc
    time.sleep(0.8)
    pydirectinput.press('esc')  # Esc
    time.sleep(0.8)
    pydirectinput.click(x=420, y=597, )

    scroll_gun()


# --- DAMASCUCS-OBSIDIAN-DMULTRA-DAIMOND---#
def camo_1():
    pyautogui.alert('Press "OK" To Being')

    pydirectinput.tripleClick(x=1655, y=587, )

    pydirectinput.click(x=409, y=269, )  # kilo

    # pydirectinput.click(x=777, y=312,)

    pydirectinput.click(x=291, y=366, )

    pydirectinput.click(x=384, y=794, )

    pydirectinput.click(x=779, y=335, )

    pydirectinput.click(x=413, y=372, )

    pydirectinput.click(x=1247, y=300, )

    pydirectinput.click(x=440, y=454, )

    pydirectinput.click(x=1356, y=1119, )

    pydirectinput.click(x=442, y=370, )

    pydirectinput.click(x=936, y=1086, )

    pydirectinput.click(x=418, y=278, )  # kilo end

    camos()

    ESC()  # exit kilo

    time.sleep(0.4)  # fal
    pydirectinput.click(x=501, y=620, )
    time.sleep(.05)
    pydirectinput.click(x=786, y=332, )

    pydirectinput.click(x=334, y=364, )

    pydirectinput.click(x=420, y=706, )

    pydirectinput.click(x=807, y=335, )

    pydirectinput.click(x=420, y=366, )

    pydirectinput.click(x=1270, y=301, )

    pydirectinput.click(x=397, y=454, )

    pydirectinput.click(x=1363, y=1125, )

    pydirectinput.click(x=411, y=364, )

    pydirectinput.click(x=956, y=1088, )

    pydirectinput.click(x=391, y=282, )  # FAL END

    camos()

    ESC()

    pydirectinput.click(x=477, y=841, )  # M4

    pydirectinput.click(x=776, y=310, )  # GUNSSMITH

    pydirectinput.click(x=319, y=366, )

    pydirectinput.click(x=406, y=793, )

    pydirectinput.click(x=799, y=339, )

    pydirectinput.click(x=408, y=541, )

    pydirectinput.click(x=1258, y=299, )

    pydirectinput.click(x=445, y=446, )

    pydirectinput.click(x=1373, y=1121, )

    pydirectinput.click(x=446, y=373, )

    pydirectinput.click(x=960, y=1086, )

    pydirectinput.click(x=421, y=285, )

    camos()

    ESC()

    pydirectinput.click(x=513, y=1076, )  # FR 5.56

    pydirectinput.click(x=783, y=315, )  # GUNSMITH

    pydirectinput.click(x=323, y=370, )

    pydirectinput.click(x=418, y=707, )

    pydirectinput.click(x=802, y=336, )

    pydirectinput.click(x=431, y=371, )

    pydirectinput.click(x=1234, y=292, )

    pydirectinput.click(x=414, y=452, )

    pydirectinput.click(x=1344, y=1124, )

    pydirectinput.click(x=403, y=376, )

    pydirectinput.click(x=964, y=1090, )

    pydirectinput.click(x=423, y=283, )  # FR 5.56 END

    camos()

    esc_scroll()

    pydirectinput.click(x=491, y=1054, )  # ODEN

    pydirectinput.click(x=781, y=327, )  # GUNSMITH

    pydirectinput.click(x=322, y=371, )

    pydirectinput.click(x=410, y=538, )

    pydirectinput.click(x=800, y=340, )

    pydirectinput.click(x=423, y=287, )

    pydirectinput.click(x=1266, y=292, )

    pydirectinput.click(x=418, y=455, )

    pydirectinput.click(x=1379, y=1121, )

    pydirectinput.click(x=412, y=373, )

    pydirectinput.click(x=962, y=1089, )

    pydirectinput.click(x=423, y=288, )

    camos()

    esc_scroll()

    pydirectinput.click(x=470, y=1068, )  # m13

    pydirectinput.click(x=773, y=309, )  # GUNSMITH

    pydirectinput.click(x=332, y=362, )

    pydirectinput.click(x=410, y=786, )

    pydirectinput.click(x=807, y=335, )

    pydirectinput.click(x=418, y=455, )

    pydirectinput.click(x=1258, y=300, )

    pydirectinput.click(x=411, y=376, )

    pydirectinput.click(x=1349, y=1124, )

    pydirectinput.click(x=429, y=450, )

    pydirectinput.click(x=965, y=1083, )

    pydirectinput.click(x=424, y=450, )

    camos()

    esc_scroll()

    pydirectinput.click(x=486, y=1066, )  # FN SCAR

    pydirectinput.click(x=777, y=314, )  # GUNSMITH

    pydirectinput.click(x=335, y=365, )

    pydirectinput.click(x=415, y=785, )

    pydirectinput.click(x=816, y=336, )

    pydirectinput.click(x=416, y=368, )

    pydirectinput.click(x=1223, y=300, )

    pydirectinput.click(x=434, y=452, )

    pydirectinput.click(x=1374, y=1123, )

    pydirectinput.click(x=411, y=373, )

    pydirectinput.click(x=975, y=1087, )

    pydirectinput.click(x=425, y=285, )

    camos()

    esc_scroll()

    pydirectinput.click(x=472, y=1042, )  # AK 47

    pydirectinput.click(x=773, y=322, )  # GUNSMITH

    pydirectinput.click(x=305, y=366, )

    pydirectinput.click(x=398, y=793, )

    pydirectinput.click(x=794, y=332, )

    pydirectinput.click(x=417, y=540, )

    pydirectinput.click(x=1357, y=1125, )

    pydirectinput.click(x=413, y=455, )

    pydirectinput.click(x=2159, y=363, )

    pydirectinput.click(x=370, y=456, )

    pydirectinput.click(x=1264, y=291, )

    pydirectinput.click(x=416, y=377, )

    camos()

    esc_scroll()

    pydirectinput.click(x=469, y=1070, )  # RAM-7

    pydirectinput.click(x=775, y=321, )  # GUNSMITH

    pydirectinput.click(x=337, y=368, )

    pydirectinput.click(x=394, y=784, )

    pydirectinput.click(x=778, y=335, )

    pydirectinput.click(x=397, y=454, )

    pydirectinput.click(x=1260, y=301, )

    pydirectinput.click(x=397, y=450, )

    pydirectinput.click(x=1364, y=1125, )

    pydirectinput.click(x=403, y=292, )

    pydirectinput.click(x=969, y=1089, )

    pydirectinput.click(x=399, y=282, )

    camos()

    esc_scroll()

    pydirectinput.click(x=462, y=1071, )  # GRAU

    pydirectinput.click(x=778, y=318, )  # GUNSMITH

    pydirectinput.click(x=338, y=360, )

    pydirectinput.click(x=399, y=789, )

    pydirectinput.click(x=799, y=339, )

    pydirectinput.click(x=408, y=377, )

    pydirectinput.click(x=1245, y=298, )

    pydirectinput.click(x=421, y=463, )

    pydirectinput.click(x=984, y=1085, )

    pydirectinput.click(x=422, y=281, )

    pydirectinput.click(x=1352, y=1125, )

    pydirectinput.click(x=397, y=369, )

    camos()

    esc_scroll()

    pydirectinput.click(x=458, y=1067, )  # AMAX

    pydirectinput.click(x=777, y=307, )  # GUNSMITH

    pydirectinput.click(x=333, y=360, )

    pydirectinput.click(x=391, y=704, )

    pydirectinput.click(x=786, y=335, )

    pydirectinput.click(x=416, y=369, )

    pydirectinput.click(x=1211, y=297, )

    pydirectinput.click(x=406, y=445, )

    pydirectinput.click(x=1353, y=1129, )

    pydirectinput.click(x=398, y=285, )

    pydirectinput.click(x=1003, y=1084, )

    pydirectinput.click(x=407, y=291, )

    camos()

    esc_scroll()

    pydirectinput.click(x=474, y=1064, )  # AN-94

    pydirectinput.click(x=779, y=319, )  # GUNSMITH

    pydirectinput.click(x=282, y=369, )

    pydirectinput.click(x=394, y=709, )

    pydirectinput.click(x=770, y=334, )

    pydirectinput.click(x=383, y=373, )

    pydirectinput.click(x=1261, y=305, )

    pydirectinput.click(x=405, y=459, )

    pydirectinput.click(x=1356, y=1129, )

    pydirectinput.click(x=395, y=367, )

    pydirectinput.click(x=974, y=1083, )

    pydirectinput.click(x=393, y=290, )

    camos()

    esc_scroll()

    pydirectinput.click(x=476, y=1068, )  # AS-VAL

    pydirectinput.click(x=774, y=324, )  # GUNSMITH

    pydirectinput.click(x=792, y=338, )

    pydirectinput.click(x=402, y=454, )

    pydirectinput.click(x=1274, y=303, )

    pydirectinput.click(x=393, y=461, )

    pydirectinput.click(x=965, y=1086, )

    pydirectinput.click(x=406, y=287, )

    pydirectinput.click(x=1341, y=1122, )

    pydirectinput.click(x=422, y=287, )

    pydirectinput.click(x=1748, y=1127, )

    pydirectinput.click(x=432, y=368, )

    camos()

    switch_tab()  # switch to SMG

    pydirectinput.click(x=480, y=407, )  # AUG SMG

    pydirectinput.click(x=779, y=318, )  # GUNSMITH

    pydirectinput.click(x=313, y=368, )

    pydirectinput.click(x=399, y=550, )

    pydirectinput.click(x=771, y=333, )

    pydirectinput.click(x=415, y=454, )

    pydirectinput.click(x=1252, y=302, )

    pydirectinput.click(x=404, y=373, )

    pydirectinput.click(x=1353, y=1128, )

    pydirectinput.click(x=430, y=455, )

    pydirectinput.click(x=959, y=1089, )

    pydirectinput.click(x=388, y=293, )

    camos()

    ESC()

    pydirectinput.click(x=498, y=611, )  # P90

    pydirectinput.click(x=780, y=306, )  # GUNSMITH

    pydirectinput.click(x=329, y=365, )

    pydirectinput.click(x=402, y=619, )

    pydirectinput.click(x=743, y=334, )

    pydirectinput.click(x=426, y=371, )

    pydirectinput.click(x=1252, y=298, )

    pydirectinput.click(x=403, y=370, )

    pydirectinput.click(x=1719, y=1124, )

    pydirectinput.click(x=409, y=286, )

    pydirectinput.click(x=913, y=1079, )

    pydirectinput.click(x=413, y=362, )

    camos()

    ESC()

    pydirectinput.click(x=461, y=852, )  # MP5 SMG

    pydirectinput.click(x=780, y=339, )  # GUNSMITH

    pydirectinput.click(x=730, y=336, )

    pydirectinput.click(x=410, y=366, )

    pydirectinput.click(x=2146, y=363, )

    pydirectinput.click(x=424, y=538, )

    pydirectinput.click(x=1364, y=1119, )

    pydirectinput.click(x=378, y=287, )

    pydirectinput.click(x=969, y=1091, )

    pydirectinput.click(x=413, y=373, )

    pydirectinput.click(x=2103, y=1083, )

    pydirectinput.click(x=405, y=703, )

    camos()

    ESC()

    pydirectinput.click(x=443, y=1046, )  # UZI

    pydirectinput.click(x=775, y=320, )  # GUNSMITH

    pydirectinput.click(x=322, y=369, )

    pydirectinput.click(x=434, y=624, )

    pydirectinput.click(x=799, y=328, )

    pydirectinput.click(x=382, y=533, )

    pydirectinput.click(x=1251, y=295, )

    pydirectinput.click(x=390, y=363, )

    pydirectinput.click(x=1339, y=1121, )

    pydirectinput.click(x=411, y=456, )

    pydirectinput.click(x=959, y=1084, )

    pydirectinput.click(x=410, y=285, )

    camos()

    esc_scroll()

    pydirectinput.click(x=454, y=1065, )  # PP19 BIZON

    pydirectinput.click(x=775, y=317, )  # GUNSMITH

    pydirectinput.click(x=312, y=365, )

    pydirectinput.click(x=408, y=791, )

    pydirectinput.click(x=757, y=335, )

    pydirectinput.click(x=407, y=370, )

    pydirectinput.click(x=1270, y=298, )

    pydirectinput.click(x=416, y=459, )

    pydirectinput.click(x=2135, y=366, )

    pydirectinput.click(x=424, y=369, )

    pydirectinput.click(x=1349, y=1122, )

    pydirectinput.click(x=419, y=287, )

    camos()

    esc_scroll()

    pydirectinput.click(x=461, y=1071, )  # MP7 SMG

    pydirectinput.click(x=781, y=314, )  # GUNSMITH

    pydirectinput.click(x=329, y=363, )

    pydirectinput.click(x=413, y=786, )

    pydirectinput.click(x=799, y=329, )

    pydirectinput.click(x=437, y=368, )

    pydirectinput.click(x=1262, y=298, )

    pydirectinput.click(x=391, y=373, )

    pydirectinput.click(x=1377, y=1121, )

    pydirectinput.click(x=401, y=371, )

    pydirectinput.click(x=959, y=1087, )

    pydirectinput.click(x=390, y=365, )

    camos()

    esc_scroll()

    pydirectinput.click(x=465, y=1068, )  # STRIKER 45 SMG

    pydirectinput.click(x=785, y=323, )  # GUNSMITH

    pydirectinput.click(x=332, y=361, )

    pydirectinput.click(x=403, y=791, )

    pydirectinput.click(x=797, y=335, )

    pydirectinput.click(x=404, y=368, )

    pydirectinput.click(x=1260, y=299, )

    pydirectinput.click(x=387, y=369, )

    pydirectinput.click(x=1390, y=1119, )

    pydirectinput.click(x=415, y=367, )

    pydirectinput.click(x=984, y=1085, )

    pydirectinput.click(x=378, y=372, )

    camos()

    esc_scroll()

    pydirectinput.click(x=475, y=1063, )  # FENNIC SMG

    pydirectinput.click(x=782, y=326, )  # GUNSMITH

    pydirectinput.click(x=764, y=334, )

    pydirectinput.click(x=415, y=367, )

    pydirectinput.click(x=1252, y=299, )

    pydirectinput.click(x=411, y=371, )

    pydirectinput.click(x=1370, y=1122, )

    pydirectinput.click(x=404, y=286, )

    pydirectinput.click(x=2172, y=1085, )

    pydirectinput.click(x=393, y=875, )

    pydirectinput.click(x=972, y=1090, )

    pydirectinput.click(x=389, y=284, )

    camos()

    esc_scroll()

    pydirectinput.click(x=471, y=1062, )  # ISO SMG

    pydirectinput.click(x=776, y=321, )  # GUNSMITH

    pydirectinput.click(x=803, y=334, )

    pydirectinput.click(x=416, y=538, )

    pydirectinput.click(x=1266, y=298, )

    pydirectinput.click(x=425, y=377, )

    pydirectinput.click(x=972, y=1083, )

    pydirectinput.click(x=392, y=377, )

    pydirectinput.click(x=1355, y=1120, )

    pydirectinput.click(x=404, y=375, )

    pydirectinput.click(x=2166, y=1082, )

    pydirectinput.click(x=385, y=875, )

    camos()

    esc_scroll()

    pydirectinput.click(x=471, y=1075, )  # sc9 smg

    pydirectinput.click(x=772, y=323, )  # GUNSMITH

    pydirectinput.click(x=746, y=336, )

    pydirectinput.click(x=436, y=622, )

    pydirectinput.click(x=1258, y=297, )

    pydirectinput.click(x=414, y=372, )

    pydirectinput.click(x=2129, y=362, )

    pydirectinput.click(x=423, y=451, )

    pydirectinput.click(x=2122, y=1082, )

    pydirectinput.click(x=379, y=708, )

    pydirectinput.click(x=1366, y=1126, )

    pydirectinput.click(x=411, y=454, )

    camos()

    switch_tab_shotgun()

    pydirectinput.click(x=470, y=408, )  # MODEL 680

    pydirectinput.click(x=776, y=322, )  # GUNDMITH

    pydirectinput.click(x=299, y=364, )

    pydirectinput.click(x=379, y=708, )

    pydirectinput.click(x=781, y=332, )

    pydirectinput.click(x=417, y=453, )

    pydirectinput.click(x=1225, y=295, )

    pydirectinput.click(x=379, y=367, )

    pydirectinput.click(x=2160, y=367, )

    pydirectinput.click(x=441, y=456, )

    pydirectinput.click(x=1301, y=1131, )

    pydirectinput.click(x=396, y=622, )

    camos()

    ESC()

    pydirectinput.click(x=486, y=629, )  # R90

    pydirectinput.click(x=777, y=328, )  # GUNSMITH

    pydirectinput.click(x=350, y=365, )

    pydirectinput.click(x=401, y=703, )

    pydirectinput.click(x=797, y=332, )

    pydirectinput.click(x=394, y=283, )

    pydirectinput.click(x=1210, y=297, )

    pydirectinput.click(x=376, y=371, )

    pydirectinput.click(x=1330, y=1123, )

    pydirectinput.click(x=407, y=458, )

    pydirectinput.click(x=1739, y=1126, )

    pydirectinput.click(x=404, y=455, )

    camos()

    ESC()

    pydirectinput.click(x=463, y=848, )  # 725

    pydirectinput.click(x=776, y=327, )  # GUNSMITH

    pydirectinput.click(x=348, y=363, )

    pydirectinput.click(x=394, y=789, )

    pydirectinput.click(x=761, y=334, )

    pydirectinput.click(x=408, y=365, )

    pydirectinput.click(x=1212, y=294, )

    pydirectinput.click(x=454, y=375, )

    pydirectinput.click(x=2143, y=363, )

    pydirectinput.click(x=383, y=455, )

    pydirectinput.click(x=1692, y=1123, )

    pydirectinput.click(x=414, y=284, )

    camos()

    ESC()

    pydirectinput.click(x=458, y=1077, )  # ORIGIN 12

    pydirectinput.click(x=776, y=323, )  # GUNSMITH

    pydirectinput.click(x=320, y=367, )

    pydirectinput.click(x=397, y=876, )

    pydirectinput.click(x=768, y=333, )

    pydirectinput.click(x=393, y=448, )

    pydirectinput.click(x=1266, y=301, )

    pydirectinput.click(x=378, y=369, )

    pydirectinput.click(x=1372, y=1127, )

    pydirectinput.click(x=403, y=458, )

    pydirectinput.click(x=1751, y=1126, )

    pydirectinput.click(x=419, y=456, )

    camos()

    esc_scroll()

    pydirectinput.click(x=436, y=1059, )  # VLK

    pydirectinput.click(x=777, y=324, )  # GUNSMITH

    pydirectinput.doubleClick(x=1336, y=671, )  # click screen

    pydirectinput.click(x=1708, y=1128, )  # not working

    pydirectinput.click(x=406, y=458, )  # NOT WORKING

    pydirectinput.click(x=795, y=335, )

    pydirectinput.click(x=420, y=458, )

    pydirectinput.click(x=1224, y=302, )

    pydirectinput.click(x=391, y=373, )

    pydirectinput.click(x=1311, y=1126, )

    pydirectinput.click(x=405, y=536, )

    pydirectinput.click(x=945, y=1088, )

    pydirectinput.click(x=351, y=288, )

    camos()

    esc_scroll()

    pydirectinput.click(x=457, y=1075, )  # JAK 12

    pydirectinput.click(x=776, y=307, )  # GUNSMITH

    pydirectinput.doubleClick(x=1336, y=671, )  # click screen

    pydirectinput.click(x=333, y=367, )

    pydirectinput.click(x=408, y=789, )

    pydirectinput.click(x=789, y=336, )

    pydirectinput.click(x=418, y=455, )

    pydirectinput.click(x=1261, y=301, )

    pydirectinput.click(x=401, y=374, )

    pydirectinput.click(x=1359, y=1120, )

    pydirectinput.click(x=397, y=456, )

    pydirectinput.click(x=956, y=1090, )

    pydirectinput.click(x=393, y=299, )

    camos()

    switch_tab_LMG()

    pydirectinput.click(x=476, y=408, )  # pkm

    pydirectinput.click(x=774, y=319, )  # gunsmith

    pydirectinput.click(x=322, y=363, )

    pydirectinput.click(x=402, y=371, )

    pydirectinput.click(x=749, y=333, )

    pydirectinput.click(x=384, y=365, )

    pydirectinput.click(x=1183, y=293, )

    pydirectinput.click(x=389, y=452, )

    pydirectinput.click(x=2178, y=362, )

    pydirectinput.click(x=398, y=454, )

    pydirectinput.click(x=962, y=1086, )

    pydirectinput.click(x=421, y=286, )

    camos()

    ESC()

    pydirectinput.click(x=475, y=640, )  # SA87

    pydirectinput.click(x=775, y=321, )  # GUNSMITH

    pydirectinput.click(x=302, y=365, )

    pydirectinput.click(x=398, y=785, )

    pydirectinput.click(x=795, y=338, )

    pydirectinput.click(x=413, y=366, )

    pydirectinput.click(x=1215, y=294, )

    pydirectinput.click(x=409, y=452, )

    pydirectinput.click(x=1356, y=1123, )

    pydirectinput.click(x=404, y=364, )

    pydirectinput.click(x=912, y=1088, )

    pydirectinput.click(x=390, y=282, )

    camos()

    ESC()

    pydirectinput.click(x=468, y=823, )  # M91

    pydirectinput.click(x=776, y=321, )  # GUNSMITH

    pydirectinput.click(x=309, y=364, )

    pydirectinput.click(x=416, y=789, )

    pydirectinput.click(x=753, y=335, )

    pydirectinput.click(x=408, y=457, )

    pydirectinput.click(x=1197, y=298, )

    pydirectinput.click(x=385, y=453, )

    pydirectinput.click(x=2128, y=361, )

    pydirectinput.click(x=417, y=535, )

    pydirectinput.click(x=954, y=1088, )

    pydirectinput.click(x=415, y=279, )

    camos()

    ESC()

    pydirectinput.click(x=465, y=1063, )  # MG34

    pydirectinput.click(x=777, y=324, )  # GUMSMITH

    pydirectinput.click(x=281, y=364, )

    pydirectinput.click(x=393, y=790, )

    pydirectinput.click(x=766, y=333, )

    pydirectinput.click(x=430, y=458, )

    pydirectinput.click(x=1246, y=296, )

    pydirectinput.click(x=388, y=366, )

    pydirectinput.click(x=1355, y=1122, )

    pydirectinput.click(x=428, y=285, )

    pydirectinput.click(x=932, y=1083, )

    pydirectinput.click(x=385, y=284, )

    camos()

    esc_scroll()

    pydirectinput.click(x=451, y=1056, )  # HOLGER

    pydirectinput.click(x=778, y=317, )  # GUNSMITH

    pydirectinput.click(x=305, y=359, )

    pydirectinput.click(x=400, y=783, )

    pydirectinput.click(x=743, y=337, )

    pydirectinput.click(x=391, y=284, )

    pydirectinput.click(x=1197, y=295, )

    pydirectinput.click(x=385, y=456, )

    pydirectinput.click(x=1361, y=1126, )

    pydirectinput.click(x=404, y=288, )

    pydirectinput.click(x=945, y=1087, )

    pydirectinput.click(x=395, y=288, )

    camos()

    esc_scroll()

    pydirectinput.click(x=458, y=1068, )  # BRUEN MK9

    pydirectinput.click(x=776, y=318, )  # GUNSMITH

    pydirectinput.click(x=312, y=365, )

    pydirectinput.click(x=377, y=781, )

    pydirectinput.click(x=788, y=332, )

    pydirectinput.click(x=388, y=371, )

    pydirectinput.click(x=1199, y=297, )

    pydirectinput.click(x=370, y=449, )

    pydirectinput.click(x=1325, y=1123, )

    pydirectinput.click(x=408, y=370, )

    pydirectinput.click(x=931, y=1089, )

    pydirectinput.click(x=428, y=282, )

    camos()

    esc_scroll()

    pydirectinput.click(x=456, y=1067, )  # finn

    pydirectinput.click(x=773, y=316, )  # GUNSMITH

    pydirectinput.click(x=308, y=364, )

    pydirectinput.click(x=400, y=790, )

    pydirectinput.click(x=800, y=332, )

    pydirectinput.click(x=390, y=705, )

    pydirectinput.click(x=1227, y=296, )

    pydirectinput.click(x=417, y=281, )

    pydirectinput.click(x=1352, y=1121, )

    pydirectinput.click(x=397, y=374, )

    pydirectinput.click(x=958, y=1089, )

    pydirectinput.click(x=383, y=293, )

    camos()

    esc_scroll()

    pydirectinput.click(x=459, y=1081, )  # RAAL MG

    pydirectinput.click(x=774, y=316, )  # GUNSMITH

    pydirectinput.click(x=290, y=361, )

    pydirectinput.click(x=382, y=787, )

    pydirectinput.click(x=750, y=337, )

    pydirectinput.click(x=395, y=370, )

    pydirectinput.click(x=1218, y=295, )

    pydirectinput.click(x=396, y=288, )

    pydirectinput.click(x=1319, y=1124, )

    pydirectinput.click(x=393, y=364, )

    pydirectinput.click(x=916, y=1085, )

    pydirectinput.click(x=391, y=538, )

    camos()

    switch_tab_marksman()

    pydirectinput.click(x=474, y=385, )  # EBR

    pydirectinput.click(x=777, y=323, )  # GUNSMITH

    pydirectinput.click(x=311, y=366, )

    pydirectinput.click(x=418, y=787, )

    pydirectinput.click(x=782, y=332, )

    pydirectinput.click(x=409, y=460, )

    pydirectinput.click(x=1185, y=297, )

    pydirectinput.click(x=404, y=290, )

    pydirectinput.click(x=1332, y=1126, )

    pydirectinput.click(x=409, y=369, )

    pydirectinput.click(x=995, y=1083, )

    pydirectinput.click(x=397, y=279, )

    camos()

    ESC()

    pydirectinput.click(x=467, y=624, )  # MK2 CARBINE

    pydirectinput.click(x=776, y=324, )  # GUNSMITH

    pydirectinput.click(x=273, y=362, )

    pydirectinput.click(x=380, y=793, )

    pydirectinput.click(x=757, y=334, )

    pydirectinput.click(x=396, y=453, )

    pydirectinput.click(x=1243, y=297, )

    pydirectinput.click(x=384, y=284, )

    pydirectinput.click(x=1663, y=331, )

    pydirectinput.click(x=344, y=1042, )

    pydirectinput.click(x=1688, y=1128, )

    pydirectinput.click(x=386, y=368, )

    camos()

    ESC()

    pydirectinput.click(x=474, y=839, )  # KAR98K

    pydirectinput.click(x=775, y=327, )  # GUNSMITH

    pydirectinput.click(x=286, y=360, )

    pydirectinput.click(x=371, y=623, )

    pydirectinput.click(x=790, y=334, )

    pydirectinput.click(x=398, y=451, )

    pydirectinput.click(x=1271, y=298, )

    pydirectinput.click(x=439, y=287, )

    pydirectinput.click(x=1686, y=330, )

    pydirectinput.click(x=337, y=875, )

    pydirectinput.click(x=1727, y=1123, )

    pydirectinput.click(x=413, y=289, )

    camos()

    ESC()

    pydirectinput.click(x=465, y=1061, )  # CROSSBOW

    pydirectinput.click(x=777, y=326, )  # GUNSMITH

    pydirectinput.click(x=290, y=366, )

    pydirectinput.click(x=395, y=280, )

    pydirectinput.click(x=777, y=329, )

    pydirectinput.click(x=384, y=457, )

    pydirectinput.click(x=1233, y=295, )

    pydirectinput.click(x=389, y=282, )

    pydirectinput.click(x=1287, y=1123, )

    pydirectinput.click(x=403, y=280, )

    pydirectinput.click(x=937, y=1085, )

    pydirectinput.click(x=391, y=283, )

    camos()

    esc_scroll()

    pydirectinput.click(x=477, y=1062, )  # sks

    pydirectinput.click(x=771, y=322, )  # gunsmith

    pydirectinput.click(x=286, y=367, )

    pydirectinput.click(x=389, y=791, )

    pydirectinput.click(x=739, y=338, )

    pydirectinput.click(x=381, y=457, )

    pydirectinput.click(x=1254, y=298, )

    pydirectinput.click(x=449, y=288, )

    pydirectinput.click(x=1352, y=1120, )

    pydirectinput.click(x=392, y=283, )

    pydirectinput.click(x=974, y=1085, )

    pydirectinput.click(x=394, y=287, )

    camos()

    esc_scroll()

    pydirectinput.click(x=447, y=1074, )  # sp-r 208

    pydirectinput.click(x=776, y=322, )  # GUNSMITH\

    pydirectinput.click(x=285, y=364, )

    pydirectinput.click(x=372, y=792, )

    pydirectinput.click(x=768, y=335, )

    pydirectinput.click(x=425, y=456, )

    pydirectinput.click(x=1200, y=300, )

    pydirectinput.click(x=451, y=284, )

    pydirectinput.click(x=1644, y=334, )

    pydirectinput.click(x=360, y=1040, )

    pydirectinput.click(x=1303, y=1123, )

    pydirectinput.click(x=404, y=456, )

    camos()

    switch_tab_sniper()

    pydirectinput.click(x=458, y=409, )  # Dragunov

    pydirectinput.click(x=776, y=323, )  # GUNSMITH

    pydirectinput.click(x=267, y=366, )

    pydirectinput.click(x=416, y=362, )

    pydirectinput.click(x=738, y=331, )

    pydirectinput.click(x=378, y=372, )

    pydirectinput.click(x=1275, y=293, )

    pydirectinput.click(x=456, y=280, )

    pydirectinput.click(x=2100, y=360, )

    pydirectinput.click(x=436, y=535, )

    pydirectinput.click(x=2100, y=1091, )

    pydirectinput.click(x=372, y=455, )

    camos()

    esc_scroll()

    pydirectinput.click(x=480, y=621, )  # HDR

    pydirectinput.click(x=772, y=321, )  # GUNSMITH

    pydirectinput.click(x=806, y=337, )

    pydirectinput.click(x=414, y=452, )

    pydirectinput.click(x=1206, y=300, )

    pydirectinput.click(x=315, y=296, )

    pydirectinput.click(x=2111, y=365, )

    pydirectinput.click(x=426, y=284, )

    pydirectinput.click(x=2091, y=1084, )

    pydirectinput.click(x=366, y=536, )

    pydirectinput.click(x=936, y=1081, )

    pydirectinput.click(x=402, y=289, )

    camos()

    ESC()

    pydirectinput.click(x=431, y=856, )  # AX50

    pydirectinput.click(x=758, y=317, )  # GUNSMITH

    pydirectinput.click(x=764, y=327, )

    pydirectinput.click(x=365, y=360, )

    pydirectinput.click(x=1218, y=291, )

    pydirectinput.click(x=422, y=271, )

    pydirectinput.click(x=2149, y=351, )

    pydirectinput.click(x=362, y=450, )

    pydirectinput.click(x=1748, y=1154, )

    pydirectinput.click(x=365, y=453, )

    pydirectinput.click(x=2161, y=1111, )

    pydirectinput.click(x=355, y=364, )

    camos()

    ESC()

    pydirectinput.click(x=422, y=1048, )  # RYTEC

    pydirectinput.click(x=777, y=319, )  # GUNSMITH

    pydirectinput.click(x=321, y=370, )

    pydirectinput.click(x=387, y=371, )

    pydirectinput.click(x=762, y=339, )

    pydirectinput.click(x=410, y=287, )

    pydirectinput.click(x=1222, y=288, )

    pydirectinput.click(x=362, y=283, )

    pydirectinput.click(x=1730, y=1128, )

    pydirectinput.click(x=381, y=454, )

    pydirectinput.click(x=2096, y=361, )

    pydirectinput.click(x=393, y=454, )

    camos()

    switch_to_pistol()

    pydirectinput.click(x=778, y=578, )  # X16 PISTOL PLUS GUNSMITH

    pydirectinput.click(x=348, y=361, )

    pydirectinput.click(x=420, y=364, )

    pydirectinput.click(x=806, y=335, )

    pydirectinput.click(x=399, y=446, )

    pydirectinput.click(x=1210, y=297, )

    pydirectinput.click(x=400, y=454, )

    pydirectinput.click(x=1344, y=1123, )

    pydirectinput.click(x=376, y=371, )

    pydirectinput.click(x=921, y=1083, )

    pydirectinput.click(x=397, y=284, )

    camos()

    ESC_pistol()

    pydirectinput.click(x=451, y=616, )  # 1911

    pydirectinput.click(x=773, y=579, )  # GUNSMITH

    pydirectinput.click(x=296, y=363, )

    pydirectinput.click(x=392, y=710, )

    pydirectinput.click(x=807, y=332, )

    pydirectinput.click(x=408, y=449, )

    pydirectinput.click(x=1189, y=299, )

    pydirectinput.click(x=355, y=370, )

    pydirectinput.click(x=1335, y=1125, )

    pydirectinput.click(x=394, y=376, )

    pydirectinput.click(x=1000, y=1082, )

    pydirectinput.click(x=377, y=281, )

    camos()

    ESC_pistol()

    pydirectinput.click(x=472, y=843, )  # .357

    pydirectinput.click(x=771, y=577, )  # GUNSMITH

    pydirectinput.click(x=725, y=331, )

    pydirectinput.click(x=432, y=449, )

    pydirectinput.click(x=1251, y=299, )

    pydirectinput.click(x=427, y=366, )

    pydirectinput.click(x=1332, y=1128, )

    pydirectinput.click(x=434, y=281, )

    pydirectinput.click(x=2130, y=1088, )

    pydirectinput.click(x=371, y=1044, )

    pydirectinput.click(x=991, y=1089, )

    pydirectinput.click(x=429, y=284, )

    camos()

    ESC_pistol()

    pydirectinput.click(x=472, y=1053, )  # M19

    pydirectinput.click(x=776, y=582, )  # GUNSMITH

    pydirectinput.click(x=286, y=366, )

    pydirectinput.click(x=397, y=449, )

    pydirectinput.click(x=758, y=332, )

    pydirectinput.click(x=397, y=372, )

    pydirectinput.click(x=1225, y=296, )

    pydirectinput.click(x=393, y=363, )

    pydirectinput.click(x=1356, y=1123, )

    pydirectinput.click(x=425, y=371, )

    pydirectinput.click(x=938, y=1087, )

    pydirectinput.click(x=396, y=282, )

    camos()

    ESC_pistol_SCROLL()

    pydirectinput.click(x=464, y=1069, )  # 50OG

    pydirectinput.click(x=776, y=579, )  # GUNSMITH

    pydirectinput.click(x=275, y=367, )

    pydirectinput.click(x=395, y=458, )

    pydirectinput.click(x=769, y=332, )

    pydirectinput.click(x=397, y=283, )

    pydirectinput.click(x=1220, y=298, )

    pydirectinput.click(x=412, y=369, )

    pydirectinput.click(x=1326, y=1124, )

    pydirectinput.click(x=394, y=371, )

    pydirectinput.click(x=993, y=1085, )

    pydirectinput.click(x=396, y=282, )

    camos()

    ESC_pistol_SCROLL()

    pydirectinput.click(x=456, y=1058, )  # RENETTI

    pydirectinput.click(x=776, y=581, )  # GUNSMITH

    pydirectinput.click(x=295, y=366, )

    pydirectinput.click(x=399, y=714, )

    pydirectinput.click(x=783, y=332, )

    pydirectinput.click(x=440, y=452, )

    pydirectinput.click(x=1171, y=302, )

    pydirectinput.click(x=333, y=367, )

    pydirectinput.click(x=1308, y=1127, )

    pydirectinput.click(x=408, y=373, )

    pydirectinput.click(x=971, y=1090, )

    pydirectinput.click(x=402, y=287, )

    camos()

    ESC_pistol_SCROLL()

    pydirectinput.click(x=450, y=1062, )  # SYKOV

    pydirectinput.click(x=780, y=574, )  # GUNSMITH

    pydirectinput.click(x=277, y=362, )

    pydirectinput.click(x=397, y=704, )

    pydirectinput.click(x=771, y=329, )

    pydirectinput.click(x=404, y=455, )

    pydirectinput.click(x=1282, y=300, )

    pydirectinput.click(x=387, y=373, )

    pydirectinput.click(x=1281, y=1121, )

    pydirectinput.click(x=364, y=369, )

    pydirectinput.click(x=991, y=1081, )

    pydirectinput.click(x=417, y=287, )

    camos()  # #


# ---GOLD-PLATINUM-DAMASCUS-OBSIDIAN---#
def camo_2():
    pyautogui.alert('Press "OK" To Being')

    pydirectinput.tripleClick(x=1655, y=587, )

    pydirectinput.click(x=409, y=269, )  # kilo

    # pydirectinput.click(x=777, y=312,)

    pydirectinput.click(x=291, y=366, )

    pydirectinput.click(x=384, y=794, )

    pydirectinput.click(x=779, y=335, )

    pydirectinput.click(x=413, y=372, )

    pydirectinput.click(x=1247, y=300, )

    pydirectinput.click(x=440, y=454, )

    pydirectinput.click(x=1356, y=1119, )

    pydirectinput.click(x=442, y=370, )

    pydirectinput.click(x=936, y=1086, )

    pydirectinput.click(x=418, y=278, )  # kilo end

    camos2()

    ESC()  # exit kilo

    time.sleep(0.4)  # fal
    pydirectinput.click(x=501, y=620, )
    time.sleep(.05)
    pydirectinput.click(x=786, y=332, )

    pydirectinput.click(x=334, y=364, )

    pydirectinput.click(x=420, y=706, )

    pydirectinput.click(x=807, y=335, )

    pydirectinput.click(x=420, y=366, )

    pydirectinput.click(x=1270, y=301, )

    pydirectinput.click(x=397, y=454, )

    pydirectinput.click(x=1363, y=1125, )

    pydirectinput.click(x=411, y=364, )

    pydirectinput.click(x=956, y=1088, )

    pydirectinput.click(x=391, y=282, )  # FAL END

    camos2()

    ESC()

    pydirectinput.click(x=477, y=841, )  # M4

    pydirectinput.click(x=776, y=310, )  # GUNSSMITH

    pydirectinput.click(x=319, y=366, )

    pydirectinput.click(x=406, y=793, )

    pydirectinput.click(x=799, y=339, )

    pydirectinput.click(x=408, y=541, )

    pydirectinput.click(x=1258, y=299, )

    pydirectinput.click(x=445, y=446, )

    pydirectinput.click(x=1373, y=1121, )

    pydirectinput.click(x=446, y=373, )

    pydirectinput.click(x=960, y=1086, )

    pydirectinput.click(x=421, y=285, )

    camos2()

    ESC()

    pydirectinput.click(x=513, y=1076, )  # FR 5.56

    pydirectinput.click(x=783, y=315, )  # GUNSMITH

    pydirectinput.click(x=323, y=370, )

    pydirectinput.click(x=418, y=707, )

    pydirectinput.click(x=802, y=336, )

    pydirectinput.click(x=431, y=371, )

    pydirectinput.click(x=1234, y=292, )

    pydirectinput.click(x=414, y=452, )

    pydirectinput.click(x=1344, y=1124, )

    pydirectinput.click(x=403, y=376, )

    pydirectinput.click(x=964, y=1090, )

    pydirectinput.click(x=423, y=283, )  # FR 5.56 END

    camos2()

    esc_scroll()

    pydirectinput.click(x=491, y=1054, )  # ODEN

    pydirectinput.click(x=781, y=327, )  # GUNSMITH

    pydirectinput.click(x=322, y=371, )

    pydirectinput.click(x=410, y=538, )

    pydirectinput.click(x=800, y=340, )

    pydirectinput.click(x=423, y=287, )

    pydirectinput.click(x=1266, y=292, )

    pydirectinput.click(x=418, y=455, )

    pydirectinput.click(x=1379, y=1121, )

    pydirectinput.click(x=412, y=373, )

    pydirectinput.click(x=962, y=1089, )

    pydirectinput.click(x=423, y=288, )

    camos2()

    esc_scroll()

    pydirectinput.click(x=470, y=1068, )  # m13

    pydirectinput.click(x=773, y=309, )  # GUNSMITH

    pydirectinput.click(x=332, y=362, )

    pydirectinput.click(x=410, y=786, )

    pydirectinput.click(x=807, y=335, )

    pydirectinput.click(x=418, y=455, )

    pydirectinput.click(x=1258, y=300, )

    pydirectinput.click(x=411, y=376, )

    pydirectinput.click(x=1349, y=1124, )

    pydirectinput.click(x=429, y=450, )

    pydirectinput.click(x=965, y=1083, )

    pydirectinput.click(x=424, y=450, )

    camos2()

    esc_scroll()

    pydirectinput.click(x=486, y=1066, )  # FN SCAR

    pydirectinput.click(x=777, y=314, )  # GUNSMITH

    pydirectinput.click(x=335, y=365, )

    pydirectinput.click(x=415, y=785, )

    pydirectinput.click(x=816, y=336, )

    pydirectinput.click(x=416, y=368, )

    pydirectinput.click(x=1223, y=300, )

    pydirectinput.click(x=434, y=452, )

    pydirectinput.click(x=1374, y=1123, )

    pydirectinput.click(x=411, y=373, )

    pydirectinput.click(x=975, y=1087, )

    pydirectinput.click(x=425, y=285, )

    camos2()

    esc_scroll()

    pydirectinput.click(x=472, y=1042, )  # AK 47

    pydirectinput.click(x=773, y=322, )  # GUNSMITH

    pydirectinput.click(x=305, y=366, )

    pydirectinput.click(x=398, y=793, )

    pydirectinput.click(x=794, y=332, )

    pydirectinput.click(x=417, y=540, )

    pydirectinput.click(x=1357, y=1125, )

    pydirectinput.click(x=413, y=455, )

    pydirectinput.click(x=2159, y=363, )

    pydirectinput.click(x=370, y=456, )

    pydirectinput.click(x=1264, y=291, )

    pydirectinput.click(x=416, y=377, )

    camos2()

    esc_scroll()

    pydirectinput.click(x=469, y=1070, )  # RAM-7

    pydirectinput.click(x=775, y=321, )  # GUNSMITH

    pydirectinput.click(x=337, y=368, )

    pydirectinput.click(x=394, y=784, )

    pydirectinput.click(x=778, y=335, )

    pydirectinput.click(x=397, y=454, )

    pydirectinput.click(x=1260, y=301, )

    pydirectinput.click(x=397, y=450, )

    pydirectinput.click(x=1364, y=1125, )

    pydirectinput.click(x=403, y=292, )

    pydirectinput.click(x=969, y=1089, )

    pydirectinput.click(x=399, y=282, )

    camos2()

    esc_scroll()

    pydirectinput.click(x=462, y=1071, )  # GRAU

    pydirectinput.click(x=778, y=318, )  # GUNSMITH

    pydirectinput.click(x=338, y=360, )

    pydirectinput.click(x=399, y=789, )

    pydirectinput.click(x=799, y=339, )

    pydirectinput.click(x=408, y=377, )

    pydirectinput.click(x=1245, y=298, )

    pydirectinput.click(x=421, y=463, )

    pydirectinput.click(x=984, y=1085, )

    pydirectinput.click(x=422, y=281, )

    pydirectinput.click(x=1352, y=1125, )

    pydirectinput.click(x=397, y=369, )

    camos2()

    esc_scroll()

    pydirectinput.click(x=458, y=1067, )  # AMAX

    pydirectinput.click(x=777, y=307, )  # GUNSMITH

    pydirectinput.click(x=333, y=360, )

    pydirectinput.click(x=391, y=704, )

    pydirectinput.click(x=786, y=335, )

    pydirectinput.click(x=416, y=369, )

    pydirectinput.click(x=1211, y=297, )

    pydirectinput.click(x=406, y=445, )

    pydirectinput.click(x=1353, y=1129, )

    pydirectinput.click(x=398, y=285, )

    pydirectinput.click(x=1003, y=1084, )

    pydirectinput.click(x=407, y=291, )

    camos2()

    esc_scroll()

    pydirectinput.click(x=474, y=1064, )  # AN-94

    pydirectinput.click(x=779, y=319, )  # GUNSMITH

    pydirectinput.click(x=282, y=369, )

    pydirectinput.click(x=394, y=709, )

    pydirectinput.click(x=770, y=334, )

    pydirectinput.click(x=383, y=373, )

    pydirectinput.click(x=1261, y=305, )

    pydirectinput.click(x=405, y=459, )

    pydirectinput.click(x=1356, y=1129, )

    pydirectinput.click(x=395, y=367, )

    pydirectinput.click(x=974, y=1083, )

    pydirectinput.click(x=393, y=290, )

    camos2()

    esc_scroll()

    pydirectinput.click(x=476, y=1068, )  # AS-VAL

    pydirectinput.click(x=774, y=324, )  # GUNSMITH

    pydirectinput.click(x=792, y=338, )

    pydirectinput.click(x=402, y=454, )

    pydirectinput.click(x=1274, y=303, )

    pydirectinput.click(x=393, y=461, )

    pydirectinput.click(x=965, y=1086, )

    pydirectinput.click(x=406, y=287, )

    pydirectinput.click(x=1341, y=1122, )

    pydirectinput.click(x=422, y=287, )

    pydirectinput.click(x=1748, y=1127, )

    pydirectinput.click(x=432, y=368, )

    camos2()

    switch_tab()  # switch to SMG

    pydirectinput.click(x=480, y=407, )  # AUG SMG

    pydirectinput.click(x=779, y=318, )  # GUNSMITH

    pydirectinput.click(x=313, y=368, )

    pydirectinput.click(x=399, y=550, )

    pydirectinput.click(x=771, y=333, )

    pydirectinput.click(x=415, y=454, )

    pydirectinput.click(x=1252, y=302, )

    pydirectinput.click(x=404, y=373, )

    pydirectinput.click(x=1353, y=1128, )

    pydirectinput.click(x=430, y=455, )

    pydirectinput.click(x=959, y=1089, )

    pydirectinput.click(x=388, y=293, )

    camos2()

    ESC()

    pydirectinput.click(x=498, y=611, )  # P90

    pydirectinput.click(x=780, y=306, )  # GUNSMITH

    pydirectinput.click(x=329, y=365, )

    pydirectinput.click(x=402, y=619, )

    pydirectinput.click(x=743, y=334, )

    pydirectinput.click(x=426, y=371, )

    pydirectinput.click(x=1252, y=298, )

    pydirectinput.click(x=403, y=370, )

    pydirectinput.click(x=1719, y=1124, )

    pydirectinput.click(x=409, y=286, )

    pydirectinput.click(x=913, y=1079, )

    pydirectinput.click(x=413, y=362, )

    camos2()

    ESC()

    pydirectinput.click(x=461, y=852, )  # MP5 SMG

    pydirectinput.click(x=780, y=339, )  # GUNSMITH

    pydirectinput.click(x=730, y=336, )

    pydirectinput.click(x=410, y=366, )

    pydirectinput.click(x=2146, y=363, )

    pydirectinput.click(x=424, y=538, )

    pydirectinput.click(x=1364, y=1119, )

    pydirectinput.click(x=378, y=287, )

    pydirectinput.click(x=969, y=1091, )

    pydirectinput.click(x=413, y=373, )

    pydirectinput.click(x=2103, y=1083, )

    pydirectinput.click(x=405, y=703, )

    camos2()

    ESC()

    pydirectinput.click(x=443, y=1046, )  # UZI

    pydirectinput.click(x=775, y=320, )  # GUNSMITH

    pydirectinput.click(x=322, y=369, )

    pydirectinput.click(x=434, y=624, )

    pydirectinput.click(x=799, y=328, )

    pydirectinput.click(x=382, y=533, )

    pydirectinput.click(x=1251, y=295, )

    pydirectinput.click(x=390, y=363, )

    pydirectinput.click(x=1339, y=1121, )

    pydirectinput.click(x=411, y=456, )

    pydirectinput.click(x=959, y=1084, )

    pydirectinput.click(x=410, y=285, )

    camos2()

    esc_scroll()

    pydirectinput.click(x=454, y=1065, )  # PP19 BIZON

    pydirectinput.click(x=775, y=317, )  # GUNSMITH

    pydirectinput.click(x=312, y=365, )

    pydirectinput.click(x=408, y=791, )

    pydirectinput.click(x=757, y=335, )

    pydirectinput.click(x=407, y=370, )

    pydirectinput.click(x=1270, y=298, )

    pydirectinput.click(x=416, y=459, )

    pydirectinput.click(x=2135, y=366, )

    pydirectinput.click(x=424, y=369, )

    pydirectinput.click(x=1349, y=1122, )

    pydirectinput.click(x=419, y=287, )

    camos2()

    esc_scroll()

    pydirectinput.click(x=461, y=1071, )  # MP7 SMG

    pydirectinput.click(x=781, y=314, )  # GUNSMITH

    pydirectinput.click(x=329, y=363, )

    pydirectinput.click(x=413, y=786, )

    pydirectinput.click(x=799, y=329, )

    pydirectinput.click(x=437, y=368, )

    pydirectinput.click(x=1262, y=298, )

    pydirectinput.click(x=391, y=373, )

    pydirectinput.click(x=1377, y=1121, )

    pydirectinput.click(x=401, y=371, )

    pydirectinput.click(x=959, y=1087, )

    pydirectinput.click(x=390, y=365, )

    camos2()

    esc_scroll()

    pydirectinput.click(x=465, y=1068, )  # STRIKER 45 SMG

    pydirectinput.click(x=785, y=323, )  # GUNSMITH

    pydirectinput.click(x=332, y=361, )

    pydirectinput.click(x=403, y=791, )

    pydirectinput.click(x=797, y=335, )

    pydirectinput.click(x=404, y=368, )

    pydirectinput.click(x=1260, y=299, )

    pydirectinput.click(x=387, y=369, )

    pydirectinput.click(x=1390, y=1119, )

    pydirectinput.click(x=415, y=367, )

    pydirectinput.click(x=984, y=1085, )

    pydirectinput.click(x=378, y=372, )

    camos2()

    esc_scroll()

    pydirectinput.click(x=475, y=1063, )  # FENNIC SMG

    pydirectinput.click(x=782, y=326, )  # GUNSMITH

    pydirectinput.click(x=764, y=334, )

    pydirectinput.click(x=415, y=367, )

    pydirectinput.click(x=1252, y=299, )

    pydirectinput.click(x=411, y=371, )

    pydirectinput.click(x=1370, y=1122, )

    pydirectinput.click(x=404, y=286, )

    pydirectinput.click(x=2172, y=1085, )

    pydirectinput.click(x=393, y=875, )

    pydirectinput.click(x=972, y=1090, )

    pydirectinput.click(x=389, y=284, )

    camos2()

    esc_scroll()

    pydirectinput.click(x=471, y=1062, )  # ISO SMG

    pydirectinput.click(x=776, y=321, )  # GUNSMITH

    pydirectinput.click(x=803, y=334, )

    pydirectinput.click(x=416, y=538, )

    pydirectinput.click(x=1266, y=298, )

    pydirectinput.click(x=425, y=377, )

    pydirectinput.click(x=972, y=1083, )

    pydirectinput.click(x=392, y=377, )

    pydirectinput.click(x=1355, y=1120, )

    pydirectinput.click(x=404, y=375, )

    pydirectinput.click(x=2166, y=1082, )

    pydirectinput.click(x=385, y=875, )

    camos2()

    esc_scroll()

    pydirectinput.click(x=471, y=1075, )  # sc9 smg

    pydirectinput.click(x=772, y=323, )  # GUNSMITH

    pydirectinput.click(x=746, y=336, )

    pydirectinput.click(x=436, y=622, )

    pydirectinput.click(x=1258, y=297, )

    pydirectinput.click(x=414, y=372, )

    pydirectinput.click(x=2129, y=362, )

    pydirectinput.click(x=423, y=451, )

    pydirectinput.click(x=2122, y=1082, )

    pydirectinput.click(x=379, y=708, )

    pydirectinput.click(x=1366, y=1126, )

    pydirectinput.click(x=411, y=454, )

    camos2()

    switch_tab_shotgun()

    pydirectinput.click(x=470, y=408, )  # MODEL 680

    pydirectinput.click(x=776, y=322, )  # GUNDMITH

    pydirectinput.click(x=299, y=364, )

    pydirectinput.click(x=379, y=708, )

    pydirectinput.click(x=781, y=332, )

    pydirectinput.click(x=417, y=453, )

    pydirectinput.click(x=1225, y=295, )

    pydirectinput.click(x=379, y=367, )

    pydirectinput.click(x=2160, y=367, )

    pydirectinput.click(x=441, y=456, )

    pydirectinput.click(x=1301, y=1131, )

    pydirectinput.click(x=396, y=622, )

    camos2()

    ESC()

    pydirectinput.click(x=486, y=629, )  # R90

    pydirectinput.click(x=777, y=328, )  # GUNSMITH

    pydirectinput.click(x=350, y=365, )

    pydirectinput.click(x=401, y=703, )

    pydirectinput.click(x=797, y=332, )

    pydirectinput.click(x=394, y=283, )

    pydirectinput.click(x=1210, y=297, )

    pydirectinput.click(x=376, y=371, )

    pydirectinput.click(x=1330, y=1123, )

    pydirectinput.click(x=407, y=458, )

    pydirectinput.click(x=1739, y=1126, )

    pydirectinput.click(x=404, y=455, )

    camos2()

    ESC()

    pydirectinput.click(x=463, y=848, )  # 725

    pydirectinput.click(x=776, y=327, )  # GUNSMITH

    pydirectinput.click(x=348, y=363, )

    pydirectinput.click(x=394, y=789, )

    pydirectinput.click(x=761, y=334, )

    pydirectinput.click(x=408, y=365, )

    pydirectinput.click(x=1212, y=294, )

    pydirectinput.click(x=454, y=375, )

    pydirectinput.click(x=2143, y=363, )

    pydirectinput.click(x=383, y=455, )

    pydirectinput.click(x=1692, y=1123, )

    pydirectinput.click(x=414, y=284, )

    camos2()

    ESC()

    pydirectinput.click(x=458, y=1077, )  # ORIGIN 12

    pydirectinput.click(x=776, y=323, )  # GUNSMITH

    pydirectinput.click(x=320, y=367, )

    pydirectinput.click(x=397, y=876, )

    pydirectinput.click(x=768, y=333, )

    pydirectinput.click(x=393, y=448, )

    pydirectinput.click(x=1266, y=301, )

    pydirectinput.click(x=378, y=369, )

    pydirectinput.click(x=1372, y=1127, )

    pydirectinput.click(x=403, y=458, )

    pydirectinput.click(x=1751, y=1126, )

    pydirectinput.click(x=419, y=456, )

    camos2()

    esc_scroll()

    pydirectinput.click(x=436, y=1059, )  # VLK

    pydirectinput.click(x=777, y=324, )  # GUNSMITH

    pydirectinput.doubleClick(x=1336, y=671, )  # click screen

    pydirectinput.click(x=1708, y=1128, )  # not working

    pydirectinput.click(x=406, y=458, )  # NOT WORKING

    pydirectinput.click(x=795, y=335, )

    pydirectinput.click(x=420, y=458, )

    pydirectinput.click(x=1224, y=302, )

    pydirectinput.click(x=391, y=373, )

    pydirectinput.click(x=1311, y=1126, )

    pydirectinput.click(x=405, y=536, )

    pydirectinput.click(x=945, y=1088, )

    pydirectinput.click(x=351, y=288, )

    camos2()

    esc_scroll()

    pydirectinput.click(x=457, y=1075, )  # JAK 12

    pydirectinput.click(x=776, y=307, )  # GUNSMITH

    pydirectinput.doubleClick(x=1336, y=671, )  # click screen

    pydirectinput.click(x=333, y=367, )

    pydirectinput.click(x=408, y=789, )

    pydirectinput.click(x=789, y=336, )

    pydirectinput.click(x=418, y=455, )

    pydirectinput.click(x=1261, y=301, )

    pydirectinput.click(x=401, y=374, )

    pydirectinput.click(x=1359, y=1120, )

    pydirectinput.click(x=397, y=456, )

    pydirectinput.click(x=956, y=1090, )

    pydirectinput.click(x=393, y=299, )

    camos2()

    switch_tab_LMG()

    pydirectinput.click(x=476, y=408, )  # pkm

    pydirectinput.click(x=774, y=319, )  # gunsmith

    pydirectinput.click(x=322, y=363, )

    pydirectinput.click(x=402, y=371, )

    pydirectinput.click(x=749, y=333, )

    pydirectinput.click(x=384, y=365, )

    pydirectinput.click(x=1183, y=293, )

    pydirectinput.click(x=389, y=452, )

    pydirectinput.click(x=2178, y=362, )

    pydirectinput.click(x=398, y=454, )

    pydirectinput.click(x=962, y=1086, )

    pydirectinput.click(x=421, y=286, )

    camos2()

    ESC()

    pydirectinput.click(x=475, y=640, )  # SA87

    pydirectinput.click(x=775, y=321, )  # GUNSMITH

    pydirectinput.click(x=302, y=365, )

    pydirectinput.click(x=398, y=785, )

    pydirectinput.click(x=795, y=338, )

    pydirectinput.click(x=413, y=366, )

    pydirectinput.click(x=1215, y=294, )

    pydirectinput.click(x=409, y=452, )

    pydirectinput.click(x=1356, y=1123, )

    pydirectinput.click(x=404, y=364, )

    pydirectinput.click(x=912, y=1088, )

    pydirectinput.click(x=390, y=282, )

    camos2()

    ESC()

    pydirectinput.click(x=468, y=823, )  # M91

    pydirectinput.click(x=776, y=321, )  # GUNSMITH

    pydirectinput.click(x=309, y=364, )

    pydirectinput.click(x=416, y=789, )

    pydirectinput.click(x=753, y=335, )

    pydirectinput.click(x=408, y=457, )

    pydirectinput.click(x=1197, y=298, )

    pydirectinput.click(x=385, y=453, )

    pydirectinput.click(x=2128, y=361, )

    pydirectinput.click(x=417, y=535, )

    pydirectinput.click(x=954, y=1088, )

    pydirectinput.click(x=415, y=279, )

    camos2()

    ESC()

    pydirectinput.click(x=465, y=1063, )  # MG34

    pydirectinput.click(x=777, y=324, )  # GUMSMITH

    pydirectinput.click(x=281, y=364, )

    pydirectinput.click(x=393, y=790, )

    pydirectinput.click(x=766, y=333, )

    pydirectinput.click(x=430, y=458, )

    pydirectinput.click(x=1246, y=296, )

    pydirectinput.click(x=388, y=366, )

    pydirectinput.click(x=1355, y=1122, )

    pydirectinput.click(x=428, y=285, )

    pydirectinput.click(x=932, y=1083, )

    pydirectinput.click(x=385, y=284, )

    camos2()

    esc_scroll()

    pydirectinput.click(x=451, y=1056, )  # HOLGER

    pydirectinput.click(x=778, y=317, )  # GUNSMITH

    pydirectinput.click(x=305, y=359, )

    pydirectinput.click(x=400, y=783, )

    pydirectinput.click(x=743, y=337, )

    pydirectinput.click(x=391, y=284, )

    pydirectinput.click(x=1197, y=295, )

    pydirectinput.click(x=385, y=456, )

    pydirectinput.click(x=1361, y=1126, )

    pydirectinput.click(x=404, y=288, )

    pydirectinput.click(x=945, y=1087, )

    pydirectinput.click(x=395, y=288, )

    camos2()

    esc_scroll()

    pydirectinput.click(x=458, y=1068, )  # BRUEN MK9

    pydirectinput.click(x=776, y=318, )  # GUNSMITH

    pydirectinput.click(x=312, y=365, )

    pydirectinput.click(x=377, y=781, )

    pydirectinput.click(x=788, y=332, )

    pydirectinput.click(x=388, y=371, )

    pydirectinput.click(x=1199, y=297, )

    pydirectinput.click(x=370, y=449, )

    pydirectinput.click(x=1325, y=1123, )

    pydirectinput.click(x=408, y=370, )

    pydirectinput.click(x=931, y=1089, )

    pydirectinput.click(x=428, y=282, )

    camos2()

    esc_scroll()

    pydirectinput.click(x=456, y=1067, )  # finn

    pydirectinput.click(x=773, y=316, )  # GUNSMITH

    pydirectinput.click(x=308, y=364, )

    pydirectinput.click(x=400, y=790, )

    pydirectinput.click(x=800, y=332, )

    pydirectinput.click(x=390, y=705, )

    pydirectinput.click(x=1227, y=296, )

    pydirectinput.click(x=417, y=281, )

    pydirectinput.click(x=1352, y=1121, )

    pydirectinput.click(x=397, y=374, )

    pydirectinput.click(x=958, y=1089, )

    pydirectinput.click(x=383, y=293, )

    camos2()

    esc_scroll()

    pydirectinput.click(x=459, y=1081, )  # RAAL MG

    pydirectinput.click(x=774, y=316, )  # GUNSMITH

    pydirectinput.click(x=290, y=361, )

    pydirectinput.click(x=382, y=787, )

    pydirectinput.click(x=750, y=337, )

    pydirectinput.click(x=395, y=370, )

    pydirectinput.click(x=1218, y=295, )

    pydirectinput.click(x=396, y=288, )

    pydirectinput.click(x=1319, y=1124, )

    pydirectinput.click(x=393, y=364, )

    pydirectinput.click(x=916, y=1085, )

    pydirectinput.click(x=391, y=538, )

    camos2()

    switch_tab_marksman()

    pydirectinput.click(x=474, y=385, )  # EBR

    pydirectinput.click(x=777, y=323, )  # GUNSMITH

    pydirectinput.click(x=311, y=366, )

    pydirectinput.click(x=418, y=787, )

    pydirectinput.click(x=782, y=332, )

    pydirectinput.click(x=409, y=460, )

    pydirectinput.click(x=1185, y=297, )

    pydirectinput.click(x=404, y=290, )

    pydirectinput.click(x=1332, y=1126, )

    pydirectinput.click(x=409, y=369, )

    pydirectinput.click(x=995, y=1083, )

    pydirectinput.click(x=397, y=279, )

    camos2()

    ESC()

    pydirectinput.click(x=467, y=624, )  # MK2 CARBINE

    pydirectinput.click(x=776, y=324, )  # GUNSMITH

    pydirectinput.click(x=273, y=362, )

    pydirectinput.click(x=380, y=793, )

    pydirectinput.click(x=757, y=334, )

    pydirectinput.click(x=396, y=453, )

    pydirectinput.click(x=1243, y=297, )

    pydirectinput.click(x=384, y=284, )

    pydirectinput.click(x=1663, y=331, )

    pydirectinput.click(x=344, y=1042, )

    pydirectinput.click(x=1688, y=1128, )

    pydirectinput.click(x=386, y=368, )

    camos2()

    ESC()

    pydirectinput.click(x=474, y=839, )  # KAR98K

    pydirectinput.click(x=775, y=327, )  # GUNSMITH

    pydirectinput.click(x=286, y=360, )

    pydirectinput.click(x=371, y=623, )

    pydirectinput.click(x=790, y=334, )

    pydirectinput.click(x=398, y=451, )

    pydirectinput.click(x=1271, y=298, )

    pydirectinput.click(x=439, y=287, )

    pydirectinput.click(x=1686, y=330, )

    pydirectinput.click(x=337, y=875, )

    pydirectinput.click(x=1727, y=1123, )

    pydirectinput.click(x=413, y=289, )

    camos2()

    ESC()

    pydirectinput.click(x=465, y=1061, )  # CROSSBOW

    pydirectinput.click(x=777, y=326, )  # GUNSMITH

    pydirectinput.click(x=290, y=366, )

    pydirectinput.click(x=395, y=280, )

    pydirectinput.click(x=777, y=329, )

    pydirectinput.click(x=384, y=457, )

    pydirectinput.click(x=1233, y=295, )

    pydirectinput.click(x=389, y=282, )

    pydirectinput.click(x=1287, y=1123, )

    pydirectinput.click(x=403, y=280, )

    pydirectinput.click(x=937, y=1085, )

    pydirectinput.click(x=391, y=283, )

    camos2()

    esc_scroll()

    pydirectinput.click(x=477, y=1062, )  # sks

    pydirectinput.click(x=771, y=322, )  # gunsmith

    pydirectinput.click(x=286, y=367, )

    pydirectinput.click(x=389, y=791, )

    pydirectinput.click(x=739, y=338, )

    pydirectinput.click(x=381, y=457, )

    pydirectinput.click(x=1254, y=298, )

    pydirectinput.click(x=449, y=288, )

    pydirectinput.click(x=1352, y=1120, )

    pydirectinput.click(x=392, y=283, )

    pydirectinput.click(x=974, y=1085, )

    pydirectinput.click(x=394, y=287, )

    camos2()

    esc_scroll()

    pydirectinput.click(x=447, y=1074, )  # sp-r 208

    pydirectinput.click(x=776, y=322, )  # GUNSMITH\

    pydirectinput.click(x=285, y=364, )

    pydirectinput.click(x=372, y=792, )

    pydirectinput.click(x=768, y=335, )

    pydirectinput.click(x=425, y=456, )

    pydirectinput.click(x=1200, y=300, )

    pydirectinput.click(x=451, y=284, )

    pydirectinput.click(x=1644, y=334, )

    pydirectinput.click(x=360, y=1040, )

    pydirectinput.click(x=1303, y=1123, )

    pydirectinput.click(x=404, y=456, )

    camos2()

    switch_tab_sniper()

    pydirectinput.click(x=458, y=409, )  # Dragunov

    pydirectinput.click(x=776, y=323, )  # GUNSMITH

    pydirectinput.click(x=267, y=366, )

    pydirectinput.click(x=416, y=362, )

    pydirectinput.click(x=738, y=331, )

    pydirectinput.click(x=378, y=372, )

    pydirectinput.click(x=1275, y=293, )

    pydirectinput.click(x=456, y=280, )

    pydirectinput.click(x=2100, y=360, )

    pydirectinput.click(x=436, y=535, )

    pydirectinput.click(x=2100, y=1091, )

    pydirectinput.click(x=372, y=455, )

    camos2()

    esc_scroll()

    pydirectinput.click(x=480, y=621, )  # HDR

    pydirectinput.click(x=772, y=321, )  # GUNSMITH

    pydirectinput.click(x=806, y=337, )

    pydirectinput.click(x=414, y=452, )

    pydirectinput.click(x=1206, y=300, )

    pydirectinput.click(x=315, y=296, )

    pydirectinput.click(x=2111, y=365, )

    pydirectinput.click(x=426, y=284, )

    pydirectinput.click(x=2091, y=1084, )

    pydirectinput.click(x=366, y=536, )

    pydirectinput.click(x=936, y=1081, )

    pydirectinput.click(x=402, y=289, )

    camos2()

    ESC()

    pydirectinput.click(x=431, y=856, )  # AX50

    pydirectinput.click(x=758, y=317, )  # GUNSMITH

    pydirectinput.click(x=764, y=327, )

    pydirectinput.click(x=365, y=360, )

    pydirectinput.click(x=1218, y=291, )

    pydirectinput.click(x=422, y=271, )

    pydirectinput.click(x=2149, y=351, )

    pydirectinput.click(x=362, y=450, )

    pydirectinput.click(x=1748, y=1154, )

    pydirectinput.click(x=365, y=453, )

    pydirectinput.click(x=2161, y=1111, )

    pydirectinput.click(x=355, y=364, )

    camos2()

    ESC()

    pydirectinput.click(x=422, y=1048, )  # RYTEC

    pydirectinput.click(x=777, y=319, )  # GUNSMITH

    pydirectinput.click(x=321, y=370, )

    pydirectinput.click(x=387, y=371, )

    pydirectinput.click(x=762, y=339, )

    pydirectinput.click(x=410, y=287, )

    pydirectinput.click(x=1222, y=288, )

    pydirectinput.click(x=362, y=283, )

    pydirectinput.click(x=1730, y=1128, )

    pydirectinput.click(x=381, y=454, )

    pydirectinput.click(x=2096, y=361, )

    pydirectinput.click(x=393, y=454, )

    camos2()

    switch_to_pistol()

    pydirectinput.click(x=778, y=578, )  # X16 PISTOL PLUS GUNSMITH

    pydirectinput.click(x=348, y=361, )

    pydirectinput.click(x=420, y=364, )

    pydirectinput.click(x=806, y=335, )

    pydirectinput.click(x=399, y=446, )

    pydirectinput.click(x=1210, y=297, )

    pydirectinput.click(x=400, y=454, )

    pydirectinput.click(x=1344, y=1123, )

    pydirectinput.click(x=376, y=371, )

    pydirectinput.click(x=921, y=1083, )

    pydirectinput.click(x=397, y=284, )

    camos2()

    ESC_pistol()

    pydirectinput.click(x=451, y=616, )  # 1911

    pydirectinput.click(x=773, y=579, )  # GUNSMITH

    pydirectinput.click(x=296, y=363, )

    pydirectinput.click(x=392, y=710, )

    pydirectinput.click(x=807, y=332, )

    pydirectinput.click(x=408, y=449, )

    pydirectinput.click(x=1189, y=299, )

    pydirectinput.click(x=355, y=370, )

    pydirectinput.click(x=1335, y=1125, )

    pydirectinput.click(x=394, y=376, )

    pydirectinput.click(x=1000, y=1082, )

    pydirectinput.click(x=377, y=281, )

    camos2()

    ESC_pistol()

    pydirectinput.click(x=472, y=843, )  # .357

    pydirectinput.click(x=771, y=577, )  # GUNSMITH

    pydirectinput.click(x=725, y=331, )

    pydirectinput.click(x=432, y=449, )

    pydirectinput.click(x=1251, y=299, )

    pydirectinput.click(x=427, y=366, )

    pydirectinput.click(x=1332, y=1128, )

    pydirectinput.click(x=434, y=281, )

    pydirectinput.click(x=2130, y=1088, )

    pydirectinput.click(x=371, y=1044, )

    pydirectinput.click(x=991, y=1089, )

    pydirectinput.click(x=429, y=284, )

    camos2()

    ESC_pistol()

    pydirectinput.click(x=472, y=1053, )  # M19

    pydirectinput.click(x=776, y=582, )  # GUNSMITH

    pydirectinput.click(x=286, y=366, )

    pydirectinput.click(x=397, y=449, )

    pydirectinput.click(x=758, y=332, )

    pydirectinput.click(x=397, y=372, )

    pydirectinput.click(x=1225, y=296, )

    pydirectinput.click(x=393, y=363, )

    pydirectinput.click(x=1356, y=1123, )

    pydirectinput.click(x=425, y=371, )

    pydirectinput.click(x=938, y=1087, )

    pydirectinput.click(x=396, y=282, )

    camos2()

    ESC_pistol_SCROLL()

    pydirectinput.click(x=464, y=1069, )  # 50OG

    pydirectinput.click(x=776, y=579, )  # GUNSMITH

    pydirectinput.click(x=275, y=367, )

    pydirectinput.click(x=395, y=458, )

    pydirectinput.click(x=769, y=332, )

    pydirectinput.click(x=397, y=283, )

    pydirectinput.click(x=1220, y=298, )

    pydirectinput.click(x=412, y=369, )

    pydirectinput.click(x=1326, y=1124, )

    pydirectinput.click(x=394, y=371, )

    pydirectinput.click(x=993, y=1085, )

    pydirectinput.click(x=396, y=282, )

    camos2()

    ESC_pistol_SCROLL()

    pydirectinput.click(x=456, y=1058, )  # RENETTI

    pydirectinput.click(x=776, y=581, )  # GUNSMITH

    pydirectinput.click(x=295, y=366, )

    pydirectinput.click(x=399, y=714, )

    pydirectinput.click(x=783, y=332, )

    pydirectinput.click(x=440, y=452, )

    pydirectinput.click(x=1171, y=302, )

    pydirectinput.click(x=333, y=367, )

    pydirectinput.click(x=1308, y=1127, )

    pydirectinput.click(x=408, y=373, )

    pydirectinput.click(x=971, y=1090, )

    pydirectinput.click(x=402, y=287, )

    camos2()

    ESC_pistol_SCROLL()

    pydirectinput.click(x=450, y=1062, )  # SYKOV

    pydirectinput.click(x=780, y=574, )  # GUNSMITH

    pydirectinput.click(x=277, y=362, )

    pydirectinput.click(x=397, y=704, )

    pydirectinput.click(x=771, y=329, )

    pydirectinput.click(x=404, y=455, )

    pydirectinput.click(x=1282, y=300, )

    pydirectinput.click(x=387, y=373, )

    pydirectinput.click(x=1281, y=1121, )

    pydirectinput.click(x=364, y=369, )

    pydirectinput.click(x=991, y=1081, )

    pydirectinput.click(x=417, y=287, )

    camos2()


# ---DAMASCUCS-DAIMOND-DMULTRA-HOT&COLD---#
def camo_3():
    pyautogui.alert('Press "OK" To Being')

    pydirectinput.tripleClick(x=1655, y=587, )

    pydirectinput.click(x=409, y=269, )  # kilo

    # pydirectinput.click(x=777, y=312,)

    pydirectinput.click(x=291, y=366, )

    pydirectinput.click(x=384, y=794, )

    pydirectinput.click(x=779, y=335, )

    pydirectinput.click(x=413, y=372, )

    pydirectinput.click(x=1247, y=300, )

    pydirectinput.click(x=440, y=454, )

    pydirectinput.click(x=1356, y=1119, )

    pydirectinput.click(x=442, y=370, )

    pydirectinput.click(x=936, y=1086, )

    pydirectinput.click(x=418, y=278, )  # kilo end

    camos3()

    ESC()  # exit kilo

    time.sleep(0.4)  # fal
    pydirectinput.click(x=501, y=620, )
    time.sleep(.05)
    pydirectinput.click(x=786, y=332, )

    pydirectinput.click(x=334, y=364, )

    pydirectinput.click(x=420, y=706, )

    pydirectinput.click(x=807, y=335, )

    pydirectinput.click(x=420, y=366, )

    pydirectinput.click(x=1270, y=301, )

    pydirectinput.click(x=397, y=454, )

    pydirectinput.click(x=1363, y=1125, )

    pydirectinput.click(x=411, y=364, )

    pydirectinput.click(x=956, y=1088, )

    pydirectinput.click(x=391, y=282, )  # FAL END

    camos3()

    ESC()

    pydirectinput.click(x=477, y=841, )  # M4

    pydirectinput.click(x=776, y=310, )  # GUNSSMITH

    pydirectinput.click(x=319, y=366, )

    pydirectinput.click(x=406, y=793, )

    pydirectinput.click(x=799, y=339, )

    pydirectinput.click(x=408, y=541, )

    pydirectinput.click(x=1258, y=299, )

    pydirectinput.click(x=445, y=446, )

    pydirectinput.click(x=1373, y=1121, )

    pydirectinput.click(x=446, y=373, )

    pydirectinput.click(x=960, y=1086, )

    pydirectinput.click(x=421, y=285, )

    camos3()

    ESC()

    pydirectinput.click(x=513, y=1076, )  # FR 5.56

    pydirectinput.click(x=783, y=315, )  # GUNSMITH

    pydirectinput.click(x=323, y=370, )

    pydirectinput.click(x=418, y=707, )

    pydirectinput.click(x=802, y=336, )

    pydirectinput.click(x=431, y=371, )

    pydirectinput.click(x=1234, y=292, )

    pydirectinput.click(x=414, y=452, )

    pydirectinput.click(x=1344, y=1124, )

    pydirectinput.click(x=403, y=376, )

    pydirectinput.click(x=964, y=1090, )

    pydirectinput.click(x=423, y=283, )  # FR 5.56 END

    camos3()

    esc_scroll()

    pydirectinput.click(x=491, y=1054, )  # ODEN

    pydirectinput.click(x=781, y=327, )  # GUNSMITH

    pydirectinput.click(x=322, y=371, )

    pydirectinput.click(x=410, y=538, )

    pydirectinput.click(x=800, y=340, )

    pydirectinput.click(x=423, y=287, )

    pydirectinput.click(x=1266, y=292, )

    pydirectinput.click(x=418, y=455, )

    pydirectinput.click(x=1379, y=1121, )

    pydirectinput.click(x=412, y=373, )

    pydirectinput.click(x=962, y=1089, )

    pydirectinput.click(x=423, y=288, )

    camos3()

    esc_scroll()

    pydirectinput.click(x=470, y=1068, )  # m13

    pydirectinput.click(x=773, y=309, )  # GUNSMITH

    pydirectinput.click(x=332, y=362, )

    pydirectinput.click(x=410, y=786, )

    pydirectinput.click(x=807, y=335, )

    pydirectinput.click(x=418, y=455, )

    pydirectinput.click(x=1258, y=300, )

    pydirectinput.click(x=411, y=376, )

    pydirectinput.click(x=1349, y=1124, )

    pydirectinput.click(x=429, y=450, )

    pydirectinput.click(x=965, y=1083, )

    pydirectinput.click(x=424, y=450, )

    camos3()

    esc_scroll()

    pydirectinput.click(x=486, y=1066, )  # FN SCAR

    pydirectinput.click(x=777, y=314, )  # GUNSMITH

    pydirectinput.click(x=335, y=365, )

    pydirectinput.click(x=415, y=785, )

    pydirectinput.click(x=816, y=336, )

    pydirectinput.click(x=416, y=368, )

    pydirectinput.click(x=1223, y=300, )

    pydirectinput.click(x=434, y=452, )

    pydirectinput.click(x=1374, y=1123, )

    pydirectinput.click(x=411, y=373, )

    pydirectinput.click(x=975, y=1087, )

    pydirectinput.click(x=425, y=285, )

    camos3()

    esc_scroll()

    pydirectinput.click(x=472, y=1042, )  # AK 47

    pydirectinput.click(x=773, y=322, )  # GUNSMITH

    pydirectinput.click(x=305, y=366, )

    pydirectinput.click(x=398, y=793, )

    pydirectinput.click(x=794, y=332, )

    pydirectinput.click(x=417, y=540, )

    pydirectinput.click(x=1357, y=1125, )

    pydirectinput.click(x=413, y=455, )

    pydirectinput.click(x=2159, y=363, )

    pydirectinput.click(x=370, y=456, )

    pydirectinput.click(x=1264, y=291, )

    pydirectinput.click(x=416, y=377, )

    camos3()

    esc_scroll()

    pydirectinput.click(x=469, y=1070, )  # RAM-7

    pydirectinput.click(x=775, y=321, )  # GUNSMITH

    pydirectinput.click(x=337, y=368, )

    pydirectinput.click(x=394, y=784, )

    pydirectinput.click(x=778, y=335, )

    pydirectinput.click(x=397, y=454, )

    pydirectinput.click(x=1260, y=301, )

    pydirectinput.click(x=397, y=450, )

    pydirectinput.click(x=1364, y=1125, )

    pydirectinput.click(x=403, y=292, )

    pydirectinput.click(x=969, y=1089, )

    pydirectinput.click(x=399, y=282, )

    camos3()

    esc_scroll()

    pydirectinput.click(x=462, y=1071, )  # GRAU

    pydirectinput.click(x=778, y=318, )  # GUNSMITH

    pydirectinput.click(x=338, y=360, )

    pydirectinput.click(x=399, y=789, )

    pydirectinput.click(x=799, y=339, )

    pydirectinput.click(x=408, y=377, )

    pydirectinput.click(x=1245, y=298, )

    pydirectinput.click(x=421, y=463, )

    pydirectinput.click(x=984, y=1085, )

    pydirectinput.click(x=422, y=281, )

    pydirectinput.click(x=1352, y=1125, )

    pydirectinput.click(x=397, y=369, )

    camos3()

    esc_scroll()

    pydirectinput.click(x=458, y=1067, )  # AMAX

    pydirectinput.click(x=777, y=307, )  # GUNSMITH

    pydirectinput.click(x=333, y=360, )

    pydirectinput.click(x=391, y=704, )

    pydirectinput.click(x=786, y=335, )

    pydirectinput.click(x=416, y=369, )

    pydirectinput.click(x=1211, y=297, )

    pydirectinput.click(x=406, y=445, )

    pydirectinput.click(x=1353, y=1129, )

    pydirectinput.click(x=398, y=285, )

    pydirectinput.click(x=1003, y=1084, )

    pydirectinput.click(x=407, y=291, )

    camos3()

    esc_scroll()

    pydirectinput.click(x=474, y=1064, )  # AN-94

    pydirectinput.click(x=779, y=319, )  # GUNSMITH

    pydirectinput.click(x=282, y=369, )

    pydirectinput.click(x=394, y=709, )

    pydirectinput.click(x=770, y=334, )

    pydirectinput.click(x=383, y=373, )

    pydirectinput.click(x=1261, y=305, )

    pydirectinput.click(x=405, y=459, )

    pydirectinput.click(x=1356, y=1129, )

    pydirectinput.click(x=395, y=367, )

    pydirectinput.click(x=974, y=1083, )

    pydirectinput.click(x=393, y=290, )

    camos3()

    esc_scroll()

    pydirectinput.click(x=476, y=1068, )  # AS-VAL

    pydirectinput.click(x=774, y=324, )  # GUNSMITH

    pydirectinput.click(x=792, y=338, )

    pydirectinput.click(x=402, y=454, )

    pydirectinput.click(x=1274, y=303, )

    pydirectinput.click(x=393, y=461, )

    pydirectinput.click(x=965, y=1086, )

    pydirectinput.click(x=406, y=287, )

    pydirectinput.click(x=1341, y=1122, )

    pydirectinput.click(x=422, y=287, )

    pydirectinput.click(x=1748, y=1127, )

    pydirectinput.click(x=432, y=368, )

    camos3()

    switch_tab()  # switch to SMG

    pydirectinput.click(x=480, y=407, )  # AUG SMG

    pydirectinput.click(x=779, y=318, )  # GUNSMITH

    pydirectinput.click(x=313, y=368, )

    pydirectinput.click(x=399, y=550, )

    pydirectinput.click(x=771, y=333, )

    pydirectinput.click(x=415, y=454, )

    pydirectinput.click(x=1252, y=302, )

    pydirectinput.click(x=404, y=373, )

    pydirectinput.click(x=1353, y=1128, )

    pydirectinput.click(x=430, y=455, )

    pydirectinput.click(x=959, y=1089, )

    pydirectinput.click(x=388, y=293, )

    camos3()

    ESC()

    pydirectinput.click(x=498, y=611, )  # P90

    pydirectinput.click(x=780, y=306, )  # GUNSMITH

    pydirectinput.click(x=329, y=365, )

    pydirectinput.click(x=402, y=619, )

    pydirectinput.click(x=743, y=334, )

    pydirectinput.click(x=426, y=371, )

    pydirectinput.click(x=1252, y=298, )

    pydirectinput.click(x=403, y=370, )

    pydirectinput.click(x=1719, y=1124, )

    pydirectinput.click(x=409, y=286, )

    pydirectinput.click(x=913, y=1079, )

    pydirectinput.click(x=413, y=362, )

    camos3()

    ESC()

    pydirectinput.click(x=461, y=852, )  # MP5 SMG

    pydirectinput.click(x=780, y=339, )  # GUNSMITH

    pydirectinput.click(x=730, y=336, )

    pydirectinput.click(x=410, y=366, )

    pydirectinput.click(x=2146, y=363, )

    pydirectinput.click(x=424, y=538, )

    pydirectinput.click(x=1364, y=1119, )

    pydirectinput.click(x=378, y=287, )

    pydirectinput.click(x=969, y=1091, )

    pydirectinput.click(x=413, y=373, )

    pydirectinput.click(x=2103, y=1083, )

    pydirectinput.click(x=405, y=703, )

    camos3()

    ESC()

    pydirectinput.click(x=443, y=1046, )  # UZI

    pydirectinput.click(x=775, y=320, )  # GUNSMITH

    pydirectinput.click(x=322, y=369, )

    pydirectinput.click(x=434, y=624, )

    pydirectinput.click(x=799, y=328, )

    pydirectinput.click(x=382, y=533, )

    pydirectinput.click(x=1251, y=295, )

    pydirectinput.click(x=390, y=363, )

    pydirectinput.click(x=1339, y=1121, )

    pydirectinput.click(x=411, y=456, )

    pydirectinput.click(x=959, y=1084, )

    pydirectinput.click(x=410, y=285, )

    camos3()

    esc_scroll()

    pydirectinput.click(x=454, y=1065, )  # PP19 BIZON

    pydirectinput.click(x=775, y=317, )  # GUNSMITH

    pydirectinput.click(x=312, y=365, )

    pydirectinput.click(x=408, y=791, )

    pydirectinput.click(x=757, y=335, )

    pydirectinput.click(x=407, y=370, )

    pydirectinput.click(x=1270, y=298, )

    pydirectinput.click(x=416, y=459, )

    pydirectinput.click(x=2135, y=366, )

    pydirectinput.click(x=424, y=369, )

    pydirectinput.click(x=1349, y=1122, )

    pydirectinput.click(x=419, y=287, )

    camos3()

    esc_scroll()

    pydirectinput.click(x=461, y=1071, )  # MP7 SMG

    pydirectinput.click(x=781, y=314, )  # GUNSMITH

    pydirectinput.click(x=329, y=363, )

    pydirectinput.click(x=413, y=786, )

    pydirectinput.click(x=799, y=329, )

    pydirectinput.click(x=437, y=368, )

    pydirectinput.click(x=1262, y=298, )

    pydirectinput.click(x=391, y=373, )

    pydirectinput.click(x=1377, y=1121, )

    pydirectinput.click(x=401, y=371, )

    pydirectinput.click(x=959, y=1087, )

    pydirectinput.click(x=390, y=365, )

    camos3()

    esc_scroll()

    pydirectinput.click(x=465, y=1068, )  # STRIKER 45 SMG

    pydirectinput.click(x=785, y=323, )  # GUNSMITH

    pydirectinput.click(x=332, y=361, )

    pydirectinput.click(x=403, y=791, )

    pydirectinput.click(x=797, y=335, )

    pydirectinput.click(x=404, y=368, )

    pydirectinput.click(x=1260, y=299, )

    pydirectinput.click(x=387, y=369, )

    pydirectinput.click(x=1390, y=1119, )

    pydirectinput.click(x=415, y=367, )

    pydirectinput.click(x=984, y=1085, )

    pydirectinput.click(x=378, y=372, )

    camos3()

    esc_scroll()

    pydirectinput.click(x=475, y=1063, )  # FENNIC SMG

    pydirectinput.click(x=782, y=326, )  # GUNSMITH

    pydirectinput.click(x=764, y=334, )

    pydirectinput.click(x=415, y=367, )

    pydirectinput.click(x=1252, y=299, )

    pydirectinput.click(x=411, y=371, )

    pydirectinput.click(x=1370, y=1122, )

    pydirectinput.click(x=404, y=286, )

    pydirectinput.click(x=2172, y=1085, )

    pydirectinput.click(x=393, y=875, )

    pydirectinput.click(x=972, y=1090, )

    pydirectinput.click(x=389, y=284, )

    camos3()

    esc_scroll()

    pydirectinput.click(x=471, y=1062, )  # ISO SMG

    pydirectinput.click(x=776, y=321, )  # GUNSMITH

    pydirectinput.click(x=803, y=334, )

    pydirectinput.click(x=416, y=538, )

    pydirectinput.click(x=1266, y=298, )

    pydirectinput.click(x=425, y=377, )

    pydirectinput.click(x=972, y=1083, )

    pydirectinput.click(x=392, y=377, )

    pydirectinput.click(x=1355, y=1120, )

    pydirectinput.click(x=404, y=375, )

    pydirectinput.click(x=2166, y=1082, )

    pydirectinput.click(x=385, y=875, )

    camos3()

    esc_scroll()

    pydirectinput.click(x=471, y=1075, )  # sc9 smg

    pydirectinput.click(x=772, y=323, )  # GUNSMITH

    pydirectinput.click(x=746, y=336, )

    pydirectinput.click(x=436, y=622, )

    pydirectinput.click(x=1258, y=297, )

    pydirectinput.click(x=414, y=372, )

    pydirectinput.click(x=2129, y=362, )

    pydirectinput.click(x=423, y=451, )

    pydirectinput.click(x=2122, y=1082, )

    pydirectinput.click(x=379, y=708, )

    pydirectinput.click(x=1366, y=1126, )

    pydirectinput.click(x=411, y=454, )

    camos3()

    switch_tab_shotgun()

    pydirectinput.click(x=470, y=408, )  # MODEL 680

    pydirectinput.click(x=776, y=322, )  # GUNDMITH

    pydirectinput.click(x=299, y=364, )

    pydirectinput.click(x=379, y=708, )

    pydirectinput.click(x=781, y=332, )

    pydirectinput.click(x=417, y=453, )

    pydirectinput.click(x=1225, y=295, )

    pydirectinput.click(x=379, y=367, )

    pydirectinput.click(x=2160, y=367, )

    pydirectinput.click(x=441, y=456, )

    pydirectinput.click(x=1301, y=1131, )

    pydirectinput.click(x=396, y=622, )

    camos3()

    ESC()

    pydirectinput.click(x=486, y=629, )  # R90

    pydirectinput.click(x=777, y=328, )  # GUNSMITH

    pydirectinput.click(x=350, y=365, )

    pydirectinput.click(x=401, y=703, )

    pydirectinput.click(x=797, y=332, )

    pydirectinput.click(x=394, y=283, )

    pydirectinput.click(x=1210, y=297, )

    pydirectinput.click(x=376, y=371, )

    pydirectinput.click(x=1330, y=1123, )

    pydirectinput.click(x=407, y=458, )

    pydirectinput.click(x=1739, y=1126, )

    pydirectinput.click(x=404, y=455, )

    camos3()

    ESC()

    pydirectinput.click(x=463, y=848, )  # 725

    pydirectinput.click(x=776, y=327, )  # GUNSMITH

    pydirectinput.click(x=348, y=363, )

    pydirectinput.click(x=394, y=789, )

    pydirectinput.click(x=761, y=334, )

    pydirectinput.click(x=408, y=365, )

    pydirectinput.click(x=1212, y=294, )

    pydirectinput.click(x=454, y=375, )

    pydirectinput.click(x=2143, y=363, )

    pydirectinput.click(x=383, y=455, )

    pydirectinput.click(x=1692, y=1123, )

    pydirectinput.click(x=414, y=284, )

    camos3()

    ESC()

    pydirectinput.click(x=458, y=1077, )  # ORIGIN 12

    pydirectinput.click(x=776, y=323, )  # GUNSMITH

    pydirectinput.click(x=320, y=367, )

    pydirectinput.click(x=397, y=876, )

    pydirectinput.click(x=768, y=333, )

    pydirectinput.click(x=393, y=448, )

    pydirectinput.click(x=1266, y=301, )

    pydirectinput.click(x=378, y=369, )

    pydirectinput.click(x=1372, y=1127, )

    pydirectinput.click(x=403, y=458, )

    pydirectinput.click(x=1751, y=1126, )

    pydirectinput.click(x=419, y=456, )

    camos3()

    esc_scroll()

    pydirectinput.click(x=436, y=1059, )  # VLK

    pydirectinput.click(x=777, y=324, )  # GUNSMITH

    pydirectinput.doubleClick(x=1336, y=671, )  # click screen

    pydirectinput.click(x=1708, y=1128, )  # not working

    pydirectinput.click(x=406, y=458, )  # NOT WORKING

    pydirectinput.click(x=795, y=335, )

    pydirectinput.click(x=420, y=458, )

    pydirectinput.click(x=1224, y=302, )

    pydirectinput.click(x=391, y=373, )

    pydirectinput.click(x=1311, y=1126, )

    pydirectinput.click(x=405, y=536, )

    pydirectinput.click(x=945, y=1088, )

    pydirectinput.click(x=351, y=288, )

    camos3()

    esc_scroll()

    pydirectinput.click(x=457, y=1075, )  # JAK 12

    pydirectinput.click(x=776, y=307, )  # GUNSMITH

    pydirectinput.doubleClick(x=1336, y=671, )  # click screen

    pydirectinput.click(x=333, y=367, )

    pydirectinput.click(x=408, y=789, )

    pydirectinput.click(x=789, y=336, )

    pydirectinput.click(x=418, y=455, )

    pydirectinput.click(x=1261, y=301, )

    pydirectinput.click(x=401, y=374, )

    pydirectinput.click(x=1359, y=1120, )

    pydirectinput.click(x=397, y=456, )

    pydirectinput.click(x=956, y=1090, )

    pydirectinput.click(x=393, y=299, )

    camos3()

    switch_tab_LMG()

    pydirectinput.click(x=476, y=408, )  # pkm

    pydirectinput.click(x=774, y=319, )  # gunsmith

    pydirectinput.click(x=322, y=363, )

    pydirectinput.click(x=402, y=371, )

    pydirectinput.click(x=749, y=333, )

    pydirectinput.click(x=384, y=365, )

    pydirectinput.click(x=1183, y=293, )

    pydirectinput.click(x=389, y=452, )

    pydirectinput.click(x=2178, y=362, )

    pydirectinput.click(x=398, y=454, )

    pydirectinput.click(x=962, y=1086, )

    pydirectinput.click(x=421, y=286, )

    camos3()

    ESC()

    pydirectinput.click(x=475, y=640, )  # SA87

    pydirectinput.click(x=775, y=321, )  # GUNSMITH

    pydirectinput.click(x=302, y=365, )

    pydirectinput.click(x=398, y=785, )

    pydirectinput.click(x=795, y=338, )

    pydirectinput.click(x=413, y=366, )

    pydirectinput.click(x=1215, y=294, )

    pydirectinput.click(x=409, y=452, )

    pydirectinput.click(x=1356, y=1123, )

    pydirectinput.click(x=404, y=364, )

    pydirectinput.click(x=912, y=1088, )

    pydirectinput.click(x=390, y=282, )

    camos3()

    ESC()

    pydirectinput.click(x=468, y=823, )  # M91

    pydirectinput.click(x=776, y=321, )  # GUNSMITH

    pydirectinput.click(x=309, y=364, )

    pydirectinput.click(x=416, y=789, )

    pydirectinput.click(x=753, y=335, )

    pydirectinput.click(x=408, y=457, )

    pydirectinput.click(x=1197, y=298, )

    pydirectinput.click(x=385, y=453, )

    pydirectinput.click(x=2128, y=361, )

    pydirectinput.click(x=417, y=535, )

    pydirectinput.click(x=954, y=1088, )

    pydirectinput.click(x=415, y=279, )

    camos3()

    ESC()

    pydirectinput.click(x=465, y=1063, )  # MG34

    pydirectinput.click(x=777, y=324, )  # GUMSMITH

    pydirectinput.click(x=281, y=364, )

    pydirectinput.click(x=393, y=790, )

    pydirectinput.click(x=766, y=333, )

    pydirectinput.click(x=430, y=458, )

    pydirectinput.click(x=1246, y=296, )

    pydirectinput.click(x=388, y=366, )

    pydirectinput.click(x=1355, y=1122, )

    pydirectinput.click(x=428, y=285, )

    pydirectinput.click(x=932, y=1083, )

    pydirectinput.click(x=385, y=284, )

    camos3()

    esc_scroll()

    pydirectinput.click(x=451, y=1056, )  # HOLGER

    pydirectinput.click(x=778, y=317, )  # GUNSMITH

    pydirectinput.click(x=305, y=359, )

    pydirectinput.click(x=400, y=783, )

    pydirectinput.click(x=743, y=337, )

    pydirectinput.click(x=391, y=284, )

    pydirectinput.click(x=1197, y=295, )

    pydirectinput.click(x=385, y=456, )

    pydirectinput.click(x=1361, y=1126, )

    pydirectinput.click(x=404, y=288, )

    pydirectinput.click(x=945, y=1087, )

    pydirectinput.click(x=395, y=288, )

    camos3()

    esc_scroll()

    pydirectinput.click(x=458, y=1068, )  # BRUEN MK9

    pydirectinput.click(x=776, y=318, )  # GUNSMITH

    pydirectinput.click(x=312, y=365, )

    pydirectinput.click(x=377, y=781, )

    pydirectinput.click(x=788, y=332, )

    pydirectinput.click(x=388, y=371, )

    pydirectinput.click(x=1199, y=297, )

    pydirectinput.click(x=370, y=449, )

    pydirectinput.click(x=1325, y=1123, )

    pydirectinput.click(x=408, y=370, )

    pydirectinput.click(x=931, y=1089, )

    pydirectinput.click(x=428, y=282, )

    camos3()

    esc_scroll()

    pydirectinput.click(x=456, y=1067, )  # finn

    pydirectinput.click(x=773, y=316, )  # GUNSMITH

    pydirectinput.click(x=308, y=364, )

    pydirectinput.click(x=400, y=790, )

    pydirectinput.click(x=800, y=332, )

    pydirectinput.click(x=390, y=705, )

    pydirectinput.click(x=1227, y=296, )

    pydirectinput.click(x=417, y=281, )

    pydirectinput.click(x=1352, y=1121, )

    pydirectinput.click(x=397, y=374, )

    pydirectinput.click(x=958, y=1089, )

    pydirectinput.click(x=383, y=293, )

    camos3()

    esc_scroll()

    pydirectinput.click(x=459, y=1081, )  # RAAL MG

    pydirectinput.click(x=774, y=316, )  # GUNSMITH

    pydirectinput.click(x=290, y=361, )

    pydirectinput.click(x=382, y=787, )

    pydirectinput.click(x=750, y=337, )

    pydirectinput.click(x=395, y=370, )

    pydirectinput.click(x=1218, y=295, )

    pydirectinput.click(x=396, y=288, )

    pydirectinput.click(x=1319, y=1124, )

    pydirectinput.click(x=393, y=364, )

    pydirectinput.click(x=916, y=1085, )

    pydirectinput.click(x=391, y=538, )

    camos3()

    switch_tab_marksman()

    pydirectinput.click(x=474, y=385, )  # EBR

    pydirectinput.click(x=777, y=323, )  # GUNSMITH

    pydirectinput.click(x=311, y=366, )

    pydirectinput.click(x=418, y=787, )

    pydirectinput.click(x=782, y=332, )

    pydirectinput.click(x=409, y=460, )

    pydirectinput.click(x=1185, y=297, )

    pydirectinput.click(x=404, y=290, )

    pydirectinput.click(x=1332, y=1126, )

    pydirectinput.click(x=409, y=369, )

    pydirectinput.click(x=995, y=1083, )

    pydirectinput.click(x=397, y=279, )

    camos3()

    ESC()

    pydirectinput.click(x=467, y=624, )  # MK2 CARBINE

    pydirectinput.click(x=776, y=324, )  # GUNSMITH

    pydirectinput.click(x=273, y=362, )

    pydirectinput.click(x=380, y=793, )

    pydirectinput.click(x=757, y=334, )

    pydirectinput.click(x=396, y=453, )

    pydirectinput.click(x=1243, y=297, )

    pydirectinput.click(x=384, y=284, )

    pydirectinput.click(x=1663, y=331, )

    pydirectinput.click(x=344, y=1042, )

    pydirectinput.click(x=1688, y=1128, )

    pydirectinput.click(x=386, y=368, )

    camos3()

    ESC()

    pydirectinput.click(x=474, y=839, )  # KAR98K

    pydirectinput.click(x=775, y=327, )  # GUNSMITH

    pydirectinput.click(x=286, y=360, )

    pydirectinput.click(x=371, y=623, )

    pydirectinput.click(x=790, y=334, )

    pydirectinput.click(x=398, y=451, )

    pydirectinput.click(x=1271, y=298, )

    pydirectinput.click(x=439, y=287, )

    pydirectinput.click(x=1686, y=330, )

    pydirectinput.click(x=337, y=875, )

    pydirectinput.click(x=1727, y=1123, )

    pydirectinput.click(x=413, y=289, )

    camos3()

    ESC()

    pydirectinput.click(x=465, y=1061, )  # CROSSBOW

    pydirectinput.click(x=777, y=326, )  # GUNSMITH

    pydirectinput.click(x=290, y=366, )

    pydirectinput.click(x=395, y=280, )

    pydirectinput.click(x=777, y=329, )

    pydirectinput.click(x=384, y=457, )

    pydirectinput.click(x=1233, y=295, )

    pydirectinput.click(x=389, y=282, )

    pydirectinput.click(x=1287, y=1123, )

    pydirectinput.click(x=403, y=280, )

    pydirectinput.click(x=937, y=1085, )

    pydirectinput.click(x=391, y=283, )

    camos3()

    esc_scroll()

    pydirectinput.click(x=477, y=1062, )  # sks

    pydirectinput.click(x=771, y=322, )  # gunsmith

    pydirectinput.click(x=286, y=367, )

    pydirectinput.click(x=389, y=791, )

    pydirectinput.click(x=739, y=338, )

    pydirectinput.click(x=381, y=457, )

    pydirectinput.click(x=1254, y=298, )

    pydirectinput.click(x=449, y=288, )

    pydirectinput.click(x=1352, y=1120, )

    pydirectinput.click(x=392, y=283, )

    pydirectinput.click(x=974, y=1085, )

    pydirectinput.click(x=394, y=287, )

    camos3()

    esc_scroll()

    pydirectinput.click(x=447, y=1074, )  # sp-r 208

    pydirectinput.click(x=776, y=322, )  # GUNSMITH\

    pydirectinput.click(x=285, y=364, )

    pydirectinput.click(x=372, y=792, )

    pydirectinput.click(x=768, y=335, )

    pydirectinput.click(x=425, y=456, )

    pydirectinput.click(x=1200, y=300, )

    pydirectinput.click(x=451, y=284, )

    pydirectinput.click(x=1644, y=334, )

    pydirectinput.click(x=360, y=1040, )

    pydirectinput.click(x=1303, y=1123, )

    pydirectinput.click(x=404, y=456, )

    camos3()

    switch_tab_sniper()

    pydirectinput.click(x=458, y=409, )  # Dragunov

    pydirectinput.click(x=776, y=323, )  # GUNSMITH

    pydirectinput.click(x=267, y=366, )

    pydirectinput.click(x=416, y=362, )

    pydirectinput.click(x=738, y=331, )

    pydirectinput.click(x=378, y=372, )

    pydirectinput.click(x=1275, y=293, )

    pydirectinput.click(x=456, y=280, )

    pydirectinput.click(x=2100, y=360, )

    pydirectinput.click(x=436, y=535, )

    pydirectinput.click(x=2100, y=1091, )

    pydirectinput.click(x=372, y=455, )

    camos3()

    esc_scroll()

    pydirectinput.click(x=480, y=621, )  # HDR

    pydirectinput.click(x=772, y=321, )  # GUNSMITH

    pydirectinput.click(x=806, y=337, )

    pydirectinput.click(x=414, y=452, )

    pydirectinput.click(x=1206, y=300, )

    pydirectinput.click(x=315, y=296, )

    pydirectinput.click(x=2111, y=365, )

    pydirectinput.click(x=426, y=284, )

    pydirectinput.click(x=2091, y=1084, )

    pydirectinput.click(x=366, y=536, )

    pydirectinput.click(x=936, y=1081, )

    pydirectinput.click(x=402, y=289, )

    camos3()

    ESC()

    pydirectinput.click(x=431, y=856, )  # AX50

    pydirectinput.click(x=758, y=317, )  # GUNSMITH

    pydirectinput.click(x=764, y=327, )

    pydirectinput.click(x=365, y=360, )

    pydirectinput.click(x=1218, y=291, )

    pydirectinput.click(x=422, y=271, )

    pydirectinput.click(x=2149, y=351, )

    pydirectinput.click(x=362, y=450, )

    pydirectinput.click(x=1748, y=1154, )

    pydirectinput.click(x=365, y=453, )

    pydirectinput.click(x=2161, y=1111, )

    pydirectinput.click(x=355, y=364, )

    camos3()

    ESC()

    pydirectinput.click(x=422, y=1048, )  # RYTEC

    pydirectinput.click(x=777, y=319, )  # GUNSMITH

    pydirectinput.click(x=321, y=370, )

    pydirectinput.click(x=387, y=371, )

    pydirectinput.click(x=762, y=339, )

    pydirectinput.click(x=410, y=287, )

    pydirectinput.click(x=1222, y=288, )

    pydirectinput.click(x=362, y=283, )

    pydirectinput.click(x=1730, y=1128, )

    pydirectinput.click(x=381, y=454, )

    pydirectinput.click(x=2096, y=361, )

    pydirectinput.click(x=393, y=454, )

    camos3()

    switch_to_pistol()

    pydirectinput.click(x=778, y=578, )  # X16 PISTOL PLUS GUNSMITH

    pydirectinput.click(x=348, y=361, )

    pydirectinput.click(x=420, y=364, )

    pydirectinput.click(x=806, y=335, )

    pydirectinput.click(x=399, y=446, )

    pydirectinput.click(x=1210, y=297, )

    pydirectinput.click(x=400, y=454, )

    pydirectinput.click(x=1344, y=1123, )

    pydirectinput.click(x=376, y=371, )

    pydirectinput.click(x=921, y=1083, )

    pydirectinput.click(x=397, y=284, )

    camos3()

    ESC_pistol()

    pydirectinput.click(x=451, y=616, )  # 1911

    pydirectinput.click(x=773, y=579, )  # GUNSMITH

    pydirectinput.click(x=296, y=363, )

    pydirectinput.click(x=392, y=710, )

    pydirectinput.click(x=807, y=332, )

    pydirectinput.click(x=408, y=449, )

    pydirectinput.click(x=1189, y=299, )

    pydirectinput.click(x=355, y=370, )

    pydirectinput.click(x=1335, y=1125, )

    pydirectinput.click(x=394, y=376, )

    pydirectinput.click(x=1000, y=1082, )

    pydirectinput.click(x=377, y=281, )

    camos3()

    ESC_pistol()

    pydirectinput.click(x=472, y=843, )  # .357

    pydirectinput.click(x=771, y=577, )  # GUNSMITH

    pydirectinput.click(x=725, y=331, )

    pydirectinput.click(x=432, y=449, )

    pydirectinput.click(x=1251, y=299, )

    pydirectinput.click(x=427, y=366, )

    pydirectinput.click(x=1332, y=1128, )

    pydirectinput.click(x=434, y=281, )

    pydirectinput.click(x=2130, y=1088, )

    pydirectinput.click(x=371, y=1044, )

    pydirectinput.click(x=991, y=1089, )

    pydirectinput.click(x=429, y=284, )

    camos3()

    ESC_pistol()

    pydirectinput.click(x=472, y=1053, )  # M19

    pydirectinput.click(x=776, y=582, )  # GUNSMITH

    pydirectinput.click(x=286, y=366, )

    pydirectinput.click(x=397, y=449, )

    pydirectinput.click(x=758, y=332, )

    pydirectinput.click(x=397, y=372, )

    pydirectinput.click(x=1225, y=296, )

    pydirectinput.click(x=393, y=363, )

    pydirectinput.click(x=1356, y=1123, )

    pydirectinput.click(x=425, y=371, )

    pydirectinput.click(x=938, y=1087, )

    pydirectinput.click(x=396, y=282, )

    camos3()

    ESC_pistol_SCROLL()

    pydirectinput.click(x=464, y=1069, )  # 50OG

    pydirectinput.click(x=776, y=579, )  # GUNSMITH

    pydirectinput.click(x=275, y=367, )

    pydirectinput.click(x=395, y=458, )

    pydirectinput.click(x=769, y=332, )

    pydirectinput.click(x=397, y=283, )

    pydirectinput.click(x=1220, y=298, )

    pydirectinput.click(x=412, y=369, )

    pydirectinput.click(x=1326, y=1124, )

    pydirectinput.click(x=394, y=371, )

    pydirectinput.click(x=993, y=1085, )

    pydirectinput.click(x=396, y=282, )

    camos3()

    ESC_pistol_SCROLL()

    pydirectinput.click(x=456, y=1058, )  # RENETTI

    pydirectinput.click(x=776, y=581, )  # GUNSMITH

    pydirectinput.click(x=295, y=366, )

    pydirectinput.click(x=399, y=714, )

    pydirectinput.click(x=783, y=332, )

    pydirectinput.click(x=440, y=452, )

    pydirectinput.click(x=1171, y=302, )

    pydirectinput.click(x=333, y=367, )

    pydirectinput.click(x=1308, y=1127, )

    pydirectinput.click(x=408, y=373, )

    pydirectinput.click(x=971, y=1090, )

    pydirectinput.click(x=402, y=287, )

    camos3()

    ESC_pistol_SCROLL()

    pydirectinput.click(x=450, y=1062, )  # SYKOV

    pydirectinput.click(x=780, y=574, )  # GUNSMITH

    pydirectinput.click(x=277, y=362, )

    pydirectinput.click(x=397, y=704, )

    pydirectinput.click(x=771, y=329, )

    pydirectinput.click(x=404, y=455, )

    pydirectinput.click(x=1282, y=300, )

    pydirectinput.click(x=387, y=373, )

    pydirectinput.click(x=1281, y=1121, )

    pydirectinput.click(x=364, y=369, )

    pydirectinput.click(x=991, y=1081, )

    pydirectinput.click(x=417, y=287, )

    camos3()


# ---OBSIDIAN-HOT&COLD-RAINBOW-BANDED---#
def camo_4():
    pyautogui.alert('Press "OK" To Being')

    pydirectinput.tripleClick(x=1655, y=587, )

    pydirectinput.click(x=409, y=269, )  # kilo

    # pydirectinput.click(x=777, y=312,)

    pydirectinput.click(x=291, y=366, )

    pydirectinput.click(x=384, y=794, )

    pydirectinput.click(x=779, y=335, )

    pydirectinput.click(x=413, y=372, )

    pydirectinput.click(x=1247, y=300, )

    pydirectinput.click(x=440, y=454, )

    pydirectinput.click(x=1356, y=1119, )

    pydirectinput.click(x=442, y=370, )

    pydirectinput.click(x=936, y=1086, )

    pydirectinput.click(x=418, y=278, )  # kilo end

    camos4()

    ESC()  # exit kilo

    time.sleep(0.4)  # fal
    pydirectinput.click(x=501, y=620, )
    time.sleep(.05)
    pydirectinput.click(x=786, y=332, )

    pydirectinput.click(x=334, y=364, )

    pydirectinput.click(x=420, y=706, )

    pydirectinput.click(x=807, y=335, )

    pydirectinput.click(x=420, y=366, )

    pydirectinput.click(x=1270, y=301, )

    pydirectinput.click(x=397, y=454, )

    pydirectinput.click(x=1363, y=1125, )

    pydirectinput.click(x=411, y=364, )

    pydirectinput.click(x=956, y=1088, )

    pydirectinput.click(x=391, y=282, )  # FAL END

    camos4()

    ESC()

    pydirectinput.click(x=477, y=841, )  # M4

    pydirectinput.click(x=776, y=310, )  # GUNSSMITH

    pydirectinput.click(x=319, y=366, )

    pydirectinput.click(x=406, y=793, )

    pydirectinput.click(x=799, y=339, )

    pydirectinput.click(x=408, y=541, )

    pydirectinput.click(x=1258, y=299, )

    pydirectinput.click(x=445, y=446, )

    pydirectinput.click(x=1373, y=1121, )

    pydirectinput.click(x=446, y=373, )

    pydirectinput.click(x=960, y=1086, )

    pydirectinput.click(x=421, y=285, )

    camos4()

    ESC()

    pydirectinput.click(x=513, y=1076, )  # FR 5.56

    pydirectinput.click(x=783, y=315, )  # GUNSMITH

    pydirectinput.click(x=323, y=370, )

    pydirectinput.click(x=418, y=707, )

    pydirectinput.click(x=802, y=336, )

    pydirectinput.click(x=431, y=371, )

    pydirectinput.click(x=1234, y=292, )

    pydirectinput.click(x=414, y=452, )

    pydirectinput.click(x=1344, y=1124, )

    pydirectinput.click(x=403, y=376, )

    pydirectinput.click(x=964, y=1090, )

    pydirectinput.click(x=423, y=283, )  # FR 5.56 END

    camos4()

    esc_scroll()

    pydirectinput.click(x=491, y=1054, )  # ODEN

    pydirectinput.click(x=781, y=327, )  # GUNSMITH

    pydirectinput.click(x=322, y=371, )

    pydirectinput.click(x=410, y=538, )

    pydirectinput.click(x=800, y=340, )

    pydirectinput.click(x=423, y=287, )

    pydirectinput.click(x=1266, y=292, )

    pydirectinput.click(x=418, y=455, )

    pydirectinput.click(x=1379, y=1121, )

    pydirectinput.click(x=412, y=373, )

    pydirectinput.click(x=962, y=1089, )

    pydirectinput.click(x=423, y=288, )

    camos4()

    esc_scroll()

    pydirectinput.click(x=470, y=1068, )  # m13

    pydirectinput.click(x=773, y=309, )  # GUNSMITH

    pydirectinput.click(x=332, y=362, )

    pydirectinput.click(x=410, y=786, )

    pydirectinput.click(x=807, y=335, )

    pydirectinput.click(x=418, y=455, )

    pydirectinput.click(x=1258, y=300, )

    pydirectinput.click(x=411, y=376, )

    pydirectinput.click(x=1349, y=1124, )

    pydirectinput.click(x=429, y=450, )

    pydirectinput.click(x=965, y=1083, )

    pydirectinput.click(x=424, y=450, )

    camos4()

    esc_scroll()

    pydirectinput.click(x=486, y=1066, )  # FN SCAR

    pydirectinput.click(x=777, y=314, )  # GUNSMITH

    pydirectinput.click(x=335, y=365, )

    pydirectinput.click(x=415, y=785, )

    pydirectinput.click(x=816, y=336, )

    pydirectinput.click(x=416, y=368, )

    pydirectinput.click(x=1223, y=300, )

    pydirectinput.click(x=434, y=452, )

    pydirectinput.click(x=1374, y=1123, )

    pydirectinput.click(x=411, y=373, )

    pydirectinput.click(x=975, y=1087, )

    pydirectinput.click(x=425, y=285, )

    camos4()

    esc_scroll()

    pydirectinput.click(x=472, y=1042, )  # AK 47

    pydirectinput.click(x=773, y=322, )  # GUNSMITH

    pydirectinput.click(x=305, y=366, )

    pydirectinput.click(x=398, y=793, )

    pydirectinput.click(x=794, y=332, )

    pydirectinput.click(x=417, y=540, )

    pydirectinput.click(x=1357, y=1125, )

    pydirectinput.click(x=413, y=455, )

    pydirectinput.click(x=2159, y=363, )

    pydirectinput.click(x=370, y=456, )

    pydirectinput.click(x=1264, y=291, )

    pydirectinput.click(x=416, y=377, )

    camos4()

    esc_scroll()

    pydirectinput.click(x=469, y=1070, )  # RAM-7

    pydirectinput.click(x=775, y=321, )  # GUNSMITH

    pydirectinput.click(x=337, y=368, )

    pydirectinput.click(x=394, y=784, )

    pydirectinput.click(x=778, y=335, )

    pydirectinput.click(x=397, y=454, )

    pydirectinput.click(x=1260, y=301, )

    pydirectinput.click(x=397, y=450, )

    pydirectinput.click(x=1364, y=1125, )

    pydirectinput.click(x=403, y=292, )

    pydirectinput.click(x=969, y=1089, )

    pydirectinput.click(x=399, y=282, )

    camos4()

    esc_scroll()

    pydirectinput.click(x=462, y=1071, )  # GRAU

    pydirectinput.click(x=778, y=318, )  # GUNSMITH

    pydirectinput.click(x=338, y=360, )

    pydirectinput.click(x=399, y=789, )

    pydirectinput.click(x=799, y=339, )

    pydirectinput.click(x=408, y=377, )

    pydirectinput.click(x=1245, y=298, )

    pydirectinput.click(x=421, y=463, )

    pydirectinput.click(x=984, y=1085, )

    pydirectinput.click(x=422, y=281, )

    pydirectinput.click(x=1352, y=1125, )

    pydirectinput.click(x=397, y=369, )

    camos4()

    esc_scroll()

    pydirectinput.click(x=458, y=1067, )  # AMAX

    pydirectinput.click(x=777, y=307, )  # GUNSMITH

    pydirectinput.click(x=333, y=360, )

    pydirectinput.click(x=391, y=704, )

    pydirectinput.click(x=786, y=335, )

    pydirectinput.click(x=416, y=369, )

    pydirectinput.click(x=1211, y=297, )

    pydirectinput.click(x=406, y=445, )

    pydirectinput.click(x=1353, y=1129, )

    pydirectinput.click(x=398, y=285, )

    pydirectinput.click(x=1003, y=1084, )

    pydirectinput.click(x=407, y=291, )

    camos4()

    esc_scroll()

    pydirectinput.click(x=474, y=1064, )  # AN-94

    pydirectinput.click(x=779, y=319, )  # GUNSMITH

    pydirectinput.click(x=282, y=369, )

    pydirectinput.click(x=394, y=709, )

    pydirectinput.click(x=770, y=334, )

    pydirectinput.click(x=383, y=373, )

    pydirectinput.click(x=1261, y=305, )

    pydirectinput.click(x=405, y=459, )

    pydirectinput.click(x=1356, y=1129, )

    pydirectinput.click(x=395, y=367, )

    pydirectinput.click(x=974, y=1083, )

    pydirectinput.click(x=393, y=290, )

    camos4()

    esc_scroll()

    pydirectinput.click(x=476, y=1068, )  # AS-VAL

    pydirectinput.click(x=774, y=324, )  # GUNSMITH

    pydirectinput.click(x=792, y=338, )

    pydirectinput.click(x=402, y=454, )

    pydirectinput.click(x=1274, y=303, )

    pydirectinput.click(x=393, y=461, )

    pydirectinput.click(x=965, y=1086, )

    pydirectinput.click(x=406, y=287, )

    pydirectinput.click(x=1341, y=1122, )

    pydirectinput.click(x=422, y=287, )

    pydirectinput.click(x=1748, y=1127, )

    pydirectinput.click(x=432, y=368, )

    camos4()

    switch_tab()  # switch to SMG

    pydirectinput.click(x=480, y=407, )  # AUG SMG

    pydirectinput.click(x=779, y=318, )  # GUNSMITH

    pydirectinput.click(x=313, y=368, )

    pydirectinput.click(x=399, y=550, )

    pydirectinput.click(x=771, y=333, )

    pydirectinput.click(x=415, y=454, )

    pydirectinput.click(x=1252, y=302, )

    pydirectinput.click(x=404, y=373, )

    pydirectinput.click(x=1353, y=1128, )

    pydirectinput.click(x=430, y=455, )

    pydirectinput.click(x=959, y=1089, )

    pydirectinput.click(x=388, y=293, )

    camos4()

    ESC()

    pydirectinput.click(x=498, y=611, )  # P90

    pydirectinput.click(x=780, y=306, )  # GUNSMITH

    pydirectinput.click(x=329, y=365, )

    pydirectinput.click(x=402, y=619, )

    pydirectinput.click(x=743, y=334, )

    pydirectinput.click(x=426, y=371, )

    pydirectinput.click(x=1252, y=298, )

    pydirectinput.click(x=403, y=370, )

    pydirectinput.click(x=1719, y=1124, )

    pydirectinput.click(x=409, y=286, )

    pydirectinput.click(x=913, y=1079, )

    pydirectinput.click(x=413, y=362, )

    camos4()

    ESC()

    pydirectinput.click(x=461, y=852, )  # MP5 SMG

    pydirectinput.click(x=780, y=339, )  # GUNSMITH

    pydirectinput.click(x=730, y=336, )

    pydirectinput.click(x=410, y=366, )

    pydirectinput.click(x=2146, y=363, )

    pydirectinput.click(x=424, y=538, )

    pydirectinput.click(x=1364, y=1119, )

    pydirectinput.click(x=378, y=287, )

    pydirectinput.click(x=969, y=1091, )

    pydirectinput.click(x=413, y=373, )

    pydirectinput.click(x=2103, y=1083, )

    pydirectinput.click(x=405, y=703, )

    camos4()

    ESC()

    pydirectinput.click(x=443, y=1046, )  # UZI

    pydirectinput.click(x=775, y=320, )  # GUNSMITH

    pydirectinput.click(x=322, y=369, )

    pydirectinput.click(x=434, y=624, )

    pydirectinput.click(x=799, y=328, )

    pydirectinput.click(x=382, y=533, )

    pydirectinput.click(x=1251, y=295, )

    pydirectinput.click(x=390, y=363, )

    pydirectinput.click(x=1339, y=1121, )

    pydirectinput.click(x=411, y=456, )

    pydirectinput.click(x=959, y=1084, )

    pydirectinput.click(x=410, y=285, )

    camos4()

    esc_scroll()

    pydirectinput.click(x=454, y=1065, )  # PP19 BIZON

    pydirectinput.click(x=775, y=317, )  # GUNSMITH

    pydirectinput.click(x=312, y=365, )

    pydirectinput.click(x=408, y=791, )

    pydirectinput.click(x=757, y=335, )

    pydirectinput.click(x=407, y=370, )

    pydirectinput.click(x=1270, y=298, )

    pydirectinput.click(x=416, y=459, )

    pydirectinput.click(x=2135, y=366, )

    pydirectinput.click(x=424, y=369, )

    pydirectinput.click(x=1349, y=1122, )

    pydirectinput.click(x=419, y=287, )

    camos4()

    esc_scroll()

    pydirectinput.click(x=461, y=1071, )  # MP7 SMG

    pydirectinput.click(x=781, y=314, )  # GUNSMITH

    pydirectinput.click(x=329, y=363, )

    pydirectinput.click(x=413, y=786, )

    pydirectinput.click(x=799, y=329, )

    pydirectinput.click(x=437, y=368, )

    pydirectinput.click(x=1262, y=298, )

    pydirectinput.click(x=391, y=373, )

    pydirectinput.click(x=1377, y=1121, )

    pydirectinput.click(x=401, y=371, )

    pydirectinput.click(x=959, y=1087, )

    pydirectinput.click(x=390, y=365, )

    camos4()

    esc_scroll()

    pydirectinput.click(x=465, y=1068, )  # STRIKER 45 SMG

    pydirectinput.click(x=785, y=323, )  # GUNSMITH

    pydirectinput.click(x=332, y=361, )

    pydirectinput.click(x=403, y=791, )

    pydirectinput.click(x=797, y=335, )

    pydirectinput.click(x=404, y=368, )

    pydirectinput.click(x=1260, y=299, )

    pydirectinput.click(x=387, y=369, )

    pydirectinput.click(x=1390, y=1119, )

    pydirectinput.click(x=415, y=367, )

    pydirectinput.click(x=984, y=1085, )

    pydirectinput.click(x=378, y=372, )

    camos4()

    esc_scroll()

    pydirectinput.click(x=475, y=1063, )  # FENNIC SMG

    pydirectinput.click(x=782, y=326, )  # GUNSMITH

    pydirectinput.click(x=764, y=334, )

    pydirectinput.click(x=415, y=367, )

    pydirectinput.click(x=1252, y=299, )

    pydirectinput.click(x=411, y=371, )

    pydirectinput.click(x=1370, y=1122, )

    pydirectinput.click(x=404, y=286, )

    pydirectinput.click(x=2172, y=1085, )

    pydirectinput.click(x=393, y=875, )

    pydirectinput.click(x=972, y=1090, )

    pydirectinput.click(x=389, y=284, )

    camos4()

    esc_scroll()

    pydirectinput.click(x=471, y=1062, )  # ISO SMG

    pydirectinput.click(x=776, y=321, )  # GUNSMITH

    pydirectinput.click(x=803, y=334, )

    pydirectinput.click(x=416, y=538, )

    pydirectinput.click(x=1266, y=298, )

    pydirectinput.click(x=425, y=377, )

    pydirectinput.click(x=972, y=1083, )

    pydirectinput.click(x=392, y=377, )

    pydirectinput.click(x=1355, y=1120, )

    pydirectinput.click(x=404, y=375, )

    pydirectinput.click(x=2166, y=1082, )

    pydirectinput.click(x=385, y=875, )

    camos4()

    esc_scroll()

    pydirectinput.click(x=471, y=1075, )  # sc9 smg

    pydirectinput.click(x=772, y=323, )  # GUNSMITH

    pydirectinput.click(x=746, y=336, )

    pydirectinput.click(x=436, y=622, )

    pydirectinput.click(x=1258, y=297, )

    pydirectinput.click(x=414, y=372, )

    pydirectinput.click(x=2129, y=362, )

    pydirectinput.click(x=423, y=451, )

    pydirectinput.click(x=2122, y=1082, )

    pydirectinput.click(x=379, y=708, )

    pydirectinput.click(x=1366, y=1126, )

    pydirectinput.click(x=411, y=454, )

    camos4()

    switch_tab_shotgun()

    pydirectinput.click(x=470, y=408, )  # MODEL 680

    pydirectinput.click(x=776, y=322, )  # GUNDMITH

    pydirectinput.click(x=299, y=364, )

    pydirectinput.click(x=379, y=708, )

    pydirectinput.click(x=781, y=332, )

    pydirectinput.click(x=417, y=453, )

    pydirectinput.click(x=1225, y=295, )

    pydirectinput.click(x=379, y=367, )

    pydirectinput.click(x=2160, y=367, )

    pydirectinput.click(x=441, y=456, )

    pydirectinput.click(x=1301, y=1131, )

    pydirectinput.click(x=396, y=622, )

    camos4()

    ESC()

    pydirectinput.click(x=486, y=629, )  # R90

    pydirectinput.click(x=777, y=328, )  # GUNSMITH

    pydirectinput.click(x=350, y=365, )

    pydirectinput.click(x=401, y=703, )

    pydirectinput.click(x=797, y=332, )

    pydirectinput.click(x=394, y=283, )

    pydirectinput.click(x=1210, y=297, )

    pydirectinput.click(x=376, y=371, )

    pydirectinput.click(x=1330, y=1123, )

    pydirectinput.click(x=407, y=458, )

    pydirectinput.click(x=1739, y=1126, )

    pydirectinput.click(x=404, y=455, )

    camos4()

    ESC()

    pydirectinput.click(x=463, y=848, )  # 725

    pydirectinput.click(x=776, y=327, )  # GUNSMITH

    pydirectinput.click(x=348, y=363, )

    pydirectinput.click(x=394, y=789, )

    pydirectinput.click(x=761, y=334, )

    pydirectinput.click(x=408, y=365, )

    pydirectinput.click(x=1212, y=294, )

    pydirectinput.click(x=454, y=375, )

    pydirectinput.click(x=2143, y=363, )

    pydirectinput.click(x=383, y=455, )

    pydirectinput.click(x=1692, y=1123, )

    pydirectinput.click(x=414, y=284, )

    camos4()

    ESC()

    pydirectinput.click(x=458, y=1077, )  # ORIGIN 12

    pydirectinput.click(x=776, y=323, )  # GUNSMITH

    pydirectinput.click(x=320, y=367, )

    pydirectinput.click(x=397, y=876, )

    pydirectinput.click(x=768, y=333, )

    pydirectinput.click(x=393, y=448, )

    pydirectinput.click(x=1266, y=301, )

    pydirectinput.click(x=378, y=369, )

    pydirectinput.click(x=1372, y=1127, )

    pydirectinput.click(x=403, y=458, )

    pydirectinput.click(x=1751, y=1126, )

    pydirectinput.click(x=419, y=456, )

    camos4()

    esc_scroll()

    pydirectinput.click(x=436, y=1059, )  # VLK

    pydirectinput.click(x=777, y=324, )  # GUNSMITH

    pydirectinput.doubleClick(x=1336, y=671, )  # click screen

    pydirectinput.click(x=1708, y=1128, )  # not working

    pydirectinput.click(x=406, y=458, )  # NOT WORKING

    pydirectinput.click(x=795, y=335, )

    pydirectinput.click(x=420, y=458, )

    pydirectinput.click(x=1224, y=302, )

    pydirectinput.click(x=391, y=373, )

    pydirectinput.click(x=1311, y=1126, )

    pydirectinput.click(x=405, y=536, )

    pydirectinput.click(x=945, y=1088, )

    pydirectinput.click(x=351, y=288, )

    camos4()

    esc_scroll()

    pydirectinput.click(x=457, y=1075, )  # JAK 12

    pydirectinput.click(x=776, y=307, )  # GUNSMITH

    pydirectinput.doubleClick(x=1336, y=671, )  # click screen

    pydirectinput.click(x=333, y=367, )

    pydirectinput.click(x=408, y=789, )

    pydirectinput.click(x=789, y=336, )

    pydirectinput.click(x=418, y=455, )

    pydirectinput.click(x=1261, y=301, )

    pydirectinput.click(x=401, y=374, )

    pydirectinput.click(x=1359, y=1120, )

    pydirectinput.click(x=397, y=456, )

    pydirectinput.click(x=956, y=1090, )

    pydirectinput.click(x=393, y=299, )

    camos4()

    switch_tab_LMG()

    pydirectinput.click(x=476, y=408, )  # pkm

    pydirectinput.click(x=774, y=319, )  # gunsmith

    pydirectinput.click(x=322, y=363, )

    pydirectinput.click(x=402, y=371, )

    pydirectinput.click(x=749, y=333, )

    pydirectinput.click(x=384, y=365, )

    pydirectinput.click(x=1183, y=293, )

    pydirectinput.click(x=389, y=452, )

    pydirectinput.click(x=2178, y=362, )

    pydirectinput.click(x=398, y=454, )

    pydirectinput.click(x=962, y=1086, )

    pydirectinput.click(x=421, y=286, )

    camos4()

    ESC()

    pydirectinput.click(x=475, y=640, )  # SA87

    pydirectinput.click(x=775, y=321, )  # GUNSMITH

    pydirectinput.click(x=302, y=365, )

    pydirectinput.click(x=398, y=785, )

    pydirectinput.click(x=795, y=338, )

    pydirectinput.click(x=413, y=366, )

    pydirectinput.click(x=1215, y=294, )

    pydirectinput.click(x=409, y=452, )

    pydirectinput.click(x=1356, y=1123, )

    pydirectinput.click(x=404, y=364, )

    pydirectinput.click(x=912, y=1088, )

    pydirectinput.click(x=390, y=282, )

    camos4()

    ESC()

    pydirectinput.click(x=468, y=823, )  # M91

    pydirectinput.click(x=776, y=321, )  # GUNSMITH

    pydirectinput.click(x=309, y=364, )

    pydirectinput.click(x=416, y=789, )

    pydirectinput.click(x=753, y=335, )

    pydirectinput.click(x=408, y=457, )

    pydirectinput.click(x=1197, y=298, )

    pydirectinput.click(x=385, y=453, )

    pydirectinput.click(x=2128, y=361, )

    pydirectinput.click(x=417, y=535, )

    pydirectinput.click(x=954, y=1088, )

    pydirectinput.click(x=415, y=279, )

    camos4()

    ESC()

    pydirectinput.click(x=465, y=1063, )  # MG34

    pydirectinput.click(x=777, y=324, )  # GUMSMITH

    pydirectinput.click(x=281, y=364, )

    pydirectinput.click(x=393, y=790, )

    pydirectinput.click(x=766, y=333, )

    pydirectinput.click(x=430, y=458, )

    pydirectinput.click(x=1246, y=296, )

    pydirectinput.click(x=388, y=366, )

    pydirectinput.click(x=1355, y=1122, )

    pydirectinput.click(x=428, y=285, )

    pydirectinput.click(x=932, y=1083, )

    pydirectinput.click(x=385, y=284, )

    camos4()

    esc_scroll()

    pydirectinput.click(x=451, y=1056, )  # HOLGER

    pydirectinput.click(x=778, y=317, )  # GUNSMITH

    pydirectinput.click(x=305, y=359, )

    pydirectinput.click(x=400, y=783, )

    pydirectinput.click(x=743, y=337, )

    pydirectinput.click(x=391, y=284, )

    pydirectinput.click(x=1197, y=295, )

    pydirectinput.click(x=385, y=456, )

    pydirectinput.click(x=1361, y=1126, )

    pydirectinput.click(x=404, y=288, )

    pydirectinput.click(x=945, y=1087, )

    pydirectinput.click(x=395, y=288, )

    camos4()

    esc_scroll()

    pydirectinput.click(x=458, y=1068, )  # BRUEN MK9

    pydirectinput.click(x=776, y=318, )  # GUNSMITH

    pydirectinput.click(x=312, y=365, )

    pydirectinput.click(x=377, y=781, )

    pydirectinput.click(x=788, y=332, )

    pydirectinput.click(x=388, y=371, )

    pydirectinput.click(x=1199, y=297, )

    pydirectinput.click(x=370, y=449, )

    pydirectinput.click(x=1325, y=1123, )

    pydirectinput.click(x=408, y=370, )

    pydirectinput.click(x=931, y=1089, )

    pydirectinput.click(x=428, y=282, )

    camos4()

    esc_scroll()

    pydirectinput.click(x=456, y=1067, )  # finn

    pydirectinput.click(x=773, y=316, )  # GUNSMITH

    pydirectinput.click(x=308, y=364, )

    pydirectinput.click(x=400, y=790, )

    pydirectinput.click(x=800, y=332, )

    pydirectinput.click(x=390, y=705, )

    pydirectinput.click(x=1227, y=296, )

    pydirectinput.click(x=417, y=281, )

    pydirectinput.click(x=1352, y=1121, )

    pydirectinput.click(x=397, y=374, )

    pydirectinput.click(x=958, y=1089, )

    pydirectinput.click(x=383, y=293, )

    camos4()

    esc_scroll()

    pydirectinput.click(x=459, y=1081, )  # RAAL MG

    pydirectinput.click(x=774, y=316, )  # GUNSMITH

    pydirectinput.click(x=290, y=361, )

    pydirectinput.click(x=382, y=787, )

    pydirectinput.click(x=750, y=337, )

    pydirectinput.click(x=395, y=370, )

    pydirectinput.click(x=1218, y=295, )

    pydirectinput.click(x=396, y=288, )

    pydirectinput.click(x=1319, y=1124, )

    pydirectinput.click(x=393, y=364, )

    pydirectinput.click(x=916, y=1085, )

    pydirectinput.click(x=391, y=538, )

    camos4()

    switch_tab_marksman()

    pydirectinput.click(x=474, y=385, )  # EBR

    pydirectinput.click(x=777, y=323, )  # GUNSMITH

    pydirectinput.click(x=311, y=366, )

    pydirectinput.click(x=418, y=787, )

    pydirectinput.click(x=782, y=332, )

    pydirectinput.click(x=409, y=460, )

    pydirectinput.click(x=1185, y=297, )

    pydirectinput.click(x=404, y=290, )

    pydirectinput.click(x=1332, y=1126, )

    pydirectinput.click(x=409, y=369, )

    pydirectinput.click(x=995, y=1083, )

    pydirectinput.click(x=397, y=279, )

    camos4()

    ESC()

    pydirectinput.click(x=467, y=624, )  # MK2 CARBINE

    pydirectinput.click(x=776, y=324, )  # GUNSMITH

    pydirectinput.click(x=273, y=362, )

    pydirectinput.click(x=380, y=793, )

    pydirectinput.click(x=757, y=334, )

    pydirectinput.click(x=396, y=453, )

    pydirectinput.click(x=1243, y=297, )

    pydirectinput.click(x=384, y=284, )

    pydirectinput.click(x=1663, y=331, )

    pydirectinput.click(x=344, y=1042, )

    pydirectinput.click(x=1688, y=1128, )

    pydirectinput.click(x=386, y=368, )

    camos4()

    ESC()

    pydirectinput.click(x=474, y=839, )  # KAR98K

    pydirectinput.click(x=775, y=327, )  # GUNSMITH

    pydirectinput.click(x=286, y=360, )

    pydirectinput.click(x=371, y=623, )

    pydirectinput.click(x=790, y=334, )

    pydirectinput.click(x=398, y=451, )

    pydirectinput.click(x=1271, y=298, )

    pydirectinput.click(x=439, y=287, )

    pydirectinput.click(x=1686, y=330, )

    pydirectinput.click(x=337, y=875, )

    pydirectinput.click(x=1727, y=1123, )

    pydirectinput.click(x=413, y=289, )

    camos4()

    ESC()

    pydirectinput.click(x=465, y=1061, )  # CROSSBOW

    pydirectinput.click(x=777, y=326, )  # GUNSMITH

    pydirectinput.click(x=290, y=366, )

    pydirectinput.click(x=395, y=280, )

    pydirectinput.click(x=777, y=329, )

    pydirectinput.click(x=384, y=457, )

    pydirectinput.click(x=1233, y=295, )

    pydirectinput.click(x=389, y=282, )

    pydirectinput.click(x=1287, y=1123, )

    pydirectinput.click(x=403, y=280, )

    pydirectinput.click(x=937, y=1085, )

    pydirectinput.click(x=391, y=283, )

    camos4()

    esc_scroll()

    pydirectinput.click(x=477, y=1062, )  # sks

    pydirectinput.click(x=771, y=322, )  # gunsmith

    pydirectinput.click(x=286, y=367, )

    pydirectinput.click(x=389, y=791, )

    pydirectinput.click(x=739, y=338, )

    pydirectinput.click(x=381, y=457, )

    pydirectinput.click(x=1254, y=298, )

    pydirectinput.click(x=449, y=288, )

    pydirectinput.click(x=1352, y=1120, )

    pydirectinput.click(x=392, y=283, )

    pydirectinput.click(x=974, y=1085, )

    pydirectinput.click(x=394, y=287, )

    camos4()

    esc_scroll()

    pydirectinput.click(x=447, y=1074, )  # sp-r 208

    pydirectinput.click(x=776, y=322, )  # GUNSMITH\

    pydirectinput.click(x=285, y=364, )

    pydirectinput.click(x=372, y=792, )

    pydirectinput.click(x=768, y=335, )

    pydirectinput.click(x=425, y=456, )

    pydirectinput.click(x=1200, y=300, )

    pydirectinput.click(x=451, y=284, )

    pydirectinput.click(x=1644, y=334, )

    pydirectinput.click(x=360, y=1040, )

    pydirectinput.click(x=1303, y=1123, )

    pydirectinput.click(x=404, y=456, )

    camos4()

    switch_tab_sniper()

    pydirectinput.click(x=458, y=409, )  # Dragunov

    pydirectinput.click(x=776, y=323, )  # GUNSMITH

    pydirectinput.click(x=267, y=366, )

    pydirectinput.click(x=416, y=362, )

    pydirectinput.click(x=738, y=331, )

    pydirectinput.click(x=378, y=372, )

    pydirectinput.click(x=1275, y=293, )

    pydirectinput.click(x=456, y=280, )

    pydirectinput.click(x=2100, y=360, )

    pydirectinput.click(x=436, y=535, )

    pydirectinput.click(x=2100, y=1091, )

    pydirectinput.click(x=372, y=455, )

    camos4()

    esc_scroll()

    pydirectinput.click(x=480, y=621, )  # HDR

    pydirectinput.click(x=772, y=321, )  # GUNSMITH

    pydirectinput.click(x=806, y=337, )

    pydirectinput.click(x=414, y=452, )

    pydirectinput.click(x=1206, y=300, )

    pydirectinput.click(x=315, y=296, )

    pydirectinput.click(x=2111, y=365, )

    pydirectinput.click(x=426, y=284, )

    pydirectinput.click(x=2091, y=1084, )

    pydirectinput.click(x=366, y=536, )

    pydirectinput.click(x=936, y=1081, )

    pydirectinput.click(x=402, y=289, )

    camos4()

    ESC()

    pydirectinput.click(x=431, y=856, )  # AX50

    pydirectinput.click(x=758, y=317, )  # GUNSMITH

    pydirectinput.click(x=764, y=327, )

    pydirectinput.click(x=365, y=360, )

    pydirectinput.click(x=1218, y=291, )

    pydirectinput.click(x=422, y=271, )

    pydirectinput.click(x=2149, y=351, )

    pydirectinput.click(x=362, y=450, )

    pydirectinput.click(x=1748, y=1154, )

    pydirectinput.click(x=365, y=453, )

    pydirectinput.click(x=2161, y=1111, )

    pydirectinput.click(x=355, y=364, )

    camos4()

    ESC()

    pydirectinput.click(x=422, y=1048, )  # RYTEC

    pydirectinput.click(x=777, y=319, )  # GUNSMITH

    pydirectinput.click(x=321, y=370, )

    pydirectinput.click(x=387, y=371, )

    pydirectinput.click(x=762, y=339, )

    pydirectinput.click(x=410, y=287, )

    pydirectinput.click(x=1222, y=288, )

    pydirectinput.click(x=362, y=283, )

    pydirectinput.click(x=1730, y=1128, )

    pydirectinput.click(x=381, y=454, )

    pydirectinput.click(x=2096, y=361, )

    pydirectinput.click(x=393, y=454, )

    camos4()

    switch_to_pistol()

    pydirectinput.click(x=778, y=578, )  # X16 PISTOL PLUS GUNSMITH

    pydirectinput.click(x=348, y=361, )

    pydirectinput.click(x=420, y=364, )

    pydirectinput.click(x=806, y=335, )

    pydirectinput.click(x=399, y=446, )

    pydirectinput.click(x=1210, y=297, )

    pydirectinput.click(x=400, y=454, )

    pydirectinput.click(x=1344, y=1123, )

    pydirectinput.click(x=376, y=371, )

    pydirectinput.click(x=921, y=1083, )

    pydirectinput.click(x=397, y=284, )

    camos4()

    ESC_pistol()

    pydirectinput.click(x=451, y=616, )  # 1911

    pydirectinput.click(x=773, y=579, )  # GUNSMITH

    pydirectinput.click(x=296, y=363, )

    pydirectinput.click(x=392, y=710, )

    pydirectinput.click(x=807, y=332, )

    pydirectinput.click(x=408, y=449, )

    pydirectinput.click(x=1189, y=299, )

    pydirectinput.click(x=355, y=370, )

    pydirectinput.click(x=1335, y=1125, )

    pydirectinput.click(x=394, y=376, )

    pydirectinput.click(x=1000, y=1082, )

    pydirectinput.click(x=377, y=281, )

    camos4()

    ESC_pistol()

    pydirectinput.click(x=472, y=843, )  # .357

    pydirectinput.click(x=771, y=577, )  # GUNSMITH

    pydirectinput.click(x=725, y=331, )

    pydirectinput.click(x=432, y=449, )

    pydirectinput.click(x=1251, y=299, )

    pydirectinput.click(x=427, y=366, )

    pydirectinput.click(x=1332, y=1128, )

    pydirectinput.click(x=434, y=281, )

    pydirectinput.click(x=2130, y=1088, )

    pydirectinput.click(x=371, y=1044, )

    pydirectinput.click(x=991, y=1089, )

    pydirectinput.click(x=429, y=284, )

    camos4()

    ESC_pistol()

    pydirectinput.click(x=472, y=1053, )  # M19

    pydirectinput.click(x=776, y=582, )  # GUNSMITH

    pydirectinput.click(x=286, y=366, )

    pydirectinput.click(x=397, y=449, )

    pydirectinput.click(x=758, y=332, )

    pydirectinput.click(x=397, y=372, )

    pydirectinput.click(x=1225, y=296, )

    pydirectinput.click(x=393, y=363, )

    pydirectinput.click(x=1356, y=1123, )

    pydirectinput.click(x=425, y=371, )

    pydirectinput.click(x=938, y=1087, )

    pydirectinput.click(x=396, y=282, )

    camos4()

    ESC_pistol_SCROLL()

    pydirectinput.click(x=464, y=1069, )  # 50OG

    pydirectinput.click(x=776, y=579, )  # GUNSMITH

    pydirectinput.click(x=275, y=367, )

    pydirectinput.click(x=395, y=458, )

    pydirectinput.click(x=769, y=332, )

    pydirectinput.click(x=397, y=283, )

    pydirectinput.click(x=1220, y=298, )

    pydirectinput.click(x=412, y=369, )

    pydirectinput.click(x=1326, y=1124, )

    pydirectinput.click(x=394, y=371, )

    pydirectinput.click(x=993, y=1085, )

    pydirectinput.click(x=396, y=282, )

    camos4()

    ESC_pistol_SCROLL()

    pydirectinput.click(x=456, y=1058, )  # RENETTI

    pydirectinput.click(x=776, y=581, )  # GUNSMITH

    pydirectinput.click(x=295, y=366, )

    pydirectinput.click(x=399, y=714, )

    pydirectinput.click(x=783, y=332, )

    pydirectinput.click(x=440, y=452, )

    pydirectinput.click(x=1171, y=302, )

    pydirectinput.click(x=333, y=367, )

    pydirectinput.click(x=1308, y=1127, )

    pydirectinput.click(x=408, y=373, )

    pydirectinput.click(x=971, y=1090, )

    pydirectinput.click(x=402, y=287, )

    camos4()

    ESC_pistol_SCROLL()

    pydirectinput.click(x=450, y=1062, )  # SYKOV

    pydirectinput.click(x=780, y=574, )  # GUNSMITH

    pydirectinput.click(x=277, y=362, )

    pydirectinput.click(x=397, y=704, )

    pydirectinput.click(x=771, y=329, )

    pydirectinput.click(x=404, y=455, )

    pydirectinput.click(x=1282, y=300, )

    pydirectinput.click(x=387, y=373, )

    pydirectinput.click(x=1281, y=1121, )

    pydirectinput.click(x=364, y=369, )

    pydirectinput.click(x=991, y=1081, )

    pydirectinput.click(x=417, y=287, )

    camos4()


print(colored("<CHOOSE CAMO CONFIG> ", "red"))
print("\n")
print(colored("[1] DAMASCUCS, OBSIDIAN, DM-ULTRA, DAIMOND", "magenta"))
print(colored("[2] GOLD, PLATINUM, DAMASCUS, OBSIDIAN", "magenta"))
print(colored("[3] DAMASCUCS, DAIMOND, DM-ULTRA, HOT&COLD", "magenta"))
print(colored("[4] OBSIDIAN, HOT&COLD, RAINBOW, BANDED", "magenta"))
useanswer = input("\nENTER TYPE : ").upper()
if useanswer == "1":
    camo_1()

if useanswer == "2":
    camo_2()

if useanswer == "3":
    camo_3()

if useanswer == "4":
    camo_4()

input()
