# imports

import pandas as pd
from faker.proxy import Faker

# tables schema

hospitals = pd.DataFrame(
    columns=["hospital_id", "hospital_name", "location", "country"]
)
patients = pd.DataFrame(
    columns=["patient_id", "patient_name", "gender", "date_of_birth", "country"]
)
diseases = pd.DataFrame(columns=["disease_id", "disease_name"])
visits = pd.DataFrame(
    columns=["visit_id", "patient_id", "hospital_id", "date_of_visit", "cost"]
)
prescriptions = pd.DataFrame(
    columns=[
        "prescription_id",
        "visit_id",
        "date_of_prescription",
        "medicine_id",
        "disease_id",
        "dosage",
    ]
)
medicine = pd.DataFrame(
    columns=["medicine_id", "medicine_name", "medicine_type", "medicine_cost"]
)
tests = pd.DataFrame(columns=["test_id", "test_name"])
observations = pd.DataFrame(
    columns=["observation_id", "visit_id", "test_id", "doctor_id", "result"]
)
doctors = pd.DataFrame(
    columns=["doctor_id", "doctor_name", "specialization", "hospital_id"]
)
past_medical_history = pd.DataFrame(
    columns=[
        "history_id",
        "patient_id",
        "disease_id",
        "date_of_diagnosis",
        "date_of_cure",
    ]
)
past_medical_treatment = pd.DataFrame(
    columns=["treatment_id", "history", "medicine_id", "date_of_start", "date_of_end"]
)

fake = Faker(locale="en_US")


def fill_hospitals(n):
    for i in range(n):
        hospitals.loc[i] = [i, fake.company(), fake.address(), fake.country()]
    print(f"completed filling {n} hospitals")


def fill_patients(n):
    for i in range(n):
        patients.loc[i] = [
            i,
            fake.name(),
            fake.random_element(elements=("M", "F")),
            fake.date_of_birth(),
            fake.country(),
        ]
    print(f"completed filling {n} patients")


def fill_diseases(n):
    for i in range(n):
        diseases.loc[i] = [i, fake.word()]
    print(f"completed filling {n} diseases")


def fill_visits(n):
    for i in range(n):
        visits.loc[i] = [
            i,
            fake.random_int(min=0, max=patients.shape[0] - 1),
            fake.random_int(min=0, max=hospitals.shape[0] - 1),
            fake.date(min=patients.loc[i]["date_of_birth"]),
            fake.random_int(min=0, max=10000),
        ]
    print(f"completed filling {n} visits")


def fill_prescriptions(n):
    for i in range(n):
        prescriptions.loc[i] = [
            i,
            fake.random_int(min=0, max=visits.shape[0] - 1),
            fake.date(),
            fake.random_int(min=0, max=medicine.shape[0] - 1),
            fake.random_int(min=0, max=diseases.shape[0] - 1),
            fake.random_int(min=0, max=10),
        ]
    print(f"completed filling {n} prescriptions")


def fill_medicine(n):
    for i in range(n):
        medicine.loc[i] = [
            i,
            fake.word(),
            fake.random_element(elements=("tablet", "syrup", "injection")),
            fake.random_int(min=0, max=1000),
        ]
    print(f"completed filling {n} medicines")


def fill_tests(n):
    for i in range(n):
        tests.loc[i] = [i, fake.word()]
    print(f"completed filling {n} tests")


def fill_observations(n):
    for i in range(n):
        observations.loc[i] = [
            i,
            fake.random_int(min=0, max=visits.shape[0] - 1),
            fake.random_int(min=0, max=tests.shape[0] - 1),
            fake.random_int(min=0, max=doctors.shape[0] - 1),
            fake.random_int(min=0, max=10),
        ]
    print(f"completed filling {n} observations")


def fill_doctors(n):
    for i in range(n):
        doctors.loc[i] = [
            i,
            fake.name(),
            fake.word(),
            fake.random_int(min=0, max=hospitals.shape[0] - 1),
        ]
    print(f"completed filling {n} doctors")


def fill_past_medical_history(n):
    for i in range(n):
        past_medical_history.loc[i] = [
            i,
            fake.random_int(min=0, max=patients.shape[0] - 1),
            fake.random_int(min=0, max=diseases.shape[0] - 1),
            fake.date(),
            fake.date(),
        ]
    print(f"completed filling {n} past medical history")


def fill_past_medical_treatment(n):
    for i in range(n):
        past_medical_treatment.loc[i] = [
            i,
            fake.random_int(min=0, max=past_medical_history.shape[0] - 1),
            fake.random_int(min=0, max=medicine.shape[0] - 1),
            fake.date(),
            fake.date(),
        ]
    print(f"completed filling {n} past medical treatment")


fill_hospitals(500)
fill_patients(10000)
fill_visits(20000)
fill_medicine(1000)
fill_tests(300)
fill_diseases(100)
fill_doctors(1000)
fill_prescriptions(15000)
fill_observations(20000)
fill_past_medical_history(1000)
fill_past_medical_treatment(1000)
