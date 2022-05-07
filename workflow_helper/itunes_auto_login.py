import subprocess
import time
from pywinauto.application import Application
from win32con import *
import sys

ACCOUNT = sys.argv[1]
PASSWORD = sys.argv[2]

print("Launching iTunes...")

def initITunes():
    subprocess.call('taskkill /f /im iTunes*', shell=True)

    app = Application().start(r"C:\Program Files\iTunes\iTunes.exe")
    app.wait_cpu_usage_lower()
    time.sleep(8)

    def debugTopWin():
        topwin = app.top_window().wait('exists')
        texts = []
        texts += topwin.texts()
        for c in topwin.iter_children():
            texts += c.texts()
        print("-- Cur top win: %s, texts: %s" % (topwin, texts))

    def cleanAllDialog():
        while True:
            topwin = app.top_window().wait('exists')
            if 'Dialog' in topwin.class_name():
                print("    Closing dialog %s" % topwin.window_text())
                app.top_window().Button0.click()
            elif 'Tour' in topwin.window_text():
                print("    Closing Window %s" % topwin.window_text())
                topwin.close()
            else:
                break
            
            app.wait_cpu_usage_lower()
            time.sleep(5)

    # Click all first-time dialogs (like License Agreements, missing audios)
    cleanAllDialog()

    # Calm down a bit before main window operations
    app.wait_cpu_usage_lower()
    debugTopWin()

    # Click main window's first-time question ("No thanks" button)
    try:
        buttonText = app.iTunes.Button11.wait('ready').window_text()
        print('Button11 text is: %s' % buttonText)
        if 'Search' not in buttonText:
            print("Clicked 'No Thanks' Button!")
            app.iTunes.Button11.click_input()
            app.wait_cpu_usage_lower()
            time.sleep(4)
        else:
            raise Exception('stub')
    except:
        print("Not founding 'No Thanks' Button, passing on...")


    # Start logging in by clicking toolbar menu "Account"
    print("Clicking Account menu...")
    app.iTunes.Application.Static3.click()
    app.wait_cpu_usage_lower()
    time.sleep(3)

    debugTopWin()

    # Detect whether we have "&S" in popup, which refers to "Sign in"
    popup = app.PopupMenu
    if '&S' not in popup.menu().item(1).text():
        popup.close()
        raise Exception("Already logged in!")
    
    print("Signin menu presented, clicking to login!")
    # not log in
    popup.menu().item(1).click_input()
    app.wait_cpu_usage_lower()
    time.sleep(8)
    debugTopWin()

    for i in range(15):
        dialog = app.top_window()
        dialogWrap = dialog.wait('ready')
        assert dialogWrap.friendly_class_name() == 'Dialog'
        time.sleep(1.0)
        try:
            if dialogWrap.window_text() == 'iTunes' \
                and dialog.Edit1.wait('ready').window_text() == 'Apple ID' \
                and dialog.Edit2.wait('ready').window_text() == 'Password' \
                and dialog.Button1.wait('exists').window_text() == '&Sign In':
                break
        except Exception as e:
            continue
    else:
        raise Exception("Failed to find login window in 15 iterations!")
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
    loginButton = dialog.Button1
    loginButton.wait('ready')
    # click multiple times as pywinauto seems to have some bug
    loginButton.click()
    time.sleep(0.5)
    try:
        loginButton.click()
        time.sleep(0.5)
        loginButton.click_input()
    except:
        pass
    

    print("Waiting login result...")
    time.sleep(10)
    debugTopWin()
    
    if app.top_window().handle == dialogWrap.handle:
        raise Exception("Failed to trigger Login button!")
    elif app.top_window().window_text() == 'Verification Failed':
        raise Exception("Verification Failed: %s" % app.top_window().Static2.window_text())


    # Finish & Cleanup
    print("Waiting all dialogs to finish")
    cleanAllDialog()


for init_i in range(3):
    try:
        initITunes()
        break
    except Exception as e:
        print("Init iTunes %d: Failed with %s" % (init_i, e))
        import traceback; traceback.print_exc()
        time.sleep(8)

print("Init iTunes Successfully!")