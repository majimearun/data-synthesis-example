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

for column in column_names:
    print(
        pai(
            main_df,
            prompt=f"Provide 10 interesting facts and figures about column '{column}' and its associated data fields.",
        )
    )

for column in column_names:
    print(
        pai(
            main_df,
            prompt=f"Compare column '{column}' with related variables and generate 10 insights that highlight their similarities and differences.",
        )
    )

for column in column_names:
    print(
        pai(
            main_df,
            prompt=f"Based on column '{column}' and its correlated data fields, predict 10 future trends or outcomes.",
        )
    )

for column in column_names:
    print(
        pai(
            main_df,
            prompt=f"Identify and explain 10 unusual patterns or outliers in column '{column}' and its logically related columns.",
        )
    )

for column in column_names:
    print(
        pai(
            main_df,
            prompt=f"Analyze the impact of column '{column}' on other variables and generate 10 insights on its influence.",
        )
    )

for column in column_names:
    print(
        pai(
            main_df,
            prompt=f"Find 10 strong correlations between column '{column}' and other relevant data fields, and explain their significance.",
        )
    )

for column in column_names:
    print(
        pai(
            main_df,
            prompt=f"Discover and describe 10 recurring patterns or trends in column '{column}' and its associated variables.",
        )
    )

for column in column_names:
    print(
        pai(
            main_df,
            prompt=f"Investigate the causal relationship between column '{column}' and other factors, providing 10 insights on potential causes or effects.",
        )
    )

for column in column_names:
    print(
        pai(
            main_df,
            prompt=f"Determine the importance of column '{column}' in predicting other variables, offering 10 insights on its significance.",
        )
    )

for column in column_names:
    print(
        pai(
            main_df,
            prompt=f"Analyze seasonal patterns in column '{column}' and its logically related columns, providing upto 10 insights on recurring trends.",
        )
    )

for column in column_names:
    print(
        pai(
            main_df,
            prompt=f"Segment customers based on column '{column}' and associated variables, generating 10 insights on different customer groups.",
        )
    )
