name = input("what is you Name? ")
favorate_color = input(" what's your favorate color? ")
print(name + " likes " + favorate_color)
birth_year = input("what is your birth year? ")
age = 2024- int(birth_year)
print(age)
your_weight = input("what is your weight lbs? ")
converted_weight = float(your_weight) * 0.45
print(converted_weight)
first = "abdi"
last = "hasen"
message = first + ' '+ last + ' is a coder'
msg = f'{first} [{last}] is a coder'
print(msg)
print(message)


is_hot = True
if is_hot :
    print('wear warm cloths')
print("wear t-shirt")

price = 1000000
havegood_credit = False

if havegood_credit:
   downpayment = 0.1 * price
   print(f"down payment: ${downpayment}")
else:
  downpayment = 0.2 * price
  print(f"down payment: ${downpayment}")

have_good_income =True
has_good_credit =False
have_creminal_record =False

if have_good_income and has_good_credit :
     print("elegble for loan")

if have_good_income or has_good_credit :
      print("elegble for loan")

if have_good_income and not have_creminal_record :
     print("elegble for loan")

name = len("ab")
if name > 3 :
    print("noral ")

elif name < 3:
    print("not ormal ")


exercise

weight = int(input("weight: "))
unit = input("(L)bs or (K)g ")
if unit.upper() == "L" :
        converted = weight * 0.45
        print(f"your are {converted} Killoos")
else:
    converted = weight / 0.45
    print(f"your are {converted}  lbs")

i = 1
while i <= 10:
    print(i)
    i += 1
print("done")