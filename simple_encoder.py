def menu():
  print("Menu")
  print("-------------")
  print("1. Encode")
  print("2. Decode")
  print("3. Quit")
  print()
  print()


def encode(num):
  num_list = list(num)
  for i in range(len(num_list)):
    num_list[i] = str(int(num[i]) + 3)
    return ''.join(num_list)

def decode(num):
  num_list = list(num)
  for i in range(len(num_list)):
    num_list[i] = str(int(num[i]) - 3)
    return ''.join(num_list)

def main():
  x = True
  while x is True:
    menu()
    menu_option = int(input("Please enter an option: "))
    if menu_option == 1:
      num = int(input("Please enter your password to encode: "))
      print("Your password has been encoded and stored! ")
      encode(num)

    elif menu_option == 3:
      x = False

main()










  
  
    



