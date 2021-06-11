from datetime import datetime
import subprocess
import os

def get_date():
     date = datetime.now().strftime("%d %B %Y")
     return date

def get_time():
    time = datetime.now().time().strftime("%H %M")
    return time

def make_file(recorded_audio):
    with open(recorded_audio.split(' ')[1] , 'w') as fil:
        pass

def full_scan():
    os.system('start cmd /k " cd C:\\ProgramData\\Microsoft\Windows^ Defender\Platform\\4.18.2105.4-0 & MpCmdRun.exe -Scan -ScanType 2 "')


def quick_scan():
    os.system('start cmd /k " cd C:\\ProgramData\\Microsoft\Windows^ Defender\Platform\\4.18.2105.4-0 & MpCmdRun.exe -Scan -ScanType 1 "')


#quick_scan()