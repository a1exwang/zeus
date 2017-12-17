# -*- coding: utf-8 -*-
import win32gui
import time
from subprocess import call


BT_TITLE = "新建BT任务"

class MyStatus:
	OK = "ok"
	UNKNOWN_ERROR = "unknown_error"
	SEED_TIMEOUT_ERROR = "seed_timeout_error"
	

status = MyStatus()


def call_thunder_bt(
		url, 
		thunder_path,
		try_seconds=10, 
		button_pos=(400, 520)):
	
	call([thunder_path, url])

	interval = 1
	t = 0
	hwnd = 0
	while True:
		hwnd = win32gui.FindWindow(None, BT_TITLE)
		print("FindWindow %d" % hwnd)
		if hwnd:
			break
		print("Waiting for thunder, %d" % t)
		time.sleep(interval)
		t += interval

		if t >= try_seconds:
			return status.SEED_TIMEOUT_ERROR
	
	print("FindWindow done %d" % hwnd)
	lParam = (button_pos[1] << 16) | button_pos[0]
	#lParam = 0x209016a
	t = 0
	interval = 0.5
	while True:
		print(win32gui.SendMessage(hwnd, 0x201, 1, lParam))
		print(win32gui.SendMessage(hwnd, 0x202, 2, lParam))
		time.sleep(interval)
		t += interval

		hwnd = win32gui.FindWindow(None, BT_TITLE)
		print("Is window closed?, %d" % hwnd)
		if not hwnd:
			break
		
		time.sleep(interval)
		t += interval

		if t >= try_seconds:
			# try to close window
			win32gui.SendMessage(hwnd, 0x10, 0, 0)
			print("CloseWindow %d" % hwnd)
			return status.SEED_TIMEOUT_ERROR
		
	return status.OK

	
def call_thunder_bt_default(url):
	return call_thunder_bt(url, "./Thunder/Program/Thunder.exe")
