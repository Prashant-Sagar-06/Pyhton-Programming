class Patient:
    def __init__(self, patient_id, name, gender, age, contact, address):
        self.__patient_id = patient_id
        self.__name = name
        self.__gender = gender
        self.__age = age
        self.__contact = contact
        self.__address = address
        
    def get_patient_info(self):
        return {
            "Patient ID": self.__patient_id,
            "Name": self.__name,
            "Gender": self.__gender,
            "Age": self.__age,
            "Contact": self.__contact,
            "Address": self.__address
        }

class Doctor:
    def __init__(self, doctor_id, name, specialization):
        self.__doctor_id = doctor_id
        self.__name = name
        self.__specialization = specialization
    
    def get_doctor_details(self):
        return {
            "Doctor ID": self.__doctor_id,
            "Doctor Name": self.__name,
            "Specialization": self.__specialization,
        }
    
class MedicalReport:
    def __init__(self):
        self.__records = {}
    
    def add_record(self, patient, doctor, diagnosis, medication): 
        patient_info = patient.get_patient_info()
        doctor_details = doctor.get_doctor_details()
        self.__records[patient_info["Patient ID"]] = {
            "Patient": patient_info,
            "Doctor": doctor_details,
            "Diagnosis": diagnosis,
            "Medication": medication
        }
    
    def get_records_by_name(self, name):
        for record_id, record_data in self.__records.items():
            if record_data["Patient"]["Name"] == name:
                print(f"ID's for the requested patient {name}:\n{record_data['Patient']}")

patient1 = Patient(1, "Shubh", "Male", 18, "+918525556689", "Mohali")
patient2 = Patient(2, "Shubhi", "Female", 18, "+918521278689", "Noida")

doctor1 = Doctor(5, "Sagar", "Heart Specialist")
doctor2 = Doctor(6, "Nikhil", "Eye Specialist")

record = MedicalReport()
record.add_record(patient1, doctor1, "Heart Problem", "Aspirin")
record.add_record(patient2, doctor2, "Myopia", "Laxobar")

name_input = input("Enter patient name: ")
record.get_records_by_name(name_input)
