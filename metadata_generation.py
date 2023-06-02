# imports

from sdv.metadata import MultiTableMetadata
from initial_generation import (
    hospitals,
    patients,
    diseases,
    visits,
    prescriptions,
    medicine,
    tests,
    observations,
    doctors,
    past_medical_history,
    past_medical_treatment,
)

metadata = MultiTableMetadata()

metadata.detect_table_from_dataframe("hospitals", hospitals)
metadata.detect_table_from_dataframe("patients", patients)
metadata.detect_table_from_dataframe("diseases", diseases)
metadata.detect_table_from_dataframe("visits", visits)
metadata.detect_table_from_dataframe("prescriptions", prescriptions)
metadata.detect_table_from_dataframe("medicine", medicine)
metadata.detect_table_from_dataframe("tests", tests)
metadata.detect_table_from_dataframe("observations", observations)
metadata.detect_table_from_dataframe("doctors", doctors)
metadata.detect_table_from_dataframe("past_medical_history", past_medical_history)
metadata.detect_table_from_dataframe("past_medical_treatment", past_medical_treatment)

# change data tpe for hospital table

metadata.update_column(table_name="hospitals", column_name="hospital_id", sdtype="id")
metadata.update_column(
    table_name="hospitals", column_name="hospital_name", sdtype="categorical"
)
metadata.update_column(
    table_name="hospitals", column_name="location", sdtype="categorical"
)
metadata.update_column(
    table_name="hospitals", column_name="country", sdtype="categorical"
)

# change data type for patients table

metadata.update_column(table_name="patients", column_name="patient_id", sdtype="id")
metadata.update_column(
    table_name="patients", column_name="patient_name", sdtype="categorical"
)
metadata.update_column(
    table_name="patients", column_name="gender", sdtype="categorical"
)
metadata.update_column(
    table_name="patients",
    column_name="date_of_birth",
    sdtype="datetime",
    datetime_format="%Y-%m-%d",
)
metadata.update_column(
    table_name="patients", column_name="country", sdtype="categorical"
)

# change data type for diseases table

metadata.update_column(table_name="diseases", column_name="disease_id", sdtype="id")
metadata.update_column(
    table_name="diseases", column_name="disease_name", sdtype="categorical"
)

# change data type for visits table

metadata.update_column(table_name="visits", column_name="visit_id", sdtype="id")
metadata.update_column(table_name="visits", column_name="patient_id", sdtype="id")
metadata.update_column(table_name="visits", column_name="hospital_id", sdtype="id")
metadata.update_column(
    table_name="visits",
    column_name="date_of_visit",
    sdtype="datetime",
    datetime_format="%Y-%m-%d",
)
metadata.update_column(table_name="visits", column_name="cost", sdtype="numerical")

# change data type for prescriptions table

metadata.update_column(
    table_name="prescriptions", column_name="prescription_id", sdtype="id"
)
metadata.update_column(table_name="prescriptions", column_name="visit_id", sdtype="id")
metadata.update_column(
    table_name="prescriptions",
    column_name="date_of_prescription",
    sdtype="datetime",
    datetime_format="%Y-%m-%d",
)
metadata.update_column(
    table_name="prescriptions", column_name="medicine_id", sdtype="id"
)
metadata.update_column(
    table_name="prescriptions", column_name="disease_id", sdtype="id"
)
metadata.update_column(
    table_name="prescriptions", column_name="dosage", sdtype="categorical"
)

# change data type for medicine table

metadata.update_column(table_name="medicine", column_name="medicine_id", sdtype="id")
metadata.update_column(
    table_name="medicine", column_name="medicine_name", sdtype="categorical"
)
metadata.update_column(
    table_name="medicine", column_name="medicine_type", sdtype="categorical"
)
metadata.update_column(
    table_name="medicine", column_name="medicine_cost", sdtype="numerical"
)

# change data type for tests table

metadata.update_column(table_name="tests", column_name="test_id", sdtype="id")
metadata.update_column(
    table_name="tests", column_name="test_name", sdtype="categorical"
)

# change data type for observations table

metadata.update_column(
    table_name="observations", column_name="observation_id", sdtype="id"
)
metadata.update_column(table_name="observations", column_name="visit_id", sdtype="id")
metadata.update_column(table_name="observations", column_name="test_id", sdtype="id")
metadata.update_column(table_name="observations", column_name="doctor_id", sdtype="id")
metadata.update_column(
    table_name="observations", column_name="result", sdtype="categorical"
)

# change data type for doctors table

metadata.update_column(table_name="doctors", column_name="doctor_id", sdtype="id")
metadata.update_column(
    table_name="doctors", column_name="doctor_name", sdtype="categorical"
)
metadata.update_column(
    table_name="doctors", column_name="specialization", sdtype="categorical"
)
metadata.update_column(table_name="doctors", column_name="hospital_id", sdtype="id")

# change data type for past_medical_history table

metadata.update_column(
    table_name="past_medical_history", column_name="history_id", sdtype="id"
)
metadata.update_column(
    table_name="past_medical_history", column_name="patient_id", sdtype="id"
)
metadata.update_column(
    table_name="past_medical_history", column_name="disease_id", sdtype="id"
)
metadata.update_column(
    table_name="past_medical_history",
    column_name="date_of_diagnosis",
    sdtype="datetime",
    datetime_format="%Y-%m-%d",
)
metadata.update_column(
    table_name="past_medical_history",
    column_name="date_of_cure",
    sdtype="datetime",
    datetime_format="%Y-%m-%d",
)

# change data type for past_medical_treatment table

metadata.update_column(
    table_name="past_medical_treatment", column_name="treatment_id", sdtype="id"
)
metadata.update_column(
    table_name="past_medical_treatment", column_name="history", sdtype="id"
)
metadata.update_column(
    table_name="past_medical_treatment", column_name="medicine_id", sdtype="id"
)
metadata.update_column(
    table_name="past_medical_treatment",
    column_name="date_of_start",
    sdtype="datetime",
    datetime_format="%Y-%m-%d",
)
metadata.update_column(
    table_name="past_medical_treatment",
    column_name="date_of_end",
    sdtype="datetime",
    datetime_format="%Y-%m-%d",
)

# set primary keys

metadata.set_primary_key("hospitals", "hospital_id")
metadata.set_primary_key("patients", "patient_id")
metadata.set_primary_key("diseases", "disease_id")
metadata.set_primary_key("visits", "visit_id")
metadata.set_primary_key("prescriptions", "prescription_id")
metadata.set_primary_key("medicine", "medicine_id")
metadata.set_primary_key("tests", "test_id")
metadata.set_primary_key("observations", "observation_id")
metadata.set_primary_key("doctors", "doctor_id")
metadata.set_primary_key("past_medical_history", "history_id")
metadata.set_primary_key("past_medical_treatment", "treatment_id")
metadata.set_primary_key("past_medical_history", "history_id")

# set foreign keys

metadata.add_relationship(
    parent_table_name="hospitals",
    parent_primary_key="hospital_id",
    child_table_name="visits",
    child_foreign_key="hospital_id",
)
metadata.add_relationship(
    parent_table_name="patients",
    parent_primary_key="patient_id",
    child_table_name="visits",
    child_foreign_key="patient_id",
)
metadata.add_relationship(
    parent_table_name="patients",
    parent_primary_key="patient_id",
    child_table_name="past_medical_history",
    child_foreign_key="patient_id",
)
metadata.add_relationship(
    parent_table_name="diseases",
    parent_primary_key="disease_id",
    child_table_name="past_medical_history",
    child_foreign_key="disease_id",
)
metadata.add_relationship(
    parent_table_name="visits",
    parent_primary_key="visit_id",
    child_table_name="prescriptions",
    child_foreign_key="visit_id",
)
metadata.add_relationship(
    parent_table_name="medicine",
    parent_primary_key="medicine_id",
    child_table_name="prescriptions",
    child_foreign_key="medicine_id",
)
metadata.add_relationship(
    parent_table_name="diseases",
    parent_primary_key="disease_id",
    child_table_name="prescriptions",
    child_foreign_key="disease_id",
)
metadata.add_relationship(
    parent_table_name="visits",
    parent_primary_key="visit_id",
    child_table_name="observations",
    child_foreign_key="visit_id",
)
metadata.add_relationship(
    parent_table_name="tests",
    parent_primary_key="test_id",
    child_table_name="observations",
    child_foreign_key="test_id",
)
metadata.add_relationship(
    parent_table_name="doctors",
    parent_primary_key="doctor_id",
    child_table_name="observations",
    child_foreign_key="doctor_id",
)
metadata.add_relationship(
    parent_table_name="past_medical_history",
    parent_primary_key="history_id",
    child_table_name="past_medical_treatment",
    child_foreign_key="history",
)
metadata.add_relationship(
    parent_table_name="medicine",
    parent_primary_key="medicine_id",
    child_table_name="past_medical_treatment",
    child_foreign_key="medicine_id",
)
