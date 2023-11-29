from pyrevit import revit, DB

uidoc = revit.uidoc
doc = revit.doc

options = DB.IFCExportOptions()
options.AddOption("ExportAnnotations", "True")

filepath = r"C:\Users\wend\Downloads"

t = DB.Transaction(doc, "Export IFC")
t.Start()


result = doc.Export(filepath, "IFC", options)

t.Commit()
