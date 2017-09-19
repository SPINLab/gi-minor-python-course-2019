# open an existing file
data_file = open('data/data.csv', 'r')




# reading data
print data_file.readline() 
print type(data_file.readline())




# read all lines
print data_file.readlines()



data = []
# process the data
for index, line in enumerate(data_file.readlines()):
#    print line

#    print line.split(',')


#    print line.rstrip('\n').split(',')
    data_line = line.rstrip('\n').split(',')
    if index != 0:
        for i, num in enumerate(data_line):
            data_line[index] = int(num)

    data.append(data_line)

print data

# close the file when done
data_file.close()


# writing data
# file gets created if it doesn't exist
output_file = open('data/processed.txt', 'w')

output_file.write('Hello, world!\n Bye, World!')

output_file.close()




# NOTE Reading and writing data can also be done as follows:
# Reading:
with open('data/data.csv', 'r') as f:
    print f.readline()

# Writing:
with open('data/processed.txt', 'w') as f:
    f.write('Hello, world!')
# This is generally considered the preferred way,
# since it guarantees the file get closed.
