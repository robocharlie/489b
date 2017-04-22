# import all the things



# initalize the sensors and ports

# timing variables

# make a threshhold value for the photoresistors
thresh = 800

# from reading the sensor we get an array of ints

rawval = [234, 254, 299, 266]
bin = [0, 0, 0, 0]
# basically want to take these value, convert to a on/off and hav those numbers
# represnt "bits" so we have 16 positions
# use dictionary to define n/s/e/w


def get_direction():

    directions = {'0000': 'Southwest',
                  '0001': 'West-Southwest',
                  '0010': 'South-Southwest',
                  '0011': 'South',
                  '0100': 'West-Northwest',
                  '0101': 'West',
                  '0110': 'Northwest',
                  '0111': 'North-Northwest',
                  '1000': 'East-Southeast',
                  '1001': 'East',
                  '1010': 'Southeast',
                  '1011': 'South-Southeast',
                  '1100': 'Northeast',
                  '1101': 'East-Northeast',
                  '1110': 'North-Northeast',
                  '1111': 'North'
                  }

    # read in values from ADC
    for val in rawval:
        if val > thresh:
            bin[rawval.index(val)] = 1
        else:
            bin[rawval.index(val)] = 0
    # return bin
    blah = "".join(str(x) for x in bin)  # hacky way to convert to string
    return directions[blah]
wind = get_direction()
print(wind)
#print(wind+1)
# print(str(wind))
# print(''.join(str(x) for x in wind))
