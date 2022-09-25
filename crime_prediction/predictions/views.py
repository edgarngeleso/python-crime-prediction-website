import base64
from io import BytesIO

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Predictions

# importing relevant libraries
from sklearn.metrics import confusion_matrix
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("Agg")
import random


def predicted_case(address, year, census_tract, location, location_description, latitude, longitude, description,
                   primary_type):
    trained_model = joblib.load("predictions/dataset/model.pkl")
    scalers = joblib.load("predictions/dataset/scaler.pkl")

    data = [address, year, census_tract, location, location_description, latitude, longitude, description,
            primary_type]
    scaled_data = scalers.fit_transform(data)
    predicted = trained_model.predict([scaled_data])

    result = "OTHER"
    if predicted == 0:
        result = "OTHER"
    elif predicted == 1:
        result = "THEFT"
    elif predicted == 2:
        result = "AGG ASLT ENHANC STRANGL/SUFFOC"
    elif predicted == 3:
        result = "AGG ASLT STRANGLE/SUFFOCATE"
    elif predicted == 4:
        result = "AGG ASLT W/MOTOR VEH FAM/DAT V"
    elif predicted == 5:
        result = "AGG ASSAULT"
    elif predicted == 6:
        result = "AGG ASSAULT FAM/DATE VIOLENCE"
    elif predicted == 7:
        result = "AGG ASSAULT ON PUBLIC SERVANT"
    elif predicted == 8:
        result = "AGG ASSAULT WITH MOTOR VEH"
    elif predicted == 9:
        result = "AGG RAPE"
    elif predicted == 10:
        result = "AGG RAPE OF A CHILD"
    elif predicted == 11:
        result = "AGG ROBBERY BY ASSAULT"
    elif predicted == 12:
        result = "AGG ROBBERY/DEADLY WEAPON"
    elif predicted == 13:
        result = "AIRPORT - BREACH OF SECURITY"
    elif predicted == 14:
        result = "AUTO THEFT"
    elif predicted == 15:
        result = "BREACH OF COMPUTER SECURITY"
    elif predicted == 16:
        result = "BURG NON RESIDENCE SHEDS"
    elif predicted == 17:
        result = "BURG OF RES - SEXUAL NATURE"
    elif predicted == 18:
        result = "BURGLARY NON RESIDENCE"
    elif predicted == 19:
        result = "BURGLARY OF COIN-OP MACHINE"
    elif predicted == 20:
        result = "BURGLARY OF RESIDENCE"
    elif predicted == 21:
        result = "BURGLARY OF VEHICLE"
    elif predicted == 22:
        result = "CAPITAL MURDER"
    elif predicted == 23:
        result = "DEADLY CONDUCT"
    elif predicted == 24:
        result = "DEADLY CONDUCT FAM/DATE VIOL"
    elif predicted == 25:
        result = "MANSLAUGHTER"
    elif predicted == 26:
        result = "MISAPPLY FIDUCIARY PROP"
    elif predicted == 27:
        result = "MURDER"
    elif predicted == 28:
        result = "PURSE SNATCHING"
    elif predicted == 29:
        result = "RAPE"
    elif predicted == 30:
        result = "RAPE OF A CHILD"
    elif predicted == 31:
        result = "ROBBERY BY ASSAULT"
    elif predicted == 32:
        result = "ROBBERY BY THREAT"
    elif predicted == 33:
        result = "TAKE WEAPON FRM POLICE OFFICER"
    elif predicted == 34:
        result = "THEFT BY SHOPLIFTING"
    elif predicted == 35:
        result = "THEFT CATALYTIC CONVERTER"
    elif predicted == 36:
        result = "THEFT FROM AUTO"
    elif predicted == 37:
        result = "THEFT FROM BUILDING"
    elif predicted == 38:
        result = "THEFT FROM PERSON"
    elif predicted == 39:
        result = "THEFT OF AUTO PARTS"
    elif predicted == 40:
        result = "THEFT OF BICYCLE"
    elif predicted == 41:
        result = "THEFT OF HEAVY EQUIPMENT"
    elif predicted == 42:
        result = "THEFT OF LICENSE PLATE"
    elif predicted == 43:
        result = "THEFT OF METAL"
    elif predicted == 44:
        result = "THEFT OF VEHICLE/OTHER"
    elif predicted == 45:
        result = "THEFT/TILL TAPPING"
    return result


@login_required()
def prediction(request):
    result = []
    if request.method == "POST":
        region = request.POST.get("region")
        c_date = request.POST.get("date")
        c_hour = request.POST.get("hour")
        latitude = request.POST.get("latitude")
        longitude = request.POST.get("longitude")
        case = predicted_case(region, "2021", f"{c_date} {c_hour}", f"({latitude}{longitude}", "Not Applicable",
                              latitude, longitude, "Not applicable", "Not applicable")

        predicted = Predictions(address=region, crime_date=c_date, hour=c_hour, latitude=latitude, longitude=longitude,
                                predicted_case=case)
        predicted.save()

        data = {"region": region, "date": c_date, "hour": c_hour, "latitude": latitude, "longitude": longitude,
                "predicted_case": case}
        result = data
    return render(request, "predictions/predict.html", {"results": result})


@login_required()
def results(request):
    return render(request, "predictions/results.html")


@login_required()
def summary(request):
    dataset = "predictions/dataset/austin_crime.csv"
    trained_model = "predictions/dataset/model.pkl"
    scalers = "predictions/dataset/scaler.pkl"

    data = pd.read_csv(dataset, nrows=100)
    df = pd.DataFrame(data)

    # clean data ie remove rows without complete data

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
    ]
    y = df.loc[:, {"address", "description"}]

    return render(request, "predictions/summary.html", {"df": "confusion matrix"})
