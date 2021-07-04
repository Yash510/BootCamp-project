
import hashlib
# Q1) Program to genrate md5 of string data
print("1) Program to genrate md5 of string data")
# Input from user initializing string
str_hash = input(" Enter your Data :- ".__str__())

# encoding input  using encode()
# then sending to md5()

result = hashlib.md5(str_hash.encode())

# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of MD5 is : = " + result.hexdigest()+'\n ')



#Q2) Hashse of string data using 3 algorithms
print("2) Hashes of string data using 3 algorithms from ")
# encoding input  using encode()
# then sending to sha384()

result1 = hashlib.sha384(str_hash.encode())

# encoding input  using encode()
# then sending to blacke2b()

result2 = hashlib.blake2b(str_hash.encode())

# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of MD5 is : = " + result.hexdigest())
print("The hexadecimal equivalent of Sha384 is : = " + result1.hexdigest())
print("The hexadecimal equivalent of Blacke2b is : = " + result2.hexdigest()+'\n')


# Q3) Add salting and iteration to your hashes
print("3) Adding salting and 2 time iteration to your hashes \n")
salt = ('a'+str_hash+'b')

# encoding input  using encode()
# then sending to md5 ()
salt_result = hashlib.md5(salt.encode())
Iter_1=salt_result.hexdigest()
# 2 itera
Iter_result=hashlib.md5(Iter_1.encode())
Iter_2=Iter_result.hexdigest()
print("Adding salting and iteration to your hashes: = "+Iter_2)