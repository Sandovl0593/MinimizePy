import os.path as Op
import os

pathAct = os.getcwd()
pathBase = Op.basename(pathAct)

for archivo in os.listdir(pathAct):
    if Op.isdir(f"..\{pathBase}\{archivo}"):
        continue
    name, extens = Op.splitext(archivo)
    if extens not in  [".cpp", ".py", ".exe"]:
        os.remove(archivo)