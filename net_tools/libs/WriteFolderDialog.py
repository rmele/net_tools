#!/usr/bin/env python

import os
from Cocoa import NSOpenPanel, NSRunningApplication, NSApplicationActivateIgnoringOtherApps, NSOKButton


class SelectWriteFolderDialog:
    """
    class to create Cocoa Write File Dialog and return value of File Path is path is entered at prompt

    """
    def __init__(self):
        self.file_path = None
        self.panel = NSOpenPanel.openPanel()
        self.panel.setCanCreateDirectories_(True)
        self.panel.setCanChooseDirectories_(True)
        self.panel.setCanChooseFiles_(False)

    def main(self):
        app = NSRunningApplication.runningApplicationWithProcessIdentifier_(os.getpid())
        app.activateWithOptions_(NSApplicationActivateIgnoringOtherApps)

        if self.panel.runModal() == NSOKButton:
            return self.panel.directory()
        else:
            return None


if __name__ == "__main__":
    import sys

    write_file = SelectWriteFolderDialog().main()
    if write_file:
        print write_file

    sys.exit()
