# function to count the elements in the string
print('python program to print the count of elements in a string in descending order') 
def make_frequent(str):
  d = dict()
  for count in str:
    if count not in d:
      d[count] = 1
    else:
      d[count] += 1
  return d

# function call 
dictionary = make_frequent('missippi')

# making into a list and sorting in descending order
string_list = []
for index in dictionary:
    string_list.append((dictionary[index],index))
string_list.sort(reverse = True)
for counter , letter in string_list:
    print(letter , counter)
      
