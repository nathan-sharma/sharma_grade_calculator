#copy and paste this code in a python programming platform to try it out!

import sys
print("Welcome to the KISD Sharma Grade Calculator!")
def color_code_average(average):
    if average >= 90:
        color_code = "\033[32m"  # Green
    elif average >= 80:
        color_code = "\033[33m"  # Yellow
    else:
        color_code = "\033[31m"  # Red
    return color_code + str(average) + "\033[0m"
def color_code_gpa(gpa): 
    if gpa>=4:
        color_code = "\033[32m"  # Green
    elif gpa>=3: 
        color_code = "\033[33m"  # Yellow
    else: 
        color_code = "\033[31m"  # Red
    return color_code + str(gpa) + "\033[0m"
while True:
    chooser = input('Enter "semester" for semester exam calculator, "grades" for grade average calculator, or "gpa" for GPA calculator : ')
    if chooser == "semester":
        break
    elif chooser == "grades":
        majors_str = input("Enter major grade scores separated by commas or category average: ")
        minors_str = input("Enter minor grade scores separated by commas or category average: ")
        others_str = input("Enter other grade scores separated by commas or category average: ")

        def average_majors():
            majors_list = majors_str.split(",")
            majors = [float(num) for num in majors_list]
            total_majors = sum(majors)
            count_majors = len(majors)
            average_majors = total_majors / count_majors
            return average_majors

        def average_minors():
            minors_list = minors_str.split(",")
            minors = [float(num) for num in minors_list]
            total_minors = sum(minors)
            count_minors = len(minors)
            average_minors = total_minors / count_minors
            return average_minors

        def average_others():
            others_list = others_str.split(",")
            others = [float(num) for num in others_list]
            total_others = sum(others)
            count_others = len(others)
            average_others = total_others / count_others
            return average_others

        average_majors = average_majors()
        average_minors = average_minors()
        average_others = average_others()
        final_average_kap = 0.6 * average_majors + 0.3 * average_minors + 0.1 * average_others
        final_average_aca = 0.5 * average_majors + 0.35 * average_minors + 0.15 * average_others
        final_average_ap = 0.7 * average_majors + 0.2 * average_minors + 0.1 * average_others
        print("KAP average:", color_code_average(round(final_average_kap, 2)))
        print("ACA average:", color_code_average(round(final_average_aca, 2)))
        print("AP average:", color_code_average(round(final_average_ap, 2)))
        sys.exit()

    elif chooser == "gpa":
        aca_letters = {"A": 4, "B": 3, "C": 2, "D": 1}
        kap_ap_letters = {"A": 5, "B": 4, "C": 3, "D": 2}

        academic_string = input("Enter letter grades of all ACADEMIC (4.0) courses you're" + ' taking separated by commas.' + " If you're taking none," + ' type "none". Also, note that A = 90-100, B = 80-89, C = 75-79, and D = 70-74. : ')
        kap_ap_string = input("Enter letter grades of all KAP and AP courses (5.0) you're" + ' taking separated by commas.' + " If you're taking none," + ' type "none" : ')
        def calc_aca(academic_string):
            points = 0
            if academic_string != "none":
                grades = academic_string.split(",")
                for grade in grades:
                    if grade in aca_letters:
                        points += aca_letters[grade]
            return points

        aca_points = calc_aca(academic_string)

        def calc_kap_ap(kap_ap_string):
            points = 0
            if kap_ap_string != "none":
                grades = kap_ap_string.split(",")
                for grade in grades:
                    if grade in kap_ap_letters:
                        points += kap_ap_letters[grade]
            return points
        kap_points = calc_kap_ap(kap_ap_string)
        if academic_string!= "none" and kap_ap_string!= "none":
            gpa = (calc_kap_ap(kap_ap_string) + calc_aca(academic_string))/(len(academic_string.split(","))  + len(kap_ap_string.split(",")))
        elif academic_string == "none" and kap_ap_string!= "none": 
            gpa = (calc_kap_ap(kap_ap_string))/(len(kap_ap_string.split()))
        elif academic_string!= "none" and kap_ap_string == "none": 
            gpa = (calc_aca(academic_string))/(len(academic_string.split(",")))

        print("Your GPA is: ", color_code_gpa(round(gpa, 3)))
        print("KAP/AP points: " + str(kap_points))
        print("ACA points: " + str(aca_points))
        sys.exit()

def avg(a, b, c):
    return (a + b + c) / 3
#lol
sw1 = float(input("Enter your average for the first six weeks: "))
sw2 = float(input("Enter your average for the second six weeks: "))
sw3 = float(input("Enter your average for the third six weeks: "))
average = int(avg(sw1, sw2, sw3))

# calculations = 0.85(average) + 0.15x
get_an_a = 20 / 3 * (89.5 - (0.85 * average))
get_a_b = 20 / 3 * (79.5 - (0.85 * average))
to_pass = 20 / 3 * (70 - (0.85 * average))
skibidi_toilet = 0.85 * average + 15

if get_an_a > 100:
    print("\033[31mYour average is guaranteed to be lower than an A.\033[0m")
elif get_an_a <= 0:
    print("\033[32mYou are guaranteed to get an A for this semester.\033[0m")
else:
    print("\033[33mTo get an A for the semester, you need a(n) " + str(round(get_an_a, 2)) + " or higher on the final.\033[0m")

if get_a_b > 100:
    print("\033[31mYour average is guaranteed to be lower than a B.\033[0m")
elif get_a_b <= 0:
    print("\033[32mYour average is guaranteed to be a B or higher.\033[0m")
else:
    print("\033[33mTo get a B for the semester, you need a(n) " + str(round(get_a_b, 2)) + " or higher on the final.\033[0m")

if to_pass > 100:
    print("\033[31mYou are guaranteed to fail for this semester. In the best case scenario, your average would be a(n) " + str(round(skibidi_toilet, 2)) + ".\033[0m")
elif to_pass <= 0:
    print("\033[32mYour average is guaranteed to be a C or higher.\033[0m")
else:
    print("\033[33mTo pass, you need a(n) " + str(round(to_pass, 2)) + " or higher on the final.\033[0m")
