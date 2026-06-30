from functions import *

def main():
    load_data()
    while True:
        option = show_menu()
        if option == 1:
            add_patient()
        elif option ==2:
            view_all_patients()
        elif option == 3:
            search_patient()
        elif option == 4:
            update_patient()
        elif option == 5:
            add_visit_note()
        elif option == 6:
            view_patient_history()
        elif option == 7:
            remove_patient()
        elif option == 8:
            total_number_patients()
        elif option == 9:
            adult_child_numbers()
        elif option == 10:
            no_visit_history()
        elif option == 11:
            search_by_symptom()
        elif option == 12:
            mark_appointment_completed()
        elif option == 13:
            save_data()
        elif option == 14:
            export_report()        
        elif option == 15:
            save_data()    # Saving data automatically 
            print("Thank you for using our Clinic Patient Management System!")
            break    
                        

main()                                         
        

             
     