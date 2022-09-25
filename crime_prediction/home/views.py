from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post
from predictions.models import Predictions
import pandas as pd
from PIL import Image


# Create your views here.

@login_required()
def home(request):
    context = {"data": Predictions.objects.all()}
    return render(request, "home/home.html", context)


@login_required()
def about(request):
    return render(request, "home/about.html")


@login_required()
def dataset(request):
    data_set = "predictions/dataset/austin_crime.csv"
    data = pd.read_csv(data_set, nrows=100)
    df = pd.DataFrame(data)

    # clean data
    # replacing null or nan values

    df = df[df["description"].notna()]

    x = df[{
        "address",
        "year",
        "timestamp",
        "location",
        "location_description",
        "latitude",
        "longitude",
        "description",
    }
    ].values
    y = df.loc[:, {"address", "description"}]


    # first_50 = []
    # for i, row in df.iterrows():
    #    first_50.append(row["address"])

    # print(df.groupby("address").count())
    context = {"address": df["address"].values, "description": df["description"], "latitude": df["latitude"],
               "longitude": df["longitude"]}
    print(df["address"])

    #for i in zip(x["address"],x["description"]):
    #    print(i)
    html_data = df.to_html()
    return render(request, "home/dataset.html", {"df": y["address"], "x": html_data})


def train_dataset(request):
    return 1
