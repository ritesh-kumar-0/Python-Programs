#Nested-if

age = 18
has_id = True

if age >= 18:
    print("You are an adult")

    if has_id:
        print("You can appear in the exam.")
    else:
        print("You must bring your id card.")
else:
    print("You are too young to appear")