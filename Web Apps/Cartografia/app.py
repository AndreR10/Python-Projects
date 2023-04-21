# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from unittest import result
from flask import Flask, jsonify, render_template, request
from projeto import bursa_wolf, molodenski, polinomial, tridimensional_inversa, gauss_direta, tridimensional_direta, gauss_inversa


# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# --------------------------------------------------------------------------------------------------------------------------------
# Cartesianas/Geográfricas - Tridimensional Inversa
# --------------------------------------------------------------------------------------------------------------------------------
@app.route('/cart_geo', methods=['POST'])
def cart_geo():
    if request.method == "POST":
        data = request.get_json()
       
        X = float(data['x'])
     
        Y = float(data['y'])
      
        Z = float(data['z'])
       
        datum = data['datum']
       
        latitude, longitude, altitude = tridimensional_inversa(X, Y, Z, datum)

        latitude = '{0} {1} {2:2.4f}'.format(int(latitude[0]), int(latitude[1]), latitude[2])
        longitude = '{0} {1} {2:2.4f}'.format(int(longitude[0]), int(longitude[1]), longitude[2])
        altitude = '{0:2.4f}'.format(float(altitude))

        results = {'Altitude': altitude, 'Latitude': latitude, 'Longitude': longitude}
        
        if X and Y and Z and datum:
            return jsonify(results)

        return jsonify({'error' : 'Missing data!'})
    
# --------------------------------------------------------------------------------------------------------------------------------
# Cartesianas/Retangulares (Opção 2) - Tridimensional Inversa -> Gauss Direta
# --------------------------------------------------------------------------------------------------------------------------------
@app.route('/cart_ret', methods=['POST'])
def cart_ret():
    if request.method == "POST":
        data = request.get_json()
        # print(data)
        # print(request.form)
        X = float(data['x'])
        # print(X)
        Y = float(data['y'])
        # print(Y)
        Z = float(data['z'])
        # print(Z)
        datum = data['datum']
        # print(datum)
        fuso = data['fuso']
        latitude, longitude, altitude = tridimensional_inversa(X, Y, Z, datum)
        if fuso:
            print("Com fuso")
            M, P = gauss_direta(latitude, longitude, fuso, datum)
        else:
            print("Sem fuso")
            M, P = gauss_direta(latitude, longitude, datum)

        M = '{0:2.4f} m'.format(M)
        P = '{0:2.4f} m'.format(P)
        

        results = {'M': M, 'P': P}
        
        if X and Y and Z and datum:
            return jsonify(results)

        return jsonify({'error' : 'Missing data!'})

# --------------------------------------------------------------------------------------------------------------------------------
# Geográficas/Retangulares (Opção 3) - Gauss Direta
# --------------------------------------------------------------------------------------------------------------------------------
@app.route('/geo_ret', methods=['POST'])
def geo_ret():
    if request.method == "POST":
        data = request.get_json()

        print(data)
        
        # latitude, longitude, altitude = tridimensional_inversa(X, Y, Z, datum)
        latitude = (float(data['latGrau']), float(data['latMin']), float(data['latSec']))
        longitude = (float(data['longGrau']), float(data['longMin']), float(data['longSec']))
        datum = data['datum']
        fuso = data['fuso']

        if fuso:
            print("Com fuso")
            M, P = gauss_direta(latitude, longitude, datum, fuso)
        else:
            print("Sem fuso")
            M, P = gauss_direta(latitude, longitude, datum)

        M = '{0:2.4f} m'.format(M)
        P = '{0:2.4f} m'.format(P)
        

        results = {'M': M, 'P': P}
        
        if latitude and longitude and datum:
            return jsonify(results)

        return jsonify({'error' : 'Missing data!'})

# --------------------------------------------------------------------------------------------------------------------------------
# Geográficas/Cartesianas (Opção 4) - Tridimensional Direta
# --------------------------------------------------------------------------------------------------------------------------------
@app.route('/geo_cart', methods=['POST'])
def geo_cart():
    if request.method == "POST":
        data = request.get_json()

        print(data)
        
        # latitude, longitude, altitude = tridimensional_inversa(X, Y, Z, datum)
        latitude = (float(data['latGrau']), float(data['latMin']), float(data['latSec']))
        longitude = (float(data['longGrau']), float(data['longMin']), float(data['longSec']))
        datum = data['datum']
        fuso = data['fuso']
        h = float(data['h'])

        if fuso:
            print("Com fuso")
            X, Y, Z = tridimensional_direta(latitude, longitude, h, datum, fuso)
        else:
            print("Sem fuso")
            X, Y, Z = tridimensional_direta(latitude, longitude, h, datum, fuso)

        X = '{0:2.4f} m'.format(X)
        Y = '{0:2.4f} m'.format(Y)
        Z = '{0:2.4f} m'.format(Z)
        

        results = {'X': X, 'Y': Y, 'Z': Z}
        
        if latitude and longitude and datum and h:
            return jsonify(results)

        return jsonify({'error' : 'Missing data!'})

# --------------------------------------------------------------------------------------------------------------------------------
# Retangulares/Geográficas (Opção 5) - Gauss Inversa
# --------------------------------------------------------------------------------------------------------------------------------
@app.route('/ret_geo', methods=['POST'])
def ret_geo():
    if request.method == "POST":
        data = request.get_json()

        print(data)
        
        # latitude, longitude, altitude = tridimensional_inversa(X, Y, Z, datum)
        M = float(data['m'])
        P = float(data['p'])
        datum = data['datum']
        fuso = data['fuso']
        

        if fuso:
            print("Com fuso")
            latitude, longitude = gauss_inversa(M, P, datum, fuso)
        else:
            print("Sem fuso")
            latitude, longitude = gauss_inversa(M, P, datum)

        latitude = '{0} {1} {2:2.4f}'.format(int(latitude[0]), int(latitude[1]), latitude[2])
        longitude = '{0} {1} {2:2.4f}'.format(int(longitude[0]), int(longitude[1]), longitude[2])
        

        results = {'Latitude': latitude, 'Longitude': longitude}
        
        if M and P and datum:
            return jsonify(results)

        return jsonify({'error' : 'Missing data!'})


# --------------------------------------------------------------------------------------------------------------------------------
# Retangulares/Cartesianas (Opção 6) - Gauss inversa -> Tridimensional direta
# --------------------------------------------------------------------------------------------------------------------------------
@app.route('/ret_cart', methods=['POST'])
def ret_cart():
    if request.method == "POST":
        data = request.get_json()

        print(data)
        
        
        M = float(data['m'])
        P = float(data['p'])
        datum = data['datum']
        fuso = data['fuso']
        h = float(data['h'])
        

        if fuso:
            print("Com fuso")
            latitude, longitude = gauss_inversa(M, P, datum, fuso)
            print(latitude)
            print(longitude)
            X, Y, Z = tridimensional_direta(latitude, longitude, h, datum)
        else:
            print("Sem fuso")
            latitude, longitude = gauss_inversa(M, P, datum)
            print(latitude)
            print(longitude)
            X, Y, Z = tridimensional_direta(latitude, longitude, h, datum)
            print(X)
            print(Y)
            print(Z)

        
        X = '{0:2.4f} m'.format(X)
        Y = '{0:2.4f} m'.format(Y)
        Z = '{0:2.4f} m'.format(Z)

        results = {'X': X, 'Y': Y, 'Z': Z}

        if M and P and datum and h:
            return jsonify(results)

        return jsonify({'error' : 'Missing data!'})


# --------------------------------------------------------------------------------------------------------------------------------
# Retangulares/Retangulares (Opção 10) - Gauss inversa (Ex 2) > Tridimensional direta (Ex 3) > Bursa-Wolf (Ex 5) > Tridimensional
# inversa (Ex 4) > Gauss direta (Ex 1)* | Polinomial
# --------------------------------------------------------------------------------------------------------------------------------
@app.route('/polinomial/ret_ret', methods=['POST'])
@app.route('/bursa_wolf/ret_ret', methods=['POST'])
def ret_ret():
    if request.method == "POST":
        data = request.get_json()

        print(data)
        
        
        M = float(data['m'])
        P = float(data['p'])
        datum1 = data['datum1']
        datum2 = data['datum2']
        datum1_name = data['datum1_name']
        datum2_name = data['datum2_name']
        fuso = data['fuso']
        h = float(data['h'])
        transform = data['transform']

        print('{0} -> {1}'.format(datum1_name, datum2_name))
        
        if transform == 'Bursa-Wolf':

            if datum1_name == 'ETRS89':
                
                latitude, longitude = gauss_inversa(M, P, datum1)
                print('{0} {1}'.format(latitude, longitude))

                X, Y, Z = tridimensional_direta(latitude, longitude, h, datum1)
                print('{0} {1} {2}'.format(X, Y, Z))

                X, Y, Z = bursa_wolf(X, Y, Z, datum2_name, invert=True)
                print('{0} {1} {2}'.format(X, Y, Z))
                
                latitude, longitude, h = tridimensional_inversa(X, Y, Z, datum2)
                print('{0} {1} {2}'.format(latitude, longitude, h))

                M, P = gauss_direta(latitude, longitude, datum2)
                print('{0} {1}'.format(M, P))
            else:
               
                latitude, longitude = gauss_inversa(M, P, datum1)
                print('{0} {1}'.format(latitude, longitude))

                X, Y, Z = tridimensional_direta(latitude, longitude, h, datum1)
                print('{0} {1} {2}'.format(X, Y, Z))

                X, Y, Z = bursa_wolf(X, Y, Z, datum1_name)
                print('{0} {1} {2}'.format(X, Y, Z))

                latitude, longitude, h = tridimensional_inversa(X, Y, Z, datum2)
                print('{0} {1} {2}'.format(latitude, longitude, h))

                M, P = gauss_direta(latitude, longitude, datum2)
                print('{0} {1}'.format(M, P))

        elif transform == 'Polinomial 2º grau':

            if datum1_name == 'ETRS89':     
                M, P = polinomial(M, P, datum2_name, invert=True)
                print('{0} {1}'.format(M, P))
            else:
                M, P = polinomial(M, P, datum1_name)
                print('{0} {1}'.format(M, P))

        M = '{0:2.4f} m'.format(M)
        P = '{0:2.4f} m'.format(P)
        H = '{0:2.4f} m'.format(h)

        results = {'M': M, 'P': P, 'Altitude': H}

        if M and P and datum1 and datum2 and h:
            return jsonify(results)

        return jsonify({'error' : 'Missing data!'})

# --------------------------------------------------------------------------------------------------------------------------------
# Geográficas/Geográficas (Opção 5) - Molodenski
# --------------------------------------------------------------------------------------------------------------------------------
@app.route('/molodenski/geo_geo', methods=['POST'])
def geo_geo():
    if request.method == "POST":
        data = request.get_json()

        print(data)
        
        
        latitude = (float(data['latGrau']), float(data['latMin']), float(data['latSec']))
        longitude = (float(data['longGrau']), float(data['longMin']), float(data['longSec']))
        datum1 = data['datum1']
        datum2 = data['datum2']
        datum1_name = data['datum1_name']
        datum2_name = data['datum2_name']
        fuso = data['fuso']
        h = float(data['h'])

        if datum1_name == 'ETRS89':
            print("ETRS89")
            latitude, longitude, h = molodenski(latitude, longitude, h, datum1, datum2_name, invert=True)
        else:
            latitude, longitude, h = molodenski(latitude, longitude, h, datum1, datum1_name)

        latitude = '{0} {1} {2:2.4f}'.format(int(latitude[0]), int(latitude[1]), latitude[2])
        longitude = '{0} {1} {2:2.4f}'.format(int(longitude[0]), int(longitude[1]), longitude[2])
        altitude = '{0:2.4f}'.format(h)
        

        results = {'Latitude': latitude, 'Longitude': longitude, 'Altitude': altitude}
        
        if latitude and longitude and datum1 and datum1_name and datum2_name:
            return jsonify(results)

        return jsonify({'error' : 'Missing data!'})







# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run(debug=True)


