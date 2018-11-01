import sys
import logging
import logging.config


def logconf(logfile='/tmp/tmp.log'):

    class _RemoveData():
        "Do not print data to the console."

        def filter(self, rec):
            return rec.levelno < logging.INFO

    conf = {
        'version': 1,
        'formatters': {
            'standard': {
                'format': '%(module)s %(asctime)s %(levelname)s: %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S',
            },
            'simple': {
                'format': '%(message)s',
            },
        },
        'filters': {
            'nodata': {
                '()': _RemoveData,
            }
        },
        'handlers': {
            'console.err': {
                'class': 'logging.StreamHandler',
                'formatter': 'standard',
                'level': 'ERROR',
                'stream': sys.stderr,
            },
            'console.dbg': {
                'class': 'logging.StreamHandler',
                'formatter': 'standard',
                'level': 'DEBUG',
                'stream': sys.stdout,
                'filters': ['nodata'],
            },
            'file.dbg': {
                'class': 'logging.FileHandler',
                'formatter': 'standard',
                'level': 'DEBUG',
                'filename': '{}.dbg'.format(logfile),
                'mode': 'w',
                'filters': ['nodata'],
            },
            'file.dat': {
                'class': 'logging.FileHandler',
                'formatter': 'simple',
                'level': 'INFO',
                'filename': logfile,
                'mode': 'w',
            },
        },
        'loggers': {
            'default': {
                'level': 'DEBUG',
                'handlers': ['console.dbg', 'file.dbg', 'file.dat'],
                'propagate': False,
            },
        },
        'root': {
            'level': 'ERROR',
            'handlers': ['console.err']
        }
    }

    logging.config.dictConfig(conf)
    log = logging.getLogger('default')
    return log
