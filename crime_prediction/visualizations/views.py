import base64
from io import BytesIO

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# Create your views here.
def create_graph():
    dataset = "predictions/dataset/austin_crime.csv"
    data = pd.read_csv(dataset, nrows=50)
    df = pd.DataFrame(data)

    pd.value_counts(df["description"]).plot.bar()

    buffer = BytesIO()
    plt.title("Cases versus their occurrence")
    plt.ylabel('Occurrences', fontsize=20)
    plt.xlabel('Cases', fontsize=20)
    plt.savefig(buffer, format="png", dpi=300, bbox_inches="tight")
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode("utf-8")
    return graphic


def crimes_in_regions():
    dataset = "predictions/dataset/austin_crime.csv"
    data = pd.read_csv(dataset, nrows=10)
    df = pd.DataFrame(data)

    pd.value_counts(df["address"]).plot.bar()

    buffer = BytesIO()
    plt.title("Regions versus Number of crimes")
    plt.ylabel('Number of crimes', fontsize=20)
    plt.xlabel('Regions', fontsize=20)
    plt.savefig(buffer, format="png",dpi=300, bbox_inches="tight")
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode("utf-8")
    return graphic

def yearly_crimes():
    dataset = "predictions/dataset/austin_crime.csv"
    data = pd.read_csv(dataset, nrows=10000)
    df = pd.DataFrame(data)

    pd.value_counts(df["year"]).plot.bar()

    buffer = BytesIO()
    plt.title("Year versus Number of crimes")
    plt.ylabel('Number of crimes', fontsize=20)
    plt.xlabel('Years', fontsize=20)
    plt.savefig(buffer, format="png",dpi=300, bbox_inches="tight")
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode("utf-8")
    return graphic

@login_required()
def visualize(request):
    return render(request, "visualizations/visualize.html",
                  {"img": create_graph(), "name": "Edgar", "img1": crimes_in_regions(), "img2":yearly_crimes()})
