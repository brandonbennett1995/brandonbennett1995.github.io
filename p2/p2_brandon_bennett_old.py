# %%
import numpy as np
import pandas as pd
import altair as alt

df = pd.read_json(
    "https://github.com/byuidatascience/data4missing/raw/master/data-raw/flights_missing/flights_missing.json")

df.head()

# %% [markdown]
# I'm going to clean up these column headers to make my work easier.

# %%
df.drop(columns=['airport_name'], inplace=True)
new_names = {
    i: '_'.join([x for x in i.split("_") if x not in ['num', 'of', 'minutes', 'airport']][1:] + [
                         x for x in i.split("_") if x not in ['num', 'of', 'minutes', 'airport']][:1]) for i in df.columns.values}
df.rename(columns=new_names, inplace=True)

# %%
df.replace(to_replace=['n/a', -999], value=np.nan, inplace=True)
df

# %%
df['month'] = np.where(df['code'] == "ATL",
                       df['month'].bfill(), df['month'].ffill())
df['year'] = np.where(df['code'] == "ATL",
                      df['year'].bfill(), df['year'].ffill())
df.pivot_table(values='code', index='year', columns='month', aggfunc='count')
df = df.replace(to_replace=['Febuary'], value='February')

# %% [markdown]
# ## Which airport has the worst delays?

# %%

by_apt = df.groupby('code')

by_apt = by_apt.agg(
    num_flights=('total_flights', 'sum'),
    num_delays=('total_delays', 'sum'),
    total_time=('total_delayed', 'sum')
).reset_index()

by_apt


# %%
by_apt = by_apt.assign(
    percent_delayed=lambda x: (x.num_delays / x.num_flights) * 100,
    avg_time_per_delay=lambda x: x.total_time / x.num_delays
)

by_apt.round(2)

# %%
alt.Chart(by_apt).mark_bar().encode(
    x=alt.X(
        "code",
        title="Airport",
        axis=alt.Axis(labelAngle=0)),
    y=alt.Y(
        "avg_time_per_delay",
        title="Minutes",
        scale=alt.Scale(domain=(40, 70)))
).properties(
    width=800,
    height=400,
    title="Average Delay Times"
)

# %%
alt.Chart(by_apt).mark_bar().encode(
    x=alt.X(
        "percent_delayed",
        title="Percent",
        scale=alt.Scale(domain=(7.5, 27.5))),
    y=alt.Y(
        "code",
        title="Airport",
        sort="-x")
).properties(
    height=200,
    width=800,
    title="Percent Delayed"
)

# %%
by_months = df.groupby(by=['month'])
by_months = by_months.agg(
    num_flights=('total_flights', 'sum'),
    num_delays=('total_delays', 'sum'),
    total_time=('total_delayed', 'sum')
).reset_index()
by_months

# %%
by_months = by_months.assign(
    percent_delays=lambda x: x.num_delays / x.num_flights * 100,
    avg_time_per_delay=lambda x: x.total_time / x.num_delays
)

by_months.round(2)

# %%
alt.Chart(by_months).mark_bar().encode(
    x=alt.X(
        "month",
        title="Month"
    ),
    y=alt.Y(
        "avg_time_per_delay",
        title="Time",
        scale=alt.Scale(domain=(50, 65))
    )
).properties(
    width=800,
    height=400,
    title="Average Time per Delay"
)

# %%
df.to_csv("flight_data.csv", index=False)
