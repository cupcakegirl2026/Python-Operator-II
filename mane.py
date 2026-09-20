print("===Smart School Day Planner===")
print("Answer three quick questions and I will plan your day!")

day=input("What day is it today? (e.g. Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday): ")

print()
print("===Your Plan===")
print("-" * 30)

if day in("Monday","Tuesday","Wednesday","Thursday","Friday"):
   print("Day type: School day -> Enjoy School!")
elif day=="saturday":
   print("Day type: Saturday-> Have a great day!")
elif day=="sunday":
   print("Day type: Sunday-> Go to church")
else:
    print("Day type: Not recongnized -> Please cheack your spelling and try" ) 