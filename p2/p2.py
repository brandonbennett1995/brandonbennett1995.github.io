# %% [markdown]
# # Late Flights & Missing Data

# %%
import numpy as np
import pandas as pd
import plotly.express as px

url = (
    "https://raw.githubusercontent.com/byuidatascience/data4missing/master/"
    "data-raw/flights_missing/flights_missing.json"
)
df = pd.read_json(url)

df.drop(columns=["airport_name"], inplace=True)
df

# %%
new_headers = {
    "airport_code": "code",
    "num_of_flights_total": "total_flights",
    "num_of_delays_carrier": "carrier_delays",
    "num_of_delays_late_aircraft": "late_aircraft_delays",
    "num_of_delays_nas": "nas_delays",
    "num_of_delays_security": "security_delays",
    "num_of_delays_weather": "weather_delays",
    "num_of_delays_total": "total_delays",
    "minutes_delayed_carrier": "carrier_time",
    "minutes_delayed_late_aircraft": "late_aircraft_time",
    "minutes_delayed_nas": "nas_time",
    "minutes_delayed_security": "security_time",
    "minutes_delayed_weather": "weather_time",
    "minutes_delayed_total": "total_time",
}

df.rename(columns=new_headers, inplace=True)
col_list = df.columns.values

# %%
df.info()

# %% [markdown]
# ## Checking the text data

# %%
df.code.value_counts(dropna=False)

# %%
df.month.value_counts(dropna=False)

# %%
df.carrier_delays.value_counts(dropna=False)

# %%
# Lets replace all n/a with pd.NA, and while we're at it, fix february's spelling
df.month.replace(["n/a", "Febuary"], [np.nan, "February"], inplace=True)
df.month.value_counts(dropna=False)

# %% [markdown]
# ## Checking numeric data

# %%
df.select_dtypes(exclude="object").describe()

# %%
df.replace(-999, np.nan, inplace=True)

# %%
df["month"] = np.where(df["code"] == "ATL", df["month"].bfill(), df["month"].ffill())

df["year"] = np.where(df["code"] == "ATL", df["year"].bfill(), df["year"].ffill())

df["year"] = pd.to_numeric(df["year"], downcast="integer")

# %%
df.code = pd.Categorical(
    df.code, ordered=False, categories=["ATL", "DEN", "IAD", "ORD", "SAN", "SFO", "SLC"]
)

df.month = pd.Categorical(
    df.month,
    ordered=True,
    categories=[
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ],
)

# %%
df.pivot_table(values="code", index="year", columns="month", aggfunc="count")

# %%
for c in ["late_aircraft_delays", "carrier_time", "nas_time"]:
    df[c].fillna(np.nan, inplace=True)

df.isna().sum()

# %%
df.query("@pd.isna(late_aircraft_delays)").head(1)

# %%
worst = df[["code", "month", "year", "total_flights", "total_delays", "total_time"]]

worst = worst.assign(
    ratio_delayed=lambda x: x.total_delays / x.total_flights,
    mins_per_delay=lambda x: x.total_time / x.total_delays,
)

worst

# %%
by_code = (
    worst.groupby("code", observed=True)
    .agg(
        avg_percent_delayed=("ratio_delayed", "mean"),
        median_percent_delayed=("ratio_delayed", "median"),
        avg_time_delay=("mins_per_delay", "mean"),
        median_time_delay=("mins_per_delay", "median"),
    )
    .reset_index()
)

by_code

# %%
fig = px.bar(
    by_code,
    x="code",
    y="avg_percent_delayed",
    range_y=[0.1, 0.3],
    color="median_percent_delayed",
    text_auto=".1%",
    hover_data=["avg_percent_delayed", "median_percent_delayed"],
    labels={
        "avg_percent_delayed": "Percent of Flights Delayed (Average)",
        "median_percent_delayed": "Percent of Flights Delayed (Median)",
        "code": "Airport",
    },
)

fig.update_layout(title_text="Percent of Flights Delayed by Airport")

fig.update_yaxes(tickformat=".0%")

fig.update_coloraxes(colorbar_tickformat=".0%")

fig.show()

# %%
fig = px.bar(
    by_code,
    x="code",
    y="avg_time_delay",
    range_y=[40, 70],
    color="median_time_delay",
    text_auto=".1f",
    hover_data=["avg_time_delay", "median_time_delay"],
    labels={
        "avg_time_delay": "Average Time Delay (Minutes)",
        "median_time_delay": "Median Time Delay (Minutes)",
        "code": "Airport",
    },
)

fig.update_layout(title_text="Time Delays by Airport")

fig.show()

# %%
by_month = (
    worst.groupby("month", observed=True)
    .agg(
        avg_percent_delayed=("ratio_delayed", "mean"),
        median_percent_delayed=("ratio_delayed", "median"),
        avg_time_delay=("mins_per_delay", "mean"),
        median_time_delay=("mins_per_delay", "median"),
    )
    .reset_index()
)

by_month

# %%
fig = px.bar(
    by_month,
    x="month",
    y="avg_percent_delayed",
    range_y=[0.14, 0.26],
    color="median_percent_delayed",
    text_auto=".1%",
    hover_data=["avg_percent_delayed", "median_percent_delayed"],
    labels={
        "avg_percent_delayed": "Average",
        "median_percent_delayed": "Median",
        "month": "Month",
    },
)

fig.update_layout(title_text="Percent of Flights Delayed by Month")

fig.update_yaxes(tickformat=".0%")

fig.update_coloraxes(colorbar_tickformat=".0%")


fig.show()

# %%
fig = px.bar(
    by_month,
    x="month",
    y="avg_time_delay",
    range_y=[50, 62],
    color="median_time_delay",
    text_auto=".1f",
    hover_data=["avg_time_delay", "median_time_delay"],
    labels={
        "avg_time_delay": "Average",
        "median_time_delay": "Median",
        "month": "Month",
    },
)

fig.update_layout(title_text="Average Delay Time by Month")

fig.show()

# %%
weather = df[
    [
        "code",
        "month",
        "year",
        "total_flights",
        "total_delays",
        "late_aircraft_delays",
        "nas_delays",
        "weather_delays",
    ]
]
weather.late_aircraft_delays.fillna(weather.late_aircraft_delays.mean(), inplace=True)
weather = weather.assign(
    total_weather_delays=lambda x: np.round(
        x.weather_delays
        + (x.late_aircraft_delays * 0.3)
        + (
            x.nas_delays
            * np.where(
                (x.month.isin(["April", "May", "June", "July", "August"])), 0.4, 0.65
            )
        )
    ),
    percent_weather_delays=lambda x: x.total_weather_delays / x.total_delays,
)
weather.head()

# %%
dat = (
    weather.groupby("code", observed=True)
    .agg(avg_ratio_weather_delays=("percent_weather_delays", "mean"))
    .reset_index()
)

dat

# %%
fig = px.bar(
    dat,
    x="code",
    y="avg_ratio_weather_delays",
    range_y=[0.25, 0.4],
    text_auto=".1%",
    labels={"avg_ratio_weather_delays": "Percent", "code": "Airport"},
)

fig.update_layout(title_text="Percent of Total Delays caused by Weather")

fig.update_yaxes(tickformat=".0%")

fig.show()
