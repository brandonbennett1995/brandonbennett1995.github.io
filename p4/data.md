## Denver residential dwelling sales for 2013

The data is called `dwellings_denver`.

### Description

Attributes of each dwelling with their selling price for homes that sold in Denver in 2013: [Source](https://www.denvergov.org/opendata/dataset/city-and-county-of-denver-real-property-sales-book-2013)

### Data format

A data frame with columns:

| Variable    | Class | Description                                              |
|:------------|:------|:---------------------------------------------------------|
| `parcel`    | `A-Z` | The parcel id                                            |
| `nbhd`      | `#`   | Neighborhood of the home                                 |
| `abstrprd`  | `#`   | No clue                                                  |
| `livearea`  | `#`   | Square footage that is liveable                          |
| `finbsmnt`  | `#`   | Square footage finished in the basement                  |
| `basement`  | `#`   | Total square footage of the basement                     |
| `yrbuilt`   | `#`   | Year the home was built                                  |
| `condition` | `A-Z` | Condition of the home (6 levels provided)                |
| `quality`   | `A-Z` | A letter ratting                                         |
| `totunits`  | `#`   | How many dwelling units in the building                  |
| `stories`   | `#`   | The number of stories                                    |
| `gartype`   | `A-Z` | Details on the garage type                               |
| `nocars`    | `#`   | Size of the garage in cars                               |
| `xtraffic`  | `T/F` | Empty                                                    |
| `floorlvl`  | `#`   | What level the living unit is on^[Mostly for apartments] |
| `numbdrm`   | `#`   | Number of bedrooms                                       |
| `numbaths`  | `#`   | Number of bathrooms                                      |
| `arcstyle`  | `A-Z` | Type of home                                             |
| `sprice`    | `#`   | Selling price                                            |
| `deduct`    | `#`   | Deduction from the selling price                         |
| `netprice`  | `#`   | Net price of home                                        |
| `tasp`      | `#`   | Tax assessed selling price                               |
| `smonth`    | `#`   | Month sold                                               |
| `syear`     | `#`   | Year sold                                                |
| `qualified` | `A-Z` | Q or U with 66 percent Q                                 |
| `status`    | `A-Z` | I or V with over 90 percent I                            |


## Denver residential dwelling sales for 2013

The data is called `dwellings_ml`.

### Description

Attributes of each dwelling with their selling price in machine learning format

<!-- [Source](https://www.denvergov.org/opendata/dataset/city-and-county-of-denver-real-property-sales-book-2013) -->

### Data format

A data frame with columns:

| Variable                           | Class | Description                             |
|:-----------------------------------|:------|:----------------------------------------|
| `abstrprd`                         | `#`   | No clue                                 |
| `arcstyle_BI-LEVEL`                | `#`   | `0 or 1`                                |
| `arcstyle_CONVERSIONS`             | `#`   | `0 or 1`                                |
| `arcstyle_END UNIT`                | `#`   | `0 or 1`                                |
| `arcstyle_MIDDLE UNIT`             | `#`   | `0 or 1`                                |
| `arcstyle_ONE AND HALF-STORY`      | `#`   | `0 or 1`                                |
| `arcstyle_ONE-STORY`               | `#`   | `0 or 1`                                |
| `arcstyle_SPLIT LEVEL`             | `#`   | `0 or 1`                                |
| `arcstyle_THREE-STORY`             | `#`   | `0 or 1`                                |
| `arcstyle_TRI-LEVEL WITH BASEMENT` | `#`   | `0 or 1`                                |
| `arcstyle_TRI-LEVEL`               | `#`   | `0 or 1`                                |
| `arcstyle_TWO AND HALF-STORY`      | `#`   | `0 or 1`                                |
| `arcstyle_TWO-STORY`               | `#`   | `0 or 1`                                |
| `basement`                         | `#`   | Total square footage of the basement    |
| `before1980`                       | `#`   | `0 or 1`                                |
| `condition_AVG`                    | `#`   | `0 or 1`                                |
| `condition_Excel`                  | `#`   | `0 or 1`                                |
| `condition_Fair`                   | `#`   | `0 or 1`                                |
| `condition_Good`                   | `#`   | `0 or 1`                                |
| `condition_VGood`                  | `#`   | `0 or 1`                                |
| `deduct`                           | `#`   | Deduction from the selling price        |
| `finbsmnt`                         | `#`   | Square footage finished in the basement |
| `gartype_att/CP`                   | `#`   | `0 or 1`                                |
| `gartype_Att/Det`                  | `#`   | `0 or 1`                                |
| `gartype_Att`                      | `#`   | `0 or 1`                                |
| `gartype_CP`                       | `#`   | `0 or 1`                                |
| `gartype_det/CP`                   | `#`   | `0 or 1`                                |
| `gartype_Det`                      | `#`   | `0 or 1`                                |
| `gartype_None`                     | `#`   | `0 or 1`                                |
| `livearea`                         | `#`   | Square footage that is liveable         |
| `netprice`                         | `#`   | Net price of home                       |
| `nocars`                           | `#`   | Size of the garage in cars              |
| `numbaths`                         | `#`   | Number of bathrooms                     |
| `numbdrm`                          | `#`   | Number of bedrooms                      |
| `parcel`                           | `A-Z` | The parcel id                           |
| `qualified_Q`                      | `#`   | `0 or 1`                                |
| `qualified_U`                      | `#`   | `0 or 1`                                |
| `quality_A`                        | `#`   | `0 or 1`                                |
| `quality_B`                        | `#`   | `0 or 1`                                |
| `quality_C`                        | `#`   | `0 or 1`                                |
| `quality_D`                        | `#`   | `0 or 1`                                |
| `quality_X`                        | `#`   | `0 or 1`                                |
| `smonth`                           | `#`   | Month sold                              |
| `sprice`                           | `#`   | Selling price                           |
| `status_I`                         | `#`   | `0 or 1`                                |
| `status_V`                         | `#`   | `0 or 1`                                |
| `stories`                          | `#`   | The number of stories                   |
| `syear`                            | `#`   | Year sold                               |
| `tasp`                             | `#`   | Tax assessed selling price              |
| `totunits`                         | `#`   | How many dwelling units in the building |
| `yrbuilt`                          | `#`   | Year the home was built                 |



## One Hot Encoded Neighborhood Variable

The data is called `dwellings_neighborhoods_ml`.

### Description

Neighborhood attributes for homes that sold in Denver in 2013: [Source](https://www.denvergov.org/opendata/dataset/city-and-county-of-denver-real-property-sales-book-2013)

### Data Format

A data frame with columns:

| Variable   | Class | Description   |
|:-----------|:------|:--------------|
| `parcel`   | `A-Z` | The parcel id |
| `nbhd_1`   | `#`   | `0 or 1`      |
| `nbhd_2`   | `#`   | `0 or 1`      |
| `nbhd_3`   | `#`   | `0 or 1`      |
| `nbhd_4`   | `#`   | `0 or 1`      |
| `nbhd_5`   | `#`   | `0 or 1`      |
| `nbhd_101` | `#`   | `0 or 1`      |
| `nbhd_104` | `#`   | `0 or 1`      |
| `nbhd_105` | `#`   | `0 or 1`      |
| `nbhd_106` | `#`   | `0 or 1`      |
| `nbhd_107` | `#`   | `0 or 1`      |
| `nbhd_108` | `#`   | `0 or 1`      |
| `nbhd_109` | `#`   | `0 or 1`      |
| `nbhd_110` | `#`   | `0 or 1`      |
| `nbhd_111` | `#`   | `0 or 1`      |
| `nbhd_112` | `#`   | `0 or 1`      |
| `nbhd_113` | `#`   | `0 or 1`      |
| `nbhd_114` | `#`   | `0 or 1`      |
| `nbhd_115` | `#`   | `0 or 1`      |
| `nbhd_116` | `#`   | `0 or 1`      |
| `nbhd_117` | `#`   | `0 or 1`      |
| `nbhd_118` | `#`   | `0 or 1`      |
| `nbhd_120` | `#`   | `0 or 1`      |
| `nbhd_121` | `#`   | `0 or 1`      |
| `nbhd_122` | `#`   | `0 or 1`      |
| `nbhd_123` | `#`   | `0 or 1`      |
| `nbhd_124` | `#`   | `0 or 1`      |
| `nbhd_127` | `#`   | `0 or 1`      |
| `nbhd_128` | `#`   | `0 or 1`      |
| `nbhd_129` | `#`   | `0 or 1`      |
| `nbhd_130` | `#`   | `0 or 1`      |
| `nbhd_131` | `#`   | `0 or 1`      |
| `nbhd_132` | `#`   | `0 or 1`      |
| `nbhd_133` | `#`   | `0 or 1`      |
| `nbhd_201` | `#`   | `0 or 1`      |
| `nbhd_202` | `#`   | `0 or 1`      |
| `nbhd_203` | `#`   | `0 or 1`      |
| `nbhd_205` | `#`   | `0 or 1`      |
| `nbhd_206` | `#`   | `0 or 1`      |
| `nbhd_207` | `#`   | `0 or 1`      |
| `nbhd_208` | `#`   | `0 or 1`      |
| `nbhd_210` | `#`   | `0 or 1`      |
| `nbhd_211` | `#`   | `0 or 1`      |
| `nbhd_212` | `#`   | `0 or 1`      |
| `nbhd_213` | `#`   | `0 or 1`      |
| `nbhd_214` | `#`   | `0 or 1`      |
| `nbhd_215` | `#`   | `0 or 1`      |
| `nbhd_216` | `#`   | `0 or 1`      |
| `nbhd_217` | `#`   | `0 or 1`      |
| `nbhd_218` | `#`   | `0 or 1`      |
| `nbhd_219` | `#`   | `0 or 1`      |
| `nbhd_220` | `#`   | `0 or 1`      |
| `nbhd_221` | `#`   | `0 or 1`      |
| `nbhd_222` | `#`   | `0 or 1`      |
| `nbhd_224` | `#`   | `0 or 1`      |
| `nbhd_225` | `#`   | `0 or 1`      |
| `nbhd_226` | `#`   | `0 or 1`      |
| `nbhd_227` | `#`   | `0 or 1`      |
| `nbhd_228` | `#`   | `0 or 1`      |
| `nbhd_229` | `#`   | `0 or 1`      |
| `nbhd_230` | `#`   | `0 or 1`      |
| `nbhd_231` | `#`   | `0 or 1`      |
| `nbhd_232` | `#`   | `0 or 1`      |
| `nbhd_233` | `#`   | `0 or 1`      |
| `nbhd_234` | `#`   | `0 or 1`      |
| `nbhd_235` | `#`   | `0 or 1`      |
| `nbhd_237` | `#`   | `0 or 1`      |
| `nbhd_238` | `#`   | `0 or 1`      |
| `nbhd_239` | `#`   | `0 or 1`      |
| `nbhd_240` | `#`   | `0 or 1`      |
| `nbhd_241` | `#`   | `0 or 1`      |
| `nbhd_242` | `#`   | `0 or 1`      |
| `nbhd_243` | `#`   | `0 or 1`      |
| `nbhd_244` | `#`   | `0 or 1`      |
| `nbhd_245` | `#`   | `0 or 1`      |
| `nbhd_247` | `#`   | `0 or 1`      |
| `nbhd_248` | `#`   | `0 or 1`      |
| `nbhd_249` | `#`   | `0 or 1`      |
| `nbhd_250` | `#`   | `0 or 1`      |
| `nbhd_252` | `#`   | `0 or 1`      |
| `nbhd_253` | `#`   | `0 or 1`      |
| `nbhd_254` | `#`   | `0 or 1`      |
| `nbhd_255` | `#`   | `0 or 1`      |
| `nbhd_256` | `#`   | `0 or 1`      |
| `nbhd_257` | `#`   | `0 or 1`      |
| `nbhd_258` | `#`   | `0 or 1`      |
| `nbhd_259` | `#`   | `0 or 1`      |
| `nbhd_260` | `#`   | `0 or 1`      |
| `nbhd_301` | `#`   | `0 or 1`      |
| `nbhd_302` | `#`   | `0 or 1`      |
| `nbhd_401` | `#`   | `0 or 1`      |
| `nbhd_402` | `#`   | `0 or 1`      |
| `nbhd_403` | `#`   | `0 or 1`      |
| `nbhd_404` | `#`   | `0 or 1`      |
| `nbhd_503` | `#`   | `0 or 1`      |
| `nbhd_504` | `#`   | `0 or 1`      |
| `nbhd_505` | `#`   | `0 or 1`      |
| `nbhd_506` | `#`   | `0 or 1`      |
| `nbhd_507` | `#`   | `0 or 1`      |
| `nbhd_508` | `#`   | `0 or 1`      |
| `nbhd_509` | `#`   | `0 or 1`      |
| `nbhd_510` | `#`   | `0 or 1`      |
| `nbhd_511` | `#`   | `0 or 1`      |
| `nbhd_512` | `#`   | `0 or 1`      |
| `nbhd_513` | `#`   | `0 or 1`      |
| `nbhd_514` | `#`   | `0 or 1`      |
| `nbhd_515` | `#`   | `0 or 1`      |
| `nbhd_517` | `#`   | `0 or 1`      |
| `nbhd_518` | `#`   | `0 or 1`      |
| `nbhd_519` | `#`   | `0 or 1`      |
| `nbhd_520` | `#`   | `0 or 1`      |
| `nbhd_521` | `#`   | `0 or 1`      |
| `nbhd_522` | `#`   | `0 or 1`      |
| `nbhd_523` | `#`   | `0 or 1`      |
| `nbhd_524` | `#`   | `0 or 1`      |
| `nbhd_525` | `#`   | `0 or 1`      |
| `nbhd_526` | `#`   | `0 or 1`      |
| `nbhd_527` | `#`   | `0 or 1`      |
| `nbhd_528` | `#`   | `0 or 1`      |
| `nbhd_529` | `#`   | `0 or 1`      |
| `nbhd_530` | `#`   | `0 or 1`      |
| `nbhd_531` | `#`   | `0 or 1`      |
| `nbhd_532` | `#`   | `0 or 1`      |
| `nbhd_533` | `#`   | `0 or 1`      |
| `nbhd_534` | `#`   | `0 or 1`      |
| `nbhd_535` | `#`   | `0 or 1`      |
| `nbhd_536` | `#`   | `0 or 1`      |
| `nbhd_537` | `#`   | `0 or 1`      |
| `nbhd_538` | `#`   | `0 or 1`      |
| `nbhd_539` | `#`   | `0 or 1`      |
| `nbhd_540` | `#`   | `0 or 1`      |
| `nbhd_541` | `#`   | `0 or 1`      |
| `nbhd_543` | `#`   | `0 or 1`      |
| `nbhd_544` | `#`   | `0 or 1`      |
| `nbhd_545` | `#`   | `0 or 1`      |
| `nbhd_546` | `#`   | `0 or 1`      |
| `nbhd_547` | `#`   | `0 or 1`      |
| `nbhd_548` | `#`   | `0 or 1`      |
| `nbhd_549` | `#`   | `0 or 1`      |
| `nbhd_550` | `#`   | `0 or 1`      |
| `nbhd_551` | `#`   | `0 or 1`      |
| `nbhd_552` | `#`   | `0 or 1`      |
| `nbhd_553` | `#`   | `0 or 1`      |
| `nbhd_555` | `#`   | `0 or 1`      |
| `nbhd_556` | `#`   | `0 or 1`      |
| `nbhd_580` | `#`   | `0 or 1`      |
| `nbhd_581` | `#`   | `0 or 1`      |
| `nbhd_582` | `#`   | `0 or 1`      |
| `nbhd_583` | `#`   | `0 or 1`      |
| `nbhd_584` | `#`   | `0 or 1`      |
| `nbhd_585` | `#`   | `0 or 1`      |
| `nbhd_586` | `#`   | `0 or 1`      |
| `nbhd_587` | `#`   | `0 or 1`      |
| `nbhd_588` | `#`   | `0 or 1`      |
| `nbhd_589` | `#`   | `0 or 1`      |
| `nbhd_590` | `#`   | `0 or 1`      |
| `nbhd_591` | `#`   | `0 or 1`      |
| `nbhd_592` | `#`   | `0 or 1`      |
| `nbhd_593` | `#`   | `0 or 1`      |
| `nbhd_594` | `#`   | `0 or 1`      |
| `nbhd_596` | `#`   | `0 or 1`      |
| `nbhd_597` | `#`   | `0 or 1`      |
| `nbhd_598` | `#`   | `0 or 1`      |
| `nbhd_599` | `#`   | `0 or 1`      |
| `nbhd_601` | `#`   | `0 or 1`      |
| `nbhd_602` | `#`   | `0 or 1`      |
| `nbhd_604` | `#`   | `0 or 1`      |
| `nbhd_605` | `#`   | `0 or 1`      |
| `nbhd_606` | `#`   | `0 or 1`      |
| `nbhd_607` | `#`   | `0 or 1`      |
| `nbhd_611` | `#`   | `0 or 1`      |
| `nbhd_612` | `#`   | `0 or 1`      |
| `nbhd_613` | `#`   | `0 or 1`      |
| `nbhd_614` | `#`   | `0 or 1`      |
| `nbhd_615` | `#`   | `0 or 1`      |
| `nbhd_616` | `#`   | `0 or 1`      |
| `nbhd_617` | `#`   | `0 or 1`      |
| `nbhd_618` | `#`   | `0 or 1`      |
| `nbhd_620` | `#`   | `0 or 1`      |
| `nbhd_621` | `#`   | `0 or 1`      |
| `nbhd_622` | `#`   | `0 or 1`      |
| `nbhd_623` | `#`   | `0 or 1`      |
| `nbhd_624` | `#`   | `0 or 1`      |
| `nbhd_625` | `#`   | `0 or 1`      |
| `nbhd_627` | `#`   | `0 or 1`      |
| `nbhd_628` | `#`   | `0 or 1`      |
| `nbhd_629` | `#`   | `0 or 1`      |
| `nbhd_630` | `#`   | `0 or 1`      |
| `nbhd_631` | `#`   | `0 or 1`      |
| `nbhd_634` | `#`   | `0 or 1`      |
| `nbhd_635` | `#`   | `0 or 1`      |
| `nbhd_636` | `#`   | `0 or 1`      |
| `nbhd_637` | `#`   | `0 or 1`      |
| `nbhd_638` | `#`   | `0 or 1`      |
| `nbhd_639` | `#`   | `0 or 1`      |
| `nbhd_640` | `#`   | `0 or 1`      |
| `nbhd_641` | `#`   | `0 or 1`      |
| `nbhd_642` | `#`   | `0 or 1`      |
| `nbhd_643` | `#`   | `0 or 1`      |
| `nbhd_644` | `#`   | `0 or 1`      |
| `nbhd_645` | `#`   | `0 or 1`      |
| `nbhd_646` | `#`   | `0 or 1`      |
| `nbhd_647` | `#`   | `0 or 1`      |
| `nbhd_648` | `#`   | `0 or 1`      |
| `nbhd_649` | `#`   | `0 or 1`      |
| `nbhd_650` | `#`   | `0 or 1`      |
| `nbhd_651` | `#`   | `0 or 1`      |
| `nbhd_652` | `#`   | `0 or 1`      |
| `nbhd_653` | `#`   | `0 or 1`      |
| `nbhd_654` | `#`   | `0 or 1`      |
| `nbhd_655` | `#`   | `0 or 1`      |
| `nbhd_656` | `#`   | `0 or 1`      |
| `nbhd_657` | `#`   | `0 or 1`      |
| `nbhd_658` | `#`   | `0 or 1`      |
| `nbhd_659` | `#`   | `0 or 1`      |
| `nbhd_660` | `#`   | `0 or 1`      |
| `nbhd_661` | `#`   | `0 or 1`      |
| `nbhd_663` | `#`   | `0 or 1`      |
| `nbhd_664` | `#`   | `0 or 1`      |
| `nbhd_665` | `#`   | `0 or 1`      |
| `nbhd_666` | `#`   | `0 or 1`      |
| `nbhd_667` | `#`   | `0 or 1`      |
| `nbhd_668` | `#`   | `0 or 1`      |
| `nbhd_669` | `#`   | `0 or 1`      |
| `nbhd_670` | `#`   | `0 or 1`      |
| `nbhd_671` | `#`   | `0 or 1`      |
| `nbhd_672` | `#`   | `0 or 1`      |
| `nbhd_673` | `#`   | `0 or 1`      |
| `nbhd_674` | `#`   | `0 or 1`      |
| `nbhd_675` | `#`   | `0 or 1`      |
| `nbhd_676` | `#`   | `0 or 1`      |
| `nbhd_678` | `#`   | `0 or 1`      |
| `nbhd_679` | `#`   | `0 or 1`      |
| `nbhd_680` | `#`   | `0 or 1`      |
| `nbhd_681` | `#`   | `0 or 1`      |
| `nbhd_682` | `#`   | `0 or 1`      |
| `nbhd_683` | `#`   | `0 or 1`      |
| `nbhd_690` | `#`   | `0 or 1`      |
| `nbhd_691` | `#`   | `0 or 1`      |
| `nbhd_692` | `#`   | `0 or 1`      |
| `nbhd_693` | `#`   | `0 or 1`      |
| `nbhd_694` | `#`   | `0 or 1`      |
| `nbhd_695` | `#`   | `0 or 1`      |
| `nbhd_698` | `#`   | `0 or 1`      |
| `nbhd_702` | `#`   | `0 or 1`      |
| `nbhd_703` | `#`   | `0 or 1`      |
| `nbhd_704` | `#`   | `0 or 1`      |
| `nbhd_705` | `#`   | `0 or 1`      |
| `nbhd_706` | `#`   | `0 or 1`      |
| `nbhd_707` | `#`   | `0 or 1`      |
| `nbhd_708` | `#`   | `0 or 1`      |
| `nbhd_709` | `#`   | `0 or 1`      |
| `nbhd_710` | `#`   | `0 or 1`      |
| `nbhd_711` | `#`   | `0 or 1`      |
| `nbhd_712` | `#`   | `0 or 1`      |
| `nbhd_713` | `#`   | `0 or 1`      |
| `nbhd_714` | `#`   | `0 or 1`      |
| `nbhd_715` | `#`   | `0 or 1`      |
| `nbhd_716` | `#`   | `0 or 1`      |
| `nbhd_717` | `#`   | `0 or 1`      |
| `nbhd_718` | `#`   | `0 or 1`      |
| `nbhd_719` | `#`   | `0 or 1`      |
| `nbhd_720` | `#`   | `0 or 1`      |
| `nbhd_801` | `#`   | `0 or 1`      |
| `nbhd_802` | `#`   | `0 or 1`      |
| `nbhd_803` | `#`   | `0 or 1`      |
| `nbhd_804` | `#`   | `0 or 1`      |
| `nbhd_805` | `#`   | `0 or 1`      |
| `nbhd_901` | `#`   | `0 or 1`      |
| `nbhd_902` | `#`   | `0 or 1`      |
| `nbhd_903` | `#`   | `0 or 1`      |
| `nbhd_904` | `#`   | `0 or 1`      |
| `nbhd_905` | `#`   | `0 or 1`      |
| `nbhd_906` | `#`   | `0 or 1`      |

