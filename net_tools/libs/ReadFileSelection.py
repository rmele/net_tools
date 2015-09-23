#!/usr/bin/env python

import os
from Cocoa import NSRunningApplication, NSOpenPanel, NSApplicationActivateIgnoringOtherApps, NSOKButton


class SelectReadFileDialog:
    def __init__(self):
        self.panel = NSOpenPanel.openPanel()
        self.panel.setCanCreateDirectories_(True)
        self.panel.setCanChooseDirectories_(True)
        self.panel.setCanChooseFiles_(True)

    def main(self):
        app = NSRunningApplication.runningApplicationWithProcessIdentifier_(os.getpid())
        app.activateWithOptions_(NSApplicationActivateIgnoringOtherApps)

        if self.panel.runModal() == NSOKButton:
            return self.panel.filename()
        else:
            return None

if __name__ == '__main__':
    import sys

    read_file = SelectReadFileDialog().main()
    if read_file:
        print read_file

    sys.exit()
