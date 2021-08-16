#remember to import json first. But i still don't know what it is
import json
person_dict = {"mom":"yvonne","dad":"steven","brother":"richard"}
person_dict["me"] = "rachel"
favorite_food = ["ice_cream","candy","chocolate"]
person_dict["my favorite foods"] = favorite_food
print(person_dict)
staff_dict = {}
staff_dict["My family"] = person_dict
print(staff_dict)

#staff_json = json.dumps(staff_dict)
#print(staff_json)
  