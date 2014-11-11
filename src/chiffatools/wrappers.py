__author__ = 'ank'


def debug(function_f):

    def wrapper(*args, **kwargs):
        print 'debugging %s!' % function_f.__name__
        print args
        print kwargs
        return  function_f(*args, **kwargs)

    wrapper.__name__ = function_f.__name__+'_debug_wrap'
    wrapper.__doc__ = function_f.__doc__

    return wrapper