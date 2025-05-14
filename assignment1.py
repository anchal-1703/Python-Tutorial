""" program to if conditions"""
import math
import statistics
"""1 area of 2D shapes"""
import math
# Circle
# radius = float(input("Enter the radius of the circle: "))
# area_circle = math.pi * radius ** 2
# print("Area of Circle:", area_circle)
# #
# # # Triangle
# base = float(input("Enter the base of the triangle: "))
# height = float(input("Enter the height of the triangle: "))
# area_triangle = 0.5 * base * height
# print("Area of Triangle:", area_triangle)
# #
# # # Rectangle
# length = float(input("Enter the length of the rectangle: "))
# width = float(input("Enter the width of the rectangle: "))
# area_rectangle = length * width
# print("Area of Rectangle:", area_rectangle)
# #
# # # Square
# side = float(input("Enter the side of the square: "))
# area_square = side ** 2
# print("Area of Square:", area_square)
# # 
# # # Trapezoid
# a = float(input("Enter the first base of the trapezoid: "))
# b = float(input("Enter the second base of the trapezoid: "))
# height = float(input("Enter the height of the trapezoid: "))
# area_trapezoid = 0.5 * (a + b) * height
# print("Area of Trapezoid:", area_trapezoid)
# #
# # # Parallelogram
# base = float(input("Enter the base of the parallelogram: "))
# height = float(input("Enter the height of the parallelogram: "))
# area_parallelogram = base * height
# print("Area of Parallelogram:", area_parallelogram)

"""volume of 3D shapes"""
# # Cube
# side = float(input("Enter the side of the cube: "))
# volume_cube = side ** 3
# print("Volume of Cube:", volume_cube)

# # Cylinder
# radius = float(input("Enter the radius of the cylinder: "))
# height = float(input("Enter the height of the cylinder: "))
# volume_cylinder = math.pi * radius ** 2 * height
# print("Volume of Cylinder:", volume_cylinder)

# # Cone
# radius = float(input("Enter the radius of the cone: "))
# height = float(input("Enter the height of the cone: "))
# volume_cone = (1/3) * math.pi * radius ** 2 * height
# print("Volume of Cone:", volume_cone)

# # Sphere
# radius = float(input("Enter the radius of the sphere: "))
# volume_sphere = (4/3) * math.pi * radius ** 3
# print("Volume of Sphere:", volume_sphere)

"""3 largest of 3"""

# a = float(input("Enter the first number: "))
# b = float(input("Enter the second number: "))
# c = float(input("Enter the third number: "))

# if a >= b and a >= c:
#     largest = a
# elif b >= a and b >= c:
#     largest = b
# else:
#     largest = c

# print("The largest number is:", largest)

"""4 year is leap or not"""

# year = int(input("Enter a year: "))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")

"""5 num is odd or even"""

# number = int(input("Enter a number: "))

# if number % 2 == 0:
#     print(f"{number} is an even number.")
# else:
#     print(f"{number} is an odd number.")

"""6 triangle is isoceles or not"""

# side1 = float(input("Enter the first side of the triangle: "))
# side2 = float(input("Enter the second side of the triangle: "))
# side3 = float(input("Enter the third side of the triangle: "))

# if side1 == side2 or side2 == side3 or side1 == side3:
#     print("The triangle is isosceles.")
# else:
#     print("The triangle is not isosceles.")


""" 7 print the quadratic root"""

# a = float(input("Enter the coefficient a: "))
# b = float(input("Enter the coefficient b: "))
# c = float(input("Enter the coefficient c: "))
# discriminant =( b ** 2) - (4 * a * c)


# if discriminant > 0:
#     root1 = (-b + math.sqrt(discriminant)) / (2 * a)
#     root2 = (-b - math.sqrt(discriminant)) / (2 * a)
#     print(f"Two distinct real roots: {root1} and {root2}")
# elif discriminant == 0:
#     root = -b / (2 * a)
#     print( f"One real root: {root}")
# else:
#     real_part = -b / (2 * a)
#     imaginary_part = math.sqrt(-discriminant) / (2 * a)
#     print( f"Two complex roots: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i")


"""8 program to print number which are not divisible by 3, 6 and 9"""

# n=int(input("enter number upto "))
# a=0
# while a<n:
#     a += 1
#     if(a%3!=0 and a%6!=0 and  a%9!=0 ):
#         print(a,end=" ")
#     else:
#         continue
"""9 multiplication table"""

# n=int(input("enter the number"))
# for i in range(1,11):
#     print(n ,"*" ,i,"=",n*i)


"""10 sum of n num"""
# n=int(input("enter number upto add"))
# sum,num=0,1
# while num<n:
#     sum+=num
#     num+=1
# print(sum)
"""11 program for fibonnaci series"""

# n=int(input("enter number"))
# a=0
# b=1
# c=0
# fib=[]
# while len(fib)<n:
#     fib.append(c)
#     a=b
#     b=c
#     c=a+b
# print(fib)

# list = [0, 1]
# if (n == 0 or n == 1):
#     print(0)
# else:
#     for i in range(2,n):
#         fib = list[i-1] + list[i-2]
#         list.append(fib)
#     print(list)
"""12 program to print factors """
# n=int(input("enter number to find factors of"))
# list =[]
# multi=1
# div =1

# for i in range(1,n+1):
#     if(n%i==0):
#         list.append(i)
# print(list)


# for sh in list:
#     multi=multi*sh
# if multi==n:
#     print(list)
# else:
#     print("error")


""" 13 to check wheater a num is palindrome or not """
# my program
# n = int(input("enter your number"))
# rev=0
# temp = n #bcoz it is global
# rem=1
# list=[]
# while rem>0:
#     rem = n%10
#     if(rem!=0):
#         list.append(rem)
#         n=n//10
# len = len(list)
# list1=[]
# for i in range(len-1,-1,-1):
#     list1.append(list[i])
# if(list == list1):
#     print(temp,"is palindrome")
# else:
#     print(temp,"is not palindrome")

"""optimized program"""
# n = int(input("Enter your number: "))
# temp = n
# reversed_num = 0
""" or """
# n=[int(n) for n in input("enter a number separated by ").split(" ")]
# n.reverse()
# print(n)

# if temp == reversed_num:
#     print(temp, "is a palindrome")
# else:
#     print(temp, "is not a palindrome")
# def is_palindrome(number):
#     original_str = str(number)
#     reversed_str = original_str[::-1]
#     return original_str == reversed_str
# number = int(input("Enter a number: "))
# if is_palindrome(number):
#     print(f"{number} is a palindrome.")
# else:
#     print(f"{number} is not a palindrome.")



""" 14 to check wheather a number is not a prime"""
# n = int(input("enter a number"))
# if n<=1:
#     print(n, " is not prime")
# else:
#     a=1
#     is_true = True
#     while a<(n//2):
#         a +=1
#         if n%a==0:
#             is_true = False
#             break
#         else:
#             is_true = True
#     if is_true:7

#         print(n, "is prime")
#     else:
#         print(n, "is not prime")




"""15 print armstrong"""
# num = int(input("enter a num"))
# lis = []
# reverse_num = 0
# while num > 0:
#     rem=num%10
#     lis.append(rem)
#     num=num//10
# n = len(lis)
# arm = 0
# for a in lis:
#     arm += a**n
# print(arm)
""" 16 program to find reverse """
# n = int(input("enter a number"))
# reversed_num = 0
# while n > 0:
#     rem = n % 10
#     reversed_num = reversed_num * 10 + rem
#     n = n // 10
# print(reversed_num)


"""HCF of a num input by user"""
# def compute_hcf(x, y):
#     while y:
#         x, y = y, x % y
#     return x

# # Input from the user
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# # Calculate HCF
# hcf = compute_hcf(num1, num2)

# print(f"The HCF of {num1} and {num2} is {hcf}.")


"""18 program to print n number of inputs and find biggest and lowest among them"""
# n = [n for n in input("no. of elements you want to input separated by space").split(" ")]
# n= int(input("no. of element you want to enter"))
# l=[]
# i=0
# while i<n:
#     num = int(input("enter the number"))
#     l.append(num)
#     i+=1
# print(max(l))
# print(min(l))
""" or """
# i=0
# lis = []
# while i <10:
#     n = int(input("enter a number"))
#     lis.append(n)
#     i+=1
# print(lis)
# print(max(lis))
# print(min(lis))

"""19 program to print avg and sum"""
# n = [int(n) for n in input("no. of elements you want to input separated by comma").split(" ")]
# sum = 0
# for sh in n:
#     sum+=sh
# print("Sum of input list is: ",sum)
# avg = statistics.mean(n)
# print("average of input list is: ",avg)

""" 20 program to input 10 numbers and then compute sum of even and product of odd numbers"""

# n = [int(n) for n in input("no. of elements you want to input separated by comma").split(",")]
# if len(n)==2 or len(n)<10:
#     print("enter 10 numbers only")
# else:
#     even=0
#     odd=1
#     for seq in n:
#         if(seq%2==0):
#             even+=seq
#         else:
#             odd*=seq
#     print("sum of even numbers in a list of numbers are: ",even)
#     print("sum of odd numbers in a list of numbers are: ",odd)

""" 21 program to count the digit 5 in a number"""
# n=[input("enter a number ")]
# str1=list(map(int,n[0]))
# print(str1.count(5))
# def count_five(number):
#     number_str = str(number)
#     count = number_str.count('5')
#     return count

# number = int(input("Enter a number: "))

# result = count_five(number)

# print(f"The digit 5 appears {result} time(s) in the number {number}.")


"""22 factorial of a number """
# n=int(input("enter a number "))
# fact=1
# a=n
# while a >= 1 :
#     fact = fact *a
#     a=a-1
# print(fact)
# sen="Leetcode eisc cool"
# n=sen.split()
# print(n)
# ui=0
# if(len(n)==1):
    
#     if(sen[0] is sen[-1]):
#         print("true")
#     else:
#         print("false")
# else:
#     for i in range(1,len(n)):
#        if(n[ui][-1] == n[i][0]):
#             ui+=1
#             print("True") 
#             if(i==len(n)):
#                 if(n[i][-1]==n[0][0]):
#                     print("True") 
#                 else:
#                     print("False")
            
#             else:
#                 print("False")
# def circular():
#     sen="MuFoevIXCZzrpXeRmTssj lYSW U jM"
#     n=sen.split()
#     print(n)
#     l=True
#     ui=0
#     while l is True:
#         if(len(n)==1):
#             return sen[0] == sen[-1]
#         else:
#             for i in range


# if(len(n)==1):   
#     if(sen[0] is sen[-1]):
#         l="y"
#     else:
#         l="n"
# else:
#     for i in range(1,len(n)):
#         if(n[ui][-1] == n[i][0]):
#             ui+=1
#             l="y" 
#             if(i==len(n)):
#                 if(n[i][-1]==n[0][0]):
#                     l="y" 
#                 else:
#                     l="n"
            
            
#         else:
#             l="n"
#     print(l)




# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def generate_primes(start, end):
#     primes = []
#     for num in range(start, end + 1):
#         if is_prime(num):
#             primes.append(num)
#     return primes

# # Input from the user
# start = int(input("Enter the start of the range: "))
# end = int(input("Enter the end of the range: "))

# # Generate prime numbers in the given range
# prime_numbers = generate_primes(start, end)

# print(f"Prime numbers between {start} and {end} are: {prime_numbers}")
# import math

# def geometric_mean(numbers):
#     product = 1
#     for num in numbers:
#         product *= num
#     return product ** (1 / len(numbers))

# def harmonic_mean(numbers):
#     denominator_sum = sum(1 / num for num in numbers if num != 0)
#     return len(numbers) / denominator_sum if denominator_sum != 0 else 0

# # Input numbers from the user
# numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))

# # Calculate means
# geo_mean = geometric_mean(numbers)
# harm_mean = harmonic_mean(numbers)

# print(f"Geometric Mean: {geo_mean}")
# print(f"Harmonic Mean: {harm_mean}")
# def decimal_to_binary(decimal):
#     return bin(decimal)[2:]

# def binary_to_decimal(binary):
#     return int(binary, 2)

# # Input from the user
# choice = input("Type '1' for Decimal to Binary or '2' for Binary to Decimal: ")

# if choice == '1':
#     decimal = int(input("Enter a decimal number: "))
#     binary = decimal_to_binary(decimal)
#     print(f"Binary equivalent of {decimal} is {binary}.")
# elif choice == '2':
#     binary = input("Enter a binary number: ")
#     decimal = binary_to_decimal(binary)
#     print(f"Decimal equivalent of {binary} is {decimal}.")
# else:
#     print("Invalid choice!")
import itertools

numbers = [4, 5, 6]
combinations = list(itertools.permutations(numbers, 3))

print("All possible combinations of 4, 5, and 6 are:")
for combo in combinations:
    print(combo)


