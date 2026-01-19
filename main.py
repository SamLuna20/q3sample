from pyscript import document, display

def check(event=None):
    selected = document.querySelector(
        '#intramuralsForm input[name="registered"]:checked'
    )

    if selected is None:
        display("Please select if you are registered.", target="output", clear=True)
    else:
        registered = selected.value
        display(f"Registered: {registered}", target="output", clear=True)

# medical = input("With medical clearance? ")
# grade = int(input("Grade level: "))
# section = input("Section: ")

# # Nested if statements for eligibility
# if registered == "yes":
#     if medical == "yes":
#         if 7 <= grade <= 10:
#             print("Congratulations! You are eligible for Intramurals.")
#             if section == 'Emerald':
#                 print("You are a member of the RED BULLDOGS!")
#             elif section == 'Ruby':
#                 print("You are a member of the GREEN HORNETS!")
#             elif section == 'Sapphire':
#                 print("You are a member of the YELLOW TIGERS!")
#             elif section == 'Topaz':
#                 print("You are a member of the BLUE BEARS!")
#             elif section == 'Jade':
#                 print("You are a member of the RED BULLDOGS!")
#         else:
#             print("Not eligible: Only Grades 7–10 may join.")
#     else:
#         print("Not eligible: Please secure a medical clearance.")
# else:
#     print("Not eligible: Please register online.")