import random
import pymongo as db
import json
# returns response as JSON

def returnJson(value, count):
    myclient = db.MongoClient("localhost:27017")
    postValList = ["username", "postTitle", "postContent"]
    commentValList = ["commentContent", "userDatails", "username", "email"]
    userValList = ["username", "email"]
    
    if value == "posts":
        
        finalResponse = []
        for x in range(count):
            username = returnUsername(myclient)
            postTitle = returnPostTitle(myclient)
            postContent = returnPostContent(myclient)
            finalResponse.append(
                {
                "userId": random.randint(0, 5),
                "username": username,
                "postTitle": postTitle,
                "postContent": postContent
                }
            )
        print(json.dumps(finalResponse, indent=10))
        return json.dumps(finalResponse, indent=10)

    elif value == 'comments':
        finalResponse = []
        for x in range(count):
            username = returnUsername(myclient)
            # posttitle same as comment content
            postTitle = returnPostTitle(myclient)
            userId = random.randint(1,5)
            email = returnEmail(myclient)
            finalResponse.append(
                {
                    "commentContent": postTitle,
                    "userDetails": {
                        "username": username,
                        "email": email,
                        "userId": userId
                    }
                }
            )
            return json.dump(finalResponse, indent=10)
    elif value == "users":
        return "User returned here"



def returnUsername(myclient):
    mydb = myclient["sampleApiGenerator"]
    mycol = mydb["usernames"]
    randomNumForId = random.randint(0, 400)
    tempname = mycol.find({"_id": randomNumForId})
    for data in tempname:
        return data['username'] 

def returnPostTitle(myclient):
    mydb = myclient["sampleApiGenerator"]
    mycol = mydb["shortStrings"]
    randomNumForId = random.randint(0, 400)
    tempname = mycol.find({"_id": randomNumForId})
    for data in tempname:
        return data['shortStr'] 

def returnPostContent(myclient):
    mydb = myclient["sampleApiGenerator"]
    mycol = mydb["longStrings"]
    randomNumForId = random.randint(0, 400)
    tempname = mycol.find({"_id": randomNumForId})
    for data in tempname:
        return data['longStr'] 

def returnEmail(myclient):
    mydb = myclient["sampleApiGenerator"]
    mycol = mydb["emails"]
    randomNumForId = random.randint(0, 400)
    tempname = mycol.find({"_id": randomNumForId})
    for data in tempname:
        return data['shortStr'] 



# if __name__ == '__main__':
#     returnJson("posts", 5)












# def returnPosts(myclient):
#     mydb = myclient["sampleApiGenerator"]
#     mycol = mydb["posts"]
#     randomNumForId = random.randint(0, 400)
#     randomNumForPostTitle = random.randint(0, 400)
#     randomNumForPostContent = random.randint(0, 400)
#     id = mycol.find({}, {'_id':randomNumForId})
#     title = mycol.find({}, {'_id':randomNumForPostTitle})
#     postContent = mycol.find({}, {'_id':randomNumForPostContent})
#     id_content = ""
#     for 