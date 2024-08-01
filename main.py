try:
  num = int(input(": "))
  addition = 0
  about_to = 0
  list_binary = [128, 64, 32, 16, 8, 4, 2, 1]
  answer = ""
  for x in range(len(list_binary)):
    about_to = addition
    about_to += list_binary[x]
    if about_to > num:
      answer+="0"
    else:
      addition+=list_binary[x]
    list_binary.remove(x)
  print(answer)
  
except:
  print("No don't try to break my program :(")
