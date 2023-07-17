# Imports
import sys
import os
import pandas as pd
import numpy as np
import tabulate

# Reading Partitioned Tables
hospitals = pd.read_csv("./data/hospitals.csv")
patients = pd.read_csv("./data/patients.csv")
visits = pd.read_csv("./data/visits.csv")
doctors = pd.read_csv("./data/doctors.csv")
diseases = pd.read_csv("./data/diseases.csv")
medicines = pd.read_csv("./data/medicines.csv")
observations = pd.read_csv("./data/observations.csv")
prescriptions = pd.read_csv("./data/prescriptions.csv")
tests = pd.read_csv("./data/tests.csv")

# Making the table into a single table, to generate insights from
main_df = pd.merge(visits, patients, on="patient_id", how="outer")
main_df = pd.merge(main_df, hospitals, on="hospital_id", how="outer")
main_df = pd.merge(main_df, observations, on="visit_id", how="outer")
main_df = pd.merge(main_df, diseases, on="disease_id", how="outer")
main_df = pd.merge(main_df, doctors, on="doctor_id", how="outer")
main_df = pd.merge(main_df, tests, on="test_id", how="outer")
main_df = pd.merge(main_df, prescriptions, on="observation_id", how="outer")
main_df = pd.merge(main_df, medicines, on="medicine_id", how="outer")

# Dropping unnecessary columns
main_df.drop(
    columns=[
        "visit_id",
        "patient_id",
        "hospital_id_x",
        "observation_id",
        "test_id",
        "doctor_id_x",
        "disease_id",
        "hospital_id_y",
        "prescription_id",
        "medicine_id",
        "doctor_id_y",
        "country_y",
    ],
    inplace=True,
)

# Renaming columns (add more if required to the list)
main_df.rename(
    {
        "hospital_name": "hospital",
        "country_x": "country",
    },
    axis=1,
    inplace=True,
)
main_df.to_csv("./data/main.csv", index=False)


def find_most_least_frequent_values(df, column1, column2):
    # Group the DataFrame by column1 and count occurrences of column2 values
    grouped = df.groupby(column1)[column2].value_counts().reset_index(name="count")

    # Find the most frequent value of column2 for each unique value of column1
    most_frequent_values = (
        grouped.groupby(column1)
        .apply(lambda x: x.nlargest(1, "count"))
        .reset_index(drop=True)
    )

    # Find the least frequent value of column2 for each unique value of column1
    least_frequent_values = (
        grouped.groupby(column1)
        .apply(lambda x: x.nsmallest(1, "count"))
        .reset_index(drop=True)
    )

    # Create a new DataFrame with the most and least frequent values of column2 for each unique value of column1
    result_df = pd.DataFrame(
        {
            column1: most_frequent_values[column1],
            "Most Frequent " + column2: most_frequent_values[column2],
            "Count MF": most_frequent_values["count"],
            "Least Frequent " + column2: least_frequent_values[column2],
            "Count LF": least_frequent_values["count"],
        }
    )

    result_df.sort_values(by=["Count MF"], inplace=True, ascending=False)
    final_df = result_df.head(5).copy()
    result_df.sort_values(by=["Count LF"], inplace=True, ascending=True)
    final_df = pd.concat([final_df, result_df.head(5).copy()])

    return final_df


def parse_dates(df):
    for column in df.columns:
        if df[column].dtype == "object":
            try:
                df[column] = pd.to_datetime(df[column])
            except ValueError:
                pass


data = main_df.copy()
parse_dates(data)
columns_names = eval(input("Enter column names (separated by commas): "))

for column_name in columns_names:
    # create a folder for each column
    os.mkdir("./insights/" + column_name)

    # Open a file in write mode
    with open(f"./insights/{column_name}/basic.txt", "w") as file:
        # Redirect the standard output to the file
        sys.stdout = file

        column = data[column_name]

        # Single column tests
        print("========================================")
        print("Insights for column:", column_name)
        print("========================================")

        print("========================================")
        print("Tests on single column:")
        print("========================================")

        if column.dtype == "object":
            # Count unique values
            unique_values_count = column.nunique()
            print("1. Unique values count:", unique_values_count)

            if unique_values_count > 1:
                # Find the most repeated values
                print("2. Most repeated values:")
                repeated_values = column.value_counts().head(5)
                for value, count in repeated_values.items():
                    print(f"   - Value '{value}' appears {count} times.")

            if unique_values_count > 1:
                # Find the least repeated values
                print("3. Least repeated values:")
                repeated_values = column.value_counts().tail(5)
                for value, count in repeated_values.items():
                    print(f"   - Value '{value}' appears {count} times.")

        elif column.dtype == "int64" or column.dtype == "float64":
            print("1. Summary statistics:")
            summary_stats = column.describe()
            for stat, value in summary_stats.items():
                print(f"   - {stat.capitalize()}: {value}")

        elif column.dtype == "datetime64[ns]":
            # Extract date-specific insights
            print("1. Date-specific insights:")
            print("   - Earliest date:", column.min().strftime("%Y-%m-%d"))
            print("   - Latest date:", column.max().strftime("%Y-%m-%d"))
            print("   - Number of unique dates:", column.nunique())

            # Compute date-based aggregations
            print("2. Date-based aggregations:")
            daily_counts = column.dt.date.value_counts().sort_index()
            daily_counts = daily_counts.sort_values(ascending=False).head(5).copy()
            print("   - Number of records per day:")
            print(daily_counts)

            monthly_counts = column.dt.to_period("M").value_counts().sort_index()
            monthly_counts = monthly_counts.sort_values(ascending=False).head(5).copy()
            print("   - Number of records per month:")
            print(monthly_counts)

            yearly_counts = column.dt.to_period("Y").value_counts().sort_index()
            yearly_counts = yearly_counts.sort_values(ascending=False).head(5).copy()
            print("   - Number of records per year:")
            print(yearly_counts)

        else:
            print("1. No insights available for this column type.")

    with open("./insights/" + column_name + "/frequent relations.txt", "w") as file:
        sys.stdout = file

        print("========================================")
        print("Tests on multiple columns:")
        print("========================================")
        if column.dtype == "int64" or column.dtype == "float64":
            numeric_columns = data.select_dtypes(include=["int64", "float64"]).columns

            for other_column in numeric_columns:
                if other_column != column_name:
                    correlation = np.corrcoef(data[column_name], data[other_column])[
                        0, 1
                    ]
                    print(f"   - Correlation with '{other_column}': {correlation}")

        elif column.dtype == "object":
            categorical_columns = data.select_dtypes(include=["object"]).columns

            for other_column in categorical_columns:
                if other_column != column_name:
                    # Find the most and least frequent values of other_column for each unique value of column_name
                    print(
                        f"   - Most and least frequent values of '{other_column}' for each unique value of '{column_name}':"
                    )
                    print(
                        tabulate.tabulate(
                            find_most_least_frequent_values(
                                data, column_name, other_column
                            ),
                            headers="keys",
                            tablefmt="fancy_grid",
                        )
                    )
        else:
            print("1. No insights available for this column type.")

    if column.dtype == "datetime64[ns]":
        object_columns = data.select_dtypes(include=["object"]).columns
        numeric_columns = data.select_dtypes(include=["int64", "float64"]).columns

        with open(
            "./insights/" + column_name + "/frequent coocurrences.txt", "w"
        ) as file:
            sys.stdout = file

            for other_column in object_columns:
                print("Getting insights for", other_column)

                print(
                    f"   - Most and least frequent values of '{other_column}' for each unique value of '{column_name}':"
                )
                print(
                    tabulate.tabulate(
                        find_most_least_frequent_values(
                            data, column_name, other_column
                        ),
                        headers="keys",
                        tablefmt="fancy_grid",
                    )
                )

        for other_column in numeric_columns:
            # similar to pobject, but find mean, mode, median, std, min, max, etc

            with open("./insights/" + column_name + "/daily stats.txt", "w") as file:
                sys.stdout = file

                print(f"checking stats of {other_column} yearly, monthly, daily: ")

                daily_stats: pd.DataFrame = data.groupby(column.dt.date)[
                    other_column
                ].describe()

                print("   - Daily stats:")
                print(
                    tabulate.tabulate(
                        daily_stats, headers="keys", tablefmt="fancy_grid"
                    )
                )

            with open("./insights/" + column_name + "/monthly stats.txt", "w") as file:
                sys.stdout = file
                monthly_stats: pd.DataFrame = data.groupby(column.dt.to_period("M"))[
                    other_column
                ].describe()

                print("   - Monthly stats:")
                print(
                    tabulate.tabulate(
                        monthly_stats, headers="keys", tablefmt="fancy_grid"
                    )
                )

            with open("./insights/" + column_name + "/yearly stats.txt", "w") as file:
                sys.stdout = file
                yearly_stats: pd.DataFrame = data.groupby(column.dt.to_period("Y"))[
                    other_column
                ].describe()

                print("   - Yearly stats:")
                print(
                    tabulate.tabulate(
                        yearly_stats, headers="keys", tablefmt="fancy_grid"
                    )
                )
