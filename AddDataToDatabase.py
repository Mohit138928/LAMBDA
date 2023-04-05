import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://lambda-13cd9-default-rtdb.firebaseio.com/",
     'storageBucket':"lambda-13cd9.appspot.com"
})

ref = db.reference('Students')

data = {
    "CSE21-073": {
        "name": "Nikhil Shukla",
        "department": "ComputerScience",
        "starting_year": 2021,
        "total_attendance": 2,
        "section": "B1",
        "year": 2,
        "last_attendance_time": "2023-03-19 04:03:00"
    },
    "CSE21-113": {
        "name": "Sudhanshu Chauhan",
        "department": "ComputerScience",
        "starting_year": 2021,
        "total_attendance": 1,
        "section": "B2",
        "year": 2,
        "last_attendance_time": "2023-03-19 04:03:00"
    },
    "CSE21-070": {
        "name": "Mohit Maurya",
        "department": "ComputerScience",
        "starting_year": 2021,
        "total_attendance": 1,
        "section": "B1",
        "year": 2,
        "last_attendance_time": "2023-03-19 04:03:00"
    },
    "CSE21-072": {
        "name": "Nikhil Sharma",
        "department": "ComputerScience",
        "starting_year": 2021,
        "total_attendance": 3,
        "section": "B1",
        "year": 2,
        "last_attendance_time": "2023-03-19 04:03:00"
    }
}


for key,value in data.items():
    ref.child(key).set(value)