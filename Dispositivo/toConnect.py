import pywifi
import time
from pywifi import const
from getpass import getpass

class PoJie():
    def __init__(self, name, text):

        self.name = name
        self.text = text
        wifi = pywifi.PyWiFi()                                 # agarrar interfaz de tarjeta de red
        self.iface = wifi.interfaces()[0]                      # Obtener tarjeta de red
        self.iface.disconnect()                                # Desconecta todas las conexiones
        time.sleep(1)
        if self.iface.status() in [const.IFACE_DISCONNECTED, 
                               const.IFACE_INACTIVE]:          # Pruebe si la tarjeta de red se ha desconectado
            print("[+] La tarjeta de red se ha desconectado correctamente")
        else:
            print("[-] Error al desconectar la tarjeta de red")

    def Connect(self):
        profile = pywifi.Profile()                             # Crear objeto de configuración wifi
        profile.ssid = self.name                               # Nombre wifi
        profile.key = str(self.text)                           # Contraseña de WiFi
        profile.auth = const.AUTH_ALG_OPEN                     # La apertura de la tarjeta de red
        profile.akm.append(const.AKM_TYPE_WPA2PSK)             # Algoritmo de cifrado wifi, generalmente WPA2PSK
        profile.cipher = const.CIPHER_TYPE_CCMP                # Unidad de cifrado
        self.iface.remove_all_network_profiles()               # Eliminar todos los archivos wifi
        tem_profile = self.iface.add_network_profile (profile) # Agregar nuevo archivo WiFi
        self.iface.connect (tem_profile)                       # Conectar
        time.sleep(1.5)

        if self.iface.status() == const.IFACE_CONNECTED:       # Juzga si la conexión es exitosa
            print("[+] Conexión exitosa")
        else:
            print("[-] No se pudo conectar")


if __name__ == "__main__":
    print("'RICARDO':         (1)\n'MOVISTAR_855D':   (2)")
    red = int(getpass("RED: "))
    if red == 1:
        obj = PoJie(name= "RICARDO", text= "a000z000")
        obj.Connect()
    elif red == 2:
        obj = PoJie(name= "MOVISTAR_855D", text= "T38Hzm925592UX64N856")
        obj.Connect()
    else:
        print("[-] No se realiza la conexión")