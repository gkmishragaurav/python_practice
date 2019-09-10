import sys
filename = "C:\Users\gaurav\\trunk\src\inSyncQA\TestCases\\api\\regression\cloudapp\Box_Cloudapp_authentication.csv"
with open(filename) as file:
    for index, line in enumerate(file):
        print("{0}: {1}".format(index+1, line))


