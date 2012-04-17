'''
C4DPluginTemplate v1.0

Copyright: Erwin Santacruz 2012 (www.990adjustments.com)
Written for CINEMA 4D R13

Name-US: C4DPluginTemplate v1.0
 
Description-US: Starting template for Maxon Cinema 4D Plugins. 
Specifically, a command type plugin. Adjust to taste. This includes
some of the information I use for my own plugins so make sure to
adjust accordingly.

Creation Date: 04/07/12
'''

import c4d
from c4d import documents, gui, plugins, bitmaps

import time, sys, os, subprocess
import logging
import webbrowser



# Testing ids 1000001 - 1000010
# be sure to use a unique ID obtained from www.plugincafe.com
__plugin_id__ = 1000001
__version__ = "1.0"
__plugin_title__ = "C4DPluginTemplate v1.0"

DUMMY = 1000
BTN_ABOUT = 1001
BTN_WEB = 1002

# String shown in status bar
HELP_TEXT = "C4DPluginTemplate"



logging.basicConfig(level=logging.DEBUG)



class MainDialog(gui.GeDialog):
    '''Main Dialog Class'''

    def InitValues(self):
        '''
        Called when the dialog is initialized by the GUI.
        True if successful, or False to signalize an error.
        '''

        print("{0} loaded. Copyright (C) 2012 Erwin Santacruz. All rights reserved.".format(__plugin_title__))
        return True

    def CreateLayout(self):
        '''
        Override - Called when C4D is about to display the dialog.
        True if successful, or False to signalize an error.
        '''

        self.SetTitle(__plugin_title__)

        # Create the menu
        self.MenuFlushAll()

        # About/Help menu
        self.MenuSubBegin("Info")
        self.MenuAddString(BTN_ABOUT, "About")
        self.MenuAddString(BTN_WEB, "Website")
        #self.MenuAddSeparator()
        self.MenuSubEnd()

        self.MenuFinished()

        return True

    def ESAbout_C4DPluginTemplate(self):
        '''Show About information dialog box.'''

        gui.MessageDialog("{0}\nCopyright (C) 2012 Erwin Santacruz.\nAll rights reserved.\n\nwww.990adjustments.com\n".format(__plugin_title__), c4d.GEMB_OK)

    def ESOpen_website(self):
        '''Open Hangover Website'''

        webbrowser.open('http://www.990adjustments.com/')

    def Message(self, msg, result):
        '''
        Override - Use to react to more messages.
        The return value depends on the message.
        '''

        pass

        return c4d.gui.GeDialog.Message(self, msg, result)

    def CoreMessage(self, id, msg):
        '''
        Override this function if you want to react to C4D core messages.
        The original message is stored in msg.
        '''

        pass

        return c4d.gui.GeDialog.CoreMessage(self, id, msg)

    def Command(self, id, msg):
        '''
        Override this function if you want to react to user clicks. Whenever the
        user clicks on a gadget and/or changes its value this function will be
        called.

        It is also called when a string menu item is selected.
        Override it to handle such events.
        '''

        if id == BTN_ABOUT:
            self.ESAbout_C4DPluginTemplate()

        if id == BTN_WEB:
            self.ESOpen_website()

        return True



class C4DPluginTemplate(plugins.CommandData):
    '''C4DPluginTemplate class'''

    dialog = None

    def Execute(self,doc):
        if self.dialog is None:
            self.dialog = MainDialog()

        return self.dialog.Open(dlgtype = c4d.DLG_TYPE_ASYNC,
                                pluginid = __plugin_id__,
                                defaultw = 300,
                                defaulth = 400)

    def RestoreLayout(self, sec_ref):
        if self.dialog is None:
            self.dialog = MainDialog()

        return self.dialog.Restore(pluginid = __plugin_id__, secret = sec_ref)



if __name__ == "__main__":
    icon = bitmaps.BaseBitmap()
    dir, file = os.path.split(__file__)
    iconPath = os.path.join(dir, "res", "icon.tif")
    icon.InitWith(iconPath)

    plugins.RegisterCommandPlugin(id = __plugin_id__,
                                  str = __plugin_title__,
                                  info = 0, 
                                  help = HELP_TEXT,
                                  dat = C4DPluginTemplate(),
                                  icon = icon)
