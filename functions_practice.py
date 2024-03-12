def hello():
    print("Hello!")
hello()


def pack(x, y, z):
    return([x, y, z])
print(pack('x', 'y', 'z'))
print(pack(1,2,3))

def eat_lunch(my_lst):
  if len(my_lst) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(my_lst)):
      if i == 0:
        print(f"First I eat {my_lst[0]}")
      else:
        print(f"Next I eat {my_lst[i]}")

eat_lunch()
eat_lunch(["steak","fries","cake"])