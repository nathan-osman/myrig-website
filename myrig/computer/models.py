from django.db import models

class Manufacturer(models.Model):
    '''
    Represents a component manufacturer
    '''
    
    name    = models.CharField(max_length=40,
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
    Represents an individual component in a computer
    '''
    
    manufacturer = models.ForeignKey(Manufacturer,
                                     help_text='The manufacturer of the component')
    model        = models.CharField(max_length=40,
                                    help_text='The model number of the component')
    
    def __unicode__(self):
        '''
        Returns a string representation of the component
        '''
        return '%s %s' % (
            self.manufacturer,
            self.model,
        )


class Chipset(Component):
    '''
    Represents a chipset
    '''


class Processor(Component):
    '''
    Represents a processor
    '''
    
    cores = models.PositiveSmallIntegerField(help_text='The number of cores in the processor')


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
    
    type = models.CharField(max_length=10,
                            choices=TYPE,
                            help_text='The type of memory')


class HardDrive(Component):
    '''
    Represents a hard drive
    '''
    
    mechanical = models.BooleanField(help_text='Whether the hard drive is mechanical')


class VideoAdapter(Component):
    '''
    Represents a video adapter
    '''


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
    
    name         = models.CharField(max_length=40,
                                    help_text='The name of the operating system')
    version      = models.CharField(max_length=40,
                                    help_text='The version name or number of the operating sytem')
    architecture = models.CharField(max_length=10,
                                    choices=ARCHITECTURE,
                                    help_text='The architecture of the operating system')


class Computer(models.Model):
    '''
    Represents the complete configuration of a computer
    '''
    
    chipset           = models.ForeignKey(Chipset,
                                          null=True,
                                          blank=True,
                                          help_text='The chipset of the computer')
    processors        = models.ManyToManyField(Processor,
                                               null=True,
                                               blank=True,
                                               help_text='The physical processors installed in the computer')
    memory            = models.ManyToManyField(Memory,
                                               null=True,
                                               blank=True,
                                               help_text='The memory modules installed in the computer')
    hard_drives       = models.ManyToManyField(HardDrive,
                                               null=True,
                                               blank=True,
                                               help_text='The hard drives installed in the computer')
    video_adapters    = models.ManyToManyField(VideoAdapter,
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
        return 'Computer'
