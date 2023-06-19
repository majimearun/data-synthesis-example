# imports

import pandas as pd
from faker.proxy import Faker
import random
import warnings

warnings.filterwarnings("ignore")

# tables schema

hospitals = pd.DataFrame(
    columns=["hospital_id", "hospital_name", "location", "country"]
)

patients = pd.DataFrame(
    columns=["patient_id", "patient_name", "gender", "date_of_birth", "country"]
)

visits = pd.DataFrame(
    columns=["visit_id", "patient_id", "hospital_id", "date_of_visit", "cost"]
)

diseases = pd.DataFrame(columns=["disease_id", "disease_name"])

tests = pd.DataFrame(columns=["test_id", "test_name", "test_for"])

observations = pd.DataFrame(
    columns=["observation_id", "visit_id", "test_id", "doctor_id", "disease_id"]
)

medicines = pd.DataFrame(
    columns=[
        "medicine_id",
        "medicine_name",
        "medicine_type",
        "medicine_cost",
        "used_for",
    ]
)

doctors = pd.DataFrame(
    columns=["doctor_id", "doctor_name", "specialization", "hospital_id"]
)

prescriptions = pd.DataFrame(
    columns=[
        "prescription_id",
        "date_of_prescription",
        "medicine_id",
        "dosage",
        "observation_id",
        "doctor_id",
    ]
)

fake = Faker(locale="en_US")

countries = []
for i in range(10):
    countries.append(fake.country())
countries = list(set(countries))


def fill_hospitals(n):
    for i in range(n):
        hospitals.loc[i] = [
            i,
            fake.company(),
            fake.address(),
            fake.random_element(countries),
        ]
    print(f"completed filling {n} hospitals")


def fill_patients(n):
    for i in range(n):
        patients.loc[i] = [
            i,
            fake.name(),
            fake.random_element(elements=("M", "F")),
            fake.date_of_birth(minimum_age=0, maximum_age=50),
            fake.random_element(elements=countries),
        ]
    print(f"completed filling {n} patients")


def fill_diseases(n):
    for i in range(n):
        diseases.loc[i] = [
            i,
            "".join([fake.name()[:2], fake.name()[-2:]]).lower().capitalize(),
        ]
    print(f"completed filling {n} diseases")


def fill_medicines(n):
    for i in range(n):
        medicines.loc[i] = [
            i,
            "".join([fake.name()[:3], fake.name()[-3:]]),
            fake.random_element(
                elements=("tablet", "syrup", "injection", "capsule", "ointment")
            ),
            fake.random_int(min=100, max=10000),
            fake.random_int(min=0, max=diseases.shape[0] - 1),
        ]
    print(f"completed filling {n} medicines")


def fill_tests(n):
    for i in range(n):
        tests.loc[i] = [
            i,
            "".join([fake.name()[:3], fake.name()[-3:]]),
            fake.random_int(min=0, max=diseases.shape[0] - 1),
        ]
    print(f"completed filling {n} tests")


def fill_doctors(n):
    for i in range(n):
        doctors.loc[i] = [
            i,
            fake.name(),
            fake.random_element(
                elements=(
                    "cardiologist",
                    "neurologist",
                    "gynecologist",
                    "pediatrician",
                    "psychiatrist",
                )
            ),
            fake.random_int(min=0, max=hospitals.shape[0] - 1),
        ]
    print(f"completed filling {n} doctors")


def fill_visits(n):
    for i in range(n):
        patient_id = fake.random_int(min=0, max=patients.shape[0] - 1)
        if visits[visits["patient_id"] == patient_id].shape[0] > 0:
            max_date = visits[visits["patient_id"] == patient_id]["date_of_visit"].max()
        visits.loc[i] = [
            i,
            patient_id,
            fake.random_int(min=0, max=hospitals.shape[0] - 1),
            None,
            fake.random_int(min=100, max=10000),
        ]
        if visits[visits.loc[i]["patient_id"] == visits["patient_id"]].shape[0] > 1:
            visits.loc[i, "date_of_visit"] = fake.date_between_dates(
                date_start=max_date,
                date_end=pd.Timestamp.today(),
            )
        else:
            visits.loc[i, "date_of_visit"] = fake.date_between_dates(
                date_start=patients.loc[visits.loc[i]["patient_id"]]["date_of_birth"],
            )

    print(f"completed filling {n} visits")


def fill_observations(n):
    for i in range(n):
        observation_id = i
        visit_id = fake.random_int(min=0, max=visits.shape[0] - 1)
        test_id = fake.random_int(min=0, max=tests.shape[0] - 1)
        doctor_id = fake.random_int(min=0, max=doctors.shape[0] - 1)
        if random.random() < 0.7:
            disease_id = tests.loc[test_id]["test_for"]
        else:
            disease_id = None
        observations.loc[i] = [
            observation_id,
            visit_id,
            test_id,
            doctor_id,
            disease_id,
        ]
    print(f"completed filling {n} observations")


def fill_prescriptions(n):
    for i in range(n):
        prescription_id = i
        date_of_prescription = fake.date_between_dates(
            date_start=visits.loc[observations.loc[i]["visit_id"]]["date_of_visit"],
            date_end=visits.loc[observations.loc[i]["visit_id"]]["date_of_visit"]
            + pd.Timedelta(days=1),
        )
        disease = observations.loc[i]["disease_id"]
        if disease is not None:
            try:
                medicine_id = (
                    medicines[medicines["used_for"] == disease].sample(1).index[0]
                )
            except:
                medicine_id = None
        else:
            medicine_id = None
        if medicine_id is not None:
            dosage = fake.random_int(min=1, max=10)
        else:
            dosage = None
        observation_id = i
        doctor_id = fake.random_int(min=0, max=doctors.shape[0] - 1)
        prescriptions.loc[i] = [
            prescription_id,
            date_of_prescription,
            medicine_id,
            dosage,
            observation_id,
            doctor_id,
        ]
    print(f"completed filling {n} prescriptions")


fill_hospitals(500)
fill_patients(10000)
fill_diseases(200)
fill_medicines(1000)
fill_tests(2000)
fill_doctors(5000)
fill_visits(20000)
fill_observations(50000)
fill_prescriptions(50000)

# convert to csv

hospitals.to_csv("./data/hospitals.csv", index=False)
patients.to_csv("./data/patients.csv", index=False)
visits.to_csv("./data/visits.csv", index=False)
medicines.to_csv("./data/medicine.csv", index=False)
tests.to_csv("./data/tests.csv", index=False)
diseases.to_csv("./data/diseases.csv", index=False)
doctors.to_csv("./data/doctors.csv", index=False)
prescriptions.to_csv("./data/prescriptions.csv", index=False)
observations.to_csv("./data/observations.csv", index=False)
