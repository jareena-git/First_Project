#https://docs.sqlalchemy.org/en/14/orm/extensions/associationproxy.html


# import random
#
#
# def incorrect_attempts():
#     attempts_remaining = input("how many incorrect attempts do you want?[1-25]")
#     if attempts_remaining.isdigit():
#         attempts_remaining = int(attempts_remaining)
#         if attempts_remaining >= 25 or attempts_remaining <= 0:
#             print("Please Enter number between [1-25]")
#         else:
#             minimum_word_len(attempts_remaining)
#     elif attempts_remaining.lower() == "NaN".lower():
#         print("NaN is not an integer between 1 and 25")
#     else:
#         print("{0}: is not an integer between 1 and 25:".
#               format(attempts_remaining))
#
#
# def minimum_word_len(attempts_remaining):
#     min_word_len = int(input("what minimum word length do you want? [4-16]"))
#     print("selecting a word...")
#     print()
#     read_word_frm_txt(min_word_len, attempts_remaining)
#
#
# def read_word_frm_txt(min_word_len, attempts_remaining):
#     with open("words.txt", mode='r') as fd:
#         words_lines = fd.readlines()
#         for words_line in words_lines:
#             words_list = words_line.split(" ")
#             select_word(words_list, min_word_len, attempts_remaining)
#
#
# def select_word(words_list, min_word_len, attempts_remaining):
#     selected_words_list = []
#     for words in range(0, len(words_list)-1):
#         if len(words_list[words]) >= min_word_len:
#             selected_words_list.append(words_list[words])
#     word = random.choice(selected_words_list)
#     replace_star(min_word_len, word, attempts_remaining)
#
#
# def replace_star(min_word_len, word, attempts_remaining):
#     print("word:", end=" ")
#     for w in range(0, len(word)-1):
#         print("*", end=" ")
#     print()
#     reduce_attempts(attempts_remaining, word)
#
#
# def reduce_attempts(attempts_remaining, word):
#     flag = 0
#     previous_guesses = ""
#     try:
#         while (attempts_remaining != 0) and flag == 0:
#             # attempts_remaining -= 1
#             previous = " "
#             print("Attempts Remaining:{0}".format(attempts_remaining))
#             print("Previous Guesses:", previous)
#             next_letter = input("Choose the next letter:")
#             attempts_remaining -= 1
#             if next_letter.isalpha():
#                 if len(next_letter) > 1:
#                     print("Enter only Single charecter")
#                     continue
#                 else:
#                     if next_letter in previous_guesses:
#                         attempts_remaining += 1
#                         print("You have already guessed that letter")
#                         print()
#                         continue
#                     else:
#                         if next_letter in word:
#                             next_letter_replicate = word.count(next_letter)
#                             for letter in range(next_letter_replicate):
#                                 previous_guesses += next_letter
#                             previous = next_letter
#                             print("{0} is in the word!".format(next_letter))
#                             print()
#                             print("word:", end=" ")
#                             for w in word:
#                                 if w in previous_guesses:
#                                     print(w, end=" ")
#                                     if len(word) == len(previous_guesses):
#                                         print('Congratulations, You won the game!')
#                                         flag = 1
#                                         break
#                                         break
#                                         break
#
#                                 else:
#                                     print("*", end=" ")
#                             print()
#
#                         else:
#                             print("{0} is not in word:".format(next_letter))
#             else:
#                 print("Enter only letter")
#                 continue
#         if attempts_remaining <= 0:
#             print()
#             print('You lost! Try again..')
#             print('The word was {}'.format(word))
#     except:
#         print()
#         print('Try again.')
#         exit()
#
#
# if __name__ == '__main__':
#     print('Starting a game of Hangman....')
#     incorrect_attempts()



# given a 1D ARRAY, negate all elements which are between 3 and 8, in place
#
# considering a 10*3 matrix, extract rows with unequal values(eg [2,2,3])








#
# import numpy as np
# def load_nobel_data():
#     nobel_daota =
#

#
#
#
# def fun(a,*d,=0, **b):
#     print(a,d,b)
#     for i in d:
#         print(i)
#
#
# fun(10,20,40,30,b=10,c=20)















# first_last_20 = dataset.loc[dataset.last_valid_index]
    # set_data = dataset.head(20),dataset.tail(20)
    # set_data = dataset[:20],dataset[-20:]
    # print(dataset.iloc[0:20,-20:-1],dataset.iloc[-20:-1])
    # print(dataset.loc[(dataset.head(20)) , (dataset.tail(20)),:])


#
#
#
# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
# def load_nobel_data():
#     dataset = pd.read_csv("Nobel.csv")
#
#     set_data = dataset.head(20), dataset.tail(20)
#     nobel_1901_2016 = dataset.loc[(dataset['year'] >= 1901) & (dataset['year'] <= 2016),['prize']]
#     print("{0} Prizes between 1901 and 2016".format(len(nobel_1901_2016)))
#     prizes_woned_male = dataset.loc[(dataset['sex'] == 'Male')]
#     print("{0} prizes woned by Male".format(len(prizes_woned_male)))
#     prizes_woned_female = dataset.loc[(dataset['sex'] == 'Female')]
#     print("{0} prizes woned by Female".format(len(prizes_woned_female)))
#     top_10_nationalities = dataset.loc[(dataset['birth_country'] == 'France') |
#                                        (dataset['birth_country'] == 'Germany') |
#                                        (dataset['birth_country'] == 'Netherlands') |
#                                        (dataset['birth_country'] == 'Denmark') |
#                                        (dataset['birth_country'] == 'Norway') |
#                                        (dataset['birth_country'] == 'Sweden') |
#                                        (dataset['birth_country'] == 'Iceland') |
#                                        (dataset['birth_country'] == 'Finland') |
#                                        (dataset['birth_country'] == 'Italy') |
#                                        (dataset['birth_country'] == 'United Kingdom'),['birth_country','prize']]
#     print("{0} Prizes woned by top 10 country".format(len(top_10_nationalities)))
#     null_data = dataset.isnull().sum()
#     print(null_data)
#
#     dataset['born_winner'] = dataset["birth_country"] == "United States of America"
#     dataset['decade'] = (np.floor(dataset["year"] / 10) * 10).astype(int)
#     winners = dataset.groupby("decade", as_index=False)["born_winner"].mean()
#     print(winners)
#
#     # Calculate the percentage of female Nobel Prize winners per decade and visualize the observations using matplotlib.pyplot
#     dataset['female_nobel_winner'] = dataset["sex"] == "Female"
#     female_winners = dataset.groupby(["decade"], as_index=False)["female_nobel_winner"].mean()
#     print(female_winners)
#     fig = plt.figure(figsize=(20, 10))
#     plt.bar(female_winners['decade'],female_winners['female_nobel_winner'])
#     plt.xlabel('decade', fontsize=10)
#     plt.ylabel('female_nobel_winner', fontsize=10)
#     plt.xticks(female_winners['decade'],fontsize=10, rotation=30)
#     plt.title('female Nobel Prize winners')
#     plt.show()
#
#     # Find out who was the first woman to win a Nobel Prize from the dataset
#     first_female = dataset[dataset["sex"] == "Female"]
#     print(first_female.nsmallest(1, "year"))
#
#     # Find the Nobel Prize winners who have received 2 or more prizes
#     print(dataset.groupby("full_name").filter(lambda x: len(x) >= 2))
#
#     # Plot the ages of the Nobel Prize Winners using a scatter Plot
#     dataset['birth_date'] = pd.to_datetime(dataset["birth_date"])
#     dataset['age'] = dataset["year"] - dataset["birth_date"].dt.year
#     plt.scatter(dataset['age'],dataset.index)
#     plt.title("Ages of the Nobel Prize Winners")
#     plt.xlabel("Age")
#     plt.show()
#
#     '''Find out the oldest winner of a Nobel Prize for the year 2016
#        and also the youngest winner of a Nobel Prize for the year 2016'''
#     oldest_winner = dataset.nlargest(n=1, columns='age')
#     print("The oldest winner in 2016 is {0}".format(oldest_winner))
#
#
#     youngest_winner = dataset.nsmallest(n=1, columns='age')
#     print("The youngest_winner in 2016 is /n:{0}".format(youngest_winner))
#
#     Print/Display the first and last 20 entries in the dataset
#     set_data = dataset.head(20), dataset.tail(20)
#     print("{0} first and last 20 rows".format(set_data))
#     Print/Display the number of Nobel Prizes handed out between 1901 and 2016
#     nobel_1901_2016 = dataset.loc[(dataset['year'] >= 1901) &
#                                   (dataset['year'] <= 2016), ['prize']]
#     print("{0} Prizes between 1901 and 2016".format(len(nobel_1901_2016)))
#     # Print/Display the number of prizes won by male and female recipients
#     prizes_woned_male = dataset.loc[(dataset['sex'] == 'Male')]
#     print("{0} prizes woned by Male".format(len(prizes_woned_male)))
#     prizes_woned_female = dataset.loc[(dataset['sex'] == 'Female')]
#     print("{0} prizes woned by Female".format(len(prizes_woned_female)))
#     # Print/Display the number of prizes won by the top 10 nationalities
#     top_10_nationalities = dataset.loc[(dataset['birth_country'] ==
#                                         'France') |
#                                        (dataset['birth_country'] ==
#                                         'Germany') |
#                                        (dataset['birth_country'] ==
#                                         'Netherlands') |
#                                        (dataset['birth_country'] ==
#                                         'Denmark') |
#                                        (dataset['birth_country'] ==
#                                         'Norway') |
#                                        (dataset['birth_country'] ==
#                                         'Sweden') |
#                                        (dataset['birth_country'] ==
#                                         'Iceland') |
#                                        (dataset['birth_country'] ==
#                                         'Finland') |
#                                        (dataset['birth_country'] ==
#                                         'Italy') |
#                                        (dataset['birth_country'] ==
#                                         'United Kingdom'),
#                                        ['birth_country', 'prize']]
#     print("{0} Prizes woned by top 10 country".format(len(top_10_nationalities)))
#     # Print/Display how many null values are present in the dataset
#     null_data = dataset.isnull().sum()
#     print(null_data)
#     # Print/Display the percentage of USA born winners per decade
#     dataset['born_winner'] = dataset["birth_country"] == "United States of America"
#     dataset['decade'] = (np.floor(dataset["year"] / 10) * 10).astype(int)
#     winners = dataset.groupby("decade", as_index=False)["born_winner"].mean()
#     print(winners)
#
#     # Calculate the percentage of female Nobel Prize winners per decade and visualize the observations using matplotlib.pyplot
#     dataset['female_nobel_winner'] = dataset["sex"] == "Female"
#     female_winners = dataset.groupby(["decade"], as_index=False)
#     ["female_nobel_winner"].mean()
#
#
# print(female_winners)
# fig = plt.figure(figsize=(20, 10))
# plt.bar(female_winners['decade'], female_winners['female_nobel_winner'])
# plt.xlabel('decade', fontsize=10)
# plt.ylabel('female_nobel_winner', fontsize=10)
# plt.xticks(female_winners['decade'], fontsize=10, rotation=30)
# plt.title('female Nobel Prize winners')
# plt.show()
#
# # Find out who was the first woman to win a Nobel Prize from the dataset
# first_female = dataset[dataset["sex"] == "Female"]
# print(first_female.nsmallest(1, "year"))
#
# # Find the Nobel Prize winners who have received 2 or more prizes
# print(dataset.groupby("full_name").filter(lambda x: len(x) >= 2))
#
# # Plot the ages of the Nobel Prize Winners using a scatter Plot
# dataset['birth_date'] = pd.to_datetime(dataset["birth_date"])
# dataset['age'] = dataset["year"] - dataset["birth_date"].dt.year
# plt.scatter(dataset['age'], dataset.index)
# plt.title("Ages of the Nobel Prize Winners")
# plt.xlabel("Age")
# plt.show()
# ''' Find out the oldest winner of a Nobel Prize for the year 2016
#    and also the youngest winner of a Nobel Prize for the year 2016'''
# oldest_winner = dataset.nlargest(n=1, columns='age')
# print("The oldest winner in 2016 is {0}".format(oldest_winner))
# youngest_winner = dataset.nsmallest(n=1, columns='age')
# print("The youngest_winner in 2016 is /n:{0}".format(youngest_winner))
#
# load_nobel_data()
#



# given a 1D ARRAY, negate all elements which are between 3 and 8, in place
#
# considering a 10*3 matrix, extract rows with unequal values(eg [2,2,3])



# # given a 1D ARRAY, negate all elements which are between 3 and 8, in place
# import numpy as np
# arr = np.arange(11)
# m = (arr>3) & (arr<8)
# arr[m]*=-1
# print(arr)
#
#
# # considering a 10*3 matrix, extract rows with unequal values(eg [2,2,3])
# import numpy as np
# extract = np.random.randint(0, 5, (10,3))
# print(extract)
# for i in range(0,10):
#     if not ((extract[i,0] == extract[i,1]) and (extract[i,0] == extract[i,2])):
#         print(extract[i])

# print(f'Found directory: {dirpath}')
# c=[chr(i) for i in [65, 66, 67]]
# print(c)
#https://www.brianheinold.net/python/python_book.html python books
# https://www.tldp.org/LDP/abs/html/abs-guide.html
# https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/Python1_Basics.html

import os
import os, sys
import  datetime
from datetime import date, timedelta
from datetime import datetime


# yesterday = date.today() - timedelta(1)
# yesterdaysDate = yesterday.strftime('%Y%m%d')
# # yesterdaysFile_myFile = yesterday.strftime('myFile_%Y%m%d.csv')
# for dirpath, dirnames, files in os.walk('D:\\TestDir\\', topdown=False):
#     for file_name in files:
#         file_name = os.path.splitext(file_name)
#         file_name = file_name[0]
#         file_name = datetime.strptime(file_name, '%Y-%m-%d').date()
#         if yesterdaysDate in file_names:
#             print("OKAY: {0} is available".format(yesterdaysFile_myFile))
#         else:
#             print("ERROR: {0} does not exist!".format(yesterdaysFile_myFile))
#
#         print(file_name)
#     for dir_name in dirnames:
#         print(dir_name)





# for dirpath, dirnames, files in os.walk('D:\\TestDir\\', topdown=False):
#     for file_name in files:
#         print(file_name)
#     for dir_name in dirnames:
#         print(dir_name)
#


#
#
# l = [10,3,9]
# inx = 0
# val = 20
# while inx < len(l):
#     if l[inx] == val:
#         break
#     inx+=1
# else:
#     l.append(val)
#     print(l)
#


#wrong
# l = [10,3,9]
# inx = 0
# val = 9
# while inx < len(l):
#     if not l[inx] == val:
#         l.append(val)
#     else:
#         break
#     inx+=1


# class Employee():
#     def __init__(self,name,age,salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#     def __eq__(self, other):
#         if self.age == other.age:
#             return  True
#         else:
#             return False
#     def __lt__(self, other):
#         if self.salary < other.salary:
#             return  True
#         else:
#             return False
# e1 = Employee("jareena",40,30000)
# e2 = Employee("sirajunnisa",20,90000)
# print(e1 == e2)
# print(e1 < e2)
#
# e1.salary = -3000
# print(e1.salary)





# class Employee():
#     def __init__(self,
#                  name,
#                  age,
#                  salary
#                 ):
#         self._name = name
#         self._age = age
#         self._salary = salary
#
#     def get_pro(self):
#         return self._salary
#
#     def set_pro(self,_salary):
#         if self._salary <= 0:
#             raise ValueError("salary should be positive")
#         else:
#             self._salary = salary
#
#     def __eq__(self, other):
#         if self._age == other._age:
#             return  True
#         else:
#             return False
#
#     def __lt__(self, other):
#         if self._salary < other._salary:
#             return  True
#         else:
#             return False
#
# e1 = Employee("jareena",40,30000)
# e2 = Employee("sirajunnisa",20,90000)
#
#
# print(e1 == e2)
# print(e1 < e2)

# e1.set_pro(-30000)
# e1.set_pro



# class Employee():
#     def __init__(self,
#                  name,
#                  age,
#                  salary
#                 ):
#         self._name = name
#         self._age = age
#         self._salary = salary
#
#     @property
#     def salary(self):
#         return self._salary
#
#     @salary.setter
#     def salary(self, salary):
#         if salary <= 0:
#             raise ValueError("salary should be positive")
#         else:
#             self._salary = salary
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, age):
#         if self.age <= 0:
#             raise ValueError("age should be positive")
#         else:
#             self._age = age
#
#
#     def __eq__(self, other):
#         if self.age == other.age:
#             return  True
#         else:
#             return False
#
#     def __lt__(self, other):
#         if self.salary < other.salary:
#             return  True
#         else:
#             return False
#
# e1 = Employee("jareena",40,-30000)
# e2 = Employee("sirajunnisa",20,90000)
#
#
# print(e1 == e2)
# print(e1 < e2)
#
# e1.name = "Rizwana"
# # e1.salary = -3000
# print(e1 == e2)
# print(e1.name)
#






# class Employee():
#     def __init__(self,
#                  name,
#                  age,
#                  salary
#                 ):
#         self.name = name
#         self.age = age
#         self.salary = salary
#
#     @property
#     def salary(self):
#         return self.salary
#
#     @salary.setter
#     def salary(self, salary):
#         if salary <= 0:
#             raise ValueError("salary should be positive")
#         else:
#             self.salary = salary
#
#     @property
#     def age(self):
#         return self.age
#
#     @age.setter
#     def age(self, age):
#         if age <= 0:
#             raise ValueError("age should be positive")
#         else:
#             self.age = age
#
#
#     def __eq__(self, other):
#         if self.age == other.age:
#             return  True
#         else:
#             return False
#
#     def __lt__(self, other):
#         if self.salary < other.salary:
#             return  True
#         else:
#             return False
#
# e1 = Employee("jareena",40,-30000)
# e2 = Employee("sirajunnisa",20,90000)
#
#
# print(e1 == e2)
# print(e1 < e2)
#
# e1.name = "Rizwana"
# # e1.salary = -3000
# print(e1 == e2)
# print(e1.name)
#


#
# lst = [1, 2]
# lst1 = [1, 2]
# print(lst is lst1)
# print(lst == lst1)
# print("lst address {0}".format(id(lst)))
# print("lst1 address {0}".format(id(lst1)))


# def fun(a, b):
#     print(a + b)
#
# x = 10
# y = 20
# fun(x, y)


# def fun(a, b, c):
#     print(a + b + c)
#
# x = 10
# y = 20
# fun(x, y, 10)



# if we want to make any argument optional by specifying respective parameter as default
# after default parameter all arguments are made default
# def fun(a, b=10, c = 20):
#     print(a + b + c)
#
# x = 1
# y = 2
# fun(x, y, 3)



# def fun(a, b = 1, c = 2):
#     print(a + b + c)
#
# x = 10
# y = 20
# fun(x)

#
# def fun(a, b = 1, c = 2):
#     print("The value a is {0}, b is {1}, c is {2}, total is {3}".format(a, b, c, a + b + c))
#
# x = 10
# y = 20
# fun(x,20)

# def fun(a, b, c):
#     print("The value a is {0}, b is {1}, c is {2}, total is {3}".format(a, b, c, a + b + c))
#
#
# fun(a=20,b=20,c=30)

# s, b, c, *d,e = {10,40,78,"python",90}
# print("s is{0},b is {1},c is {2},d is {3},e is {4}".format(s,b,c,d,e))

# d1 = {"name":"jareena","id":6}
# d2 = {"name":"jareena1","id":9}
# d3 = {"email":"jareena@gmail.com","address":"Vijayawada"}
# d = [*d1,*d2,*d3]
# print("The name count is {0}".format(d.count("name")))
# d1 = {*d1,*d2,*d3}
# print(d1)
# print(d)

# saibabu.o@tcs.com
# bhiravprasad.bachu@tcs.com (Bhiravprasad  Bachu)



# lst = [10, 20, [30,40]]
# a, b, (*d, e)= lst
# print("a is {0}, b is {1}, d is {2}, e is {3}".format(a, b, d, e))


# def fun(a, b, c, *d):
#     print("a is {0}, b is {1}, d is {2}".format(a, b, d))
#
# lst = "python"
# fun(*lst)
# https://treyhunner.com/2018/04/keyword-arguments-in-python/ very importent

# def fun(a, b, *c, d): #after arbitory argument we should not pass any positional parameter, we will get key only argument error here
#     print("a is {0}, b is {1}, d is {2}".format(a, b, d))
#
# lst = "python"
# fun(*lst)



# def fun(a, b, *c, d):
#     print("a is {0}, b is {1}, d is {2}".format(a, b, d))
#
# lst = "python"
# fun(*lst,d=20) # d is key only argument
#
#
# def outer():
#     count = 10
#     def innner():
#         print("The counter value is {0}".format(count))
#     return innner()
# d = outer()()
# print(d.__code__.co_freevars)
# print(d.__closur__)
#

#
# def out():
#     x=[1,2,3]
#     print("before innner{0}".format(hex(id(x))))
#     def inner():
#         y = x
#         print("after innner{0}".format(hex(id(y))))
#     return inner
# o = out()()

# def modify_free_val():
#     val = 0
#     print("outer scope: {0}, memory: {1}".format(val,hex(id(val))))
#     def inc_count():
#         nonlocal val
#         print("inner scope before count : {0}, memory: {1}".format(val, hex(id(val))))
#         val+=1
#         print("inner scope: {0}, memory: {1}".format(val,hex(id(val))))
#     return inc_count
#
# d = modify_free_val()
# d()



#
#
# def modify_free_val():
#     val = 0
#     print("outer scope: {0}, memory: {1}".format(val,hex(id(val))))
#     def inc_count():
#         nonlocal val
#         print("inner scope before count : {0}, memory: {1}".format(val, hex(id(val))))
#         val+=1
#         print("inner scope: {0}, memory: {1}".format(val,hex(id(val))))
#     return inc_count
#
# d = modify_free_val()
# d()
#
# def out(x):
#     x = 10
#     def inner(y):
#         return x + 1
#     return inner
# o = out(10)
# o(2)  0x7ffecbd37ce0

# def create():
#     lst = []
#     for n in range(1,4):
#         lst.append(lambda x, y=n  : x + y)
#     return lst
# obj = create()
# print(obj[0](10))
# print(obj.__closure__)
# print(obj.__code__.co_freevars)
# print(obj)

# x = [[0,0]]
# print(x)
# print(id(x))
# print("before con : {0}".format(id(x[0])))
# a = x + x
# print(a)
# print(id(a))
# print("after con : {0}".format(id(a[1])))
# print(x[0]==a[0]==a[1])

# lst = ['s','a','l']
# str_var = "jar"
# up_str = " ".join(list(str_var)+lst)
# print(up_str)


# lst = [1,2,4]
# def do_some(l):
#     lst.append("jareena")
# do_some(lst)
# print(lst)
#
# tup = (1,2,4)
# def do_some(l):
#     print(tup + ("jareena",))
# do_some(tup)
# print(tup)

# lst = [1,2,4,5,43]
# def do_some(l):
#     l[2:6] = (12,32,9,49,49)
# do_some(lst)
# print(lst)


# tup = (1,2,4,5,43)
# def do_some(tup):
#     print(tup[2:6] + (12,32,9,49,49))
# do_some(tup)
# print(tup)

# lst = [1,2,4]
# def do_some(lst):
#     print(hex(id(lst)))
#     print(lst.append(29))
#     result = lst.append(29)
#     print(hex(id(result)))
#     print(result)
# do_some(lst)
# print(lst)

# l = [1,2,3]
# print(l.reverse())
# print(l)


# l = [[1,2,3],'c','d']
# def fun(lst):
#     print(l)
#     l2 = l.copy()
#     print(l[0] is l2[0])
#     print(l[1] is l2[1])
#     print(l2)
# fun(l)
#
# l = ('c','d')
# def fun(lst):
#     print(id(lst))
#     lst = lst + ('e',)
#     print(id(lst))
# fun(l)


#
# l = ['c','d']
# def fun(lst):
#     print(id(lst))
#     lst = lst + ['e']
#     print("after concatination{0}".format(id(lst[0])))
#     print(id(lst))
# fun(l)
# print("outside {0}".format(id(l[0])))

# t=(10,29)
# print("t :{0}".format(id(t)))
# t1 = tuple(t)
# print("t1 :{0}".format(id(t1)))
# print(t1,"\n\n")


# t=[10,29]
# print("list t :{0}".format(id(t)))
# t1 = list(t)
# print("list t1 :{0}".format(id(t1)))
# print(t[0] is t1[0])
# print(t1)
#

# t = (10, 30)
# print(id(t))
# t2 = t[:]  #here if we are creating t2 with entire t slicing then both t and t2 pointing to the same object
# print(t[0] is t2[0]) #even elements or objects in containers of t and t2 are also same
# print(id(t2))

# def fun(tup):
#     print(id(tup))
#     t2 = tup[1:]  #here if we are creating t2 with entire t slicing then both t and t2 pointing to the same object
#     print(tup[1] is t2[0]) #even elements or objects in containers of t and t2 are also same
#     print(id(t2))
#
# t = (10, 30)
# fun(t)
# x = "python"
# a = x + x
# print(a)
#
# from copy import copy, deepcopy
# def fun(a):
#     def __init__(self, a):
#         self.a = a
#
#
# x = [1,2]
# obj = fun(x)
# print(x is obj.a)
# cp = copy(obj)
#
# print(obj.a is cp.a)


#Note:
#container memory address is different but elements in both containers pointing to same memory address
# lst = [[1,2],[3,4]]
# emp_lst = []
# emp_lst = [e.copy() for e in lst]
# print(emp_lst)
# emp_lst[0][0] = 100
# print(id(lst[0][0]),lst)
# print(id(emp_lst[0][0]),emp_lst)
# print("\n\n\n")


# lst = [[[1,1],[2,2]],[[3,3],[4,4]]]
# emp_lst = []
# emp_lst = [[i.copy() for i in e] for e in lst]
# print(emp_lst)
# emp_lst[0][0][0] = 100
# print(id(lst[0][0][0]),lst)
# print(id(emp_lst[0][0][0]),emp_lst)
# print(emp_lst)
# print(lst)
#
# print()
# print("second list in lst elements: {0}".format(id(lst[0][0])))
# print("second list in emp_lst elements: {0}".format(id(emp_lst[0][0])))
# print()
#
# print("second list in lst elements: {0}".format(id(lst[0][0][0])))
# print("second list in emp_lst elements: {0}".format(id(emp_lst[0][0][0])))
# print("\n")
#


# def fun(l):
#     index = 0
#     lst_new = []
#     while True:
#         try:
#             element = l.__getitem__(index)
#         except IndexError:
#             break
#         lst_new.append(element**2)
#         index+=1
#     print(lst_new)
#
# lst = [1,3,2,5,4]
# obj = fun(lst)

# class custom_sequence():
#     def __init__(self, n):
#         self.n = n
#     def __getitem__(self, item):
#         if item < 0 or item >= self.n:
#             raise IndexError
#         else:
#             print(f"This is donder getitem function")
#
#
# obj = custom_sequence(10)
# # obj.__getitem__(10)
# for i in obj:
#     print(i)


# lst = [1,2,3]
# lst[0:1] = {4,5,6,7}
# print(lst)















# class Custom_Sqnce:
#     def __init__(self,n):
#         self.n = n
#
#     def __getitem__(self, item , lst, item1):
#         result = lst[item1]
#         print(result)
#         # if item < 0 or item >= self.n:
#         #     raise IndexError
#         # else:
#         #     result = lst.__getitem__(item1)
#         #     print(result)
# l = [12, 36, 37]
# obj = Custom_Sqnce(10)
# obj.__getitem__(9, l, 2)


# lst = [12,34,23]
# lst.extend((12,43,65))
# print(lst)

# import numbers
# class sam:
#     def __init__(self, x, y):
#         if isinstance(x, numbers.Real) and isinstance(y, numbers.Real):
#             self.pt = (x, y)
#         else:
#             raise TypeError
#     def __str__(self):
#         self.__repr__()
#     def __repr__(self):
#         f'sam(x = {self.pt[0]}, y = {self.pt[1]}))'
#
#
# obj = sam(12, 78)
# a,b = obj


#
# a = 'a'
# b = 'b'
# print(a < b)


# dic = {'a':120,'b':130, 'c':12}
# print(sorted(dic))
# print(sorted(dic,key=lambda k:dic[k]))

# dic = ["jare", "mehna", "yauna"]
# def lenght(s):
#     return len(s)
# print(sorted(dic,key=lenght))
# https://tcsglobal.udemy.com/course/the-complete-python-postgresql-developer-course/learn/lecture/4707546#overview
#
# def lenght(s,s1):
#     return len(s), len(s1)
#
# emp = []
# upper = ""
# lst = ["jare", "ma", "yauna"]
# def sort_func(l,emp_lst):
#     for element in l:
#         for ele2 in range(1, len(l)):
#             if len(element) > len(l[ele2]):
#                 upper+=element
#             else:
#                 emp_lst.append(ele2)
#     print(emp_lst)
#
# sort_func(lst,emp)

# from statistics import mean
# def fun(*args):
#     return mean(args)
#
# lst = list(map(int,input("enter number").split()))
# result = fun(*lst)
# print("%.6f"%result)
# print(result)
#


# nter number98 98 09 78 43
# 65.20




















# reverse
# save classes with area method
# a=10
# b =20
# a, b = b, a
# print("a is {0} and b is {1}".format(a,b))


# https://www.codegrepper.com/code-examples/r/python+practice+questions


#
# class Car():
#     def __init__(self,max_speed,units):
#         self.max_speed = max_speed
#         self.units = units
#     def __str__(self):
#         if self.max_speed == 94:
#             return "Car with maximum spead of {} and the units is {}".format(self.max_speed,self.units)
#         else:
#             '''if we does not return something in function then function return NONE'''
#             return  "Car with maximum spead of {} and the units is {}".format(self.max_speed,self.units)
#
# obj = Car(94,"mph")
# print(obj.__str__())
#
#
#
#



#
# from statistics import mean
# def fun(*args):
#     return mean(args)
#
# lst = list(map(int, input("Enter list of numbers").split()))
# result = fun(*lst)
# print("%.2f"%result)









































#elements in both container pointing to the same memory address
# but the elements are immutable so we cant make changes on i
# lst = [(1,2),(3,4)]
# emp_lst = []
# emp_lst = [e for e in lst]
# print(emp_lst)
# # emp_lst[0][0] = 100
# print(id(lst[0][0]),lst)
# print(id(emp_lst[0][0]),emp_lst)


#To avoid making changes on one container elements will effect on another container elements
# lst = [[1,2],[3,4]]
# emp_lst = []
# emp_lst = [e.copy() for e in lst]
# print(emp_lst)
# # print(id(lst[0][0]),lst)
# # print(id(emp_lst[0][0]),emp_lst)
# emp_lst[0][0] = 100
#
# print(id(lst[0][0]),lst)
# print(id(emp_lst[0][0]),emp_lst)

# print(emp_lst)






# from copy import copy, deepcopy
# lst = [1,2,3]
# emp_lst = []
# emp_lst = copy(lst)
# print(lst)
# print(emp_lst)
# print(id(lst[0]) is id(emp_lst[0]))
# print(id(lst[1]) is id(emp_lst[1]))
# # print("check elements memory addresss: {0}".format(id(lst[0]) is id(emp_lst[0])))
# print(id(lst) is id(emp_lst))
# print(id(lst))
# print(id(emp_lst))

