import os
from Cocoa import NSAlert, NSOpenPanel, NSSavePanel, NSOKButton, NSDate, NSUserNotification, NSUserNotificationCenter, NSInformationalAlertStyle
from Cocoa import NSRunningApplication, NSApplicationActivateIgnoringOtherApps


def send_notification(title, subtitle, info_text, delay=0, sound=False, userInfo={}):
    notification = NSUserNotification.alloc().init()
    notification.setTitle_(title)
    notification.setSubtitle_(subtitle)
    notification.setInformativeText_(info_text)
    notification.setUserInfo_(userInfo)
    if sound:
        notification.setSoundName_("NSUserNotificationDefaultSoundName")
    notification.setDeliveryDate_(NSDate.dateWithTimeInterval_sinceDate_(delay, NSDate.date()))
    NSUserNotificationCenter.defaultUserNotificationCenter().scheduleNotification_(notification)


def set_alert_panel(message, info):
    buttons = ["OK", "Cancel"]
    alert = NSAlert.alloc().init()
    alert.setMessageText_(message)
    alert.setInformativeText_(info)
    alert.setAlertStyle_(NSInformationalAlertStyle)

    app = NSRunningApplication.runningApplicationWithProcessIdentifier_(os.getpid())
    app.activateWithOptions_(NSApplicationActivateIgnoringOtherApps)

    for button in buttons:
        alert.addButtonWithTitle_(button)

    buttonPressed = alert.runModal()
    return buttonPressed


def get_directory_dialog():
    """
    Cocoa Open Directory Dialog box
    :return:
    """
    panel = NSOpenPanel.openPanel()
    panel.setCanCreateDirectories_(True)
    panel.setCanChooseDirectories_(True)
    panel.setCanChooseFiles_(False)

    app = NSRunningApplication.runningApplicationWithProcessIdentifier_(os.getpid())
    app.activateWithOptions_(NSApplicationActivateIgnoringOtherApps)

    if panel.runModal() == NSOKButton:
        return panel.directory()
    else:
        return None


def get_file_dialog():
    """
    Cocoa Open File Dialog box
    :return:
    """
    panel = NSOpenPanel.openPanel()

    panel.setCanCreateDirectories_(True)
    panel.setCanChooseDirectories_(True)
    panel.setCanChooseFiles_(True)

    app = NSRunningApplication.runningApplicationWithProcessIdentifier_(os.getpid())
    app.activateWithOptions_(NSApplicationActivateIgnoringOtherApps)

    if panel.runModal() == NSOKButton:
        return panel.filename()
    else:
        return None


def set_file_dialog():
    """
    Cocoa Save File Dialog obx
    :return:
    """
    panel = NSSavePanel.savePanel()
    panel.setCanCreateDirectories_(True)
    panel.setCanChooseDirectories_(True)
    panel.setCanChooseFiles_(True)

    app = NSRunningApplication.runningApplicationWithProcessIdentifier_(os.getpid())
    app.activateWithOptions_(NSApplicationActivateIgnoringOtherApps)

    if panel.runModal() == NSOKButton:
        return panel.filename()
    else:
        return None


if __name__ == '__main__':
    my_file = get_file_dialog()
    print my_file

    # my_new_file = set_file_dialog()
    # print my_new_file

    # my_path = get_directory_dialog()
    # print my_path

    # my_text = set_alert_panel('boosh', 'kakow')
    # print my_text

    # send_notification("Title", "Subtitle", "the message, with sound", sound=True)

