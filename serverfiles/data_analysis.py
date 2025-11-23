# -*- coding: utf-8 -*-

from pyspark.sql import SparkSession

from load import read_file
from plots import countplot, distribution

def main():
    """
    Run basic analysis on input data.
    """
    spark = SparkSession.builder.appName("Data Analysis").getOrCreate()
    df = read_file(spark, "transactions.ndjson")

    # Look at the distribution of values of all the numerical columns
    deicmal_cols = [col for col, dtype in df.dtypes if "decimal" in dtype]
    for col in deicmal_cols:
        distribution(df.select(col), col)

    categorical_cols = [
        "creditLimit",
        "merchantName",
        "acqCountry",
        "merchantCountryCode",
        "posEntryMode",
        "posConditionCode",
        "merchantCategoryCode",
        "transactionType"
    ]

    for col in categorical_cols:
        countplot(df.select(col), col)


if __name__ == "__main__":
    main()

# EOF
