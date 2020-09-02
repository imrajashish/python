#Write a Python program to find the number of notes (Sample of notes: 10, 20, 50, 100, 200 and 500 ) against a given amount.
def no_notes(a):
      Q = [500, 200, 100, 50, 20, 10]
      x = 0
      for i in range(6):
          q = Q[i]
          x += int(a / q)
          a = int(a % q)
          if a > 0:
              x = -1
              return x
print(no_notes(880))
print(no_notes(1000))


#Write a Python program to create a sequence where the first four members of the sequence are equal to one, and each successive term of the sequence is equal to the sum of the four previous ones. Find the Nth member of the sequence
def new_seq(n):
    if n==1 or n==2 or n==3 or n==4:
        return 1
    return new_seq(n-1) + new_seq(n-2) + new_seq(n-3) + new_seq(n-4)
print(new_seq(5))
print(new_seq(6))
print(new_seq(7))

#Write a Python program that accept a positive number and subtract from this number the sum of its digits and so on. Continues this operation until the number is positive.
def repeat_times(n):
      s = 0
      n_str = str(n)
      while (n > 0):
          n -= sum([int(i) for i in list(n_str)])
          n_str = list(str(n))
          s += 1
          return s
print(repeat_times(9))
print(repeat_times(21))

#Write a Python program to find the number of divisors of a given integer is even or odd.
def divisor(n):
      for i in range(n):
          x = len([i for i in range(1,n+1) if not n % i])
          return x
print(divisor(15))
print(divisor(12))
print(divisor(9))
print(divisor(6))
print(divisor(3))

#Write a Python program to find the digits which are absent in a given mobile number.
def absent_digits(n):
      all_nums = set([0,1,2,3,4,5,6,7,8,9])
      n = set([int(i) for i in n])
      n = n.symmetric_difference(all_nums)
      n = sorted(n)
      return n
print(absent_digits([9,8,3,2,2,0,9,7,6,3]))


