input_data = open('input.txt' , 'r')
data = input_data.read()
i = 0
max = 0
a = 0
for i in range (0, len(data)):
    if data[i] =='0':
        a = a + 1

    if a > max:
        max = a

    if data[i] =='1':
        a = 0


output = open('output.txt', 'w')
output.write(str(max))

input_data.close()
output.close()
