# -*- coding: utf-8 -*-

from pathlib import Path
from typing import List

import cv2 as cv
import IPython.display as display
import ipywidgets as widgets
import matplotlib.pyplot as plt
import seaborn as sns

def countplot(dataframe, y, hue=None, **kwargs):
    """
    """

    dataframe = dataframe.toPandas()
    sns.countplot(data=dataframe, y=y, hue=hue, **kwargs)
    plt.xlabel("Count")
    plt.ylabel(y)
    if hue is not None:
        plt.title(f"{y} by {hue}")
        plt.savefig(f"figures/{y}_barchart_with_{hue}.png",
                    bbox_inches="tight")
    else:
        plt.title(f"{y}")
        plt.savefig(f"figures/{y}_barchart.png",
                    bbox_inches="tight")
    plt.close()

def distribution(dataframe, x):
    """
    """
    
    dataframe = dataframe.toPandas()
    sns.histplot(data=dataframe, x=x, kde=True)
    plt.xlabel(x)
    plt.ylabel("Frequency")
    #plt.xscale("symlog", linthresh=100)
    plt.title(f"{x}")
    plt.savefig(f"figures/{x}_distribution.png",
                    bbox_inches="tight")
    plt.close()

def catplot(dataframe, x, y, hue=None, kind=None, **kwargs):
    """
    """
    if kind == None:
        kind = "strip"
    dataframe = dataframe.toPandas()
    sns.catplot(data=dataframe, x=x, y=y, hue=hue, kind=kind, **kwargs)
    if hue is not None:
        plt.title(f"{x} vs {y} {kind} by {hue}")
        plt.savefig(f"figures/{y}_{kind}plot_by_{x}_with_{hue}.png",
                    bbox_inches="tight")
    else:
        plt.title(f"{x} vs {y} {kind} plot")
        plt.savefig(f"figures/{y}_{kind}plot_by_{x}.png",
                    bbox_inches="tight")
    plt.close()

def display_images(imgfiles: List[str], width=300, height=300):
    """
    Display images in-line in ipython environment.

    Args:
        imgfiles (List): list of image file names to display.
    """

    images = []
    for imgfile in imgfiles:
        image = open(Path("figures") / imgfile, "rb").read()
        images.append(widgets.Image(value=image, format="png", width=width, height=height))
    widgetbox=widgets.HBox(images)
    display.display(widgetbox)

# EOF
