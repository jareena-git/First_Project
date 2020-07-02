# https://realpython.com/how-to-use-numpy-arange/
# def sum_of_two_nums(num1,num2):
#     try:
#         num1=int(num1)
#         num2=int(num2)
#         total = num1 + num2
#         if (total == 20 or
#                 num1 == 20 or
#                 num2 == 20):
#             print("True")
#         else:
#             print("False")
#     except ValueError:
#         print("Please enter valid integer value")
#
# num1=input("Enter First Number")
# num2=input("Enter Second Number")
# obj=sum_of_two_nums(num1,num2)
# #
# #
# def capitaliz_1_and_4(name):
#     if len(name) >= 1:
#         update_str=""
#         for n in range(len(name)-1):
#             if (n == 0 or
#                     n == 3):
#                 update_str=update_str + name[n].capitalize()
#             else:
#                 update_str=update_str + name[n]
#
#         print(update_str)
#     else:
#         print("Empty string")
#
# name=input("Please enter name")
# obj=capitaliz_1_and_4(name)
#
# #
# #
# def three_of_next_three(lst):
#
#     for l in range(len(lst)-1):
#         if lst[l] == 3:
#             if lst[l] == lst[l+1]:
#                 print("True")
#             else:
#                 print("False")
#         else:
#             print("False")
#
# lst = [
#     2, 22, 3,
#     3, 32, 3,
#     3]
# obj=three_of_next_three(lst)
# #
#
# def repeat_every_char_3(name):
#     repeat_name = ""
#     for char in range(len(name)):
#         repeat_name=repeat_name + (name[char] * 3)
#     print(repeat_name)
#
#
# name=input("Enter name")
# obj=repeat_every_char_3(name)
#
#
#
#
#


# # Calculate Prime number
# def calculate_prime():
#     num = 2
#     count = 0
#     i = 0
#     if num > 1:
#         while num <= 100:
#             for dev in range(2,10):
#                 if ((num % dev) == 0) and (dev != num):
#                     count = count + 1
#                     break
#             if count >= 1:
#                 count=0
#             else:
#                 print("Prime number{0}".format(num))
#             num = num + 1
# obj = calculate_prime()
#


#


#
# Python 3 Programming - 55193
# Python 3 Functions and OOPS - 55194
# Numpy - 55936
# Pandas - 55937
# Matplotlib - 56869
# Qualis - 57661

# and not ((num % 1) == 0)

# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, and 97.




# def times_table(number):
#     if number.isdigit():
#         number = int(number)
#         [print("{0} * {1} = {2}".format(num,number,num * number)) for num in range(1,11)]
#     else:
#         print("Please enter valid number")
# number = input("Please enter number between 1 to 12")
# times_table(number)


#Generate Pattern using @
# def generate_pattern():
#     for i in range(1,5):
#         for j in range(i):
#             print("@",end=" ")
#         print(" ")
#     for i in range(3,0,-1):
#         for j in range(i):
#             print("@",end=" ")
#         print(" ")
#
# obj=generate_pattern()


# def armstrong():
#     num = int(input("Enter a number"))
#     sum = 0
#     temp = num
#     while temp > 0:
#        digit = temp % 10
#        sum += digit ** 3
#        temp //= 10
#     # display the result
#     if num == sum:
#        print(num,"is an Armstrong number")
#     else:
#        print(num,"is not an Armstrong number")
#
# obj = armstrong()
#https://www.youtube.com/watch?v=mmiIjmo-GwQ&feature=emb_rel_end


# def my(a,b):
#     if(a%2==0 & b%2==0):
#         print(min(a,b))
#     else:
#         print(max(a,b))
# my(1,3)
# 6591
# def fun():
#     a, b, *c, d = [10, 20, "jareena", 12, 13]
#     print(a, b, c, d)
# fun()

# def fun():
#     a, *b, (c, *d) = [10, 20, 30, "Python Programmig"]
#     print(a, b, c, d)
# fun()

# def fun():
#     a, b, *d = (10, 20, "jareena", 12, 13)
#     print(a, b, d)
# fun()


# def fun():
#     d1={'a':1,'b':3}
#     d2 = {'c': 1, 'd': 3}
#     a, b, *c = {'x':10, 'y':20,'z':d1,'i':d2}
#     print(a, b,c)
# fun()

# d1={'a':1,'b':3}
# d2 = {'c': 1, 'd': 3}
#
# def fun(a, b, *c, d):
#     print(a, b, c, d)
#
# fun(d1,20,d2,40,80,d=70)


# d1={'a':1,'b':3}
# d2 = {'c': 1, 'd': 3}
#
# def fun(a, *c, d):
#     print(a, c, d)
#
# fun(d1,d=100)

# def fun(a, b, c):
#     print(a, b, c)
#
# l = [10,39,40]
# fun(*l)

# def fun():
#     st = "Python Programming Language"
#     a = st[0]
#     b = st[1]
#     *c, (*d, e) = st[2:]
#     print(a, b, c, d, e)
#     *c, (*d, e) = st[:]
#     print(a, b, c, d, e)
#
# fun()
#
#
# list = [1,2,3,4,5,9,9,0,8]
# print(list[:3])
# print(list[3:])
# print(list[::2])
# print(list[::3])
# print(list[::3])
# print(list[::4])
# print(list[::-1])
# print(list[:4:2])
# #odd alternatives
# print(list[1::2])
#
# def fun():
#     k = [3,4,5,6,7,8,9]
#     print(k[::2])
#     print(k[:5:2])
#     print(k[1::2])
# fun()

#range operation to revers the list in decending order
# print(list(range(1,100))[::-1])
#     # print(i)

#
# s='jareena'
# for i in s:
#     print(i)

# def fun():
#     s = "Python Programming Language"
#     a = s[0]
#     b = s[2]
#
#     print(list(s[:]))
    #

    # a, b, *c = s[0], s[1], s[2:]
    # print(a)
    # print(b)
    # print(c)

    # why c returning empty list
    # a, b, *c, d   = s[0], s[1], list(s[2:])
    # print(a)
    # print(b)
    # print(c)
    # print(d)

    # why i am getting error here for c even i am passing list
     # *c = list(s[3:]) ask


    # its working when we place d
    # *c, d = list(s[3:])
    # print(c)
    # print(d)


    # print(list(s[2:]))
    # print(a)
    # print(b)
    # print(c)
    # print(d)

    # print(list(s[3:]))
    # l = list(s[3:len(s)])

    # *c , d = list(s[3:])[::-1]
    # print(c)
    # print(d)

    # *c, d, (*e, f) = list(s[3::-1])
    # print(c)
    # print(d)
    # print(e)
    # print(f)
    #

    # *c,(d, *e) = list(s[::2])
    # print(c)
    # print(d)
    # print(e)

    #returning entaire slice as single element in list
    # print(s[2:])
    # print(list(s[2:]))
    # why c getting list inside list
    # *c, (d, *e) = list(s[::2]), list(s[1::2])
    # print(c)
    # print(d)
    # print(e)
    # *c, d = list(s[3::-1])
    # print(c)
    # print(d)

    # # false
    # print(bool(None))
    # # false
    # print(bool(""))
    # # false
    # print(bool(0))
    # # true
    # print(bool(1))
# fun()


#
# def fun(average):
#     if average >= 90:
#         print("Distinct")
#     elif 60 <= average <= 90:
#         print("Above average")
#     elif average <= 40 and average >=60:
#         print("Average")
#     else:
#         print("Fail")
#
# fun(68.0)


# def fun():
    # s = "Hello Python"
    # st = ""
    # for i in range(len(s)-1, 0-1,-1):
    #     st = st + s[i]
    # print(f"updated string {st}")
    # print(s[::-1])
    # print(s[-1::-1])

    # k = [3, 4, 5, 6, 7, 8, 9]
    # print(k[0::2])
    # print(k[0:5:2])
    # print(k[1::2])
    # print(bool(5))
    # tup2 = tuple("Welcome")
    # for word in tup2:
    #     for w in word:
    #         if "e" in w:
# fun()


# def fun():
#     a = 0
#     if a:
#         print(a)
#     else:
#         print (False)
# fun()  Remove these words ‘is’, ‘in’, ‘to’, ‘no’ from the text list.
# def removable(t):
#     if "is" in t:
#         t.replace("is","")
#         print(t)
#     elif "in" in t:
#         t.replace("in","")
#     elif "to" in t:
#         t.replace("to","")
#     elif "no" in t:
#         t.replace("no","")
#     return t
#
#
# def sliptable(t):
#     word = t.split()
#     return word
#
#
# # 164273012
#
# def remove_word():
#     remove_list = ["is", "in", "to", "no"]
#     text = ["Life is beautiful", "No need to overthink", "Meditation help in overcoming depression"]
#     lst=[ word.replace(word,"") if word in remove_list else word for t in text for word in sliptable(t)]
#     print(lst)
# remove_word()


#
#
# def sliptable(t, remove_list):
#     word = t.split()
#     update_str = []
#     for w in word:
#         if w in remove_list:
#             continue
#         else:
#             update_str.append(w)
#     return " ".join(update_str)
#
#
#
# def remove_word():
#     remove_list = ["is", "in", "to", "no"]
#     text = ["Life is beautiful","No need to overthink","Meditation help in overcoming depression"]
#     lst=[sliptable(t, remove_list) for t in text]
#     print(lst)
#
# remove_word()


# # def sliptable(t, remove_list):
# #     word = t.split()
# #     update_str = ""
# #     for w in word:
# #         if w in remove_list:
# #             w.replace(word,"")
# #             " ".join()
# #     return word
#
#
#
#
# # 164273012
#
# def remove_word():
#     remove_list = ["is", "in", "to", "no"]
#     text = ["Life is beautiful", "No need to overthink", "Meditation help in overcoming depression"]
#     lst=[word if word in remove_list else word for t in text for word in sliptable(t, remove_list)]
#     print(lst)
# remove_word()



# list of even number
# def even_numbers():
#     lst =[num for num in range(2, 200) if num % 2 == 0]
#     print(lst)
# even_numbers()





# def cuboid():
#     x = input("Enter x value")
#     y = input("Enter y value")
#     z = input("Enter z value")
#     n = input("Enter n value")
#     if x.isdigit() and y.isdigit() and z.isdigit():
#         x = int(x)
#         y = int(y)
#         z = int(z)
#         n = int(n)
#         lst = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if ((i + j + k) != n)]
#         print(lst)
#     else:
#         print("Please enter valid integer value")
# cuboid()



#
#
# import numpy as np
#
# import numpy as np
# n = [[-1, -2, -3, -4], [-2,-4, -6, -8]]
# y = np.array(n)
# print(y.ndim)
# print(y.shape)
# print(y.size)
# print(y.dtype)
# print(y.nbytes)
#
# import numpy as np
# x1 =np.array([[[-1, 1],[-2, 2],[-3, 3],[-4, 4]]])
#
# print(x1.ndim)
# print(x1.shape)
# print(x1.size)
#
#
#
# import numpy as np
# x2 =np.ones(shape=(3, 2, 2))
# print(x2)
# x3 =np.eye(4, 4, k = -1)
# print(x3)
#
# import numpy as np
# x = np.random.rand(3, 4, 2)
# print(x)



# Remove word program
# def sliptable(t, remove_list):
#     word = t.split()
#     update_str = []
#     for w in word:
#         if w.lower() in remove_list:
#             continue
#         else:
#             update_str.append(w)
#     return " ".join(update_str)
#
#
#
# def remove_word():
#     remove_list = ["is", "in", "to", "no"]
#     text = ["Life is beautiful","No need to overthink","Meditation help in overcoming depression"]
#     lst=[sliptable(t, remove_list) for t in text]
#     print(lst)
#
# remove_word()


# Expected Ouput: ['Life beautiful', 'need overthink', 'Meditation help overcoming depression']

# https://www.w3resource.com/python-exercises/numpy/index-array.php

# import numpy as np
# x = np.arange(20)
# y = x.reshape(2, 10)
# print(np.hsplit(y))



# import numpy as np
# x = np.arange(20)
# print(x)
# y = x.reshape(2, 10)
# np.hsplit(y, 2)


import numpy as np
p = np.arange(3, 15, 3)
p.reshape(2, 2)
q = np.arange(15, 33, 3)
q.reshape(2, 3)
np.hstack((p, q))


import numpy as np
y = np.arange(1, 7).reshape(2, 3)
z = np.sqrt(y)
print(z)
print(np.add(z,5))



