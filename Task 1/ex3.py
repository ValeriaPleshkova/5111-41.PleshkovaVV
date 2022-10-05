vowels = "a o u i e"
symbol = input ()

if vowels.upper().__contains__(symbol.upper()):
   print("гласная")
elif symbol=='Y':
   print("гласная и согласная")
else:
   print("согласная")