# -*- coding: utf-8 -*-

import json
import typing

from pyspark.ml import Pipeline
from pyspark.ml.feature import OneHotEncoder, StringIndexer
from pyspark.sql import DataFrame, Row, SparkSession
from pyspark.sql.functions import to_timestamp
from pyspark.sql.types import \
    BooleanType, CharType, DateType, DecimalType, FloatType, StructField, \
    StructType, TimestampType, VarcharType 

def read_file(spark: SparkSession, filename: str):
    """
    Read a file containing rows of json objects and build a pyspark DataFrame.

    Args:
        filename (str): The path to the file to read.

    Returns:
        df (spark.sql.DataFrame): A DataFrame containing the data from the
            file.
    """

    df = spark.read.json(filename, multiLine=False)

    timecols = ["transactionDateTime"]
    for col in timecols:
        df = df.withColumn(
            col,
            to_timestamp(
                df.select(col)[col],
                "yyyy-MM-dd'T'HH:mm:ss.SSS'Z'"
            )
        )
    datecols = ["currentExpDate", "accountOpenDate"]
    for col in datecols:
        df = df.withColumn(
            col,
            df.select(col)[col].cast(DateType())
        )

    float_cols = [col for col, dtype in df.dtypes if dtype == 'double']
    for col in float_cols:
        df = df.withColumn(col, df.select(col)[col].cast(DecimalType(10, 2)))

    drop = [
        "echoBuffer",
        "merchantCity",
        "merchantState",
        "merchantZip",
        "posOnPremises",
        "recurringAuthInd"
    ]
    df = df.drop(*drop)
    
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
    df = df.replace("", "empty", subset=categorical_cols)
    df = onehot_index(df, categorical_cols)

    return df

def onehot_index(dataframe: DataFrame, columns: list):
    """
    """

    indexers = []
    encoders = []
    indexed_cols = []
    for column in columns:
        if column not in dataframe.columns:
            raise ValueError(f"Column {column} not found in DataFrame.")
        indexed_col = f"{column}Indexed"
        encoded_col = f"{column}Encoded"
        indexers.append(
            StringIndexer(
                inputCol=column,
                outputCol=indexed_col,
                handleInvalid="keep"
            )
        )
        encoders.append(
            OneHotEncoder(
                inputCol=indexed_col,
                outputCol=encoded_col,
                dropLast=False
            )
        )

    pipeline = Pipeline(stages=indexers + encoders)
    model = pipeline.fit(dataframe)
    dataframe = model.transform(dataframe)

    return dataframe

if __name__ == "__main__":
    spark = SparkSession.builder.appName("test").getOrCreate()

    df = read_file(spark, "transactions.ndjson")

# EOF
