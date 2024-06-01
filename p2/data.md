# Missing Data

## Motor Trend Car Road Tests

The data is called `mtcars_missing`. The data was extracted from the *1974 Motor Trend US* magazine, and comprises fuel consumption and 10 aspects of automobile design and performance for 32 automobiles *(1973–74 models)*.

### Data Source

- [Motor Trend Car Road Tests (1974)](https://figshare.com/articles/dataset/Motor_Trend_Car_Road_Tests/3122005)

### Data Format

A data frame with columns:

| Variable | Class     | Description                              |
|:---------|:----------|:-----------------------------------------|
| `car`    | character | N/A                                      |
| `mpg`    | numeric   | Miles/(US) gallon                        |
| `cyl`    | integer   | Number of cylinders                      |
| `disp`   | numeric   | Displacement (cu.in.)                    |
| `hp`     | integer   | Gross horsepower                         |
| `drat`   | numeric   | Rear axle ratio                          |
| `wt`     | numeric   | Weight (1000 lbs)                        |
| `qsec`   | numeric   | 1/4 mile time                            |
| `vs`     | integer   | Engine (0 = V-shaped, 1 = straight)      |
| `am`     | integer   | Transmission (0 = automatic, 1 = manual) |
| `gear`   | integer   | Number of forward gears                  |
| `carb`   | integer   | Number of carburetors                    |

## Airline Delays (US)

The data is called `flights_missing`. Monthly Airline Delays by Airport for US Flights, 2003-2016

### Data Sources

- [CORGIS](https://think.cs.vt.edu/corgis/datasets/json/airlines/airlines.json)
- [BYUI-Github](https://github.com/byuistats/CSE250)

### Data Format

A data frame with columns:

| Variable                        | Class     | Description                    |
|:--------------------------------|:----------|:-------------------------------|
| `airport_code`                  | character | Airport Code                   |
| `airport_name`                  | character | Airport Name                   |
| `month`                         | character | Month                          |
| `year`                          | integer   | Year                           |
| `num_of_flights_total`          | integer   | Number Of Flights Total        |
| `num_of_delays_carrier`         | character | Number Of Delays Carrier       |
| `num_of_delays_late_aircraft`   | integer   | Number Of Delays Late Aircraft |
| `num_of_delays_nas`             | integer   | Number Of Delays Nas           |
| `num_of_delays_security`        | integer   | Number Of Delays Security      |
| `num_of_delays_weather`         | integer   | Number Of Delays Weather       |
| `num_of_delays_total`           | integer   | Number Of Delays Total         |
| `minutes_delayed_carrier`       | integer   | Minutes Delayed Carrier        |
| `minutes_delayed_late_aircraft` | integer   | Minutes Delayed Late Aircraft  |
| `minutes_delayed_nas`           | integer   | Minutes Delayed Nas            |
| `minutes_delayed_security`      | integer   | Minutes Delayed Security       |
| `minutes_delayed_weather`       | integer   | Minutes Delayed Weather        |
| `minutes_delayed_total`         | integer   | Minutes Delayed Total          |
