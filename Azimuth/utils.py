import simplekml
from math import radians,cos,sin,pi

def vectorDistancia (lat, long, radio, azimuth):
    latRadians = radians(lat)
    # longRadians = radians(long)
    azimuthRadians = radians(azimuth)

    earthRadiusAtLat = cos(latRadians) * 6371000
    distBetweenLongDegrees = 2 * pi * earthRadiusAtLat / 360
    distBetweenLatDegrees = 2 * pi * 6371000 / 360

    deltaLong = sin(azimuthRadians) * radio / distBetweenLongDegrees
    deltaLat = cos(azimuthRadians) * radio / distBetweenLatDegrees

    finalLat = lat + deltaLat
    finalLong = long + deltaLong

    return (finalLong,finalLat)

def poligonos(lat, long,radio,azimuth,apertura=60,sides=20):
    if (sides < 1):
        return None

    angulito = apertura / sides

    polList = [(long,lat)]

    inicial = azimuth - apertura

    rango = [inicial + (x*angulito) for x in range(0,(2*sides)+1)]

    for alpha in rango:
        polList.append(vectorDistancia(lat,long,radio,alpha))

    polList.append((long,lat))
    return polList

def kmlFile(celda,lat,long,radio,azimuth,apertura):
    puntos = poligonos(float(lat),float(long),radio,azimuth,apertura)

    kml = simplekml.Kml()

    pol = kml.newpolygon(name=celda)

    pol.outerboundaryis = puntos
    pol.style.polystyle.color = '990000ff'

    return kml