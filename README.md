# Destiny-String-Extractor
This project extracts strings from the popular game Destiny 2. 
String files are represented by a special tag of bytes 65 00 80 80. 
Right after this tag there is 2 bytes that tell how many bytes of characters there are in the file. AKA arraySize.
After these 2 bytes there is 6 bytes of empty space before the string array.
Using this knowledge we can determine how to grab the strings from each file without getting garbage values and other stuff the file may have.
Ive included photos to show these tags and an example of a file.

<img alt="tagExample.PNG" src="https://github.com/ejw9fc/Destiny-String-Extractor/blob/main/tagExample.PNG?raw=true" data-hpc="true" class="Box-sc-g0xbh4-0 fzFXnm">

Follow the instructions on the program.
Make sure your path to the files is correct using forward slashes and don't use quotations.
Once the program is complete you can view your results in the folder.
Thank you!
