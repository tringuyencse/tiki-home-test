import csv
import pandas as pd
from datetime import datetime

# DEFINE
ERROR_CSV = "CSV file is not match rule"
FILE_NAME = "test.csv"
FILE_NAME_WAS_SORTED = "sorted.csv"
FILE_NAME_WAS_FINISHED = "finished.csv"


def isPhoneNumber(phoneNumber):
    if len(phoneNumber) != 10:
        return False
    else:
        return True


def sortCVSFile(fileName, fieldsSort, fileExport, sortByASC):
    try:
        # making data frame from csv file
        data = pd.read_csv(fileName)

        # get total row of csv file include header
        totalRows = data.shape[0] + 1

        # check csv file
        if totalRows <= 1:
            print(ERROR_CSV)
            return

        # sorting data frame by Phone and then By Activation date
        data.sort_values(fieldsSort, axis=0, ascending=sortByASC, inplace=True)

        # export new csv
        data.to_csv(fileExport, sep=',', encoding='utf-8', index=False)

    except:

        print(ERROR_CSV)


def main():
    # create finish file
    with open(FILE_NAME_WAS_FINISHED, mode='w') as finishFile:
        finishFileWriter = csv.writer(finishFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        finishFileWriter.writerow(['PHONE_NUMBER', 'REAL_ACTIVATION_DATE'])
        finishFile.close()

    # sort csv file then it will export a new csv file that was sorted
    sortCVSFile(FILE_NAME, ["PHONE_NUMBER", "ACTIVATION_DATE"], FILE_NAME_WAS_SORTED, False)

    # using new csv file that was sorted to continue
    try:
        with open(FILE_NAME_WAS_SORTED, 'r') as sortedFile:
            reader = csv.reader(sortedFile)
            index = 0
            previousRow = []

            for currentRow in reader:
                # skip if this row is header
                if index == 0:
                    index += 1
                    continue

                # phone number to string
                currentRow[0] = '0' + str(currentRow[0])
                if not isPhoneNumber(currentRow[0]):
                    print(ERROR_CSV)
                    break

                if not previousRow:
                    previousRow = currentRow
                elif currentRow[0] == previousRow[0] and currentRow[2] == "":
                    print(ERROR_CSV)
                    break
                # compare phone and compare activation date with deactivation date
                # elif currentRow[0] == previousRow[0] and currentRow[2] == previousRow[1]:
                #     previousRow[1] = currentRow[1]
                elif (currentRow[0] == previousRow[0] and (datetime.strptime(previousRow[1], '%Y-%m-%d') - datetime.strptime(currentRow[2], '%Y-%m-%d')).days < 30):
                    previousRow[1] = currentRow[1]
                else:
                    finishData = [previousRow[0], previousRow[1]]
                    with open(FILE_NAME_WAS_FINISHED, mode='a') as finishFile:
                        writer = csv.writer(finishFile)
                        writer.writerow(finishData)
                        finishFile.close()
                    if currentRow[2] != "":
                        previousRow = []
                    else:
                        previousRow = currentRow

            # last data
            if previousRow and previousRow[2] == "":
                finishData = [previousRow[0], previousRow[1]]
                with open(FILE_NAME_WAS_FINISHED, mode='a') as finishFile:
                    writer = csv.writer(finishFile)
                    writer.writerow(finishData)
                    finishFile.close()

        sortedFile.close()

        print("DONE")

    except:

        print(ERROR_CSV)


main()



