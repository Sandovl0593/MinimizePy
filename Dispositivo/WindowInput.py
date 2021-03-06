from ctypes import c_int, WINFUNCTYPE, windll
from ctypes.wintypes import HWND, LPCWSTR, UINT

# Envoltorio de ctypes
prototype = WINFUNCTYPE(c_int, HWND, LPCWSTR, LPCWSTR, UINT)
paramflags = (1, "hwnd", 0), (1, "text", "Hi"), (1, "caption", "Hello from ctypes"), (1, "flags", 0)
MessageBox = prototype(("MessageBoxW", windll.user32), paramflags)

# Contenido
name =  input()
MessageBox(0, name, "Contenido", 0)