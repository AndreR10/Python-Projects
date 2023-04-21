import math

datums = {
    '1': {
        'name': 'ETRS89',
        'a': 6378137,
        'f': 1/298.257222101,
        'fator_escala': 1,
        'lat0': math.radians(39+40/60+5.73/3600),
        'lon0': -(math.radians(8+7/60+59.19/3600)),
    },
    '2': {
        'name': 'Datum Lisboa',
        'a': 6378388,
        'f': 1/297,
        'fator_escala': 1,
        'lat0': math.radians(39+40/60+0/3600),
        'lon0': -(math.radians(8+7/60+54.862/3600)),
    },
    '3': {
        'name': 'Datum 73',
        'a': 6378388,
        'f': 1/297,
        'fator_escala': 1,
        'lat0': math.radians(39+40/60+0/3600),
        'lon0': -(math.radians(8+7/60+54.862/3600)),
    },
    '4': {
        'name': 'ITRF93',
        'a': 6378137,
        'f': 1/298.257222101,
        'fator_escala': 0.9996,
        'lat0': math.radians(0),
        # 'lon0': [-(math.radians(33)), -(math.radians(27)), -(math.radians(15))],
        'fuso_lon0': {
            '25': -(math.radians(33)),
            '26': -(math.radians(27)),
            '28': -(math.radians(15)),
        }
    }
}

transform = {
    'Bursa-Wolf' : {
        'Datum Lisboa': {
            'delta_X': -283.088,
            'delta_Y': -70.693,
            'delta_Z': 117.445,
            'Rx': - math.radians(1.157/3600),
            'Ry': math.radians(0.059/3600),
            'Rz': - math.radians(0.652/3600),
            'alpha': - 4.058 * 10 ** (-6)
        },

        'Datum 73': {
            'delta_X': -230.994,
            'delta_Y': 102.591,
            'delta_Z': 25.199,
            'Rx': math.radians(0.633/3600),
            'Ry': - math.radians(0.239/3600),
            'Rz': math.radians(0.900/3600),
            'alpha': 1.950 * 10 ** (-6)
        }
    },
    'Molodensky': {
        'Datum Lisboa': {
            'delta_X': -303.861,
            'delta_Y': -60.693,
            'delta_Z': 103.607,
            'delta_a': -251.000,
            'delta_f': -1.4192686*10**(-5)
        },

        'Datum 73': {
            'delta_X': -223.150,
            'delta_Y': 110.132,
            'delta_Z': 36.711,
            'delta_a': -251.000,
            'delta_f': -1.4192686 * 10 ** (-5)
        }
    },
    'Polinomial': {
        'Datum 73': {
            'a0': 0.28961,
            'a1': 129999.16977,
            'a2': -5.26888,
            'a3': -0.32257,
            'a4': -0.87853,
            'a5': -1.22237,
            'b0': -0.08867,
            'b1': 2.39595,
            'b2': 279997.91435,
            'b3': 0.15146,
            'b4': 1.11109,
            'b5': -1.06143,
            'X0': 0,
            'Y0': 0,
            'h': 130000,
            'k': 280000
        },

        'Datum Lisboa': {
            'a0': 1.38051,
            'a1': 129998.56256,
            'a2': -1.69483,
            'a3': -0.57226,
            'a4': -2.9606,
            'a5': -2.45601,
            'b0': 0.80894,
            'b1': 1.31669,
            'b2': 279995.74505,
            'b3': 0.24888,
            'b4': 2.65999,
            'b5': -3.86484,
            'X0': 0,
            'Y0': 0,
            'h': 130000,
            'k': 280000
        }
    }
}




def abcdef_values(e):

    A = 1 + 3/4 * (e ** 2) + 45/64 * (e ** 4) + 175/256 * (e ** 6) + \
        11025/16384 * (e ** 8) + 43659/65536 * (e ** 10)

    B = 3/4 * (e ** 2) + 15/16 * (e ** 4) + 525/512 * (e ** 6) + \
        2205/2048 * (e ** 8) + 72765/65536 * (e ** 10)

    C = 15/64 * (e ** 4) + 105/256 * (e ** 6) + 2205 / \
        4096 * (e ** 8) + 10395/16384 * (e ** 10)

    D = 35/512 * (e ** 6) + 315/2048 * (e ** 8) + 31185/131072 * (e ** 10)

    E = 315/16384 * (e ** 8) + 3465/65536 * (e ** 10)

    F = 3465/131072 * (e ** 10)

    return {
        'A': A,
        'B': B,
        'C': C,
        'D': D,
        'E': E,
        'F': F
    }


def dd2dms(decimaldegree, direction='x'):
    # if type(decimaldegree) != 'float':

    if type(decimaldegree) != 'float':
        try:
            decimaldegree = float(decimaldegree)
        except:
            print('\nERROR: Could not convert %s to float.' %
                  (type(decimaldegree)))
            return 0
    if decimaldegree < 0:
        decimaldegree = -decimaldegree
        if direction == 'x':
            appendix = 'W'
        else:
            appendix = 'S'
    else:
        if direction == 'x':
            appendix = 'E'
        else:
            appendix = 'N'
    minutes = decimaldegree % 1.0*60
    seconds = minutes % 1.0*60

    return '{0}°{1}\'{2:2.3f}"{3}'.format(int(math.floor(decimaldegree)), int(math.floor(minutes)), seconds, appendix)


def dms(deg):
    f, d = math.modf(deg)
    s, m = math.modf(abs(f) * 60)
    return (d, m, s * 60)
    # return '{0} {1} {2:2.4f}'.format(int(d), int(m), s * 60)
