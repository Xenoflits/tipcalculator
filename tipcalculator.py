bill = int(input("How much is the bill?\n"))
tip = int(input("How much tip you want to give in %?"))
people = int(input("How many people you want to split the bill with?"))
total = bill + bill * (tip / 100)
total_per_person = total / people
print(f"Each person will have to pay € {total_per_person:.2f}")