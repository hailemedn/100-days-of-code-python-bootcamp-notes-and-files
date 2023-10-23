# def prime_checker(number):
#     counter = 0
#     for num in range(2, number):
#         if (number % num == 0):
#             counter += 1
    
#     if (number == 1 or counter == 2):
#         print("It's a prime number")
#     else:
#         print("It's not a prime number")

# n = int(input("Check this number: "))
# prime_checker(number=n)



# Angela's code
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if(number % i == 0):
            is_prime = False
    if is_prime and number != 0:
        print("It is a prime number")
    else: 
        print("It's not a prime number")

n = int(input("Check this number: "))
prime_checker(number=n)