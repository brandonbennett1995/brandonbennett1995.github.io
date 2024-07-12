# Missing Data

## Airline Delays (US)

The data is called `flights_missing`. Monthly Airline Delays by Airport for US Flights, 2003-2016

### Data Sources

- [CORGIS](https://think.cs.vt.edu/corgis/datasets/json/airlines/airlines.json)
- [BYUI-Github](https://github.com/byuistats/CSE250)

### Data Format

A data frame with columns:

| Variable                        | Class     | Description                    |
| :------------------------------ | :-------- | :----------------------------- |
| `airport_code`                  | character | Airport Code                   |
| `airport_name`                  | character | Airport Name                   |
| `month`                         | character | Month                          |
| `year`                          | integer   | Year                           |
| `num_of_flights_total`          | integer   | Number Of Flights Total        |
| `num_of_delays_carrier`         | character | Number Of Delays Carrier       |
| `num_of_delays_late_aircraft`   | integer   | Number Of Delays Late Aircraft |
| `num_of_delays_nas`             | integer   | Number Of Delays NAS           |
| `num_of_delays_security`        | integer   | Number Of Delays Security      |
| `num_of_delays_weather`         | integer   | Number Of Delays Weather       |
| `num_of_delays_total`           | integer   | Number Of Delays Total         |
| `minutes_delayed_carrier`       | integer   | Minutes Delayed Carrier        |
| `minutes_delayed_late_aircraft` | integer   | Minutes Delayed Late Aircraft  |
| `minutes_delayed_nas`           | integer   | Minutes Delayed NAS            |
| `minutes_delayed_security`      | integer   | Minutes Delayed Security       |
| `minutes_delayed_weather`       | integer   | Minutes Delayed Weather        |
| `minutes_delayed_total`         | integer   | Minutes Delayed Total          |

## Notes

```python
df.shape  # This returns (rows, columns)

# What does a row represent in this dataset?
# - A row is a reported ufo sighting

# What are the different ways missing values are encoded?

# Object columns
df['column_name'].value_counts(dropna=False)

# Numeric columns
df.['column_name'].describe()  # -999 looks like a missing value encoding


# How many np.nan in each column?
df.isna().sum()
```
