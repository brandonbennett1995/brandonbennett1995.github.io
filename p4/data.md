# Denver residential dwelling sales for 2013

```python
# Things to do to explore the data

```

The data is called `dwellings_denver`.

***Description***

Attributes of each dwelling with their selling price for homes that sold in Denver in 2013

[Data Source](https://www.denvergov.org/opendata/dataset/city-and-county-of-denver-real-property-sales-book-2013)

***Data Format***

A data frame with columns:

| Variable  | Class     | Description                               |
|:----------|:----------|:------------------------------------------|
| parcel    | character | The parcel id                             |
| nbhd      | numeric   | Neigborhood of the home                   |
| abstrprd  | numeric   | No clue                                   |
| livearea  | numeric   | Square footage that is liveable           |
| finbsmnt  | numeric   | Square footage finished in the basement   |
| basement  | numeric   | Total square footage of the basement      |
| yrbuilt   | numeric   | Year the home was built                   |
| condition | character | Condition of the home (6 levels provided) |
| quality   | character | A letter rating                           |
| totunits  | numeric   | How many dwelling units in the building   |
| stories   | numeric   | The number of stories                     |
| gartype   | character | Details on the garage type                |
| nocars    | numeric   | Size of the garage in cars                |
| xtraffic  | logical   | Emtpy                                     |
| floorlvl  | numeric   | What level the living unit is on          |
| numbdrm   | numeric   | Number of bedrooms                        |
| numbaths  | numeric   | Number of bathrooms                       |
| arcstyle  | character | Type of home                              |
| sprice    | numeric   | Selling price                             |
| deduct    | numeric   | Deduction from the selling price          |
| netprice  | numeric   | Net price of home                         |
| tasp      | numeric   | Tax assesed selling price                 |
| smonth    | numeric   | Month sold                                |
| syear     | numeric   | Year sold                                 |
| qualified | character | Q or U with 66 percent Q                  |
| status    | character | I or V with over 90 percent I             |

## Residential Dwelling Sales 2013 (ML Ready)

The data is called `dwellings_ml`.

***Description***

Attributes of each dwelling with their selling price in machine learning format

[Data Source](https://www.denvergov.org/opendata/dataset/city-and-county-of-denver-real-property-sales-book-2013)

***Data Format***

A data frame with columns:

| Variable                         | Class     | Description                             |
|:---------------------------------|:----------|:----------------------------------------|
| parcel                           | character | The parcel id                           |
| abstrprd                         | numeric   | No clue^[Um, What?]                     |
| livearea                         | numeric   | Square footage that is liveable         |
| finbsmnt                         | numeric   | Square footage finished in the basement |
| basement                         | numeric   | Total square footage of the basement    |
| yrbuilt                          | numeric   | Year the home was built                 |
| totunits                         | numeric   | How many dwelling units in the building |
| stories                          | numeric   | The number of stories                   |
| nocars                           | numeric   | Size of the garage in cars              |
| numbdrm                          | numeric   | Number of bedrooms                      |
| numbaths                         | numeric   | Number of bathrooms                     |
| sprice                           | numeric   | Selling price                           |
| deduct                           | numeric   | Deduction from the selling price        |
| netprice                         | numeric   | Net price of home                       |
| tasp                             | numeric   | Tax assesed selling price               |
| smonth                           | numeric   | Month sold                              |
| syear                            | numeric   | Year sold                               |
| condition_AVG                    | numeric   | 0 (Doesn't Have) or 1 (Has)             |
| condition_Excel                  | numeric   | 0 (Doesn't Have) or 1 (Has)             |
| condition_Fair                   | numeric   | 0 (Doesn't Have) or 1 (Has)             |
| condition_Good                   | numeric   | 0 (Doesn't Have) or 1 (Has)             |
| condition_VGood                  | numeric   | 0 (Doesn't Have) or 1 (Has)             |
| quality_A                        | numeric   | 0 (Doesn't Have) or 1 (Has)             |
| quality_B                        | numeric   | 0 (Doesn't Have) or 1 (Has)             |
| quality_C                        | numeric   | 0 (Doesn't Have) or 1 (Has)             |
| quality_D                        | numeric   | 0 (Doesn't Have) or 1 (Has)             |
| quality_X                        | numeric   | 0 (Doesn't Have) or 1 (Has)             |
| gartype_Att                      | numeric   | 0 (Doesn't Have) or 1 (Has)             |
| gartype_Att/Det                  | numeric   | 0 (Doesn't Have) or 1 (Has)             |
| gartype_CP                       | numeric   | 0 (Doesn't Have) or 1 (Has)             |
| gartype_Det                      | numeric   | 0 (Doesn't Have) or 1 (Has)             |
| gartype_None                     | numeric   | 0 (Doesn't Have) or 1 (Has)             |
| gartype_att/CP                   | numeric   | 0 (Doesn't Have) or 1 (Has)             |
| gartype_det/CP                   | numeric   | 0 (Doesn't Have) or 1 (Has)             |
| arcstyle_BI-LEVEL                | numeric   | 0 (Doesn't Have) or 1 (Has)             |
| arcstyle_CONVERSIONS             | numeric   | 0 (Doesn't Have) or 1 (Has)             |
| arcstyle_END UNIT                | numeric   | 0 (Doesn't Have) or 1 (Has)             |
| arcstyle_MIDDLE UNIT             | numeric   | 0 (Doesn't Have) or 1 (Has)             |
| arcstyle_ONE AND HALF-STORY      | numeric   | 0 (Doesn't Have) or 1 (Has)             |
| arcstyle_ONE-STORY               | numeric   | 0 (Doesn't Have) or 1 (Has)             |
| arcstyle_SPLIT LEVEL             | numeric   | 0 (Doesn't Have) or 1 (Has)             |
| arcstyle_THREE-STORY             | numeric   | 0 (Doesn't Have) or 1 (Has)             |
| arcstyle_TRI-LEVEL               | numeric   | 0 (Doesn't Have) or 1 (Has)             |
| arcstyle_TRI-LEVEL WITH BASEMENT | numeric   | 0 (Doesn't Have) or 1 (Has)             |
| arcstyle_TWO AND HALF-STORY      | numeric   | 0 (Doesn't Have) or 1 (Has)             |
| arcstyle_TWO-STORY               | numeric   | 0 (Doesn't Have) or 1 (Has)             |
| qualified_Q                      | numeric   | 0 (Doesn't Have) or 1 (Has)             |
| qualified_U                      | numeric   | 0 (Doesn't Have) or 1 (Has)             |
| status_I                         | numeric   | 0 (Doesn't Have) or 1 (Has)             |
| status_V                         | numeric   | 0 (Doesn't Have) or 1 (Has)             |
| before1980                       | numeric   | 0 (Doesn't Have) or 1 (Has)             |

## One hot encoded neighbordood Variable

The data is called `dwellings_neighborhoods_ml`.

***Description***

Neighborhood attributes for homes that sold in Denver in 2013

[Data Source](https://www.denvergov.org/opendata/dataset/city-and-county-of-denver-real-property-sales-book-2013)

***Data Format***

A data frame with columns:

| Variable | Class   | Description       |
|:---------|:--------|:------------------|
| nbhd_1   | numeric | Neighborhood #1   |
| nbhd_2   | numeric | Neighborhood #2   |
| nbhd_3   | numeric | Neighborhood #3   |
| nbhd_4   | numeric | Neighborhood #4   |
| nbhd_5   | numeric | Neighborhood #5   |
| nbhd_101 | numeric | Neighborhood #101 |
| nbhd_104 | numeric | Neighborhood #104 |
| nbhd_105 | numeric | Neighborhood #105 |
| nbhd_106 | numeric | Neighborhood #106 |
| nbhd_107 | numeric | Neighborhood #107 |
| nbhd_108 | numeric | Neighborhood #108 |
| nbhd_109 | numeric | Neighborhood #109 |
| nbhd_110 | numeric | Neighborhood #110 |
| nbhd_111 | numeric | Neighborhood #111 |
| nbhd_112 | numeric | Neighborhood #112 |
| nbhd_113 | numeric | Neighborhood #113 |
| nbhd_114 | numeric | Neighborhood #114 |
| nbhd_115 | numeric | Neighborhood #115 |
| nbhd_116 | numeric | Neighborhood #116 |
| nbhd_117 | numeric | Neighborhood #117 |
| nbhd_118 | numeric | Neighborhood #118 |
| nbhd_120 | numeric | Neighborhood #120 |
| nbhd_121 | numeric | Neighborhood #121 |
| nbhd_122 | numeric | Neighborhood #122 |
| nbhd_123 | numeric | Neighborhood #123 |
| nbhd_124 | numeric | Neighborhood #124 |
| nbhd_127 | numeric | Neighborhood #127 |
| nbhd_128 | numeric | Neighborhood #128 |
| nbhd_129 | numeric | Neighborhood #129 |
| nbhd_130 | numeric | Neighborhood #130 |
| nbhd_131 | numeric | Neighborhood #131 |
| nbhd_132 | numeric | Neighborhood #132 |
| nbhd_133 | numeric | Neighborhood #133 |
| nbhd_201 | numeric | Neighborhood #201 |
| nbhd_202 | numeric | Neighborhood #202 |
| nbhd_203 | numeric | Neighborhood #203 |
| nbhd_205 | numeric | Neighborhood #205 |
| nbhd_206 | numeric | Neighborhood #206 |
| nbhd_207 | numeric | Neighborhood #207 |
| nbhd_208 | numeric | Neighborhood #208 |
| nbhd_210 | numeric | Neighborhood #210 |
| nbhd_211 | numeric | Neighborhood #211 |
| nbhd_212 | numeric | Neighborhood #212 |
| nbhd_213 | numeric | Neighborhood #213 |
| nbhd_214 | numeric | Neighborhood #214 |
| nbhd_215 | numeric | Neighborhood #215 |
| nbhd_216 | numeric | Neighborhood #216 |
| nbhd_217 | numeric | Neighborhood #217 |
| nbhd_218 | numeric | Neighborhood #218 |
| nbhd_219 | numeric | Neighborhood #219 |
| nbhd_220 | numeric | Neighborhood #220 |
| nbhd_221 | numeric | Neighborhood #221 |
| nbhd_222 | numeric | Neighborhood #222 |
| nbhd_224 | numeric | Neighborhood #224 |
| nbhd_225 | numeric | Neighborhood #225 |
| nbhd_226 | numeric | Neighborhood #226 |
| nbhd_227 | numeric | Neighborhood #227 |
| nbhd_228 | numeric | Neighborhood #228 |
| nbhd_229 | numeric | Neighborhood #229 |
| nbhd_230 | numeric | Neighborhood #230 |
| nbhd_231 | numeric | Neighborhood #231 |
| nbhd_232 | numeric | Neighborhood #232 |
| nbhd_233 | numeric | Neighborhood #233 |
| nbhd_234 | numeric | Neighborhood #234 |
| nbhd_235 | numeric | Neighborhood #235 |
| nbhd_237 | numeric | Neighborhood #237 |
| nbhd_238 | numeric | Neighborhood #238 |
| nbhd_239 | numeric | Neighborhood #239 |
| nbhd_240 | numeric | Neighborhood #240 |
| nbhd_241 | numeric | Neighborhood #241 |
| nbhd_242 | numeric | Neighborhood #242 |
| nbhd_243 | numeric | Neighborhood #243 |
| nbhd_244 | numeric | Neighborhood #244 |
| nbhd_245 | numeric | Neighborhood #245 |
| nbhd_247 | numeric | Neighborhood #247 |
| nbhd_248 | numeric | Neighborhood #248 |
| nbhd_249 | numeric | Neighborhood #249 |
| nbhd_250 | numeric | Neighborhood #250 |
| nbhd_252 | numeric | Neighborhood #252 |
| nbhd_253 | numeric | Neighborhood #253 |
| nbhd_254 | numeric | Neighborhood #254 |
| nbhd_255 | numeric | Neighborhood #255 |
| nbhd_256 | numeric | Neighborhood #256 |
| nbhd_257 | numeric | Neighborhood #257 |
| nbhd_258 | numeric | Neighborhood #258 |
| nbhd_259 | numeric | Neighborhood #259 |
| nbhd_260 | numeric | Neighborhood #260 |
| nbhd_301 | numeric | Neighborhood #301 |
| nbhd_302 | numeric | Neighborhood #302 |
| nbhd_401 | numeric | Neighborhood #401 |
| nbhd_402 | numeric | Neighborhood #402 |
| nbhd_403 | numeric | Neighborhood #403 |
| nbhd_404 | numeric | Neighborhood #404 |
| nbhd_503 | numeric | Neighborhood #503 |
| nbhd_504 | numeric | Neighborhood #504 |
| nbhd_505 | numeric | Neighborhood #505 |
| nbhd_506 | numeric | Neighborhood #506 |
| nbhd_507 | numeric | Neighborhood #507 |
| nbhd_508 | numeric | Neighborhood #508 |
| nbhd_509 | numeric | Neighborhood #509 |
| nbhd_510 | numeric | Neighborhood #510 |
| nbhd_511 | numeric | Neighborhood #511 |
| nbhd_512 | numeric | Neighborhood #512 |
| nbhd_513 | numeric | Neighborhood #513 |
| nbhd_514 | numeric | Neighborhood #514 |
| nbhd_515 | numeric | Neighborhood #515 |
| nbhd_517 | numeric | Neighborhood #517 |
| nbhd_518 | numeric | Neighborhood #518 |
| nbhd_519 | numeric | Neighborhood #519 |
| nbhd_520 | numeric | Neighborhood #520 |
| nbhd_521 | numeric | Neighborhood #521 |
| nbhd_522 | numeric | Neighborhood #522 |
| nbhd_523 | numeric | Neighborhood #523 |
| nbhd_524 | numeric | Neighborhood #524 |
| nbhd_525 | numeric | Neighborhood #525 |
| nbhd_526 | numeric | Neighborhood #526 |
| nbhd_527 | numeric | Neighborhood #527 |
| nbhd_528 | numeric | Neighborhood #528 |
| nbhd_529 | numeric | Neighborhood #529 |
| nbhd_530 | numeric | Neighborhood #530 |
| nbhd_531 | numeric | Neighborhood #531 |
| nbhd_532 | numeric | Neighborhood #532 |
| nbhd_533 | numeric | Neighborhood #533 |
| nbhd_534 | numeric | Neighborhood #534 |
| nbhd_535 | numeric | Neighborhood #535 |
| nbhd_536 | numeric | Neighborhood #536 |
| nbhd_537 | numeric | Neighborhood #537 |
| nbhd_538 | numeric | Neighborhood #538 |
| nbhd_539 | numeric | Neighborhood #539 |
| nbhd_540 | numeric | Neighborhood #540 |
| nbhd_541 | numeric | Neighborhood #541 |
| nbhd_543 | numeric | Neighborhood #543 |
| nbhd_544 | numeric | Neighborhood #544 |
| nbhd_545 | numeric | Neighborhood #545 |
| nbhd_546 | numeric | Neighborhood #546 |
| nbhd_547 | numeric | Neighborhood #547 |
| nbhd_548 | numeric | Neighborhood #548 |
| nbhd_549 | numeric | Neighborhood #549 |
| nbhd_550 | numeric | Neighborhood #550 |
| nbhd_551 | numeric | Neighborhood #551 |
| nbhd_552 | numeric | Neighborhood #552 |
| nbhd_553 | numeric | Neighborhood #553 |
| nbhd_555 | numeric | Neighborhood #555 |
| nbhd_556 | numeric | Neighborhood #556 |
| nbhd_580 | numeric | Neighborhood #580 |
| nbhd_581 | numeric | Neighborhood #581 |
| nbhd_582 | numeric | Neighborhood #582 |
| nbhd_583 | numeric | Neighborhood #583 |
| nbhd_584 | numeric | Neighborhood #584 |
| nbhd_585 | numeric | Neighborhood #585 |
| nbhd_586 | numeric | Neighborhood #586 |
| nbhd_587 | numeric | Neighborhood #587 |
| nbhd_588 | numeric | Neighborhood #588 |
| nbhd_589 | numeric | Neighborhood #589 |
| nbhd_590 | numeric | Neighborhood #590 |
| nbhd_591 | numeric | Neighborhood #591 |
| nbhd_592 | numeric | Neighborhood #592 |
| nbhd_593 | numeric | Neighborhood #593 |
| nbhd_594 | numeric | Neighborhood #594 |
| nbhd_596 | numeric | Neighborhood #596 |
| nbhd_597 | numeric | Neighborhood #597 |
| nbhd_598 | numeric | Neighborhood #598 |
| nbhd_599 | numeric | Neighborhood #599 |
| nbhd_601 | numeric | Neighborhood #601 |
| nbhd_602 | numeric | Neighborhood #602 |
| nbhd_604 | numeric | Neighborhood #604 |
| nbhd_605 | numeric | Neighborhood #605 |
| nbhd_606 | numeric | Neighborhood #606 |
| nbhd_607 | numeric | Neighborhood #607 |
| nbhd_611 | numeric | Neighborhood #611 |
| nbhd_612 | numeric | Neighborhood #612 |
| nbhd_613 | numeric | Neighborhood #613 |
| nbhd_614 | numeric | Neighborhood #614 |
| nbhd_615 | numeric | Neighborhood #615 |
| nbhd_616 | numeric | Neighborhood #616 |
| nbhd_617 | numeric | Neighborhood #617 |
| nbhd_618 | numeric | Neighborhood #618 |
| nbhd_620 | numeric | Neighborhood #620 |
| nbhd_621 | numeric | Neighborhood #621 |
| nbhd_622 | numeric | Neighborhood #622 |
| nbhd_623 | numeric | Neighborhood #623 |
| nbhd_624 | numeric | Neighborhood #624 |
| nbhd_625 | numeric | Neighborhood #625 |
| nbhd_627 | numeric | Neighborhood #627 |
| nbhd_628 | numeric | Neighborhood #628 |
| nbhd_629 | numeric | Neighborhood #629 |
| nbhd_630 | numeric | Neighborhood #630 |
| nbhd_631 | numeric | Neighborhood #631 |
| nbhd_634 | numeric | Neighborhood #634 |
| nbhd_635 | numeric | Neighborhood #635 |
| nbhd_636 | numeric | Neighborhood #636 |
| nbhd_637 | numeric | Neighborhood #637 |
| nbhd_638 | numeric | Neighborhood #638 |
| nbhd_639 | numeric | Neighborhood #639 |
| nbhd_640 | numeric | Neighborhood #640 |
| nbhd_641 | numeric | Neighborhood #641 |
| nbhd_642 | numeric | Neighborhood #642 |
| nbhd_643 | numeric | Neighborhood #643 |
| nbhd_644 | numeric | Neighborhood #644 |
| nbhd_645 | numeric | Neighborhood #645 |
| nbhd_646 | numeric | Neighborhood #646 |
| nbhd_647 | numeric | Neighborhood #647 |
| nbhd_648 | numeric | Neighborhood #648 |
| nbhd_649 | numeric | Neighborhood #649 |
| nbhd_650 | numeric | Neighborhood #650 |
| nbhd_651 | numeric | Neighborhood #651 |
| nbhd_652 | numeric | Neighborhood #652 |
| nbhd_653 | numeric | Neighborhood #653 |
| nbhd_654 | numeric | Neighborhood #654 |
| nbhd_655 | numeric | Neighborhood #655 |
| nbhd_656 | numeric | Neighborhood #656 |
| nbhd_657 | numeric | Neighborhood #657 |
| nbhd_658 | numeric | Neighborhood #658 |
| nbhd_659 | numeric | Neighborhood #659 |
| nbhd_660 | numeric | Neighborhood #660 |
| nbhd_661 | numeric | Neighborhood #661 |
| nbhd_663 | numeric | Neighborhood #663 |
| nbhd_664 | numeric | Neighborhood #664 |
| nbhd_665 | numeric | Neighborhood #665 |
| nbhd_666 | numeric | Neighborhood #666 |
| nbhd_667 | numeric | Neighborhood #667 |
| nbhd_668 | numeric | Neighborhood #668 |
| nbhd_669 | numeric | Neighborhood #669 |
| nbhd_670 | numeric | Neighborhood #670 |
| nbhd_671 | numeric | Neighborhood #671 |
| nbhd_672 | numeric | Neighborhood #672 |
| nbhd_673 | numeric | Neighborhood #673 |
| nbhd_674 | numeric | Neighborhood #674 |
| nbhd_675 | numeric | Neighborhood #675 |
| nbhd_676 | numeric | Neighborhood #676 |
| nbhd_678 | numeric | Neighborhood #678 |
| nbhd_679 | numeric | Neighborhood #679 |
| nbhd_680 | numeric | Neighborhood #680 |
| nbhd_681 | numeric | Neighborhood #681 |
| nbhd_682 | numeric | Neighborhood #682 |
| nbhd_683 | numeric | Neighborhood #683 |
| nbhd_690 | numeric | Neighborhood #690 |
| nbhd_691 | numeric | Neighborhood #691 |
| nbhd_692 | numeric | Neighborhood #692 |
| nbhd_693 | numeric | Neighborhood #693 |
| nbhd_694 | numeric | Neighborhood #694 |
| nbhd_695 | numeric | Neighborhood #695 |
| nbhd_698 | numeric | Neighborhood #698 |
| nbhd_702 | numeric | Neighborhood #702 |
| nbhd_703 | numeric | Neighborhood #703 |
| nbhd_704 | numeric | Neighborhood #704 |
| nbhd_705 | numeric | Neighborhood #705 |
| nbhd_706 | numeric | Neighborhood #706 |
| nbhd_707 | numeric | Neighborhood #707 |
| nbhd_708 | numeric | Neighborhood #708 |
| nbhd_709 | numeric | Neighborhood #709 |
| nbhd_710 | numeric | Neighborhood #710 |
| nbhd_711 | numeric | Neighborhood #711 |
| nbhd_712 | numeric | Neighborhood #712 |
| nbhd_713 | numeric | Neighborhood #713 |
| nbhd_714 | numeric | Neighborhood #714 |
| nbhd_715 | numeric | Neighborhood #715 |
| nbhd_716 | numeric | Neighborhood #716 |
| nbhd_717 | numeric | Neighborhood #717 |
| nbhd_718 | numeric | Neighborhood #718 |
| nbhd_719 | numeric | Neighborhood #719 |
| nbhd_720 | numeric | Neighborhood #720 |
| nbhd_801 | numeric | Neighborhood #801 |
| nbhd_802 | numeric | Neighborhood #802 |
| nbhd_803 | numeric | Neighborhood #803 |
| nbhd_804 | numeric | Neighborhood #804 |
| nbhd_805 | numeric | Neighborhood #805 |
| nbhd_901 | numeric | Neighborhood #901 |
| nbhd_902 | numeric | Neighborhood #902 |
| nbhd_903 | numeric | Neighborhood #903 |
| nbhd_904 | numeric | Neighborhood #904 |
| nbhd_905 | numeric | Neighborhood #905 |
| nbhd_906 | numeric | Neighborhood #906 |
