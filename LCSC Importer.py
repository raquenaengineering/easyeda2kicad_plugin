import pcbnew
import wx
import os
import sys

# add the `easyeda2kicad` folder to sys.path to make it importable
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "easyeda2kicad"))

from easyeda2kicad.__main__ import main as easyeda_main  # import the main function from easyeda2kicad

class EasyEDAImporterPlugin(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "LCSC Part Importer"
        self.category = "Utility"
        self.description = "Import a part from LCSC to KiCad using easyeda2kicad"
        self.show_toolbar_button = True  # optional, defaults to False
        self.icon_file_name = os.path.join(os.path.dirname(__file__), "easyeda2kicad", "lcsc_logo.png")

    def Run(self):
        # open a dialog to get the lcsc part number
        dialog = wx.TextEntryDialog(None, "Enter LCSC Part Number:", "LCSC Part Importer", "")
        
        if dialog.ShowModal() == wx.ID_OK:
            part_number = dialog.GetValue().strip()
            
            # run easyeda2kicad's main function with the part number
            try:
                result = easyeda_main(["--full", f"--lcsc_id={part_number}"])  # pass arguments as needed
                wx.MessageBox(f"Part imported successfully.", "Success")
            except Exception as e:
                wx.MessageBox(f"Error importing part:\n{str(e)}", "Execution Error", style=wx.ICON_ERROR)

        dialog.Destroy()

# register the plugin with kicad
EasyEDAImporterPlugin().register()