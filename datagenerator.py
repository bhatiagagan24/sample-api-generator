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

def longstringUpload(x):
    mydb = myclient["sampleApiGenerator"]
    mycol = mydb["longStrings"]
    randBodyLen = random.randint(200, 1000)
    randBody = ""
    for i in range(randBodyLen):
        randChar = random.randint(97, 122)
        randBody += str(chr(randChar))
    longString = {
        "_id": x,
        "longStr": randBody
    }
    dbupload = mycol.insert_one(longString)


def shortStringUpload(x):
    mydb = myclient["sampleApiGenerator"]
    mycol = mydb["shortStrings"]
    randBodyLen = random.randint(50, 199)
    randBody = ""
    for i in range(randBodyLen):
        randChar = random.randint(97, 122)
        randBody += str(chr(randChar))
    shortString = {
        "_id": x,
        "shortStr": randBody
    }
    dbupload = mycol.insert_one(shortString)


# . -> \u002e
def randomEmails(x):
    mydb = myclient["sampleApiGenerator"]
    mycol = mydb["emails"]
    randEmaillens = random.randint(8, 20)
    randEmail = ""
    for i in range(randEmaillens):
        randChar = random.randint(97, 122)
        randEmail += str(chr(randChar))
    randEmail += "@randomMail\u002ecom"
    email = {
        "_id": x,
        "shortStr": randEmail
    }
    dbupload = mycol.insert_one(email)

# Random numbers
def randomNumbers(x):
    mydb = myclient["sampleApiGenerator"]
    mycol = mydb["nums"]
    randBodyLen = random.randint(5, 11)
    randNum = ""
    for i in range(randBodyLen):
        randChar = random.randint(0, 9)
        randNum += str(randChar)
    # print(randNum, end="\n")
    randNum = int(randNum)
    nums = {
        "_id": x,
        "number": randNum
    }
    dbupload = mycol.insert_one(nums)



def generateUserNames(x):
    mydb = myclient["sampleApiGenerator"]
    mycol = mydb["usernames"]
    randBodyLen = random.randint(5,10)
    # randNumPosition = [y for y in range(0, random.randint(0, randBodyLen-1))]
    randNumPositions = [y for y in range(random.randint(1, int(randBodyLen/2)), random.randint(int(randBodyLen/2)+1, randBodyLen-1))]
    print(randNumPositions)
    userName = ""
    for y in range(randBodyLen):
        if y in randNumPositions:
            userName += str(random.randint(0,9))
        else:
            randChar = random.randint(97, 122)
            userName += str(chr(randChar))
    username = {
        "_id": x,
        "username": userName,
    }
    dbupload = mycol.insert_one(username)




if __name__ == '__main__':
    # generatePostData()
    for x in range(400):
        # longstringUpload(x)
        # randomNumbers(x)
        # randomEmails(x)
        # shortStringUpload(x)
        generateUserNames(x)
