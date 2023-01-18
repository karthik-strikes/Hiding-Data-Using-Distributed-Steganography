Base conversion from a DEC
Dividing into blocks and getting the mixed up secret message as an array(/list)
Finding the "k" blocks from a given secret message
Firstly we start with the Base conversion from a base value provide to hex, oct, etc. 
we will Find the "k" blocks from a given secret message which we converted upon base value.
THen Dividing into blocks and getting them mixed-up secret message as an array
Bits of the same cloud are grouped together and Creating the Matrix which stores the bits according to the respective clouds 
After that will  Create a matrix containing the corresponding files for each bit from the "List.txt" file - a list of all files
Now we are Writing a file that contains the list of files in each cloud.

Till now the embedding part of the steganography process has been done. 
Now will start the extraction part of the steganography process of the project. Here we take the input from user again about the no of clouds and base value to verify.
We  read from file and converted the file-names with their corresponding values, reading them from the file containing the
"list of all files" and storing into another matrix.
Now Converting alphabets as decimal values  from the Matrix to get our secret message
Converting the decimal to a secret message again.
Now  Deleting the file having the files in the cloud.
Now we are creating the password and generating its hash value then check that an unhashed password matches one that has previously been hashed

Executing Input & Output :

The following code input  is obtained to run the embedding part of the steganography process is run in the project :

Enter the number of clouds:4
Enter secret message:1010101010
Enter base value:16

The following code output is obtained when the embedding part of the steganography process is run in the project with the given input:

Base value =  3C34EB12
['2', '1', 'B', 'E', '4', '3', 'C', '3']
Cloud 0

 article0.docx

 news1.docx

Cloud 1

 bills0.xlsx

 data1.xlsx

Cloud 2

 bill0.xlsx

 articlex1.docx

Cloud 3

 datazz0.xlsx

 data1.xlsx

The following code Input needs to be mentioned  when we run the extraction part of the steganography process is run in the project:

enter the number of clouds:4
Enter base value:16

The following code output is obtained when the extraction part of the steganography process is run in the project:

[['2', '1', 11, 14], ['4', '3', 12, '3']]
decimal = 1010101010
Secret Message = 1010101010
File removed.

The following code output is obtained when the Hash Function is implemented where the
password matches –

Enter password: k
Passowrd:  b'k'         Salt: b'$2b$12$4B4g17Q3IfZYC5RHbvSSbO'
Hashed pwd:  b'$2b$12$4B4g17Q3IfZYC5RHbvSSbOB2gT3zGWAhPrBhpOjsizKePYcD5.mO.'
Enter password again: k
It Matches!