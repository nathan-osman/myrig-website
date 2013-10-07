from django.contrib.auth.models import User
from django.db import models
from myrig.computer.quantity import Quantity
from south.modelsinspector import add_introspection_rules

class SIIntegerField(models.PositiveIntegerField):
    '''
    Implements storage for a positive integer value of an SI unit
    '''
    
    __metaclass__ = models.SubfieldBase
    
    def __init__(self, unit, *args, **kwargs):
        '''
        Initializes the model field
        '''
        self.unit = unit
        super(SIIntegerField, self).__init__(*args, **kwargs)
    
    def to_python(self, value):
        '''
        Returns a Quantity object representing the value
        '''
        if isinstance(value, Quantity):
            return value
        elif value:
            return Quantity(int(value), self.unit)
        else:
            return None
    
    def get_prep_value(self, value):
        '''
        Returns a representation of the value suitable for the database
        '''
        return int(value)

# Allows the field to be used in South migrations
add_introspection_rules([
    (
        [SIIntegerField,],
        [],
        {
            'unit': ['unit', {},],
        },
    ),
], ['^myrig\.computer\.models\.SIIntegerField',])

class Manufacturer(models.Model):
    '''
    Represents a component manufacturer
    '''
    
    name = models.CharField(max_length=40,
                            help_text='The registered name of the company')
    website = models.URLField(null=True,
                              blank=True,
                              help_text='The official website of the company')

    def __unicode__(self):
        '''
        Returns a string representation of the company
        '''
        return self.name

class Component(models.Model):
    '''
    Represents an individual component
    '''
    
    manufacturer = models.ForeignKey(Manufacturer,
                                     help_text='The manufacturer of the component')
    model = models.CharField(max_length=40,
                             help_text='The model number of the component')
    
    def __unicode__(self):
        '''
        Returns a string representation of the component
        '''
        return self._format((
            self.manufacturer,
            self.model,
        ))
    
    def _format(self, values):
        '''
        Joins the values in the provided list that are nonzero
        '''
        return ' '.join((str(v) for v in values if v))

class Chipset(Component):
    '''
    Represents a chipset
    '''

class Processor(Component):
    '''
    Represents a processor
    '''
    
    series = models.CharField(max_length=40,
                              null=True,
                              blank=True,
                              help_text='The series of the processor')
    clock_speed = SIIntegerField(unit='Hz',
                                 help_text='The clock speed of the processor (in Hz)')
    cores = models.PositiveSmallIntegerField(help_text='The number of cores in the processor')
    
    def __unicode__(self):
        '''
        Returns a string representation of the processor
        '''
        return self._format((
            self.manufacturer,
            self.series,
            self.model,
            '%dx%s' % (
                self.cores,
                self.clock_speed,
            ),
        ))

class Memory(Component):
    '''
    Represents a memory module
    '''
    
    TYPE = (
        ('SDRAM', 'SDRAM',),
        ('DDR',   'DDR',),
        ('DDR2',  'DDR2',),
        ('DDR3',  'DDR3',),
    )
    
    size = SIIntegerField(unit='B',
                          help_text='The storage capacity of the memory (in bytes)')
    type = models.CharField(max_length=10,
                            choices=TYPE,
                            help_text='The type of memory')
    
    def __unicode__(self):
        '''
        Returns a string representation of the memory
        '''
        return self._format((
            self.manufacturer,
            self.size,
            self.get_type_display(),
        ))
    
    class Meta:
        verbose_name_plural = 'Memory'

class HardDrive(Component):
    '''
    Represents a hard drive
    '''
    
    size = SIIntegerField(unit='B',
                          help_text='The storage capacity of the hard drive (in bytes)')
    ssd = models.BooleanField(help_text='Whether the hard drive is solid state')
    
    def __unicode__(self):
        '''
        Returns a string representation of the hard drive
        '''
        return self._format((
            self.manufacturer,
            self.size,
            'SSD' if self.ssd else None,
        ))

class VideoAdapter(Component):
    '''
    Represents a video adapter
    '''
    
    memory = SIIntegerField(unit='B',
                            help_text='The amount of video memory in the video adapter (in bytes)')

class OperatingSystem(models.Model):
    '''
    Represents a specific edition of an operating system
    '''
    
    ARCHITECTURE = (
        ('x86',     'x86',),
        ('x86-64',  'x86-64',),
        ('ARM',     'ARM',),
        ('PowerPC', 'PowerPC',),
    )
    
    name = models.CharField(max_length=40,
                            help_text='The name of the operating system')
    version = models.CharField(max_length=40,
                               help_text='The version name or number of the operating sytem')
    architecture = models.CharField(max_length=10,
                                    choices=ARCHITECTURE,
                                    help_text='The architecture of the operating system')
    
    def __unicode__(self):
        '''
        Returns a string representation of the operating system
        '''
        return '%s %s %s' % (
            self.name,
            self.version,
            self.get_architecture_display(),
        )

class Computer(models.Model):
    '''
    Represents the complete configuration of a computer
    '''
    
    chipset = models.ForeignKey(Chipset,
                                null=True,
                                blank=True,
                                help_text='The chipset of the computer')
    processors = models.ManyToManyField(Processor,
                                        null=True,
                                        blank=True,
                                        help_text='The physical processors installed in the computer')
    memory = models.ManyToManyField(Memory,
                                    null=True,
                                    blank=True,
                                    help_text='The memory modules installed in the computer')
    hard_drives = models.ManyToManyField(HardDrive,
                                         null=True,
                                         blank=True,
                                         help_text='The hard drives installed in the computer')
    video_adapters = models.ManyToManyField(VideoAdapter,
                                            null=True,
                                            blank=True,
                                            help_text='The video adapters installed in the computer')
    operating_systems = models.ManyToManyField(OperatingSystem,
                                               null=True,
                                               blank=True,
                                               help_text='The operating systems installed on the computer')
    
    def __unicode__(self):
        '''
        Returns a string representation of the computer
        '''
        return '%s %s' % (
            self.processors,
            self.memory,
        )

class Rig(models.Model):
    '''
    Represents a computer owned by a user
    '''
    
    user = models.ForeignKey(User, help_text='The owner of the rig')
    computer = models.ForeignKey(Computer, help_text='The computer owned by the user')
    
    def __unicode__(self):
        '''
        Returns a string representation of the rig
        '''
        return self.computer
