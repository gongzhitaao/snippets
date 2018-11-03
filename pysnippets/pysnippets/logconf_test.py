import os
from logconf import logconf

LOGFILE = '{}.log'.format(__name__)
# By default, the debug file add a suffix '.dbg' to the logfile.  It captures
# everything that prints on the console.
DBGFILE = '{}.dbg'.format(LOGFILE)


def test_show_debug(capsys):
    log = logconf(LOGFILE)
    msg = 'should see this message in console'
    log.debug(msg)
    captured = capsys.readouterr()
    assert msg in captured.out
    os.remove(DBGFILE)


def test_write_dbgfile():
    log = logconf(LOGFILE)
    msg = 'should see this message in dbgfile'
    log.debug(msg)
    assert os.path.exists(DBGFILE)
    out = open(DBGFILE).read()
    assert msg in out
    os.remove(DBGFILE)


def test_write_logfile():
    log = logconf(LOGFILE)
    msg = 'this msg should be saved in the logfile'
    log.info(msg)
    assert os.path.exists(LOGFILE)
    out = open(LOGFILE).read()
    assert msg == out.strip()
    os.remove(DBGFILE)
    os.remove(LOGFILE)


def test_noshow_info(capsys):
    log = logconf(LOGFILE)
    msg = 'should not see this msg in console'
    log.info(msg)
    captured = capsys.readouterr()
    assert msg not in captured.out
    os.remove(DBGFILE)
    os.remove(LOGFILE)
