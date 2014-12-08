def years():
    year = 1900
    day = count = 0
    d = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    m = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    while year < 2000:
        
        for x in xrange(0, 12):
            day += months[x]
            
            if months[x] < 30 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                day += 1
            if day % 7 == 6:
                count += 1
            day = day % 7
            print m[(x + 1) % 12], d[day]
        year += 1
        print year
    print count

def main():
    years()

main()
