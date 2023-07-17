# Data Pattern identification using Synthetic data

## Part 1

Identify different attributes related to patient medical data tied to hospital visits, where a patient visits the doctors in the hospital for treatment, consultation, surgery, follow up, pharmacy, diagnosis, scans, etc. Attributes must cover the following areas:

Hospitals, location, patient, disease, products, medicines, lab tests, datetime dimension, laboratory observations, reports, doctor information, past medical conditions, past treatment history, etc.

Prepare synthetic data for the same set of attributes, have at least six years of data.

1. Important aspects of the data to note are the relations and the logic behind each medical record.

2. One patient with ID say #123 marked as a male, cannot be a different gender in a different row for the same patient record.Similarly, the same logic applies to other fields.

3. One patient can have one more visit.

4. One patient record will mostly be associated with only one hospital.

5. Patient can be a returning patient depending on the medical disease he/she has, so patient record duration can span more than one year.

6. Have at least 200 unique medical diseases/concerns in the records.

7. Have at least 10K patients.

8. Have at least 500 hospitals in the data, location within a specific country.

## Part 2

Once the data is generated, write a generic script/ model to identify patterns and trends in the data across medical conditions/ products used/ seasonality/ location-based, etc. The goal is to identify and generate interesting insights from the data, with little to no manual intervention.

Few sample patterns or insights

1. City “X” has the highest number of increasing “covid” cases

2. Hospital ABC treatedthe highest number of childrenin the entire state for <medical condition>

3. There is a decline in the patient flow in CDE Hospital

## Few technical points to note:

-   Either Python or Javascript can be used for the program

-   Data can be stored in a database and read in the code or can be kept in multiple files (if the data size is large).

-   Use Divide and conquer approaches to load and efficiently process data to generate the desired output.

-   The system must generate at least50-60 insights from the data

-   Any open-source ML library can be used if needed, for modelling•Dataset must be clean and should not take much time for preprocessing.

## Input Instructions:

1. Have the program take an argument as an input, the argument can be of type Array. It can contain either one item or multiple items.

2. The program must read this array of item(s), the values in the array will be the attribute names of the dataset generated. The model must generate insights for the attributes passed in the argument. Example: If “lab tests”is one of the values passed in the argument, the system must generate insights including the lab tests attribute. The program can use any of the other attributes associated with this lab test to produce output, like a datetime field, or patient ID field, depending on the value of the lab test, For example, if the value of a specific lab test is below the normal range, it can be an abnormal one, and the program can compare it with other data of the patient and produce insights.
