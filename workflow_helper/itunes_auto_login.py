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

# Click all first-time dialogs (like License Agreements, missing audios)
cleanAllDialog()

# Calm down a bit before main window operations
app.wait_cpu_usage_lower()
time.sleep(5)

debugTopWin()

# Click main window's first-time question ("No thanks" button)
app.iTunes.Button11.click_input()

app.wait_cpu_usage_lower()
time.sleep(4)

# Start logging in by clicking toolbar menu "Account"
print("Clicking Account menu...")
app.iTunes.Application.Static3.click()
app.wait_cpu_usage_lower()
time.sleep(3)

debugTopWin()

# Detect whether we have "&S" in popup, which refers to "Sign in"
popup = app.PopupMenu
if '&S' in popup.menu().item(1).text():
    print("Signin menu presented, clicking to login!")
    # not log in
    popup.menu().item(1).click_input()
    app.wait_cpu_usage_lower()
    time.sleep(8)
    debugTopWin()

    for i in range(60):
        dialog = app.top_window()
        dialogWrap = dialog.wait('ready')
        assert dialogWrap.friendly_class_name() == 'Dialog'
        time.sleep(1.0)
        try:
            if dialogWrap.window_text() == 'iTunes' \
                and dialog.Edit1.wait('ready').window_text() == 'Apple ID' \
                and dialog.Edit2.wait('ready').window_text() == 'Password' \
                and dialog.Button0.wait('exists').window_text() == '&Sign In':
                break
        except Exception as e:
            pass
    
    app.wait_cpu_usage_lower()

    print("Setting login dialog edit texts")

    appleid_Edit = dialog.Edit1
    appleid_Edit.wait('ready')
    appleid_Edit.click_input()
    appleid_Edit.type_keys(ACCOUNT)
    appleid_Edit.set_edit_text(ACCOUNT)
    time.sleep(3)

    pass_Edit = dialog.Edit2
    pass_Edit.wait('ready')
    pass_Edit.click_input()
    pass_Edit.type_keys(PASSWORD)
    pass_Edit.set_edit_text(PASSWORD)
    time.sleep(3)
    
    print("Clicking login button!")
    loginButton = dialog.Button0
    loginButton.wait('ready')
    loginButton.click()
else:
    print("Already logged in!")
    popup.close()

debugTopWin()

# Finish & Cleanup
print("Waiting all dialogs to finish")
time.sleep(10)
cleanAllDialog()