# Data Synthesis Example

## Problem Statement

Identify different attributes related to patient medical data tied to hospital visits,
where a patient visits the doctors in the hospital for treatment, consultation,
surgery, follow up, pharmacy, diagnosis, scans, etc.

Attributes must cover the following areas: Hospitals, location, patient, disease,
products, medicines, lab tests, datetime dimension, laboratory observations,
reports, doctor information, past medical conditions, past treatment history, etc.

Prepare synthetic data for the same set of attributes, have at least six years of data.

1. Important aspects of the data to note are the relations and the logic behind each medical record.
2. One patient with ID say #123 marked as a male, cannot be a different gender in a different row for the same patient record. Similarly, the same logic applies to other fields.
3. One patient can have one more visit.
4. One patient record will mostly be associated with only one hospital.
5. Patient can be a returning patient depending on the medical disease he/she has, so patient record duration can span more than one year.
6. Have at least 200 unique medical diseases/concerns in the records.
7. Have at least 10K patients.
8. Have at least 500 hospitals in the data, location within a specific country.
