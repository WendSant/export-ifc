import os
from pyrevit import revit, DB

uidoc = revit.uidoc
doc = revit.doc

options = DB.IFCExportOptions()
options.AddOption("ExportAnnotations", "True")

downloads_dir = os.path.expanduser("~" + os.sep + "Downloads")

filepath = os.path.join(downloads_dir)

t = DB.Transaction(doc, "Export IFC")
t.Start()

result = doc.Export(filepath, "IFC", options)

t.Commit()
