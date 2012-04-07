'''
C4DPluginTemplate v1.0

Copyright: Erwin Santacruz 2010 (www.990adjustments.com)
Written for CINEMA 4D R12.016

Name-US: 
Description-US: 


Creation Date: 

'''

import c4d
from c4d import gui, plugins, bitmaps

import time, sys, os, subprocess
import logging, logging.handlers, shelve




#Testing ids 1000001 - 1000010
__plugin_id__ = 1000001
__version__ = "1.0"
__plugin_title__ = "C4DPluginTemplate v1.0"

DUMMY = 1000
HELP_TEXT = ""


class MainDialog(gui.GeDialog):

    def InitValues(self):
        '''
        Called when the dialog is initialized by the GUI.
        True if successful, or False to signalize an error.
        '''

        print("{0} loaded. (C) 2012 Erwin Santacruz. All rights reserved.".format(__plugin_title__))
        return True


    def CreateLayout(self):
        '''
        Override - Called when C4D is about to display the dialog.
        True if successful, or False to signalize an error.
        '''

        self.SetTitle(__plugin_title__)
        return True


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

        if id == DUMMY:
            pass

        return True

    def about_C4DPluginTemplate(self):
        '''Show About information dialog box.'''

        gui.MessageDialog("{0}\nby Erwin Santacruz 2012\n\nwww.990adjustments.com\n".format(__plugin_title__), c4d.GEMB_OK)


class C4DPluginTemplate(plugins.CommandData):
    '''C4DPluginTemplate class'''

    dialog = None

    def Execute(self,doc):
        if self.dialog is None:
            self.dialog = MainDialog()

        return self.dialog.Open(dlgtype = c4d.DLG_TYPE_ASYNC, pluginid = __plugin_id__, defaultw = 200, defaulth = 100)

    def RestoreLayout(self, sec_ref):
        if self.dialog is None:
            self.dialog = MainDialog()

        return self.dialog.Restore(pluginid = __plugin_id__, secret = sec_ref)


if __name__ == "__main__":
    icon = bitmaps.BaseBitmap()
    dir, file = os.path.split(__file__)
    iconPath = os.path.join(dir, "res", "icon.tif")
    icon.InitWith(iconPath)

    plugins.RegisterCommandPlugin(id = __plugin_id__, str = __plugin_title__, info = 0, help = HELP_TEXT, dat = C4DPluginTemplate(), icon = icon)
