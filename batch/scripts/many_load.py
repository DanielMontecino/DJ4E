import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

# name	description	justification	year	longitude	latitude	area_hectares	category	state	region	iso


from unesco.models import Site, Category, State, Region, Iso


def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Site.objects.all().delete()
    Category.objects.all().delete()
    State.objects.all().delete()
    Region.objects.all().delete() 
    Iso.objects.all().delete() 

    # Format
    # name  description justification year longitude latitude area_hectares category state region iso
    

    for row in reader:
        print()
        print(row)
        c, created = Category.objects.get_or_create(name=row[7])
        i, created = Iso.objects.get_or_create(name=row[10])
        r, created = Region.objects.get_or_create(name=row[9])
        print(row[7], c)
        print(row[10], i)
        print(row[9], r)
        s, created = State.objects.get_or_create(name=row[8], iso=i, region=r)
        s.save()
        print(row[8], s)
        print("VALUES")
        print(row[3:7])
        year = int(row[3]) if row[3].strip() != '' else None
        lat = float(row[5]) if row[5].strip() != '' else None
        lon = float(row[4]) if row[4].strip() != '' else None
        area = float(row[6]) if row[6].strip() != '' else None

        site, created = Site.objects.get_or_create(name=row[0], category=c, iso=i,  description=row[1], justification=row[2], year=year, longitude=lon, latitude=lat, area_hectares=area, state=s)

        site.save()
