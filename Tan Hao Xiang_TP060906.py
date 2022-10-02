from os import cpu_count


#show menu
def menu():
    while True:
        print("\nWelcome to the vaccination registration and administration system!") 
        print("""
        
            New Patient Registration                  : Enter 1
            Vaccine administration                    : Enter 2
            Patient record and Vaccination status     : Enter 3
            Statistical information                   : Enter 4
            Exit                                      : Enter Q

        """)

        user_action = input("Select the action you would like to proceed by typing number above: ")

        
        if user_action == "1" :
            new_patient_registration()
                
                

        elif user_action == "2" :
            vaccine_administration()
                
            
        elif user_action == "3" :
            patient_record()
                
                
                
        elif user_action == "4" :
            statistical_information()
            
                
            
        elif user_action == "q" or user_action == "Q" :
            break


        else:
            print("Invalid, please type again")




#generate patients id for vaccination
def id():
    try:
        total = 0
        with open("patients.txt", "r") as f:
            total = sum(1 for _ in f)
            count = total + 1
            return count
    
    except:
        count = 1
        return count



#register new patient
def new_patient_registration():
    print("\nSelect the vaccination centre\n\tVaccination Centre 1: Enter VC1\n\tVaccination Centre 2: Enter VC2")
    #prompt vaccination centre
    vaccination_centre = input("\nSelect the vaccination centre by typing VC1 or VC2: ")
    #prompt patient name
    name = input("\nEnter your name: ")
    #prompt patient age
    age = int(input("\nEnter your age: "))
    #prompt patient contact number
    contact_number = input("\nEnter your contact number: ")
    #prompt patient email address
    email_address = input("\nEnter your email address: ")
    #get patient id
    patient_id = id()

    #set registration date to today
    import datetime
    registration_date = datetime.date.today()

    #show vaccination type based on age group

    if age < 12:
        print("You are not eligible for vaccination")
        menu()

    #vaccination type for under 18
    elif age < 18:
        print("\nYou are eligible for these vaccines:")
        #show vaccine type for selection
        print("""
        Please select one vaccine you prefer (by typing the vaccine code):
        Vaccine code            Dosage required         Interval between doses
        AF                       2                       2 weeks (14 days)
        BV                       2                       3 weeks (21 days)
        DM                       2                       4 weeks (28 days)

        """)
        
        vaccine_selection = input("Enter the vaccine code: ")
        add_patient(patient_id, name, age, contact_number, email_address, vaccination_centre, vaccine_selection, registration_date)
        print("The record has been saved")
        

    #vaccination type for age group from 18 to 45  
    elif age >= 18 and age <= 45:
        print("\nYou are eligible for these vaccines")
        print("""
        Please select one vaccine you prefer (by typing the vaccine code):
        Vaccine code            Dosage required         Interval between doses
        AF                       2                       2 weeks (14 days)
        BV                       2                       3 weeks (21 days)
        CZ                       2                       3 weeks (21 days)
        DM                       2                       3 weeks (21 days)
        EC                       1                       -----------------



        
        """)
        vaccine_selection = input("Enter the vaccine code: ")
        add_patient(patient_id, name, age, contact_number, email_address, vaccination_centre, vaccine_selection, registration_date)
        print("The record has been saved")
        



    #vaccination type for age group over 45
    else:
        print("\nYou are eligible for these vaccines")
        print("""
        Please select one vaccine you prefer (#by typing the vaccine code):
        Vaccine code            Dosage required         Interval between doses
        AF                       2                       2 weeks (14 days)
        BV                       2                       3 weeks (21 days)
        DM                       2                       3 weeks (21 days)
        EC                       1                       -----------------
        """)   
        
        vaccine_selection = input("Enter the vaccine code: ")
        add_patient(patient_id, name, age, contact_number, email_address, vaccination_centre, vaccine_selection, registration_date)
        print("The record has been saved")

    return new_patient_registration   
 

#save patient information into txt file
def add_patient(patient_id, name, age, contact_number, email_address, vaccination_centre, vaccine_selection, registration_date): #patient_id

    data =[]  
    patient_data_information = []
    patient_data_information.append(patient_id)
    patient_data_information.append(name)
    patient_data_information.append(age)
    patient_data_information.append(contact_number)
    patient_data_information.append(email_address)
    patient_data_information.append(vaccination_centre)
    patient_data_information.append(vaccine_selection)
    patient_data_information.append(registration_date)
    data.append(patient_data_information)
    vaccine = []
    vaccination_information = []
    vaccination_information.append(patient_id)
    vaccination_information.append(vaccine_selection)
    vaccination_information.append(registration_date)
    vaccine.append(vaccination_information)

    with open("patients.txt", "a+" ) as f:
        for patient_data_information in data:
            for line in patient_data_information:
                f.write(str(line))
                f.write("\t")
            f.write("\n")
        
        print("Registered" ,name, "with", vaccine_selection)

    with open("vaccination.txt", "a+" ) as f:
        for vaccination_information in vaccine:
            for line in vaccination_information:
                f.write(str(line))
                f.write("\t")
            f.write("\n")
    
    



def patient_record():
    patientId = int(input('Enter the patient id: '))
    x = patientId - 1


    #write vaccination status of the patient to the text file
    def vaccination_status():

        with open('patients.txt', 'r') as txtfile:
            lines = txtfile.readlines()

        writetoendofline(lines, patientId - 1, "\t" + status)

        with open('patients.txt', 'w') as txtfile:
            txtfile.writelines(lines)


    #get second dose date
    import datetime
    system_date = datetime.date.today()
    first_dose_date = datetime.date(2021, 9, 1)

    second_dose_date = second_dose()
    #get patient status
    if system_date < first_dose_date:
        status = "new"
        print("Vaccination status is", status)
        vaccination_status()
        
    elif system_date >= first_dose_date:
        status = "Completed-D1"
        print("Vaccination status is", status)
        vaccination_status()
        
    elif system_date >= second_dose_date:
        status = "Completed"
        print("Vaccination status is", status)
        vaccination_status()

       
    else:
        status = "Completed"
        print("Vaccination status is", status)
        vaccination_status()

    #print patient information by prompting patient id    
    with open('patients.txt', 'r') as f:
        lines = f.readlines()
    
        print(lines[x])


    return patient_record




def second_dose():

    #find second dose date
    vaccine_selection = input("Enter your vaccine selection: ")
    import datetime
    first_dose_date = datetime.date(2021, 9, 1)

    if (vaccine_selection == "AF") or (vaccine_selection == "af") :
        second_dose_date = first_dose_date + datetime.timedelta(14)
        return second_dose_date

    elif (vaccine_selection == "BV") or (vaccine_selection == "bv") or (vaccine_selection == "CZ") or (vaccine_selection == "cz"):
        second_dose_date = first_dose_date + datetime.timedelta(21)        
        return second_dose_date
        
    
    elif (vaccine_selection == "DM") or (vaccine_selection == "dm"):
        second_dose_date = first_dose_date + datetime.timedelta(28)
        return second_dose_date
        
    else:
        second_dose_date = "No second dose"
        return second_dose_date



#show pending vaccination date  
def vaccine_administration():

    import datetime
    first_dose_date = datetime.date(2021, 9, 1)
    second_dose_date = second_dose()
    dose_number = input("Enter your pending vaccination dose number(D1,D2): ")
    if dose_number == "D1":
        print("Please come to get your dose 1 on", first_dose_date)
    elif dose_number == "D2":
        print("Please come to get your dose 2 on", second_dose_date)
    else:
        print("You have finished vaccination")
    return vaccine_administration




#function for write to the end of line in text file
def writetoendofline(lines, line_no, append_txt):
    lines[line_no] = lines[line_no].replace('\n', '') + append_txt + '\n'



#show statistical information based on vaccination centre
def statistical_information():
    with open("patients.txt", "r") as f:
        count = 0
        for line in f:
            if "VC1" in line:
                count = count + 1

    with open("patients.txt", "r") as f1:
        cnt = 0
        for line1 in f1:
            if "VC2" in line1:
                cnt = cnt + 1
    
    with open("patients.txt", "r") as f2:
        cnt1 = 0
        for line2 in f2:
            if "VC1" and "Completed-D1" in line2:
                cnt1 = cnt1 + 1

    with open("patients.txt", "r") as f3:
        cnt2 = 0
        for line2 in f3:
            if "VC1" and "Completed" in line2:
                cnt2 = cnt2 + 1

    with open("patients.txt", "r") as f4:
        cnt3 = 0
        for line3 in f4:
            if "VC2" and "Completed-D1" in line3:
                cnt3 = cnt3 + 1

    with open("patients.txt", "r") as f5:
        cnt4 = 0
        for line4 in f5:
            if "VC2" and "Completed" in line4:
                cnt4 = cnt4 + 1

    print("\nTotal patients of vaccinated in VC1 :", count)    #print total patients in vc1
    print("Total patients waiting for dose 2 in VC1 :", cnt1)  #print total patients waiting for dose 2 in vc1
    print("Total patients completed vaccination in VC1 :", cnt2)   #print total patients completed vaccination in vc1
    print("Total patients of vaccinated in VC2 :", cnt)   #print total patients in vc2
    print("Total patients waiting for dose 2 in VC2 :", cnt3)   #print total patients waiting for dose 2 in vc2
    print("Total patients completed vaccination in VC2 :", cnt4) #print total patients completed vaccination in vc2
    return statistical_information

menu()









