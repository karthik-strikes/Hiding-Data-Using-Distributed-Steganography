######## DATA EMBEDDING CODE #########
# Secret Message = 1010101010
 # n = 4, B = ?
## Base conversion from a DEC
def basefromDec(num,bs): #Maximum base - 16 (for our project)
    varBas = ""
    while num>0:
        digit = int(num%bs)
        if digit<10:
            varBas += str(digit)
        else:
            varBas += chr(ord('A')+digit-10) #Using uppercase letters
        num //= bs
    varBas = varBas[::-1] #To reverse the string
    return varBas
##Enter details
n = int(input("enter number of clouds :"))
Secret = int(input("Enter secret message :"))
B = int(input("Enter base value :")) # base value max - 16
bs = basefromDec(Secret,B)
print("base value = ", bs)
Secret = bs
## Finding the "k" blocks from given secret message
count = 0
for i in Secret:
    count = count + 1
k = count//n
count_s = count #count_of_secret_in_bits

 
### Dividing into blocks and getting the mixed up secret message as an array(/list)
S_new = []
for i in range(0,count):
    S_new.append(-1) #default value
num = []
s_mat = []
count = 0
#s = Secret
s = []
s.append(Secret)
i = 0
c = 0
while(s!=False):
    if(s):
        c = c + 1
    else:
        break
    rem = s.pop() #rem = s % 10
    num.append(rem)
    s_mat.append(rem)
    count = count + 1
    if(count == n):
        for x in range(4):
            S_new[i] = num.pop()
            i = i+1
        num.clear()
        count = 0
## Bits of the same cloud are grouped together
 ## Creating the Matrix which stores the bits according to the respective clouds (clouds incolumn(j))
s = []
for c in Secret:
 s.append(c)
s.reverse() # reverse of secret message in list form
print(s)
mat_arr = []
for i in range(0,k):
    mat_col = []
    for j in range(0,n):
        mat_col.append(s[i*n+j])
    mat_arr.append(mat_col)
#print("mat_arr = ",mat_arr)
## Creating matrix containing the corresponding files for each bit from "List.txt" file - list of all files
files_mat = []
for i in range(0,k):
    mat_col = []
    for j in range(0,n):
        mat_col.append("")
    files_mat.append(mat_col)
#print("files_mat=",files_mat)

file = open("C:\\Users\\KARTHIK\\Videos\\Crypto\\List.txt","r")
for i in range(0,k):
    for j in range(0,n):
        temp = mat_arr[i][j]
        value = str(i) + " " + str(temp) + " "
        #value = str(temp)
        file.seek(0)
        while True:
            line = file.readline()
            if not line:
                break;
            if value in line:
               # line = file.readline()
               files_mat[i][j] = line;
               #print(i , j ,files_mat[i][j])

file.close()

## Writing a file that contains the list of files in each cloud
 ## OUTPUT
clouds_file = open("C:\\Users\\KARTHIK\\Videos\\Crypto\\Files_in_Clouds.txt","w+")

for j in range(0,n):
    clouds_file.write("Cloud " + str(j) + "\n")
    for i in range(0,k):
        temp = files_mat[i][j]
        clouds_file.write(temp)
clouds_file.close()
## Reading from written file
clouds_file = open("C:\\Users\\KARTHIK\\Videos\\Crypto\\Files_in_Clouds.txt","r")
while True:
    line = clouds_file.readline()
    if not line:
        break;
    elif 'Cloud' in line:
        print(line)
    else:
        print(line[3:])

clouds_file.close()
################ DATA EMBEDDING CODE ##################The following code fragment contains the extraction part of the steganography process of the project –
########## Extraction CODE ########## 
# n = 4
#k = 2 #in this example with Secret = 1010101010
#B = ?
n = int(input("enter number of clouds :"))
B = int(input("Enter base value :"))
#k_files = input("Enter name of file :")
#clouds_file = input("Enter file name containing the files in clouds")
## Reading from file containing the "list of files in each cloud" and storing into a matrix - cloud_list[]
# creating and initializing the matrix
cloud_list = []
for i in range(0,k):
    mat_col = []
    for j in range(0,n):
        mat_col.append("")
    cloud_list.append(mat_col)

# reading from file and storing into matrix
file = open("C:\\Users\\KARTHIK\\Videos\\Crypto\\Files_in_Clouds.txt","r") 
# rb - reading in binary format
for j in range(0,n):
    file.seek(0)
    while True:
        line = file.readline()
        if not line:
            break;
        value = "Cloud " + str(j)
        if value in line:
            for i in range(0,k):
                line = file.readline()
                cloud_list[i][j] = line.strip();
file.close()

#print("cloud_list=",cloud_list)
## converting the file-names with their corresponding values, reading them from the file containing the
 ## "list of all files" and storing into another matrix - mat[]
# creating and initializing matrix - mat[]
mat = []
for i in range(0,k):
    mat_col = []
    for j in range(0,n):
        mat_col.append(-1)
    mat.append(mat_col)

#print ("mat=",mat)
# storing corresponding values into matrix by reading from file - List
f = open("C:\\Users\\KARTHIK\\Videos\\Crypto\\List.txt", "r")
li = []
for i in range(0,k):
    for j in range(0,n):
        file_name = cloud_list[i][j]
        f.seek(0)
        while True:
            line = f.readline()
            if not line:
                break;
            if file_name in line:
                #line_str = line.decode('utf-8')
                #pos = len(line_str) + 4
                #f.seek(-pos, 1)
                x = line[2:3]
                mat[i][j] = x
                break;
f.close()

## Converting alphabets as decimal values
li = ['A', 'B', 'C', 'D', 'E', 'F']
i=0
while (i < k):
    for j in range(0,n):
        for ele in li:
            if(mat[i][j] == ele):
                mat[i][j] = 9 + li.index(ele) + 1
    i=i+1
print(str(mat))
## Getting a decimal value from the Matrix to get our secret message -- using formula
decimal = 0
t = 0
x = 0
for i in range(0,k):
    for j in range(0,n):
        x = int(mat[i][j])
        temp = x * pow(B,(i*n+j))
        decimal = decimal + temp
print("decimal = " + str(decimal))
## Converting decimal to base
secret_message = str(decimal)

print("Secret Message = " + secret_message)
if(secret_message == Secret):
    print("Secret found!")


 
## Delete the file having the files in cloud - Files_in_Clouds
import os
os.remove("C:\\Users\\KARTHIK\\Videos\\Crypto\\Files_in_Clouds.txt")
print("File removed.")
######## EXTRACTION CODE #######
# #The following code fragment implements the ‘Bcrypt’ hash function for our project –
## BCRYPT HASH FUNCTION
import bcrypt
# REGISTERING time #
password = input("Enter password: ").encode("utf-8")
# Hash a password for the first time, with a randomly-generated salt
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(password, salt)
print(" Passowrd: ",password, "\t Salt:", salt, "\n Hashed pwd: ", hashed)
# LOGIN time #
# Check that an unhashed password matches one that has previously been hashed
pwd = input("Enter password again: ").encode("utf-8")
if bcrypt.checkpw(pwd, hashed):
    print("It Matches!")
else:
    print("It Does not Match. ")
######