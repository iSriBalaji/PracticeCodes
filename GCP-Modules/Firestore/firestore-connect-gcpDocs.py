import firebase_admin
from datetime import datetime
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate('GCP-Modules/Firestore/firestore-creds.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client(database_id="cguru-pde")
print(f"Connected to Firestore project: {db.project}")


users_ref = db.collection("steps")
docs = users_ref.stream()

for doc in docs:
    print(f"{doc.id} => {doc.to_dict()}")

print("--"*50)

doc_ref = db.collection("users").document("alovelace")
doc_ref.set({"first": "Sri Balaji", "last": "Musk", "born": 2020})

now = datetime.now()
newdata = {"date": now, "load_dt": now, "step_count": 7120}
steps_add = db.collection("steps").add(newdata)

print("Data Added Successfully!")