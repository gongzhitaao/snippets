def elapsed(sec):
    "Format elapsed seconds."
    if sec < 60:
        val = sec
        unit = 's'
    elif sec < 60 * 60:
        val = sec / 60
        unit = 'm'
    elif sec < 24 * 60 * 60:
        val = sec / (60 * 60)
        unit = 'h'
    elif sec < 7 * 24 * 60 * 60:
        val = sec / (24 * 60 * 60)
        unit = 'd'
    return '{v:.5f}{u}'.format(v=val, u=unit)
