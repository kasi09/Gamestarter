import os
import os.path

import xbmcgui

xbmcgui.Dialog().ok("Gamestarter", "Installing GameMaker Pi ports, please do not power off or reboot your Raspberry Pi.")

script_file = os.path.realpath(__file__)
directory = os.path.dirname(script_file)

# xbmcgui.Dialog().ok("Gamestarter", "Done!")
# os.system("sh "+directory+"/resources/bin/install_iarl.sh")

# os.system("sh  /storage/.kodi/addons/script.gamestarter/resources/bin/install_gamemaker.sh")
os.system("sh  https://github.com/bite-your-idols/gamemaker-pi/raw/master/gamemaker-gamestarter.sh")

xbmcgui.Dialog().ok("Gamestarter", "GameMaker Pi ports installed, please reboot your Raspberry Pi.")
