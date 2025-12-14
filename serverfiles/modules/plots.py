# -*- coding: utf-8 -*-

from pathlib import Path
from typing import List

import cv2 as cv
import IPython.display as display
import ipywidgets as widgets
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns

def countplot(dataframe, y, hue=None, **kwargs):
    """
    Wrapper function to seaborn countplot that includes formatting and file write.
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

def distribution(dataframe, x, hue=None, **kwargs):
    """
    Wrapper function to seaborn histplot that includes formatting and file write.
    """
    
    dataframe = dataframe.toPandas()
    sns.histplot(data=dataframe, x=x, hue=hue, **kwargs)
    plt.xlabel(x)
    plt.ylabel("Frequency")
    if hue is not None:
        plt.title(f"{x} by {hue}")
        plt.savefig(f"figures/{x}_distribution_by_{hue}.png",
                    bbox_inches="tight")
    else:
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

def display_images(imgfiles: List[str], width=300, height=300, ncols=4):
    """
    Display images in-line in ipython environment.

    Args:
        imgfiles (List): list of image file names to display.
    """

    plt.close()
    if len(imgfiles) <= ncols:
        ncols = len(imgfiles)
        plt.figure(figsize=(width*ncols, height))
        fig, ax = plt.subplots(1,ncols)
        for i, imgfile in enumerate(imgfiles):
            ax[i].axis("off")
            ax[i].imshow(mpimg.imread(Path("figures") / imgfile))
    else:
        nrows = round(np.ceil(len(imgfiles) / ncols))
        plt.figure(figsize=(width*ncols, height*nrows))
        fig, ax = plt.subplots(ncols, nrows)
        for i, imgfile in enumerate(imgfiles):
            row = i % ncols
            col = i // ncols
            ax[row, col].axis("off")
            ax[row, col].imshow(impimg.imread(Path("figures") / imgfile))
    """
    images = []
    for imgfile in imgfiles:
        image = open(Path("figures") / imgfile, "rb").read()
        images.append(widgets.Image(value=image, format="png", width=width, height=height))
    widgetbox=widgets.HBox(images)
    display.display(widgetbox)
    """

# EOF
