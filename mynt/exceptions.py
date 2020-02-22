# -*- coding: utf-8 -*-


class MyntException(Exception):
    code = 1
    
    
    def __init__(self, message, *args):
        self.message = message
        self.debug = args
    
    
    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        message = '!! {0}'.format(self.message)
        
        for d in self.debug:
            message += '\n..  {0}'.format(d)
        
        return message


class ConfigException(MyntException):
    pass

class ContentException(MyntException):
    pass

class FileSystemException(MyntException):
    pass

class OptionException(MyntException):
    code = 2

class ParserException(MyntException):
    pass

class RendererException(MyntException):
    pass
