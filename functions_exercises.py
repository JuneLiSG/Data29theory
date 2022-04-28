print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:

def divisors(num: int):
    list_1 = []
    for i in range(1, num+1):
        if num % i == 0:
            list_1.append(i)
    return list_1

print(divisors(12))

print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:
# def divisors_two(num1: int, num2: int):
#     if num1 < num2:
#         if num1 in divisors(num2):
#             return True
#         return False
#     if num2 < num1:
#         if num2 in divisors(num1):
#             return True
#         return False

def is_factor(num1: int, num2: int):
    if num1 in divisors(num2) or num2 in divisors(num1):
        return True
    else:
        return False

print(is_factor(12, 7))


# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# A2a:

def position(letter: str = "a"):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z", " "]
    return alphabet.index(letter.lower())

print(position())


print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:
# def id(name: str = "bob"):
#     id_number = ""
#     for i in range (0, len(name)):
#         id_number.append(alphabet.index(name[i]))
#     return join(id_number)

def id(name: str = "bob"):
    id_number = ""
    for i in range(0, len(name)):
        id_number = id_number + str(position(name[i]))
    return id_number

print(id())

def id_two(name: str = "bob"):
    id_number = ""
    for i in name:
        id_number = id_number + str(position(i))
    return id_number

print(id_two())

print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:

def password_create(name: str = "bob"):
    sum_of_id = 0
    password = 0
    for i in list(id(name)):
        sum_of_id = (sum_of_id) + int(i)
    password = int(id(name)) - int(sum_of_id)
    # print(list(id(name)))
    # print(sum_of_id)
    # print(id(name))
    return password

print(password_create())


def password_create_two(name: str):
    id_code = id(name)
    id_code_str = str(id(name))
    id_sum = 0
    for i in id_code_str:
        id_sum += int(i)
    return id_code - id_sum

# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:
# user_num = input("Please put in a number: ")

def is_prime(num: int):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
    return prime

print(is_prime(12))

# def is_prime_two(num: int):
#     count = int(2)
#     while count < num-1:
#         if num % count > 0:
#             count += 1
#         if num % count == 0:
#             return False
#             break
#     if count == num-1:
#         return True

# these don't take into account the full range of numbers for ie don't take into account
# 0, 1, or 2 which are based on the technicalities of what a prime number is

print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:

def is_prime_with_check(num):
    if num.isdigit():
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
        return prime
    else:
        print("invalid input")

is_prime_with_check(41)

print(is_prime_with_check(32))
# -------------------------------------------------------------------------------------- #