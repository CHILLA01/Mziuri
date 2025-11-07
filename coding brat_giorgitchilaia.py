#1
def near_ten(num):
 remainder = num % 10
 return remainder <= 2 or remainder >= 8

#2
def alarm_clock(day, vacation):
    if vacation:
        if day == 0 or day == 6:
            return "off"
        else:
            return "10:00"
    else:
        if day == 0 or day == 6:
            return "10:00"
        else:
            return "7:00"

#3
def squirrel_play(temp, is_summer):
  if is_summer:
      return 60 <= temp <= 100
  else:
      return 60 <= temp <= 90

#4
def sorta_sum(a, b):
    total = a + b
    if 10 <= total <= 19:
        return 20
    return total

#5
def in1to10(n, outside_mode):
    if outside_mode:
        return n <= 1 or n >= 10
    else:
        return 1 <= n <= 10

#6
def lucky_sum(a, b, c):
    total = 0
    for i in [a, b, c]:
        if i == 13:
            break
        total += i
    return total