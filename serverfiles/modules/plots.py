# -*- coding: utf-8 -*-

import typing

import cv2 as cv
import matplotlib.pyplot as plt
import seaborn as sns

def countplot(dataframe, x, hue=None, **kwargs):
    """
    """

    dataframe = dataframe.toPandas()
    sns.countplot(data=dataframe, y=x, hue=hue, **kwargs)
    plt.xlabel(x)
    plt.ylabel("Count")
    if hue is not None:
        plt.savefig(f"figures/{x}_barchart_with_{hue}.png")
    else:
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

def catplot(dataframe, x, y, hue=None, kind=None, **kwargs):
    """
    """
    if kind == None:
        kind = "strip"
    dataframe = dataframe.toPandas()
    sns.catplot(data=dataframe, x=x, y=y, hue=hue, kind=kind, **kwargs)
    if hue is not None:
        plt.savefig(f"figures/{y}_{kind}plot_by_{x}_with_{hue}.png")
    else:
        plt.savefig(f"figures/{y}_{kind}plot_by_{x}.png")
    plt.close()

# EOF
