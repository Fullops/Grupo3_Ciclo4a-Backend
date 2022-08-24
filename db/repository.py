from typing import TypeVar, Generic, get_args
from db.db import Db
from bson import DBRef
from bson.objectid import ObjectId
from models.student_model import StudentModel
T = TypeVar('T')

class Repository(Generic[T]):
  def __init__(self):
    name = get_args(self.__orig_bases__[0] )[0].__name__.lower().replace('model','')
    self.db = Db()
    self.collection = self.db.collection(name)
  
  def get_all(self):
    results = self.collection.find()
    data = []
    for r in results:
      r["_id"] = r["_id"].__str__()
      r = self.transform_object_ids(r)
      r = self.get_values_db_ref(r)
      data.append(r)
    return data
  
  def get_by_id(self, id):
    result = self.collection.find_one({"_id": ObjectId(id)})
    result["_id"] = result["_id"].__str__()
    result = self.transform_object_ids(result)
    result = self.get_values_db_ref(result)
    return result
  
  
  def transform_object_ids(self, x):
    for attribute in x.keys():
      if isinstance(x[attribute], ObjectId):
        x[attribute] = x[attribute].__str__()
      elif isinstance(x[attribute], list):
        x[attribute] = self.format_list(x[attribute])
      elif isinstance(x[attribute], dict):
        x[attribute]=self.transform_object_ids(x[attribute])
    return x
  
  def format_list(self, x):
    newList = []
    for item in x:
      if isinstance(item, ObjectId):
        newList.append(item.__str__())
    if len(newList) == 0:
      newList = x
    return newList
  
  def get_values_db_ref(self, x):
    keys = x.keys()
    for k in keys:
      if isinstance(x[k], DBRef):
        collection = self.db[x[k].collection]
        valor = collection.find_one({"_id": ObjectId(x[k].id)})
        valor["_id"] = valor["_id"].__str__()
        x[k] = valor
        x[k] = self.get_values_db_ref(x[k])
      elif isinstance(x[k], list) and len(x[k]) > 0:
        x[k] = self.get_values_db_ref(x[k])
      elif isinstance(x[k], dict) :
        x[k] = self.get_values_db_ref(x[k])
    return x