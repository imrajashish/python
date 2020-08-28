             #_______________________________________________________#
                       #Sample Solution:-
#Write a Python program to sort (ascending and descending) a dictionary by value.
import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('Original dictionary : ',d)
sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1)))
print('Dictionary in ascending order by value : ',sorted_d)
sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1),reverse=True))
print('Dictionary in descending order by value : ',sorted_d)

#Write a Python script to concatenate following dictionaries to create a new one.
s = {1:10,2:30}
s.update({3:40,5:"Ashish"})
print(s)

#Write a Python script to concatenate following dictionaries to create a new one.
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dict4 = {}
for d in (dic1,dic2,dic3):
        dict4.update(d)
print(dict4)

#Write a Python script to check whether a given key already exists in a dictionary.
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
is_key_present(5)
is_key_present(9)
             #_______________________________________________________#
