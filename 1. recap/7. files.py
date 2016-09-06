# open an existing file
data_file = open('data/data.csv', 'r')




# reading data
print data_file.readline()
print type(data_file.readline())




# read all lines
# print data.readlines()




# process the data
for line in data_file.readlines():
    print line

    print line.split(',')


    print line.rstrip('\n').split(',')

    data = line.rstrip('\n').split(',')

print data

# close the file when done
data_file.close()


# writing data
output_file = open('data/processed.txt', 'w')

output_file.write('Hello, world!')
output_file.close()

## NOTE planning to work with data? Use a mature and robust data/reading writin module.