'''
    Name: Cross-analysis model for early detection for COVID-19
    Autors: Ana Maria Campos, Diego Mauricio Sanchez
    Date: September 23, 2021
    
'''

import time

def first_diganostic_young(body_temp, hearth_rate, saturation):
    if body_temp > 36.5 and body_temp < 37.5:
        pass
        if hearth_rate > 51 and hearth_rate < 101:
            if saturation > 92 and saturation < 101:
                print("Patient (young) is stable\n")
            else:
                print("Patient (young) goes into alarm1 state\n")
        else:
            print("Patient (young) goes into alarm1 state\n")
    else:
        print("Patient (young) goes into alarm1 state\n")
        return print("** Do a new diagnostic within five minutes **\n")

def second_diagnostic_young(body_temp, hearth_rate, saturation):
    body_temp = float(input("Body Temperature\n"))
    hearth_rate = int(input("Type Hearth Rate\n"))
    saturation = float(input("Type Saturation\n"))
    if body_temp < 38:
        pass
        if hearth_rate > 150 and hearth_rate < 50:
            pass
            if saturation > 92 and saturation < 89:
                print("Patient (young) is stable\n")
            else:
                print("Patient (young) goes into alarm2 state\n")
        else:
            print("Patient (young) goes into alarm2 state\n")
    else:
        print("Patient (young) goes into alarm2 state\n")

    return print("** Do a new diagnostic within five minutes **\n")

def third_diganostic_young(body_temp, hearth_rate, saturation):
    body_temp = float(input("Body Temperature\n"))
    hearth_rate = int(input("Type Hearth Rate\n"))
    saturation = float(input("Type Saturation\n"))
    if body_temp < 38:
        pass
        if hearth_rate < 160:
            pass
            if saturation < 88 and saturation > 85:
                print("Patient (young) remains in alarm2 state\n")
            else:
                print("Patient (young) goes into alarm3 state\n")
        else:
            print("Patient (young) goes into alarm3 state\n")
    else:
        print("Patient (young) goes into alarm3 state\n")

    return print("** Do a new diagnostic within five minutes **\n")

    



def first_diganostic_adult(body_temp, hearth_rate, saturation):
    if body_temp > 36.5 and body_temp < 37.5:
        pass
        if hearth_rate > 51 and hearth_rate < 101:
            if saturation > 92 and saturation < 101:
                print("Patient (adult) is stable\n")
            else:
                print("Patient (adult) goes into alarm1 state\n")
        else:
            print("Patient (adult) goes into alarm1 state\n")

        return print("** Do a new diagnostic within five minutes **\n")

def second_diagnostic_adult(body_temp, hearth_rate, saturation):
    body_temp = float(input("Body Temperature\n"))
    hearth_rate = int(input("Type Hearth Rate\n"))
    saturation = float(input("Type Saturation\n"))
    if body_temp < 38:
        pass
        if hearth_rate > 150 and hearth_rate < 50:
            pass
            if saturation > 92 and saturation < 89:
                print("Patient (adult) is stable\n")
            else:
                print("Patient (adult) goes into alarm2 state\n")
        else:
            print("Patient (adult) goes into alarm2 state\n")
    else:
        print("Patient (adult) goes into alarm2 state\n")

    return print("** Do a new diagnostic within five minutes **\n")

def third_diganostic_adult(body_temp, hearth_rate, saturation):
    body_temp = float(input("Body Temperature\n"))
    hearth_rate = int(input("Type Hearth Rate\n"))
    saturation = float(input("Type Saturation\n"))
    if body_temp < 38:
        pass
        if hearth_rate < 160:
            pass
            if saturation < 88 and saturation > 85:
                print("Patient (adult) remains in alarm2 state\n")
            else:
                print("Patient (adult) goes into alarm3 state\n")
        else:
            print("Patient (adult) goes into alarm3 state\n")
    else:
        print("Patient (adult) goes into alarm3 state\n")

    return print("** Do a new diagnostic within five minutes **\n")


age = int(input("Type your age\n"))
body_temp = float(input("Body Temperature\n"))
hearth_rate = int(input("Type Hearth Rate\n"))
saturation = float(input("Type Saturation\n"))

#diagnostic()
if age < 18:
    first_diganostic_young(body_temp, hearth_rate, saturation)
    time.sleep(5)  # 300 seconds for 5 minutes
    second_diagnostic_young(body_temp, hearth_rate, saturation)
    time.sleep(5)  # 300 seconds for 5 minutos 
    third_diganostic_young(body_temp, hearth_rate, saturation)

elif age > 18:
    first_diganostic_adult(body_temp, hearth_rate, saturation)
    time.sleep(5)  # 300 seconds for 5 minutes
    second_diagnostic_adult(body_temp, hearth_rate, saturation)
    time.sleep(5)  # 300 seconds for 5 minutes
    third_diganostic_adult(body_temp, hearth_rate, saturation)
    time.sleep(5)  # 300 seconds for 5 minutes

else:
    print("Do a new diagnostic")