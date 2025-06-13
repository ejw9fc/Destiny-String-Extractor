import os

def readUnkStringFolders(folderPath, outputFileName):
    processedData = bytearray()
    for root, dirs, files in os.walk(folderPath):
        print("Opening Subfolder:", root)
        print("")
        for fileName in files:
            filePath = os.path.join(root, fileName)
            with open(filePath, 'rb') as file:
                byteData = file.read()
                processedData += processData(byteData)
                if b'\x65\x00\x80\x80' in byteData:  # Check if the pattern is found
                    processedData += b'\n\n'  # Add newline after processing if pattern is found

    outputFilePath = os.path.join(folderPath, outputFileName)
    with open(outputFilePath, 'wb') as outputFile:
        outputFile.write(processedData)

def processData(data):
    hexPattern = bytes.fromhex('65008080')
    index = 0
    processedData = bytearray()
    while index < len(data):
        try:
            startIndex = data.index(hexPattern, index)
        except ValueError:
            break
        index = startIndex + len(hexPattern)
        
        # Read the next 2 bytes to determine how many bytes of chars there are
        bytesToOutput = int.from_bytes(data[index:index+2], byteorder='big')
        index += 2
        
        # Output the specified number of bytes that we got from bytesToOutput
        processedData += data[index+6:index+6+bytesToOutput]
        index += bytesToOutput
    
    return processedData

if __name__ == "__main__":
    folderRead = input("Format: C:/UnkFolder/\nEnter the folder path: ")  # Folder path
    outputFileName = input("Format: name.txt\nEnter the output file name: ")
    readUnkStringFolders(folderRead, outputFileName)
    print("Thank you for using the string extractor! You can check your results in your input folder.")
