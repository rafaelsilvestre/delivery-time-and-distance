from math import radians, sin, atan2, sqrt, cos

def distance(p1, p2):
    # Approximate radius of the earth
    R = 6371.0

    lat1 = radians(p1[0])
    lon1 = radians(p1[1])
    lat2 = radians(p2[0])
    lon2 = radians(p2[1])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance

if __name__ == '__main__':
    p1 = (-16.6297431, -49.2785835)
    p2 = (-16.6419884,-49.3239934)

    distance = distance(p1, p2)
    average_speed = 32

    a = int((distance / average_speed) * 60)

    print('Distance {}km'.format(distance))
    print('Speed {}km'.format(average_speed))
    print('Time {}m'.format(a))