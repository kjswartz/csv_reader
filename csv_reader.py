# read in csv of animals and string of counties they belong to
# create a csv of counties and string of animals associated
# encoding used due to file being from windows and containing 's 
import csv

COUNTIES = dict()

def main():
    with open('./species.csv', newline='', encoding="cp1251") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for row in reader:            
            counties = row['County(ies)'].split(', ')
            for county in counties:
                if county in COUNTIES: 
                    COUNTIES[county].append(format_name(row))
                else: 
                    COUNTIES[county] = [format_name(row)]
    write_out()

def write_out():
    with open('./species_by_county.csv', 'w', newline='', encoding="cp1251") as csvfile:
        fieldnames = ['County', 'Animals']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for county, animals in COUNTIES.items() :
            writer.writerow({'County': county, 'Animals': ', '.join(animals)})


def format_name(row) -> str:
    return '{0} ({1})'.format(row['Common Name'], row['Status 2018'])

if __name__ == "__main__":
    main()