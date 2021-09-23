# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Write code to assign the string "You can apply to
# SI!" to output if the string "SI 106" is in the list courses.
# If it is not in courses, assign the value "Take SI 106!" to the variable output.
courses = ["ENGR 101", "SI 110", "ENG 125", "SI 106", "CHEM 130"]
if "SI 106" in courses:
    output="You can apply to SI!"
else:
    output = "Take SI 106!"
