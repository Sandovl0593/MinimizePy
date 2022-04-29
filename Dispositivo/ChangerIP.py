import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface para cambiar direccion MAC")
    parser.add_option("-m", "--mac", dest="new_mac", help="Nueva direccion MAC")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Por favor indicar una interfaz, usa --help para mas imformacion")
    elif not options.new_mac:
        parser.error("[-] Por favor indicar una direccion MAC, usa --help para mas imformacion")
    return options

def change_mac(interface, new_mac):
    print(f"[+] Cambiando direccion MAC {interface} a {new_mac}")
    subprocess.call(["ipconfig", interface, "down"])
    subprocess.call(["ipconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ipconfig", interface, "up"])

options = get_arguments()
change_mac(options.interface, options.new_mac)
