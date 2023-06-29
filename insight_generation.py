# imports

import pandas as pd

hospitals = pd.read_csv("./data/hospitals.csv")
patients = pd.read_csv("./data/patients.csv")
visits = pd.read_csv("./data/visits.csv")
doctors = pd.read_csv("./data/doctors.csv")
diseases = pd.read_csv("./data/diseases.csv")
medicines = pd.read_csv("./data/medicines.csv")
observations = pd.read_csv("./data/observations.csv")
prescriptions = pd.read_csv("./data/prescriptions.csv")
tests = pd.read_csv("./data/tests.csv")


main_df = pd.merge(visits, patients, on="patient_id", how="outer")
main_df = pd.merge(main_df, hospitals, on="hospital_id", how="outer")
main_df = pd.merge(main_df, observations, on="visit_id", how="outer")
main_df = pd.merge(main_df, diseases, on="disease_id", how="outer")
main_df = pd.merge(main_df, doctors, on="doctor_id", how="outer")
main_df = pd.merge(main_df, tests, on="test_id", how="outer")
main_df = pd.merge(main_df, prescriptions, on="observation_id", how="outer")
main_df = pd.merge(main_df, medicines, on="medicine_id", how="outer")

main_df.to_csv("./data/main.csv", index=False)

palm_api_key = "AIzaSyCes53YLYZZ38hHeWVYG9IoLx_svGFAvg4"


from pandasai import PandasAI
from pandasai.llm.google_palm import GooglePalm

llm = GooglePalm(palm_api_key)
pai = PandasAI(llm, conversational=True)

column_names = ["patient_name", "hospital_name"]

for column in column_names:
    print(
        pai(
            main_df,
            prompt=f"give me 10 insights about column {column}, and its logically related columns where each insight is unique",
        )
    )
