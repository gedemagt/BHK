import glib

from pyudev import Context, Monitor

def do_print():
    print("jon")
    print("jon")
    print("jon")
    print("jon")
    print("jon")
    print("jon")
    print("jon")


try:
    from pyudev.glib import MonitorObserver

    def device_event(observer, device):
        do_print()
except:
    from pyudev.glib import GUDevMonitorObserver as MonitorObserver

    def device_event(observer, action, device):
        do_print()

context = Context()
monitor = Monitor.from_netlink(context)

monitor.filter_by(subsystem='usb')
observer = MonitorObserver(monitor)

observer.connect('device-event', device_event)
monitor.start()

glib.MainLoop().run()
