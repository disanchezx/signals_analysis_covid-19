'''
    Name: Cross-analysis model for early detection for COVID-19
    Autors: Ana Maria Campos, Diego Mauricio Sanchez
    Date: September 23, 2021
    
'''

import time     # Time library, delays
# -------------------------------------------------------------------------
# Infant Diagnostic Functions

def first_diganostic_infant(body_temp, hearth_rate, saturation):
    if body_temp > 37.5 and body_temp < 38:             # If the Body Temperature is out of range, then read the following variable
        pass
        if hearth_rate > 100 and hearth_rate < 130:         # If the Hearth Rate is out of range, then read the following variable
            pass
            if saturation > 92 and saturation < 101:            # If the Saturation is out of range, then read the following variable
                print("Patient (infant) is stable\n")              # if all variables are in the range, the individual is classified as "stable".
            # If any variable is not in the range, the patient's classification is printed and the variable to be taken into account is detailed.
            else:
                print("Patient (infant) goes into alarm1 state (Diagnostic: Oxygen Saturation out of range)\n")
        else:
            print("Patient (infant) goes into alarm1 state (Diagnostic: Hearth Rate out of range)\n")
    else:
        print("Patient (infant) goes into alarm1 state (Diagnostic: High temperature)\n")

        # There is a waiting time between each diagnosis
        return print("** Do a new diagnostic within five minutes **\n")

def second_diagnostic_infant(body_temp, hearth_rate, saturation):
    body_temp = float(input("Body Temperature\n"))
    hearth_rate = int(input("Type Hearth Rate\n"))
    saturation = float(input("Type Saturation\n"))
    if body_temp < 38:
        pass
        if hearth_rate > 100 and hearth_rate < 140:
            pass
            if saturation > 92 and saturation < 100:
                print("Patient (infant) is stable\n")
            else:
                print("Patient (infant) goes into alarm2 state (Diagnostic: Oxygen Saturation out of range)\n")
        else:
            print("Patient (infant) goes into alarm2 state (Diagnostic: Hearth Rate out of range)\n")
    else: 
        print("Patient (infant) goes into alarm2 state (Diagnostic: High temperature)\n")

    return print("** Do a new diagnostic within five minutes **\n")

def third_diganostic_infant(body_temp, hearth_rate, saturation):
    body_temp = float(input("Body Temperature\n"))
    hearth_rate = int(input("Type Hearth Rate\n"))
    saturation = float(input("Type Saturation\n"))
    if body_temp < 38:
        pass
        if hearth_rate < 140:
            pass
            if saturation < 88 and saturation > 85:
                print("Patient (infant) remains in alarm2 state\n")
            else:
                print("Patient (infant) goes into alarm3 state (Diagnostic: Oxygen Saturation out of range)\n")
        else:
            print("Patient (infant) goes into alarm3 state (Diagnostic: Hearth Rate out of range)\n")
    else:
        print("Patient (infant) goes into alarm3 state (Diagnostic: High temperature)\n")

    return print("** Do a new diagnostic within five minutes **\n")

# ------------------------------------------------------------------------------
# Preschool Child Diacnostic Function

def first_diganostic_preschool_child(body_temp, hearth_rate, saturation):
    if body_temp > 37.5 and body_temp < 38:
        pass
        if hearth_rate > 79 and hearth_rate < 120:
            pass
            if saturation > 92 and saturation < 101:
                print("Patient (preschool child) is stable\n")
            else:
                print("Patient (preschool child) goes into alarm1 state (Diagnostic: Oxygen Saturation out of range)\n")
        else:
            print("Patient (preschool child) goes into alarm1 state (Diagnostic: Hearth Rate out of range)\n")
    else:
        print("Patient (preschool child) goes into alarm1 state (Diagnostic: High temperature)\n")

        return print("** Do a new diagnostic within five minutes **\n")
    

def second_diagnostic_preschool_child(body_temp, hearth_rate, saturation):
    body_temp = float(input("Body Temperature\n"))
    hearth_rate = int(input("Type Hearth Rate\n"))
    saturation = float(input("Type Saturation\n"))
    if body_temp > 37.5 and body_temp < 38:
        pass
        if hearth_rate > 79 and hearth_rate < 120:
            pass
            if saturation > 92 and saturation < 101:
                print("Patient (preschool child) is stable\n")
            else:
                print("Patient (preschool child) goes into alarm2 state (Diagnostic: Oxygen Saturation out of range)\n")
        else:
            print("Patient (preschool child) goes into alarm2 state (Diagnostic: Hearth Rate out of range)\n")
    else:
        print("Patient (preschool child) goes into alarm2 state (Diagnostic: High temperature)\n")

    return print("** Do a new diagnostic within five minutes **\n")

def third_diganostic_preschool_child(body_temp, hearth_rate, saturation):
    body_temp = float(input("Body Temperature\n"))
    hearth_rate = int(input("Type Hearth Rate\n"))
    saturation = float(input("Type Saturation\n"))
    if body_temp > 37.5 and body_temp < 38:
        pass
        if hearth_rate > 79 and hearth_rate < 120:
            pass
            if saturation > 92 and saturation < 101:
                print("Patient (preschool child) remains in alarm2 state\n")
            else:
                print("Patient (preschool child) goes into alarm3 state (Diagnostic: Oxygen Saturation out of range)\n")
        else:
            print("Patient (preschool child) goes into alarm3 state (Diagnostic: Hearth Rate out of range\n")
    else:
        print("Patient (preschool child) goes into alarm3 state (Diagnostic: High temperature)\n")

    return print("** Do a new diagnostic within five minutes **\n")

# ----------------------------------------------------------------------------------
# Child Diagnostic Function

def first_diganostic_child(body_temp, hearth_rate, saturation):
    if body_temp > 37 and body_temp < 37.5:
        pass
        if hearth_rate > 79 and hearth_rate < 101:
            pass
            if saturation > 92 and saturation < 101:
                print("Patient (child) is stable\n")
            else:
                print("Patient (child) goes into alarm1 state (Diagnostic: Oxygen Saturation out of range)\n")
        else:
            print("Patient (child) goes into alarm1 state (Diagnostic: Hearth Rate out of range\n")
    else:
        print("Patient (child) goes into alarm1 state (Diagnostic: High temperature)\n")

        return print("** Do a new diagnostic within five minutes **\n")

def second_diagnostic_child(body_temp, hearth_rate, saturation):
    body_temp = float(input("Body Temperature\n"))
    hearth_rate = int(input("Type Hearth Rate\n"))
    saturation = float(input("Type Saturation\n"))
    if body_temp > 37 and body_temp < 37.5:
        pass
        if hearth_rate > 79 and hearth_rate < 101:
            pass
            if saturation > 92 and saturation < 101:
                print("Patient (child) is stable\n")
            else:
                print("Patient (child) goes into alarm2 state (Diagnostic: Oxygen Saturation out of range)\n")
        else:
            print("Patient (child) goes into alarm2 state (Diagnostic: Hearth Rate out of range\n")
    else:
        print("Patient (child) goes into alarm2 state (Diagnostic: High temperature)\n")

    return print("** Do a new diagnostic within five minutes **\n")

def third_diganostic_child(body_temp, hearth_rate, saturation):
    body_temp = float(input("Body Temperature\n"))
    hearth_rate = int(input("Type Hearth Rate\n"))
    saturation = float(input("Type Saturation\n"))
    if body_temp > 37 and body_temp < 37.5:
        pass
        if hearth_rate > 79 and hearth_rate < 101:
            pass
            if saturation > 92 and saturation < 101:
                print("Patient (child) remains in alarm2 state\n")
            else:
                print("Patient (child) goes into alarm3 state (Diagnostic: Oxygen Saturation out of range)\n")
        else:
            print("Patient (child) goes into alarm3 state (Diagnostic: Hearth Rate out of range\n")
    else:
        print("Patient (child) goes into alarm3 state (Diagnostic: High temperature)\n")

    return print("** Do a new diagnostic within five minutes **\n")
# -------------------------------------------------------------------------------------
# Adolescent Diagnostic Functions

def first_diganostic_adolescent(body_temp, hearth_rate, saturation):
    if body_temp > 36.5 and body_temp < 37.5:
        pass
        if hearth_rate > 51 and hearth_rate < 101:
            pass
            if saturation > 94 and saturation < 101:
                print("Patient (adolescent) is stable\n")
            else:
                print("Patient (adolescent) goes into alarm1 state (Diagnostic: Oxygen Saturation out of range)\n")
        else:
            print("Patient (adolescent) goes into alarm1 state (Diagnostic: Hearth Rate out of range\n")
    else:
        print("Patient (adolescent) goes into alarm1 state (Diagnostic: High temperature)\n")

        return print("** Do a new diagnostic within five minutes **\n")

def second_diagnostic_adolescent(body_temp, hearth_rate, saturation):
    body_temp = float(input("Body Temperature\n"))
    hearth_rate = int(input("Type Hearth Rate\n"))
    saturation = float(input("Type Saturation\n"))
    if body_temp > 36.5 and body_temp < 37.5:
        pass
        if hearth_rate > 51 and hearth_rate < 101:
            pass
            if saturation > 94 and saturation < 101:
                print("Patient (adolescent) is stable\n")
            else:
                print("Patient (adolescent) goes into alarm2 state (Diagnostic: Oxygen Saturation out of range)\n")
        else:
            print("Patient (adolescent) goes into alarm2 state (Diagnostic: Hearth Rate out of range\n")
    else:
        print("Patient (adolescent) goes into alarm2 state (Diagnostic: High temperature)\n")

    return print("** Do a new diagnostic within five minutes **\n")

def third_diganostic_adolescent(body_temp, hearth_rate, saturation):
    body_temp = float(input("Body Temperature\n"))
    hearth_rate = int(input("Type Hearth Rate\n"))
    saturation = float(input("Type Saturation\n"))
    if body_temp > 36.5 and body_temp < 37.5:
        pass
        if hearth_rate > 51 and hearth_rate < 101:
            pass
            if saturation > 94 and saturation < 101:
                print("Patient (adolescent) remains in alarm2 state\n")
            else:
                print("Patient (adolescent) goes into alarm3 state (Diagnostic: Oxygen Saturation out of range)\n")
        else:
            print("Patient (adolescent) goes into alarm3 state (Diagnostic: Hearth Rate out of range\n")
    else:
        print("Patient (adolescent) goes into alarm3 state (Diagnostic: High temperature)\n")

    return print("** Do a new diagnostic within five minutes **\n")
# -------------------------------------------------------------------------------------------
# Adult diagnostic Functions

def first_diganostic_adult(body_temp, hearth_rate, saturation):
    if body_temp > 36.2 and body_temp < 37.2: 
        pass
        if hearth_rate > 59 and hearth_rate < 81:
            pass
            if saturation > 94 and saturation < 101:
                print("Patient (adult) is stable\n")
            else:
                print("Patient (adult) goes into alarm1 state (Diagnostic: Oxygen Saturation out of range)\n")
        else:
            print("Patient (adult) goes into alarm1 state (Diagnostic: Hearth Rate out of range\n")
    else:
        print("Patient (adult) goes into alarm1 state (Diagnostic: High temperature)\n")

    return print("** Do a new diagnostic within five minutes **\n")

def second_diagnostic_adult(body_temp, hearth_rate, saturation):
    body_temp = float(input("Body Temperature\n"))
    hearth_rate = int(input("Type Hearth Rate\n"))
    saturation = float(input("Type Saturation\n"))
    if body_temp > 36.2 and body_temp < 37.2:
        pass
        if hearth_rate > 59 and hearth_rate < 81:
            pass
            if saturation > 94 and saturation < 101:
                print("Patient (adult) is stable\n")
            else:
                print("Patient (adult) goes into alarm2 state (Diagnostic: Oxygen Saturation out of range)\n")
        else:
            print("Patient (adult) goes into alarm2 state (Diagnostic: Hearth Rate out of range\n")
    else:
        print("Patient (adult) goes into alarm2 state (Diagnostic: High temperature)\n")

    return print("** Do a new diagnostic within five minutes **\n")

def third_diganostic_adult(body_temp, hearth_rate, saturation):
    body_temp = float(input("Body Temperature\n"))
    hearth_rate = int(input("Type Hearth Rate\n"))
    saturation = float(input("Type Saturation\n"))
    if body_temp > 36.2 and body_temp < 37.2:
        pass
        if hearth_rate > 59 and hearth_rate < 81:
            pass
            if saturation > 94 and saturation < 101:
                print("Patient (adult) remains in alarm2 state\n")
            else:
                print("Patient (adult) goes into alarm3 state (Diagnostic: Oxygen Saturation out of range)\n")
        else:
            print("Patient (adult) goes into alarm3 state (Diagnostic: Hearth Rate out of range\n")
    else:
        print("Patient (adult) goes into alarm3 state (Diagnostic: High temperature)\n")

    return print("** Do a new diagnostic within five minutes **\n")
# -----------------------------------------------------------------------------------------------

age = int(input("Type your age\n"))
body_temp = float(input("Body Temperature\n"))
hearth_rate = int(input("Type Hearth Rate\n"))
saturation = float(input("Type Saturation\n"))

if age == 0 or age < 2:
    first_diganostic_infant(body_temp, hearth_rate, saturation)
    time.sleep(5)  # 300 seconds for 5 minutes
    second_diagnostic_infant(body_temp, hearth_rate, saturation)
    time.sleep(5)  # 300 seconds for 5 minutes
    third_diganostic_infant(body_temp, hearth_rate, saturation)

elif age == 2 or age < 6:
    first_diganostic_preschool_child(body_temp, hearth_rate, saturation)
    time.sleep(5)  # 300 seconds for 5 minutes
    second_diagnostic_preschool_child(body_temp, hearth_rate, saturation)
    time.sleep(5)  # 300 seconds for 5 minutes
    third_diganostic_preschool_child(body_temp, hearth_rate, saturation)
    time.sleep(5)  # 300 seconds for 5 minutes

elif age == 6 or age < 13:
    first_diganostic_child(body_temp, hearth_rate, saturation)
    time.sleep(5)  # 300 seconds for 5 minutes
    second_diagnostic_child(body_temp, hearth_rate, saturation)
    time.sleep(5)  # 300 seconds for 5 minutes
    third_diganostic_child(body_temp, hearth_rate, saturation)
    time.sleep(5)  # 300 seconds for 5 minutes

elif age == 13 or age < 16:
    first_diganostic_adolescent(body_temp, hearth_rate, saturation)
    time.sleep(5)  # 300 seconds for 5 minutes
    second_diagnostic_adolescent(body_temp, hearth_rate, saturation)
    time.sleep(5)  # 300 seconds for 5 minutes
    third_diganostic_adolescent(body_temp, hearth_rate, saturation)
    time.sleep(5)  # 300 seconds for 5 minutes

elif age == 16 or age > 15:
    first_diganostic_adult(body_temp, hearth_rate, saturation)
    time.sleep(5)  # 300 seconds for 5 minutes
    second_diagnostic_adult(body_temp, hearth_rate, saturation)
    time.sleep(5)  # 300 seconds for 5 minutes
    third_diganostic_adult(body_temp, hearth_rate, saturation)
    time.sleep(5)  # 300 seconds for 5 minutes
