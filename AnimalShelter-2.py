from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.

        self.client = MongoClient('mongodb://localhost:54398')
        self.database = self.client['AAC']

        # Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert(data)  # data should be dictionary \n",
            if insert!=0:
                return True
            else:
                return False           
        else:
            raise Exception("Nothing to save, because data parameter is empty")
        # Create method to implement the R in CRUD.
    def read(self, criteria=None):
        # criteria is not None then this find will return all rows which matches the criteria
        if criteria:
        # {'_id':False} just omits the unique ID of each row
            data = self.database.animals.find(criteria,{"_id":False})
        else:
        #if there is no search criteria then all the rows will be return
            data = self.database.animals.find({} , {"_id":False})
        return data

# Create method to implement the U in CRUD.
    def update(self, newData=None):
        #criteria is not None then this find will return all rows which matches the criteria 
        if newData:
            results = self.database.animals.find_one(newData, {"_id":False, "name":1, "type":1})
            if results is not None:
                changeData = self.database.animals.update_one(self, newData)
                print("Data updated successfully: ")
                return newData
            else:
                changeData = self.database.animals.insert_one(newData)
                print("Data added successfully: ")
                return changeData
        else:
            results = self.database.animals.find_one({}, {"_id":False, "name":1, "type":1})
            return False


#Create method to implement the D in CRUD.
    def delete(self, data):
        if data is not None:
            #delete the documents
            deleted = self.database.animals.delete_many(data)
            #result = "Documents deleted: " + json.dumps(deleted.deleted_count)
            #return result
        else:
            raise Exception("No valid record provided")
    

