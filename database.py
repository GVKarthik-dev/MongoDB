import pymongo
import random

# MongoDB connection
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["school"]  # Replace with your database name
collection = db["students"]

# Sample data
names = ["Alice", "Bob", "Charlie", "David", "Ella", "Frank", "Grace", "Hannah", "Isaac", "Jack"]
genders = ["male", "female"]
subjects = ["MPC", "BPC"]
fulltime_values = [True, False]

# Generate and insert 50 random student records
for i in range(50):
    student = {
        "_id": i,
        "name": random.choice(names),
        "gpa": round(random.uniform(0, 4), 2),  # Random GPA between 0 and 4 with 2 decimal places
        "fulltime": random.choice(fulltime_values),
        "gender": random.choice(genders),
        "subject": random.choice(subjects),
        # You can add other fields as needed here
    }
    collection.insert_one(student)

print("Sample data inserted successfully.")
