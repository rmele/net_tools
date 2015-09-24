from AppKit import NSScreen

resolutions = [(screen.frame().size.width, screen.frame().size.height)
               for screen in NSScreen.screens()]

for res in resolutions:
    print res
