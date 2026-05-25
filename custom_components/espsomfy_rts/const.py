"""Constants for the QA RF Hub / ESPSomfy RTS integration.

Supports both:
- Somfy RTS shades (original ESPSomfy-RTS functionality)
- Open-protocol RF devices (PT2262/EV1527/HT6P20B/Period-OOK/Dooya) — QA RF Hub fork

The QA RF Hub firmware exposes RF devices via separate endpoints on the web
server port (80), while shades use the api server port (8081). The WebSocket
on port 8080 broadcasts events for both shade and RF device state changes.
"""

from homeassistant.const import Platform

VERSION = "v2.5.0"
DOMAIN = "espsomfy_rts"
MANUFACTURER = "QA Automação"
API_CONTROLLER = "/controller"
API_SHADES = "/shades"
API_GROUPS = "/groups"
API_SHADECOMMAND = "/shadeCommand"
API_GROUPCOMMAND = "/groupCommand"
API_TILTCOMMAND = "/tiltCommand"
API_DISCOVERY = "/discovery"
API_LOGIN = "/login"
API_SETPOSITIONS = "/setPositions"
API_SETSENSOR = "/setSensor"
API_BACKUP = "/backup"
API_REBOOT = "/reboot"
API_RESTORE = "/restore"
# QA RF Hub — RF device endpoints (served on web server port 80, not api 8081)
API_RFDEVICES = "/rfdevices"
API_RFDEVICE = "/rfdevice"
API_RFSEND = "/rfsend"

EVT_CONTROLLER = "controller"
EVT_SHADESTATE = "shadeState"
EVT_GROUPSTATE = "groupState"
EVT_SHADECOMMAND = "shadeCommand"
EVT_SHADEADDED = "shadeAdded"
EVT_SHADEREMOVED = "shadeRemoved"
EVT_CONNECTED = "connected"
EVT_FWSTATUS = "fwStatus"
EVT_UPDPROGRESS = "updateProgress"
EVT_WIFISTRENGTH = "wifiStrength"
EVT_ETHERNET = "ethernet"
EVT_MEMSTATUS = "memStatus"
# QA RF Hub — RF device events
EVT_RFSTATE = "rfState"
EVT_RFDEVICES = "rfDevices"
EVT_RFLEARNING = "rfLearning"

ATTR_RESTOREFILE = "Restore File"
ATTR_AVAILABLE_MODES = "???"

PLATFORMS: list[Platform] = [
    Platform.BINARY_SENSOR,
    Platform.BUTTON,
    Platform.COVER,
    Platform.SENSOR,
    Platform.SWITCH,
    Platform.UPDATE,
]
