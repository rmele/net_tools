#!/usr/bin/env python

import os
from Cocoa import NSSavePanel, NSRunningApplication, NSApplicationActivateIgnoringOtherApps, NSOKButton


class SelectWriteFileDialog:
    """
    class to create Cocoa Write File Dialog and return value of File Path is path is entered at prompt

    """
    def __init__(self):
        self.file_path = None
        self.panel = NSSavePanel.savePanel()
        self.panel.setCanCreateDirectories_(True)
        self.panel.setCanChooseDirectories_(True)
        self.panel.setCanChooseFiles_(True)

    def main(self):
        app = NSRunningApplication.runningApplicationWithProcessIdentifier_(os.getpid())
        app.activateWithOptions_(NSApplicationActivateIgnoringOtherApps)

        status = self.panel.runModal()

        if status == NSOKButton:
            return self.panel.filename()
        else:
            return None


if __name__ == "__main__":
    import sys

    write_file = SelectWriteFileDialog().main()
    if write_file:
        print write_file

    sys.exit()
