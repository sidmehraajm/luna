from Luna.core import workspace
from Luna.core import optionVarFn
from PySide2 import QtWidgets
reload(workspace)

prevPath = optionVarFn.getOptionVar(optionVarFn.LunaVars.previous_workspace, default="")
path = QtWidgets.QFileDialog.getExistingDirectory(None, "Set Luna workspace", "")
if path:
    test_workspace = workspace.Workspace.set(path)