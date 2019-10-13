from timeit import default_timer as timer
import converter

def dtbconverter(inputFile="input.txt", outputFile="output.txt"):
    numbers = []
    with open(inputFile) as input_text_file:
        for line in input_text_file.readlines():
            numbers.append(int(str(line).strip("\n")))
    with open(outputFile, 'a') as output_text_file:
        for num in numbers:
            output_text_file.write(str(converter.decimalToBinary(num)) + '\n')

def btdconverter(inputFile="input.txt", outputFile="output.txt"):
    numbers = []
    with open(inputFile) as input_text_file:
        for line in input_text_file.readlines():
            numbers.append(int(str(line).strip("\n")))
    with open(outputFile, 'a') as output_text_file:
        for num in numbers:
            output_text_file.write(str(converter.binaryToDecimal(num)) + '\n')

print('--------------------------------------')
print('PYTHON BINARY AND DECIMAL CONVERTER')
print('--------------------------------------')
print('Usage: Open input.txt and put in your binary or decimal numbers. Then, Answer the input(s). dtb is decimal to binary and btd is binary to decimal.')
typeOfConverter = input('What type of converter (dtb or btd): ')

start = timer()

if (typeOfConverter == 'dtb'):
    dtbconverter()
elif (typeOfConverter == 'btd'):
    btdconverter()

end = timer()
print('File Generated!')
print('Time taken to generate: ' + str(round(end - start, 4)))