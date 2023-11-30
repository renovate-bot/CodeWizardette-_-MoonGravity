import datetime
import ephem
import csv
def calculate_gravitational_pull(observer):
    moon = ephem.Moon()
    moon.compute(observer)
    gravitational_pull = moon.mag
    return gravitational_pull
def calculate_gravitational_effect(gravitational_pull, distance):
    g = 6.67430 * (10 ** -11)
    m1 = 7.34767 * (10 ** 22)
    m2 = 5.97237 * (10 ** 24)
    r = (distance * 1000) + 384_400_000
    gravitational_effect = (g * m1 * m2) / (r ** 2)
    return gravitational_effect
def calculate_distance(observer):
    moon = ephem.Moon()
    moon.compute(observer)
    distance = moon.earth_distance * 149_597_870.7
    return distance
#İstanbul
observer = ephem.Observer()
observer.lat = '41.0082'
observer.lon = '28.9784'
observer.elev = 0
start_date = datetime.date(2027, 1, 1)
end_date = datetime.date(2028, 1, 1)
filename = 'ay_kuvveti.csv'
fieldnames = ['Tarih', 'Kütle Çekim Kuvveti', 'Yerçekimi Etkisi']
with open(filename, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    while start_date < end_date:
        observer.date = start_date
        distance = calculate_distance(observer)
        if distance < 380000:
            for hours in [24, 36]:
                observer.date = start_date + datetime.timedelta(hours=hours)
                gravitational_pull = calculate_gravitational_pull(observer)
                gravitational_effect = calculate_gravitational_effect(gravitational_pull, distance)
                writer.writerow({'Tarih': start_date, 'Kütle Çekim Kuvveti': gravitational_pull, 'Yerçekimi Etkisi': gravitational_effect})
        start_date += datetime.timedelta(days=1)
print("CSV dosyası başarıyla oluşturuldu.")
