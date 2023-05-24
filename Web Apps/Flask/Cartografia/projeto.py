import sys
import math
from utility import datums, dd2dms, abcdef_values, dms, transform


def gauss_direta(coor_lat, coor_lon, datum, *fuso):
    """
        Realiza a transformação direta das coordenadas geodésicas (latitude, longitude) dos vértices dados
        em coordenadas(M, P)
    """

    print("-- Gauss Direta --")

    flag = True

    while flag:

        if datum == str(4):
            print(fuso)
            # fuso = input("Indique o fuso: ")

            a = datums[datum]['a']
            f = datums[datum]['f']

            e = math.sqrt(f * (2 - f))

            fator_escala = datums[datum]['fator_escala']

            lat_g, lat_m, lat_s = coor_lat
            lon_g, lon_m, lon_s = coor_lon

            lat = math.radians(
                int(lat_g)+float(lat_m)/60+float(lat_s)/3600)

            lat0 = datums[datum]['lat0']

            lon = -(math.radians(int(abs(lon_g)) +
                    float(lon_m)/60+float(lon_s)/3600))

            lon0 = datums[datum]['fuso_lon0'][fuso[0]]

        else:

            a = datums[datum]['a']
            f = datums[datum]['f']
            e = math.sqrt(f * (2 - f))

            fator_escala = datums[datum]['fator_escala']

            lat_g, lat_m, lat_s = coor_lat
            lon_g, lon_m, lon_s = coor_lon

            lat = math.radians(
                int(lat_g)+float(lat_m)/60+float(lat_s)/3600)

            lat0 = datums[datum]['lat0']

            lon = -(math.radians(int(abs(lon_g)) +
                    float(lon_m)/60+float(lon_s)/3600))

            lon0 = datums[datum]['lon0']
        flag = False

    A, B, C, D, E, F = abcdef_values(e).values()

    sigma = a * (1 - (e ** 2)) * (A * (lat - lat0) - B/2 * (math.sin(2 * lat) -
                                                            math.sin(2 * lat0)) + C/4 * (math.sin(4 * lat) - math.sin(4 * lat0)) - D/6 * (math.sin(6 * lat) - math.sin(6 * lat0)) + E/8 * (math.sin(8 * lat) - math.sin(8 * lat0)) - F/10 * (math.sin(10 * lat) - math.sin(10 * lat0)))

    num = a * (1 - (e ** 2))
    den = (1 - ((e ** 2) * (math.sin(lat) ** 2))) ** (3/2)
    ro = num / den
    # ro=6.359520906685529e+06

    N = a / (1 - (e ** 2 * math.sin(lat) ** 2)) ** (1/2)
    # N= 6.386208074769094e+06

    k1 = (N / ro) - math.tan(lat) ** 2
    k2 = (N / ro) + (4 * (N ** 2 / ro ** 2)) - (math.tan(lat) ** 2)

    one = 4 * ((N ** 3) / (ro ** 3)) * (1 - 6 * (math.tan(lat) ** 2))
    two = ((N ** 2) / (ro ** 2)) * (1 + 8 * (math.tan(lat) ** 2))
    three = 2 * (N / ro) * (math.tan(lat) ** 2)
    four = math.tan(lat) ** 4

    k3 = one + two - three + four

    k4 = (8 * ((N ** 4) / (ro ** 4)) * (11 - 24 * (math.tan(lat) ** 2))) - (28 *
                                                                            ((N ** 3)/(ro ** 3)) * (1 - 6 * (math.tan(lat) ** 2))) + (((N ** 2) / (ro ** 2)) * (1 - 32 * (math.tan(lat) ** 2))) - (2 * (N/ro) * (math.tan(lat) ** 2)) + (math.tan(lat) ** 4)
    k5 = 61 - 479 * (math.tan(lat) ** 2) + 179 * \
        (math.tan(lat) ** 4) - (math.tan(lat) ** 6)

    k6 = 1385 - 3111 * (math.tan(lat) ** 2) + 543 * \
        (math.tan(lat) ** 4) + (math.tan(lat) ** 6)

    landa = lon - lon0

    y = fator_escala * (sigma + ((landa ** 2)/2) * N * math.sin(lat) * math.cos(lat) + ((landa ** 4)/24) * N * math.sin(lat)
                        * (math.cos(lat) ** 3) * k2 + ((landa ** 6) / 720) * N * math.sin(lat) * (math.cos(lat) ** 5) * k4 + ((landa ** 8)/40320) * N * math.sin(lat) * (math.cos(lat) ** 7) * k6)

    x = fator_escala * (landa * N * math.cos(lat) + ((landa ** 3) / 6)
                        * N * (math.cos(lat) ** 3) * k1 + ((landa ** 5)/120) * N * (math.cos(lat) ** 5) * k3 + ((landa ** 7) / 5040) * N * (math.cos(lat) ** 7) * k5)

    
    
    
    if datum == '3':
        print("M: {0} m".format(round(x + 180.598, 2)))
        print("P: {0} m".format(round(y - 86.990, 2)))
        return x, y
    elif datum == '4':
        print("M: {0} m".format(round(x + 500000, 2)))
        print("P: {0} m".format(round(y, 2)))
        return x, y
    else:
        print("M: {0} m".format(round(x, 2)))
        print("P: {0} m".format(round(y, 2)))
        return x, y


def tridimensional_direta(coor_lat, coor_lon, h, datum, *fuso):
    """
        Realiza a transformação direta entre coordenadas geodésicas (latitude, longitude, h) dos vértices em
        coordenadas cartesianas tridimensionais (X, Y, Z)
    """
    print("-- Tridimensional Direta --")

    print(coor_lat)
    print(coor_lon)

    a = datums[datum]['a']
    f = datums[datum]['f']

    e = math.sqrt(f * (2 - f))

    lat_g, lat_m, lat_s = coor_lat
    lon_g, lon_m, lon_s = coor_lon

    lat = math.radians(
        int(lat_g)+float(lat_m)/60+float(lat_s)/3600)

    lon = -(math.radians(abs(int(lon_g))+float(lon_m)/60+float(lon_s)/3600))

    N = a / (1 - (e ** 2 * math.sin(lat) ** 2)) ** (1/2)

    X = (N + h) * math.cos(lat) * math.cos(lon)
    Y = (N + h) * math.cos(lat) * math.sin(lon)

    Z = ((1 - e ** 2) * N + h) * math.sin(lat)

    # print("X: {0} m".format(round(X, 4)))
    # print("Y: {0} m".format(round(Y, 4)))
    # print("Z: {0} m".format(round(Z, 4)))
    return X, Y, Z


def tridimensional_inversa(X, Y, Z, datum):
    """
        Realiza a transformação inversa entre coordenadas tridimensionais (X, Y, Z) dos vértices em
        coordenadas geodésicas  (latitude, longitude, h)
    """
    print("-- Tridimensional Inversa --")

    a = datums[datum]['a']

    f = datums[datum]['f']

    e = math.sqrt(f * (2 - f))

    longitude_styled = dd2dms(math.degrees(math.atan(Y / X)), direction='x')

    longitude = dms(math.degrees(math.atan(Y / X)))

    P = (X ** 2 + Y ** 2) ** (1/2)

    lat_aprox = math.atan(Z / (P * (1 - e ** 2)))

    delta_fi = 10 ** -8

    while abs(delta_fi) > (10 ** -10):
        N = a / (1 - (e ** 2 * math.sin(lat_aprox) ** 2)) ** (1/2)

        h = (P / math.cos(lat_aprox)) - N

        new_lat = math.atan((Z + e ** 2 * N * math.sin(lat_aprox)) / P)

        delta_fi = new_lat - lat_aprox

        lat_aprox = new_lat

    latitude_styled = dd2dms(math.degrees(lat_aprox), direction='y')
    latitude = dms(math.degrees(lat_aprox))
    

    print(latitude_styled, longitude_styled, h)
    return latitude, longitude, h


def opcion_one():
    datum = input(
        'Qual o Datum? \n1 - ETRS89\n2 - Datum Lisboa\n3 - Datum 73\n4 - ITRF93\nOpção: ')

    flag = True
    while flag:
        if datum == "1":
            flag = False
            print(datums[datum]['name'])
        elif datum == "2":
            flag = False
            print(datums[datum]['name'])
        elif datum == "3":
            flag = False
            print(datums[datum]['name'])
        elif datum == "4":
            flag = False
            print(datums[datum]['name'])
        else:
            sys.stderr.write(
                'A opção indicada não é válida\n-----------------------------\n')
            datum = input(
                'Qual o Datum? \n1 - ETRS89\n2 - Datum Lisboa\n3 - Datum 73\n4 - ITRF93\nOpção: ')

    print("O datum escolhido foi: {0}".format(datums[datum]['name']))
    print("------------------------------------------------------")

    return datum


def gauss_inversa(M, P, datum, *fuso):
    """
        Realiza a transformação inversa das coordenadas retangulares (M,P) dos vértices geodésicos
        em coordenadas geodésicas(latitude, longitude)
    """
    print("-- Gauss Inversa--")

    a = datums[datum]['a']
    f = datums[datum]['f']
    e = math.sqrt(f * (2 - f))

    A, B, C, D, E, F = abcdef_values(e).values()

    # Datum 73
    if datum == str(3):
        fator_escala = datums[datum]['fator_escala']

        lat0 = datums[datum]['lat0']
        lon0 = datums[datum]['lon0']
        P = P + 86.990
        M = M - 180.598

        sigma_aprox = float(P) / fator_escala

        lat_aprox = lat0 + (sigma_aprox / A * a * (1 - (e ** 2)))

    #  PTRA08-UTM/ITRF93
    elif datum == str(4):
        fator_escala = datums[datum]['fator_escala']

        lat0 = datums[datum]['lat0']
        lon0 = datums[datum]['fuso_lon0'][fuso]

        M = M - 500000

        sigma_aprox = float(P) / fator_escala

        lat_aprox = lat0 + (sigma_aprox / A * a * (1 - (e ** 2)))

    # PT-TM06/ETRS89 e Datum Lisboa
    else:
        fator_escala = datums[datum]['fator_escala']

        lat0 = datums[datum]['lat0']

        lon0 = datums[datum]['lon0']

        sigma_aprox = float(P) / fator_escala

        lat_aprox = lat0 + (sigma_aprox / A * a * (1 - (e ** 2)))

    delta_fi = 10 ** -8

    while abs(delta_fi) > (10 ** -10):
        num = a * (1 - (e ** 2))
        den = (1 - ((e ** 2) * (math.sin(lat_aprox) ** 2))) ** (3/2)
        ro = num / den

        sigma = a * (1 - (e ** 2)) * (A * (lat_aprox - lat0) - B/2 * (math.sin(2 * lat_aprox) -
                                                                      math.sin(2 * lat0)) + C/4 * (math.sin(4 * lat_aprox) - math.sin(4 * lat0)) - D/6 * (math.sin(6 * lat_aprox) - math.sin(6 * lat0)) + E/8 * (math.sin(8 * lat_aprox) - math.sin(8 * lat0)) - F/10 * (math.sin(10 * lat_aprox) - math.sin(10 * lat0)))

        delta_fi = (sigma_aprox - sigma) / ro

        lat_aprox = lat_aprox + delta_fi

    # print("Latitude aproximada: ", lat_aprox)

    N = a / (1 - (e ** 2 * math.sin(lat_aprox) ** 2)) ** (1/2)
    t = math.tan(lat_aprox)
    psi = N / ro

    # print("PSI: ", psi)
    # print("Fator de escala: ", fator_escala)

    lat = lat_aprox - (t / (fator_escala *
                       ro)) * (M ** 2 / (2 * fator_escala * N)) + (t / (fator_escala * ro)) * (M ** 4 / (24 * fator_escala ** 3 * N ** 3)) * (-4*psi**2 + 9*psi * (1 - t ** 2) + 12 * t ** 2) - (t / (fator_escala * ro)) * (M ** 6 / (720 * fator_escala ** 5 * N ** 5)) * (8 * psi ** 4 * (11 - 24 * t ** 2) - 12 * psi ** 3 * (21 - 71 * t ** 2) + 15 * psi ** 2 * (15 - 98 * t ** 2 + 15 * t ** 4) + 180 * psi * (5 * t ** 2 - 3 * t ** 4) - 360 * t ** 4) + (t / (fator_escala * ro)) * (M ** 8 / (40320 * fator_escala ** 7 * N ** 7)) * (1385 + 3633 * t ** 2 + 4095 * t ** 4 + 1575 * t ** 6)

    lon = (((M / (fator_escala * N)) - (M ** 3 / (6 * fator_escala ** 3 * N ** 3)) * (psi + 2 * t ** 2) + (M ** 5 / (120 * fator_escala ** 5 * N ** 5)) * (-4 * psi ** 3 * (1 - 6 * t ** 2) + psi **
           2 * (9 - 68 * t ** 2) + 72 * psi * t ** 2 + 24 * t ** 4) - (M ** 7 / (5040 * fator_escala ** 7 * N ** 7)) * (61 + 662 * t ** 2 + 1320 * t ** 4 + 720 * t ** 6)) / math.cos(lat_aprox)) + lon0

    # print("Latitude final deg: ", math.degrees(lat))
    # print("Longitude final deg: ", math.degrees(lon))

    latitude = dms(math.degrees(lat))
    longitude = dms(math.degrees(lon))

    print(dd2dms(math.degrees(lat), direction='y'))
    print(dd2dms(math.degrees(lon), direction='x'))
    return latitude, longitude

def bursa_wolf(X, Y, Z, datum_name, invert=False):
    
    if invert:
       delta_X, delta_Y, delta_Z, Rx, Ry, Rz, alpha = [-i for i in transform['Bursa-Wolf'][datum_name].values()]
    else:
        delta_X, delta_Y, delta_Z, Rx, Ry, Rz, alpha = transform['Bursa-Wolf'][datum_name].values()
    
    
    Xn = delta_X + (1 + alpha) * (X - Y * Rz + Ry * Z)
    Yn = delta_Y + (1 + alpha) * (Rz * X + Y - Rx * Z)
    Zn = delta_Z + (1 + alpha) * (-Ry * X + Rx * Y + Z)

    # print(Xn, Yn, Zn)
    return Xn, Yn, Zn


def molodenski(latitude, longitude, h, datum, datum_name, invert=False):

    if invert:
       delta_X, delta_Y, delta_Z, delta_a, delta_f = [-i for i in transform['Molodensky'][datum_name].values()]
    else:
        delta_X, delta_Y, delta_Z, delta_a, delta_f = transform['Molodensky'][datum_name].values()
   

    lat_g, lat_m, lat_s = latitude
    lon_g, lon_m, lon_s = longitude

    lat = math.radians(
        int(lat_g)+float(lat_m)/60+float(lat_s)/3600)

    lon = -(math.radians(abs(int(lon_g))+float(lon_m)/60+float(lon_s)/3600))

    a = datums[datum]['a']
    f = datums[datum]['f']
    e = math.sqrt(f * (2 - f))

    num = a * (1 - (e ** 2))
    den = (1 - ((e ** 2) * (math.sin(lat) ** 2))) ** (3/2)
    ro = num / den
    
    b = a * (1 - f)
    N = a / (1 - (e ** 2 * math.sin(lat) ** 2)) ** (1/2)
  

    lat_out = lat + ((-delta_X * math.sin(lat) * math.cos(lon) - delta_Y * math.sin(lat) * math.sin(lon) + delta_Z * math.cos(lat) + delta_a * (
        e ** 2 * N * math.sin(lat) * math.cos(lat) / a) + delta_f * math.sin(lat) * math.cos(lat) * ((a/b) * ro + (b/a) * N)) / (ro + h))

    lon_out = lon + ((-delta_X * math.sin(lon) + delta_Y *
                    math.cos(lon)) / ((N + h) * math.cos(lat)))

    h_out = h + delta_X * math.cos(lat) * math.cos(lon) + delta_Y * math.cos(lat) * math.sin(lon) + delta_Z * math.sin(lat) - delta_a * (a/N) + delta_f * ((b/a) * N * math.sin(lat) ** 2)
    
    latitude = dms(math.degrees(lat_out))
    longitude = dms(math.degrees(lon_out))

    print(dd2dms(math.degrees(lat_out), direction='y'))
    print(dd2dms(math.degrees(lon_out), direction='x'))

    return latitude, longitude, h_out


def polinomial(M, P, datum_name, invert=False):

    if invert:
        a0, a1, a2, a3, a4, a5, b0, b1, b2, b3, b4, b5, X0, Y0, h, k = [ -i for i in transform['Polinomial'][datum_name].values()]

    else:
        a0, a1, a2, a3, a4, a5, b0, b1, b2, b3, b4, b5, X0, Y0, h, k = transform['Polinomial'][datum_name].values()

 

    u = (M - X0) / (h)

    v = (P - Y0) / (k)

    Mn = a0 + a1 * u + a2 * v + a3 * u ** 2 + a4 * u * v + a5 * v ** 2
    Pn = b0 + b1 * u + b2 * v + b3 * u ** 2 + b4 * u * v + b5 * v ** 2

    return Mn, Pn



def main():
    try:
        option = input(
            'A transformação que pretende consiste em transformar coordenadas num mesmo datum (opção 1) ou entre data distintos (opção 2)? ')

        flag = True
        while flag:

            if option == "1":
                datum = opcion_one()
                option = input(
                    'Quais as coordenadas de entrada e de saida?\n1 - Cartesianas/Geográfricas\n2 - Cartesianas/Retangulares\n3 - Geográficas/Geográfricas\n4 - Geográficas/Cartesianas\n5 - Retangulares/Geográfricas\n6 - Retangulares/Cartesianas\nOpção: ')

                flag = True
                while flag:
                    # --------------------------------------------------------------------------------------------------------------------------------
                    # Cartesianas/Geográfricas - Tridimensional Inversa
                    # --------------------------------------------------------------------------------------------------------------------------------
                    if option == "1":
                        try:
                            X, Y, Z = map(float, input(
                                "Indique as coordenadas tridimensionais. X Y Z: ").split())

                            flag = False
                        except ValueError:
                            print(
                                "Os valores indicados não são números. Tente novamente!\n------------------------------------------------------\n")

                        tridimensional_inversa(X, Y, Z, datum)

                        flag = False

                    # --------------------------------------------------------------------------------------------------------------------------------
                    # Cartesianas/Retangulares (Opção 2) - Tridimensional Inversa -> Gauss Direta
                    # --------------------------------------------------------------------------------------------------------------------------------
                    elif option == "2":
                        try:
                            
                            X, Y, Z = map(float, input(
                                "Indique as coordenadas tridimensionais. X Y Z: ").split())
                            print(X)
                            print(Y)
                            print(Z)
                            # X = 4993821.5571
                            # Y = -676850.4038
                            # Z = 3896819.7516
                            flag = False
                        except ValueError:
                            print(
                                "Os valores indicados não são números. Tente novamente!\n------------------------------------------------------\n")
                        coord_geo = tridimensional_inversa(X, Y, Z, datum)

                        latitude, longitude, h = coord_geo

                        print(latitude,
                              longitude, h)

                        gauss_direta(latitude, longitude, datum)

                        flag = False

                    # --------------------------------------------------------------------------------------------------------------------------------
                    # Geográficas/Retangulares (Opção 3) - Gauss Direta
                    # --------------------------------------------------------------------------------------------------------------------------------
                    elif option == "3":
                        # Verificar valores dados para o datum 4
                        try:
                            lat = map(float, input(
                                "Indique as coordenadas geódesicas, Grausº Minutos' Segundos'' para Latitude: ").split())
                            log = map(float, input(
                                "Indique as coordenadas geódesicas, Grausº Minutos' Segundos'' para Longitude: ").split())

                            # print(lat)
                            # print(log)
                            flag = False
                        except ValueError:
                            print(
                                "Os valores indicados não são números. Tente novamente!\n------------------------------------------------------\n")

                        gauss_direta(lat, log, datum)

                        flag = False

                    # --------------------------------------------------------------------------------------------------------------------------------
                    # Geográficas/Cartesianas (Opção 4) - Tridimensional Direta
                    # --------------------------------------------------------------------------------------------------------------------------------
                    elif option == "4":
                        try:
                            lat = map(float, input(
                                "Indique as coordenadas geódesicas, Grausº Minutos' Segundos'' para Latitude: ").split())
                            log = map(float, input(
                                "Indique as coordenadas geódesicas, Grausº Minutos' Segundos'' para Longitude: ").split())
                            h = float(input("h: "))
                            # print(lat)
                            # print(log)
                            flag = False
                        except ValueError:
                            print(
                                "Os valores indicados não são números. Tente novamente!\n------------------------------------------------------\n")

                        tridimensional_direta(lat, log, h, datum)

                        flag = False

                    # --------------------------------------------------------------------------------------------------------------------------------
                    # Retangulares/Geográficas (Opção 5) - Gauss Inversa
                    # --------------------------------------------------------------------------------------------------------------------------------
                    elif option == "5":
                        try:

                            M, P = map(float, input(
                                "Indique as coordenadas. M P: ").split())
                            print(M)
                            print(P)

                            # M = 36448.61
                            # P = -196253.96

                            flag = False
                        except ValueError:
                            print(
                                "Os valores indicados não são números. Tente novamente!\n------------------------------------------------------\n")

                        gauss_inversa(M, P, datum)

                        flag = False
                    # --------------------------------------------------------------------------------------------------------------------------------
                    # Retangulares/Cartesianas (Opção 6) - Gauss inversa -> Tridimensional direta
                    # --------------------------------------------------------------------------------------------------------------------------------
                    elif option == "6":
                        try:
                            M, P = map(float, input(
                                "Indique as coordenadas. M P: ").split())
                            print(M)
                            print(P)

                            # M = 36448.61
                            # P = -196253.96

                            flag = False
                        except ValueError:
                            print(
                                "Os valores indicados não são números. Tente novamente!\n------------------------------------------------------\n")

                        latitude, longitude = gauss_inversa(M, P, datum)

                        # Onde ir buscar o h?
                        # Pedir o h

                        tridimensional_direta(latitude, longitude, h, datum)

                        flag = False
                    else:
                        sys.stderr.write(
                            'A opção indicada não é válida\n-----------------------------\n')
                        option = input(
                            'Quais as coordenadas de entrada e de saida?\n1 - Cartesianas/Geográfricas\n2 - Cartesianas/Retangulares\n3 - Geográficas/Geográfricas\n4 - Geográficas/Cartesianas\n5 - Retangulares/Geográfricas\n6 - Retangulares/Cartesianas\nOpção: ')
                flag = False
            elif option == "2":
                flag = True
                option = input(
                    'Qual o datum de entrada e o de saída? \n1 - Datum Lisboa/ETRS89\n2 - Datum 73/ETRS89\n3 - ETRS89/Datum Lisboa\n4 - ETRS89/Datum 73\nOpção: ')
                while flag:
                    if option == "1":
                        datums = (2, 1)
                        flag = False
                    elif option == "2":
                        datums = (3, 1)
                        flag = False

                    elif option == "3":
                        datums = (1, 2)
                        flag = False

                    elif option == "4":
                        datums = (1, 3)
                        flag = False
                    else:
                        sys.stderr.write(
                            'A opção indicada não é válida\n-----------------------------\n')
                        option = input(
                            'Qual o datum de entrada e o de saída? \n1 - Datum Lisboa/ETRS89\n2 - Datum 73/ETRS89\n3 - ETRS89/Datum Lisboa\n4 - ETRS89/Datum 73\nOpção: ')

                flag = True
                option_2 = input(
                    'Qual a transformação que pretende utilizar?\n1 - Bursa-Wolf\n2 - Molodenski\n3 - Polinomial 2º grau\nOpção: ')
                while flag:
                    if option_2 == '1':
                        trans = 'Bursa Wolf'

                        flag = True
                        option_3 = input(
                            'Quais as coordenadas de entrada e de saida?\n1 - Cartesianas/Geográfricas\n2 - Cartesianas/Retangulares\n3 - Geográficas/Geográfricas\n4 - Geográficas/Cartesianas\n5 - Retangulares/Geográfricas\n6 - Retangulares/Cartesianas\nOpção: ')

                        while flag:
                            if option_3 == "9":
                                try:
                                    X, Y, Z = map(float, input(
                                        "Indique as coordenadas tridimensionais. X Y Z: ").split())

                                    flag = False
                                except ValueError:
                                    print(
                                        "Os valores indicados não são números. Tente novamente!\n------------------------------------------------------\n")

                                tridimensional_inversa(X, Y, Z, datum)

                                flag = False

                            else:
                                print("Não disponivel!")
                                print("Escolha outra opção")
                                option_3 = input(
                                    'Quais as coordenadas de entrada e de saida?\n1 - Cartesianas/Geográfricas\n2 - Cartesianas/Retangulares\n3 - Geográficas/Geográfricas\n4 - Geográficas/Cartesianas\n5 - Retangulares/Geográfricas\n6 - Retangulares/Cartesianas\nOpção: ')
                            
                        flag = False
                    
                    
                    elif option_2 == '2':
                        trans = 'Molodenski'
                        flag = False
                    elif option_2 == '3':
                        trans = 'Polinomial'
                        flag = False
                    else:
                        sys.stderr.write(
                            'A opção indicada não é válida\n-----------------------------\n')
                        option = input(
                            'Qual a transformação que pretende utilizar?\n1 - Bursa-Wolf\n2 - Molodenski\n3 - Polinomial 2º grau\nOpção: ')

                flag = True
                option_3 = input(
                    'Quais as coordenadas de entrada e de saida?\n1 - Cartesianas/Geográfricas\n2 - Cartesianas/Retangulares\n3 - Geográficas/Geográfricas\n4 - Geográficas/Cartesianas\n5 - Retangulares/Geográfricas\n6 - Retangulares/Cartesianas\nOpção: ')

                while flag:
                    if option_3 == "9":
                        try:
                            X, Y, Z = map(float, input(
                                "Indique as coordenadas tridimensionais. X Y Z: ").split())

                            flag = False
                        except ValueError:
                            print(
                                "Os valores indicados não são números. Tente novamente!\n------------------------------------------------------\n")

                        tridimensional_inversa(X, Y, Z, datum)

                        flag = False

                    else:
                        print("Não disponivel!")
                        print("Escolha outra opção")
                        option_3 = input(
                    'Quais as coordenadas de entrada e de saida?\n1 - Cartesianas/Geográfricas\n2 - Cartesianas/Retangulares\n3 - Geográficas/Geográfricas\n4 - Geográficas/Cartesianas\n5 - Retangulares/Geográfricas\n6 - Retangulares/Cartesianas\nOpção: ')
                    
            else:
                sys.stderr.write(
                    'A opção indicada não é válida\n-----------------------------\n')
                option = input(
                    'A transformação que pretende consiste em transformar coordenadas num mesmo datum (opção 1) ou entre data distintos (opção 2)? ')

    except KeyboardInterrupt:
        print("\nPrograma terminado!")
        exit()


if __name__ == '__main__':
    main()
