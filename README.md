# Tiki Home Test

#### Description

Given a list of at most N records (in CSV format), each record describes an usage period
of a specific mobile phone number.

Note that one phone number can occurs multiple times in this list, because of 2 reasons:

● This phone number can change from prepaid plan to postpaid plan, or vice versa,
at anytime just by sending an SMS to the operator.

● Or, the owner of this phone number can stop using it, and after 1-2 months, it is
reused by another person .

Beside, some data is not recorded, we just have the phone number and its activation or
deactivation, because of 2 reasons:

● Activation date is the date that the phone number is started being used by a owner
with a specific plan (prepaid or postpaid).

● Deactivation date is the date that the phone number is stopped being used by a
owner with the registered plan.

Moreover, the records don't need to follow any specific order of time, and the records of
the same number don't need to be consecutive .

This is an example of the list, given as a CSV file:

```csv
PHONE_NUMBER,ACTIVATION_DATE,DEACTIVATION_DATE 
0987000001,2016-03-01,2016-05-01 
0987000002,2016-02-01,2016-03-01 
0987000001,2016-01-01,2016-03-01 
0987000001,2016-12-01, 
0987000002,2016-03-01,2016-05-01 
0987000003,2016-01-01,2016-01-10 
0987000001,2016-09-01,2016-12-01 
0987000002,2016-05-01, 
0987000001,2016-06-01,2016-09-01
```

In this list, ACTIVATION_DATE and DEACTIVATION_DATE are represented with YYYY-
MM-DD format. DEACTIVATION_DATE may be empty, which means that the phone is

still being used by its current owner.

#### Requirement:
● Find a list of unique phone numbers together with the actual activation date.
Describe in detail your strategy and algorithm to solve this problem.

● Implement your solution in any programming language, with input is a CSV file as
described above, and write the output as another CSV file with following format:

#### Installing

###### Requirement
```
    Python 2.7.12
    Please copy your csv file to this project's root folder and rename to "test.csv"!
```
###### How to run
```
    git clone https://github.com/tringuyencse/tiki-home-test
    cd tiki-home-test
    python main.py
```

#### Solution
```
    First, I sort (DESC) for csv file by phone and then by activation date 
    Then, read row by row to check data and save to finish.csv file 
```