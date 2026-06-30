import json
patients = []

#   INPUT VALIDATION
def get_valid_input(prompt):
    while True:
        value = input(prompt)
        if not value:
            print("This field cannot be empty!")
        else:
            return value
        
#   SHOWING THE MENU
def show_menu(): 
    print("\nWelcome to the Clinic Patient Management System\n")
    print("1. Add New Patient\n2. View All Patients\n3. Search Patient\n4. Update Patient Info\n5. Add Visit Note\n6. View Patient History\n7. Delete Patient\n8. Total Number of Patients\n9. Adults vs Child Count\n10. View Patients with No History\n11. Search by Symptom\n12. Mark Appointment Completed\n13. Save Data\n14. Make a Simple Report\n15. EXIT")
    while True:
        try:
            option = int(input("\nCould you please choose an option: "))
            if 1 <= option <= 15:
                return option
            else:
                print("Please chose a valid option from 1 to 15!")
        except ValueError:
            print("Please chose a valid option from 1 to 15!")


    

#   ADDING PATIENTS
def add_patient():
        name = get_valid_input("Enter the patient's name: ")  
        while True:
            try:
                age = int(get_valid_input("Enter patient's age: "))
                if age > 0:
                    break
                else:
                    print("Please enter a valid age (greater than Zero)!")
            except ValueError:
                print("Please enter a valid age (greater than Zero)!")
        phone = get_valid_input("Enter patient's phone number: ")
        symptoms = get_valid_input("If the patient has any symptoms, please add them as well, type none if the patient doesn't have any symptoms: ")
        date = get_valid_input("Enter the appointment date: ")
        patient = {
            "id": len(patients) + 1,
            "name": name,
            "age": age,
            "phone": phone,
            "symptoms": symptoms,
            "date": date,
            "visits": [],
            "status": "pending"    
            }
        patients.append(patient)
        print("\nPatient added successfully!\n")


# VIEWING ALL PATIENTS
def view_all_patients():
        if len(patients) == 0:
            print("\nNo patients found!\n")
            return
        sorting_key = get_valid_input("How do you want to view patients?\n1. By ID\n2. By name\n")
        if sorting_key == "1":
            for patient in patients:
                print(f"ID: {patient['id']}")
                print(f"Name: {patient['name']}")
                print(f"Age: {patient['age']}")
                print(f"Phone: {patient['phone']}")
                print(f"Symptoms: {patient['symptoms']}")
                print("---------------------------------")
        if sorting_key == "2":
            sorted_patients = sorted(patients, key=lambda p: p["name"])
            for patient in sorted_patients:
                print(f"Name: {patient['name']}")
                print(f"ID: {patient['id']}")
                print(f"Age: {patient['age']}")
                print(f"Phone: {patient['phone']}")
                print(f"Symptoms: {patient['symptoms']}")
                print("---------------------------------")


#   SEARCH FOR A PATIENT
def search_patient():
    search_key = get_valid_input("Enter patient name or ID you are searching for: ")
    found = False
    for patient in patients:
        if search_key.lower() in patient["name"].lower() or search_key == str(patient["id"]):
            print(f"ID: {patient['id']}")
            print(f"Name: {patient['name']}")
            print(f"Age: {patient['age']}")
            print(f"Phone: {patient['phone']}")
            print(f"Symptoms: {patient['symptoms']}")
            found = True
            break
    if not found:
        print("Patient not found!")


#   UPDATE PATIENT INFO
def update_patient():
    found = False
    search_key2 = get_valid_input("Enter patient's name or ID you want to edit his/her info: ")
    for patient in patients:
        if search_key2.lower() in patient["name"].lower() or search_key2 == str(patient["id"]):
            found = True
            print("What do you want to update?\n1. Name\n2. Age\n3. Phone\n4. Symptoms")
            search_key3 = get_valid_input("Chose an option: ")
            if search_key3 == "1":
                updated_name = get_valid_input("Enter the new name: ")
                patient['name'] = updated_name
            if search_key3 == "2":
                updated_age = get_valid_input("Enter the new age: ")
                patient['age'] = updated_age
            if search_key3 == "3":
                updated_phone = get_valid_input("Enter the new phone number: ")
                patient['phone'] = updated_phone
            if search_key3 == "4":
                updated_symptoms = get_valid_input("Enter the new symptoms separated by a comma: ")
                patient['symptoms'] = updated_symptoms
            print("Patient updated successfully!")
            break
    if not found:
        print("Patient not found!")


#   VIEW PATIENT HISTOTY
def view_patient_history():
    found = False
    search_key = get_valid_input("Enter patient's name or ID you want to view his/her history: ")   
    for patient in patients:
        if search_key.lower() in patient["name"].lower() or search_key == str(patient["id"]):
            found = True
            print(f"Name: {patient['name']}")
            print("\n")
            if not patient["visits"]:
                print(f"No visit history found for {patient['name']}!")
            else:
                for visit in patient["visits"]:
                    print(f"Date: {visit['date']}")
                    print(f"Doctor: {visit['doctor']}")
                    print(f"Notes: {visit['note']}")
                    print(f"Advices: {visit['advice']}")
            break
    if not found:
        print("Patient not found!")

#   TOTAL NUMBER OF PATIENTS
def total_number_patients():
    print(f"The total number of patients is {len(patients)}")


#   ADULTS & CHILDREN NUMBERS
def adult_child_numbers():
    adults = 0
    children = 0
    for patient in patients:
        if patient["age"] >= 18:
            adults += 1
        else:
            children += 1
    print(f"           The total number of adults patients is {adults} and the total number of children is {children}")            
                

#   SHOWING PATIENTS WITHOUT VISIT HISTORY
def no_visit_history():
    for patient in patients:
        if not patient["visits"]:
            print("          The following patient doesn't have any visit history so far!\n")
            print(f"Name: {patient['name']}")
            print(f"ID: {patient['id']}")
            print("---------------------------------")



#   REMOVING A SPECIFIC PATIENT
def remove_patient():
    search_key = get_valid_input("Enter patient name or ID you you need to remove: ")
    found = False
    for patient in patients:
        if search_key.lower() in patient["name"].lower() or search_key == str(patient["id"]):
            confirmation = get_valid_input(f"Are you sure you want to delete {patient['id']}'s info? (yes/no): ")
            if confirmation.lower() == "yes":
                patients.remove(patient)
                found = True
                print("Patient removed successfully!")
                break
            else:
                print("Deletion cancelled!")    
    if not found:
        print("Patient not found!")


#   SEARCHING BY SYMPTOMS
def search_by_symptom():
    symptom = get_valid_input("Enter symptom to search for: ")
    found = False
    for patient in patients:
        if symptom.lower() in patient["symptoms"].lower():
            print(f"ID: {patient['id']}")
            print(f"Name: {patient['name']}")
            print(f"Age: {patient['age']}")
            print(f"Phone: {patient['phone']}")
            print(f"Symptoms: {patient['symptoms']}")
            print("---------------------------------")
            found = True
    if not found:
        print("No patients found with this symptom!")        




#   ADDING VISIT NOTES
def add_visit_note():
    found = False
    search_key = get_valid_input("Enter patient's name or ID you wish to add visit note for: ") 
    for patient in patients:
        if search_key.lower() in patient["name"].lower() or search_key == str(patient["id"]):
            found = True
            print(f"You will add note for {patient['name']}")
            visit_date = get_valid_input("Enter visit date (dd-mm-yyyy): ")
            dr_name = get_valid_input("Enter doctor name: ")
            visit_note = get_valid_input("Enter visit notes: ")
            advices = get_valid_input("Enter prescription/advice: ")

            visit = {
                "date": visit_date,
                "doctor": dr_name,
                "note": visit_note,
                "advice": advices,
            }
            patient["visits"].append(visit)
            print("Visit note added successfully!")
            break
    if not found:
        print("Patient not found!")



#   MARKING APPOINTMENT COMPLETED
def mark_appointment_completed():
    search_key = get_valid_input("Enter patient name or ID you you need to remove: ")
    found = False
    for patient in patients:
        if search_key.lower() in patient["name"].lower() or search_key == str(patient["id"]):
            found = True
            if len(patient["visits"]) > 0:
                if patient["status"] == "Completed":
                    print("Appointment already completed!")
                else:
                    patient["status"] = "Completed"
                    print("Appointment marked as completed!")
            else:
                print("This patient has no visits yet!")        
    if not found:
        print("Patient not found!")
           


#   EXPORTING A SIMPLE REPORT TO A TEXT FILE
def export_report():
    with open("report.txt", "w") as file:
        file.write(f"Total patients: {len(patients)}\n")
        file.write("====================\n")
        for patient in patients:
            file.write(f"ID: {patient['id']}\n")
            file.write(f"Name: {patient['name']}\n")
            file.write(f"Age: {patient['age']}\n")
            file.write("---------------------\n")
    print("Report exported successfully to report.txt!")        


#   SAVING THE DATA
def save_data():
    with open("patients.json", "w") as file:
        json.dump(patients, file)
    print("Data saved successfully!")


#   LOADING THE DATA
def load_data():
    global patients
    try:
        with open("patients.json", "r") as file:
            patients = json.load(file)
    except:
        print("No saved data found. The program starts with an empty system!") 