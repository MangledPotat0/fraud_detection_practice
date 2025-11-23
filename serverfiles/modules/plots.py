# -*- coding: utf-8 -*-

import typing

import cv2 as cv
import matplotlib.pyplot as plt
import seaborn as sns

def countplot(dataframe, x):
    """
    """

    dataframe = dataframe.toPandas()
    sns.countplot(data=dataframe, y=x)
    plt.xlabel(x)
    plt.ylabel("Count")
    plt.savefig(f"figures/{x}_barchart.png")
    plt.close()

def distribution(dataframe, x):
    """
    """
    
    dataframe = dataframe.toPandas()
    sns.histplot(data=dataframe, x=x, kde=True)
    plt.xlabel(x)
    plt.ylabel("Frequency")
    #plt.xscale("symlog", linthresh=100)
    plt.savefig(f"figures/{x}_distribution.png")
    plt.close()

# EOF
