import time
from pywinauto.application import Application
from win32con import *
import sys

ACCOUNT = sys.argv[1]
PASSWORD = sys.argv[2]

print("Launching iTunes...")

app = Application().start(r"C:\Program Files\iTunes\iTunes.exe")
app.wait_cpu_usage_lower()
time.sleep(3)

def debugTopWin():
    print("-- Cur top win: %s" % app.top_window().wait('exists'))

def cleanAllDialog():
    while True:
        topwin = app.top_window().wait('exists')
        if 'Dialog' in topwin.class_name():
            print("    Closing dialog %s" % topwin.window_text())
            app.top_window().Button0.click()
        else:
            break
        
        app.wait_cpu_usage_lower()
        time.sleep(3)

cleanAllDialog()

app.wait_cpu_usage_lower()
time.sleep(2)

debugTopWin()

print("Clicking Account menu...")
app.iTunes.Application.Static3.click()
app.wait_cpu_usage_lower()
time.sleep(3)

debugTopWin()

popup = app.PopupMenu
if '&S' in popup.menu().item(1).text():
    print("Signin menu presented, clicking to login!")
    # not log in
    popup.menu().item(1).click_input()
    app.wait_cpu_usage_lower()
    time.sleep(6)
    debugTopWin()
    
    print("Setting login dialog edit texts")
    dialog = app.iTunesDialog
    appleid_Edit = dialog.Edit1
    pass_Edit = dialog.Edit2
    appleid_Edit.set_edit_text(ACCOUNT)
    time.sleep(1)
    pass_Edit.type_keys('123')
    time.sleep(1)
    pass_Edit.set_edit_text(PASSWORD)
    time.sleep(1)
    
    print("Clicking login button!")
    loginButton = dialog.Button0
    loginButton.click()
else:
    print("Already logged in!")
    popup.close()

debugTopWin()

print("Waiting all dialogs to finish")
time.sleep(10)
cleanAllDialog()