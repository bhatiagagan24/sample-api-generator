# python script to randomly generate data and upload to the mongoDB so that it can be served

import pymongo as db
import random
myclient = db.MongoClient("localhost:27017")

def generatePostData():
    mydb = myclient["sampleApiGenerator"]
    mycol = mydb["posts"]
    listOfPosts = []
    count = 1
    for i in range(0, 400):
        randTitleLen = random.randint(50, 100)
        randBodyLen = random.randint(100, 400)
        randTitle = ""
        randBody = ""
        noOfRandomNewLines = random.randint(0, 10)
        randomNewLinesPos = [j for j in range(100, 399)]
        for i in range(randTitleLen):
            randChar = random.randint(97, 123)
            randTitle += str(chr(randChar))
        for i in range(randBodyLen):
            randChar = random.randint(97, 123)
            randBody += str(chr(randChar))
            if i in randomNewLinesPos:
                randBody += "\n" 
        posts = {
                "_id": count,
                "userId" : random.randint(0, 10),
                "title": randTitle,
                "body": randBody
            }
        count += 1
        in1 = mycol.insert_one(posts)
    print(in1)


if __name__ == '__main__':
    generatePostData()
