class Hospital:
    total_patients = 0
    def __init__(self, name, patient_condition):
        self.name = name
        self.patient_condition = patient_condition
        Hospital.total_patients += 1
# Instance method
    def admit_patient(self):
        print(f"{self.name} admitted to the hospital with {self.patient_condition}")

# Class method
    @classmethod
    def get_total_patients(cls):
        print(f"Total patients in the hospital: {cls.total_patients}")
# Static method
    @staticmethod
    def hospital_info():
        print("This hospital provides heart speciality services.")

# Create instances of Hospital
patient1 = Hospital("Ram", "Fever")
patient2 = Hospital("Pooja", "Accident")

# Call instance method
patient1.admit_patient()
patient2.admit_patient()

# Call class method
Hospital.get_total_patients()

# Call static method
Hospital.hospital_info()
