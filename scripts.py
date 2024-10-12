

# Say "Hello,world!" with Python

if __name__ == '__main__':
    string = "Hello, World!"
    print(string)

# Python If-Else


if __name__ == '__main__':
    n = int(input().strip())
    if n>=1 and n<=100:
        if n%2!=0:
            print("Weird")
        else:
            if n>=2 and n<=5:
                print("Not Weird")
            if n>=6 and n<=20:
                print("Weird")
            if n>20:
                print("Not Weird")

# Arithmetic Operators


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)

# Python: Division


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)

# Loops


if __name__ == '__main__':
    n = int(input())
    for i in range(0,n):
        print(i**2)

#Write a function 


def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%100!=0:
        if year%4==0:
            return True
        return leap
    else:
        if year%400==0:
            return True
        return leap
    

year = int(input())
print(is_leap(year))

#Print Function


if __name__ == '__main__':
    n = int(input())
    i=1
    while i<=n :
        print(i,end="")
        i+=1



#List Comprehensions

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
coordinate = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
print(coordinate) 

#Find the Runner-up Score!

if __name__ == '__main__':
    n = int(input())
    arr = set(map(int, input().split()))
    runner_up = sorted(arr, reverse=True)[1]
    print(runner_up)
            


#Nested Lists

if __name__ == '__main__':
    lista=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lista.append([name,score])
    set_scores = sorted(set(score for name, score in lista))
    second_lowest_score = set_scores[1]
    ordered_names=[]
    for name,score in lista:
        if score == second_lowest_score:
            ordered_names.append(name)
    ordered_names.sort()
    for name in ordered_names:
        print(name)

#Finding the percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    average = 0
    marks = student_marks[query_name]
    size = len(marks)
    for mark in marks:
        average+=mark
    average = average/size
    print(f'{average:.2f}')

#Lists

if __name__ == '__main__':
    N = int(input())
    lista = []
    for i in range(N):
        string = input().split(None,1)
        if string[0] == "print":
            print(lista)
        if string[0] == "sort":
            lista.sort()
        if string[0] == "pop":
            lista.pop()
        if string[0] == "reverse":
            lista.reverse()    
        else:
            if string[0] == "append":
                lista.append(int(string[1]))
            if string[0] == "remove":
                if int(string[1]) in lista:
                    lista.remove(int(string[1]))
            if string[0] == "insert":
                value = string[1].split()
                lista.insert(int(value[0]),int(value[1]))
 
#Tuples

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = ()
    for element in integer_list:
        t = t + (element,)
    print(hash(t))   


#sWAP Case

def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

#String Split and Join 

def split_and_join(line):
    # write your code here
    splitted_string = line.split()
    return "-".join(splitted_string)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)  

#What's Your Name?

def print_full_name(first, last):
    # Write your code here
    string = "Hello "+first+" "+last+"! You just delved into python."
    print(string)

#Mutations

def mutate_string(string, position, character):
    return string[:position]+character+string[position+1:]   

#Find a string

def count_substring(string, sub_string):
    count = 0
    start = 0
    while start < len(string):
        index = string.find(sub_string, start)
        if index != -1:
            count += 1
            start = index + 1
        else:
            break
    return count

#String Validators

if __name__ == '__main__':
    s = input()
    exit = 0
    for char in s:
        if char.isalnum():
            print(True)
            exit=1
            break
    if not exit:
        print(False)
    exit = 0
    for char in s:
        if char.isalpha():
            print(True)
            exit=1
            break
    if not exit:
        print(False)
    exit = 0

    for char in s:
        if char.isdigit():
            print(True)
            exit=1
            break
    if not exit:
        print(False)
    exit = 0

    for char in s:
        if char.islower():
            print(True)
            exit=1
            break
    if not exit:
        print(False)
    exit = 0

    for char in s:
        if char.isupper():
            print(True)
            exit=1
            break
    if not exit:
        print(False)
   
    
        

 #Text Alignment

thickness = int(input())
for i in range(thickness):
    print(("H" * (2 * i + 1)).center(thickness * 2, " "))
for i in range(thickness+1):
    print(("H"*thickness+(thickness*3)*" "+"H"*thickness).rjust(thickness*5 + thickness//2 ," "))
for i in range(thickness//2 + 1):
    print(("H"*(thickness*5)).rjust(thickness*5 + thickness//2," "))
for i in range(thickness):
    print(("H"*thickness+(thickness*3 )*" "+"H"*thickness).rjust(thickness*5 + thickness//2," "))
print(("H"*thickness+(thickness*3)*" "+"H"*thickness).rjust(thickness*5 + thickness//2," "))
for i in range(thickness):
    print(("H" * (2 * (thickness-i) - 1)).center(thickness * 2, " ").rjust(thickness*6," "))


#Text Wrap 

def wrap(string, max_width):
    sub_string=""
    for i in range(0,len(string),max_width):
        sub_string = sub_string + string[i:i+max_width] + "\n"
    return sub_string

#Designer Door Mat

rows,cols = input().split()
rows = int(rows)
cols = int(cols)
for i in range(1, rows, 2):
        pattern = ".|." * i
        print(pattern.center(cols, '-'))
print("WELCOME".center(cols, '-'))
for i in range(rows - 2, 0, -2):
    pattern = ".|." * i
    print(pattern.center(cols, '-'))

#String Formatting

def print_formatted(number):
    # your code goes here
    space_padding = len(str(bin(number)[2:]))+1
    for i in range(1,number+1):
        print(str(i).rjust(space_padding-1," ")+str(oct(i)[2:]).rjust(space_padding," ")+str(hex(i)[2:]).upper().rjust(space_padding," ")+str(bin(i)[2:]).rjust(space_padding," "))


#Alphabet Rangoli

import string
def print_rangoli(size):
    # your code goes here
    alphabet = string.ascii_lowercase
    letters = [alphabet[i] for i in range(size)]
    for i in range(size - 1, 0, -1):
        pattern = '-'.join(letters[size - 1:i:-1] + letters[i:size])
        print(pattern.center(size * 4 - 3, '-'))
        
    print('-'.join(letters[size - 1::-1] + letters[1:size]).center(size * 4 - 3, '-'))
    
    for i in range(1, size):
        pattern = '-'.join(letters[size - 1:i:-1] + letters[i:size])
        print(pattern.center(size * 4 - 3, '-')) 

#Capitalize!

def solve(s):
    upper_string = s.split(" ")
    string = ""
    for i in range(len(upper_string)):
        upper_string[i] = upper_string[i].capitalize()
    for i in range(len(upper_string)):
        string += upper_string[i]
        string += " "
    return string

#The Minion Game

def minion_game(string):
    # your code goes here
    score_stuart=0
    score_kevin=0
    length = len(string)
    for i in range(length):
        if string[i] in "AEIOU":
            score_kevin+=length-i
        if string[i] in "BCDFGHJKLMNPQRSTVWYXZ":
            score_stuart+=length-i

    if score_stuart > score_kevin:
        print("Stuart "+str(score_stuart))
    elif score_stuart < score_kevin:
        print("Kevin "+str(score_kevin))
    else:
        print("Draw")

#Merge The Tools!

def merge_the_tools(string, k):
    # your code goes here
    for i in range(0,len(string),k):
        print("".join(set(list(string[i:i+k]))))

#Introduction to Sets

def average(array):
    # your code goes here
    new_set = set(array)
    n = len(new_set)
    avg = 0
    for elem in new_set:
        avg+=elem
    return round(avg/n,3)

#No Idea!

sizes = input().split()
n = sizes[0]
m = sizes[1]
array = list(map(int,input().split()))
A = set(map(int,input().split()))
B = set(map(int,input().split()))
happiness = 0
for elem in array:
    if elem in A:
        happiness+=1
    if elem in B:
        happiness-=1

print(happiness)

#Symmetric Difference

size1 = int(input())
lis1 = input().split()
newset1 = set(list(map(int,lis1)))
size2 = int(input())
lis2 = input().split()
newset2 = set(list(map(int,lis2)))
new_set = (newset1.union(newset2)).difference(newset1.intersection(newset2))
new_set = sorted(new_set)
for elem in new_set:
    print(elem)



#Set.add()

n = int(input())
new_set = set()
for i in range(n):
    new_set.add(input())
print(len(new_set))

#Set .discard(), .remove() & .pop()

n = int(input())
s = set(map(int, input().split()))
commands = int(input())
for i in range(commands):
    command = input().split()
    if command[0]=="pop" and len(s)>0:
        s.pop()
    if command[0] == "remove":
        elemento = int(command[1])
        if elemento in s:
            s.remove(elemento)
    if command[0] == "discard":
        elemento = int(command[1])
        s.discard(elemento)
sum_set = 0
for elem in s:
    sum_set+=elem
print(sum_set)


#Set .union() Operation

n1 = int(input())
english = set(map(int, input().split()))
n2 = int(input())
french = set(map(int, input().split()))
print(len(english.union(french)))

#Set .intersection() Operation

n1 = int(input())
english = set(map(int, input().split()))
n2 = int(input())
french = set(map(int, input().split()))
print(len(english.intersection(french)))

#Set .difference() Operation

n1 = int(input())
english = set(map(int, input().split()))
n2 = int(input())
french = set(map(int, input().split()))
print(len(english.difference(french)))

#Set .symmetric_difference() Operation

n1 = int(input())
english = set(map(int, input().split()))
n2 = int(input())
french = set(map(int, input().split()))
print(len(english.symmetric_difference(french)))

#Set Mutations

sizeA = int(input())
A = set(map(int, input().split()))
number_sets = int(input())
for i in range(number_sets):
    command = input().split()
    new_set = set(map(int, input().split()))
    if command[0] == "intersection_update":
        A.intersection_update(new_set)
    if command[0] == "symmetric_difference_update":
        A.symmetric_difference_update(new_set)
    if command[0] == "difference_update":
        A.difference_update(new_set)
    if command[0] == "update":
        A.update(new_set)
sum_set = 0
for elem in A:
    sum_set+=elem
print(sum_set)

#The Captain's Room

K = int(input())
lis = list(map(int, input().split()))
sum_set = sum(set(lis))*K
sum_list = sum(lis)
print((sum_set - sum_list)//(K-1))

#Check Subset

T = int(input())
for i in range(T):
    sizeA = int(input())
    A = set(map(int, input().split()))
    sizeB = int(input())
    B = set(map(int, input().split()))
    print(A == A.intersection(B))

#Check Strict Superset

a = True
A = set(map(int, input().split()))
n = int(input())
for i in range(n):
    B = set(map(int, input().split()))
    if B == A or B.intersection(A) != B:
        a = False
        break
print(a)


#collections.Counter()

from collections import Counter
X  = int(input())
shoe_sizes = Counter(list(map(int,input().split())))
customers = int(input())
earn = 0
for i in range(customers):
    size,offer = map(int, input().split())  
    if shoe_sizes[size] > 0:
        shoe_sizes[size]-=1
        earn+= offer
print(earn)

#DefaultDict Tutorial

from collections import defaultdict
n , m = map(int, input().split())
d = defaultdict(list)
for i in range(1,n+1):
    letter = input()
    d[letter].append(i)
for i in range(m):
    letter = input()
    if letter in d.keys():
        print(" ".join(map(str, d[letter])))
    else:
        print(-1)

#Collections.namedtuple()

N = int(input())
index = input().split().index("MARKS")
avg = 0
for i in range(N):
    avg+=int(input().split()[index])
print(avg/N)

#Collections.OrderedDict()

N = int(input())
ordered_dict = {}
for _ in range(N):
    key, value = input().rsplit(None, 1)
    value = int(value)
    if key not in ordered_dict.keys():
        ordered_dict[key] = value
    else:
        ordered_dict[key]= ordered_dict[key] + value
for key in ordered_dict.keys():
    print(key+" "+str(ordered_dict[key]))

#Word Order

from collections import Counter
size = int(input())
lis = []
for i in range(size):
    lis.append(input())
d = Counter(lis)
print(len(d))
for elem in d.values():
    print(elem,end=" ")

#Collections.deque()

from collections import deque
d = deque()
N = int(input())
for i in range(N):
    command = input().split()
    if command[0] == "append":
        d.append(int(command[1]))
    if command[0] == "pop":
        d.pop()
    if command[0] == "popleft":
        d.popleft()
    if command[0] == "appendleft":
        d.appendleft(int(command[1]))
for elem in d:
    print(elem, end=" ")

#Company Logo

s = input()
lis = Counter(s)
left_elements = 3
for key, value in lis.most_common():
        if left_elements==0:
            break
        keys = [chiave for chiave, valore in lis.items() if valore == value]
        if len(keys) == 1:
            print(key, end=" ")
            print(value)
        else:
            keys = sorted(keys)
            print(keys[0],end = " ")
            print(lis[keys[0]])
            del lis[keys[0]]
        left_elements-=1    

#Piling Up!

from collections import deque
T = int(input())
for i in range(T):
    n = int(input())
    d = deque(map(int, input().split()))
    previous_cube = float("inf")
    checked = True
    while (len(d) > 1 and checked):
        right, left = d[-1], d[0]
        if right <= previous_cube and left <= previous_cube:
            if right > left:
                previous_cube = right
                d.pop()
            else:
                previous_cube = left
                d.popleft()
        else:
            checked = False
    if checked and d[0] <= previous_cube:
        print("Yes")
    else:
        print("No")


#Calendar Module

import calendar
s = list(map(int, input().split()))
cal = calendar.weekday(s[2], s[0], s[1])
print(calendar.day_name[cal].upper())


#Time Delta

from datetime import datetime
def time_delta(t1, t2):
    time_format = "%a %d %b %Y %H:%M:%S %z"
    time_secs1 = datetime.strptime(t1, time_format)
    time_secs2 = datetime.strptime(t2, time_format)
    time_difference = abs(time_secs1 - time_secs2)
    return str(int(time_difference.total_seconds()))


#Exceptions

T = int(input())
for i in range(T):
    
    a, b =  input().split()
    try:
        print(int(a) // int(b))
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)
        
#Zipped!

N, X = map(int, input().split())
tot = []
for i in range(X):
    marks = [list(map(float, input().split()))]
    tot += marks
tot_marks = list(zip(*tot))
for elem in tot_marks:
    print(sum(elem) / X)


#Athlete Sort

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    ordered_list = sorted(arr, key=lambda x: x[k])
    for elem in ordered_list:
        for i in range(m):
            print(elem[i], end=" ")
        print("")

#ginortS

string = input()
upper_char = []
lower_char = []
odd_digits = []
even_digits = []
for char in string:
    if char.isalpha() and char.isupper():
        upper_char.append(char)
    if char.isalpha and char.islower():
        lower_char.append(char)
    if char.isdigit() and int(char)% 2 == 0:
        even_digits.append(char)
    if char.isdigit() and int(char)% 2 != 0:
        odd_digits.append(char)

print("".join(sorted(lower_char)+sorted(upper_char)+sorted(odd_digits)+sorted(even_digits)))

#Map and Lambda Function

cube = lambda x: x**3

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence
    
#Detect Floating Point Number

size = int(input())
a = True
for i in range(size):
    N = input()
    try:
        float(N)
        if "." not in N:
            print(not a)
        elif "+" in N and "-" in N:
            print(not a)
        elif N.find(".")<=len(N)-1 and not N[N.find(".")+1:].isdigit():
            print(not a)
        else:
            print(a)
        
    except ValueError:
        print(not a)

#Re.split()

regex_pattern = r"\.|,"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))

#Group(),Groups() & Groupdict()

import re
string = input()
regex = r'([a-zA-Z0-9])\1+'
substring = re.search(regex, string)
if substring:
    print(substring.group(1))
else:
    print(-1)

#Re.findall() & Re.finditer()

import re
string = input()
regex = r'(?<=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])[aeiouAEIOU]{2,}(?=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])'
if len(re.findall(regex, string))==0:
    print(-1)
else:
    for elem in re.findall(regex, string):
        print(elem)

#Re.start() & Re.end()

import re
string = input()
substring = input()
regex = r''+substring
if not re.search(regex, string):
    print("(-1, -1)")   
else:
    start = 0
    count = 0
    for i in range(len(string)-len(substring)):
        match = re.search(regex, string[start:])
        if match:
            print('('+ str(match.start() + count)+ ', ' + str(match.end()-1 +count)+')')
            start = match.end() - 1 + count
            count = len(string) - len(string[start:])
        if not match:
            break
        if match.start() == match.end()-1:
            start+=1
            count+=1

#Regex Substitution

import re
N = int(input())
for i in range(N):
    string = input()
    string = re.sub(r'(?<=\s)(&{2})(?=\s)', "and", string)
    if "||" not in string:
        print(string)
    else:
        print(re.sub(r'(?<=\s)(\|{2})(?=\s)', "or", string))

#Validating Roman Numerals

regex_pattern = r"(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))

#Validating phone numbers

import re
N = int(input())
regex = r'\b(7|8|9)(\d{9})$'
for i in range(N):
    string = input()
    if re.match(regex, string):
        print("YES")
    else:
        print("NO")

#Validating and Parsing Email Addresses

import re
N = int(input())
regex = r'<([a-zA-Z])(\w|\.|\-)+@([a-zA-Z]+)\.([a-zA-Z]{1,3})>'
for i in range(N):
    string = input()
    lis = string.split()
    if re.match(regex, lis[1]):
        print(string)

#Hex Color Code

import re
N = int(input())
regex = r'\#([0-9A-Fa-f]{3}|[0-9A-Fa-f]{6})(?:\;|\,|\))'
for i in range(N):
    string = input()
    lis = re.findall(regex, string)
    for el in lis:
        print("#"+el)

#HTML Parser - Part 1

from html.parser import HTMLParser
class MyHTLMParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        if attrs:
            for element in attrs:
                print("-> "+element[0]+" >", element[1])
        
    def handle_endtag(self, tag):
        print("End   :", tag)
        
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        if attrs:
            for element in attrs:
                print("-> "+element[0]+" >", element[1])          
 
N = int(input())
parser = MyHTLMParser()

for i in range(N):
    string = input()
    parser.feed(string)

#HTML Parser - Part 2

from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if "\n" in data:
            print(">>> Multi-line Comment")
            print(data)
        else:
            print(">>> Single-line Comment")
            print(data)
        
    def handle_data(self, data):
        if data!="\n":
            print(">>> Data")
            print(data) 
html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()

#Detect HTML Tags, Attributes and Attribute Values

from html.parser import HTMLParser
class MyHTLMParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        if attrs:
            for element in attrs:
                print("-> "+element[0]+" >", element[1])
                     
    def handle_startendtag(self, tag, attrs):
        print(tag)
        if attrs:
            for element in attrs:
                print("-> "+element[0]+" >", element[1])  
N = int(input())
parser = MyHTLMParser()

for i in range(N):
    string = input()
    parser.feed(string)

#Validating UID

import re
N = int(input())
regex_alpha = r'.*[A-Z].*[A-Z].*'
regex_digit = r'.*[0-9].*[0-9].*[0-9].*'
regex_char  = r'[a-zA-Z0-9]{10}'
regex_double =r'^(?!.*(.).*\1).+$'
for i in range(N):
    string = input()
    if re.match(regex_alpha,string) and re.match(regex_digit,string) and re.match(regex_char,string) and re.match(regex_double,string):
        print("Valid")
    else:
        print("Invalid")

#Validating Credit Card Numbers

import re
N = int(input())
regex_digit = r'^[4-6][0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}$'
regex_double = r'^(?!.*([0-9])-?\1-?\1-?\1).*$'
for i in range(N):
    string = input()
    if re.search(regex_digit,string) and re.search(regex_double,string):
        print("Valid")
    else:
        print("Invalid")

#Validating Postal Codes

regex_integer_in_range = r"^[1-9][0-9]{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"([0-9])(?=[0-9]\1)"	# Do not delete 'r'.
import re
P = input()
print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

#Matrix Script

import math
import os
import random
import re
import sys
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
regex = r'(?<=[A-Za-z0-9])[\s|@|#|$|%|&]+(?=[A-Za-z0-9])'
matrix = []
string = ''
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
for i in range(m):
    for j in range(n):
        string += matrix[j][i]
print(re.sub(regex,' ',string),end="")
        
#XML 1 - Find the Score

def get_attr_number(node):
    count = 0
    for element in node.iter():
        count+=len(element.attrib)
    return count

#XML2 - Find the Maximum Depth

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    level+=1
    if level > maxdepth:
        maxdepth = level
    for el in elem:
        child_depth = depth(el,level)
     

#Standardize Mobile Number Using Decorators

import re
def wrapper(f):
    def fun(l):
        regex = r'^(\+91|91|0)'
        lis = []
        for el in l:
            string = el
            if len(el)>10:
                string = re.sub(regex,"",el)
            format_string = '+91 {} {}'.format(string[:5], string[5:])
            lis.append(format_string)
        return f(lis)
            
    return fun        

#Decorators 2 - Name Directory

def person_lister(f):
    def inner(people):
        # complete the function
        lis = sorted(people, key=lambda x: int(x[2]))
        return [f(person) for person in lis]
        
    return inner

#Arrays

import numpy
def arrays(arr):
    return numpy.array(arr,float)[::-1]

# Shape and Reshape

lis = list(map(int,input().split()))
arr = numpy.array(lis)
print(numpy.reshape(arr,(3,3)))

# Transpose and Flatten

N,M = map(int,input().split())
lis = []
for i in range(N):
    lis.append(list(map(int,input().split())))
arr = numpy.array(lis)
print(numpy.transpose(arr))
print(arr.flatten())

#Concatenate

N,M,P = map(int, input().split())
lis = []
lis2 = []
for _ in range(N):
    lis.append(list(map(int, input().split())))
for _ in range(M):
    lis2.append(list(map(int, input().split())))
arr1 = numpy.array(lis)
arr2 = numpy.array(lis2)
print(numpy.concatenate((arr1,arr2), axis = 0))

#Zeros and Ones

lis  = list(map(int ,input().split()))
arr = numpy.array(lis)
print(numpy.zeros(arr, dtype = numpy.int))
print(numpy.ones(arr, dtype = numpy.int))

#Eye and Identity

numpy.set_printoptions(legacy='1.13')
n,m = map(int, input().split())
print(numpy.eye(n,m))

#Array Mathematics

n, m = map(int, input().split())
lis1 = []
lis2 = []
for _ in range(n):
    lis1.append(list(map(int, input().split())))
for _ in range(n):
    lis2.append(list(input().split()))
arr1 = numpy.array(lis1, int)
arr2 = numpy.array(lis2, int)
print(numpy.add(arr1, arr2))
print(numpy.subtract(arr1, arr2))
print(numpy.multiply(arr1, arr2))
print(numpy.floor_divide(arr1, arr2))
print(numpy.mod(arr1, arr2))
print(numpy.power(arr1, arr2))

#Floor, Ceil and Rint

numpy.set_printoptions(legacy='1.13')
arr = numpy.array(list(map(float, input().split())))
print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))

#Sum and Prod

n, m = map(int, input().split())
lis = []
for _ in range(n):
    lis.append(list(map(int, input().split())))
arr = numpy.array(lis)
print(numpy.prod(numpy.sum(arr, axis = 0)))  

#Min and Max

n, m = map(int, input().split())
lis = []
for _ in range(n):
    lis.append(list(map(int, input().split())))
arr = numpy.array(lis)
print(numpy.max(numpy.min(arr, axis = 1)))  

#Mean, Var, and Std

n, m = map(int, input().split())
lis = []
for _ in range(n):
    lis.append(list(map(int, input().split())))
arr = numpy.array(lis)
print(numpy.mean(arr, axis=1))
print(numpy.var(arr, axis=0))
print(round(numpy.std(arr, axis=None),11))

#Dot and Cross

n = int(input())
lis1 = []
lis2=[]
for _ in range(n):
    lis1.append(list(map(int, input().split())))
for _ in range(n):
    lis2.append(list(map(int, input().split())))
arr1 = numpy.array(lis1)
arr2 = numpy.array(lis2)
print(numpy.dot(arr1, arr2))

#Inner and Outer

A = numpy.array(list(map(int, input().split())))
B = numpy.array(list(map(int, input().split())))
print(numpy.inner(A, B))
print(numpy.outer(A, B))

#Polynomials

pol = numpy.array(list(map(float, input().split())))
x = int(input())
print(numpy.polyval(pol, x))

#Linear Algebra

n = int(input())
lis = []
for _ in range(n):
    lis.append(list(map(float, input().split())))
print(round(numpy.linalg.det(lis),2))

#Birthday Cake Candles

def birthdayCakeCandles(candles):
    # Write your code here
    max_candle = max(candles)
    count = 0
    for elem in candles:
        if elem == max_candle:
            count+=1
    return count

#Number Line Jumps

def kangaroo(x1, v1, x2, v2):
    current_pos1=x1
    current_pos2 = x2
    while True:
        if current_pos1 == current_pos2:
            return "YES"
        if (current_pos1<current_pos2 and v1 <= v2) or  (current_pos1 > current_pos2 and v1 >= v2):
            return "NO"
        current_pos1+=v1
        current_pos2+=v2

#Viral Advertising

def viralAdvertising(n):
    liked = 5//2
    cumulative = liked
    for i in range(n-1):
        liked = (3*liked)//2
        cumulative += liked
    return cumulative

#Recursive Digit Sum

def superDigit(n, k):
    if len(n)==1:
        return int(n)
    else:
        count = 0
        for char in n:
            count += int(char)
        count = count*k
        return superDigit(str(count), 1)  
    
#Insertion Sort - Part 1

def insertionSort1(n, arr):
    number = arr[n-1]
    if len(arr) == 1:
        print(number)
        return
    i = n-2
    while number<arr[i] and i>=0:
        arr[i+1] = arr[i]
        for el in arr:
            print(el, end=" ")
        print("\n",end="")
        i-=1
    arr[i+1]=number
    for el in arr:
        print(el, end =" ")

#Insertion Sort - Part 2

def insertionSort2(n, arr):
    if len(arr) == 1:
        print(arr[0])
        return
    for i in range(1, n):
        insertionSort1(i+1, arr)
        for el in arr:
            print(el, end=" ")
        print("\n",end="")