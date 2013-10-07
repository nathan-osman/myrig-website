from django.contrib import admin
from myrig.computer.models import Manufacturer, Chipset, Processor, Memory, HardDrive, VideoAdapter, OperatingSystem, Computer, Rig

admin.site.register(Manufacturer)
admin.site.register(Chipset)
admin.site.register(Processor)
admin.site.register(Memory)
admin.site.register(HardDrive)
admin.site.register(VideoAdapter)
admin.site.register(OperatingSystem)
admin.site.register(Computer)
admin.site.register(Rig)
