import urllib.request
import json

def main():
    # weburl = urllib.request.urlopen("http://www.google.com")
    # print("result code : " + str(weburl.getcode()))
    # data = weburl.read()
    # print(data)

    urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_hour.geojson"

    weburl = urllib.request.urlopen(urlData)
    print("result code : " + str(weburl.getcode()))

    if weburl.getcode() == 200 :
        data = weburl.read()
        printResults(data)
    else:
        print("Error received, cannot parse results")

def printResults(df):
    theJson =  json.load(df)

    if "title" in theJson["metadata"]:
        print(theJson["metadata"]["title"])

    count = theJson["metadata"]["count"]
    print(str(count) + " events recorded")

if __name__ == "__main__":
    main()