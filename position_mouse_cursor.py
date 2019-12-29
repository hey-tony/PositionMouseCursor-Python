#!/usr/bin/env python3

import sys, pyautogui

import gi
gi.require_version("Gdk", "3.0")
from gi.repository import Gdk


def move_mouse_to_monitor( selectedMonitor: int ):
    """Moves mouse to selected monitor"""
    monitors = query_monitors()
    totalMonitors = len( monitors )
    if selectedMonitor >= totalMonitors:
        print("Desired monitor index is out of bounds.\nTotal monitors:", totalMonitors)
        return
    selectedMonitor = monitors[ selectedMonitor ]
    ( monitor_name, x_pos, y_pos, width, height ) = selectedMonitor
    pyautogui.moveTo( x_pos+(width/2), y_pos+(height/2) )



def query_monitors() -> []:
    """Queries information for all available monitors."""
    monitors = []

    gdkdsp = Gdk.Display.get_default()
    
    for i in range(gdkdsp.get_n_monitors()):
        monitor = gdkdsp.get_monitor(i)
        scale = monitor.get_scale_factor()
        geo = monitor.get_geometry()
        # print( "{}: {}x{}".format(i, geo.width,geo.height) )
        monitors.append([
            monitor.get_model()] + [n * scale for n in [
                geo.x, geo.y, geo.width, geo.height
            ]
        ])
    return monitors



if __name__ == "__main__":
    monitor = sys.argv[1] if len(sys.argv) > 0 else 0
    move_mouse_to_monitor( int(monitor) )
