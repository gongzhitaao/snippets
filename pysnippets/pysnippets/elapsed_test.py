from elapsed import elapsed

from timeit import default_timer as timer
import time
import pytest


def test_usage():
    d0 = 0.7
    t0 = timer()
    # You could do nothing, something interesting, or sleeping.
    time.sleep(d0)
    t1 = timer()
    msg = elapsed(t1 - t0)
    d1 = float(msg[:-1])
    assert d1 == pytest.approx(d0, 0.01)


def test_second():
    x = 1.23456
    y0 = '1.23456s'
    y1 = elapsed(x)
    assert y1 == y0


def test_minute():
    x = 61.23456
    y0 = '1.02058m'
    y1 = elapsed(x)
    assert y1 == y0


def test_hour():
    x = 3612.34567
    y0 = '1.00343h'
    y1 = elapsed(x)
    assert y1 == y0


def test_day():
    x = 86476.54321
    y0 = '1.00089d'
    y1 = elapsed(x)
    assert y1 == y0


def test_large():
    x = 8640000
    y0 = '100.00000d'
    y1 = elapsed(x)
    assert y1 == y0
