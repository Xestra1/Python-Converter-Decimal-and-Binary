from timeit import default_timer as timer
import converter

def dtbconverter(formating=2, inputFile="input.txt", outputFile="output.txt"):
    numbers = []
    with open(inputFile) as input_text_file:
        for line in input_text_file.readlines():
            numbers.append(int(str(line).strip("\n")))
    with open(outputFile, 'a') as output_text_file:
        for num in numbers:
            output_text_file.write(str(converter.decimalToBinary(num, formating)) + '\n')

def btdconverter(formating=2, inputFile="input.txt", outputFile="output.txt"):
    numbers = []
    with open(inputFile) as input_text_file:
        for line in input_text_file.readlines():
            numbers.append(int(str(line).strip("\n")))
    with open(outputFile, 'a') as output_text_file:
        for num in numbers:
            output_text_file.write(str(converter.binaryToDecimal(num, formating)) + '\n')

print('--------------------------------------')
print('PYTHON BINARY AND DECIMAL CONVERTER')
print('--------------------------------------')
print('Usage: Open input.txt and put in your binary or decimal numbers. Then, Answer the inputs. To look at formating options look at the README.md on github. dtb is decimal to binary and btd is binary to decimal.')
typeOfConverter = input('What type of converter (dtb or btd): ')
typeOfFormat = input('What type of format (0, 1, 2) default is 2: ')

start = timer()

if (typeOfConverter == 'dtb'):
    dtbconverter(typeOfFormat)
elif (typeOfConverter == 'btd'):
    btdconverter(typeOfFormat)

end = timer()
print('File Generated!')
print('Time taken to generate: ' + str(end - start))