import hashlib
import json
import math
import os
# import pywhatkit

# pywhatkit.sendwhatmsg("+910123456789", "Hi", 13, 30)

data_file = "data.json"

# Check if data file exists, otherwise create an empty file with an empty JSON array
if not os.path.exists(data_file):
    with open(data_file, "w") as f:
        json.dump([], f)

try:
    while True:
        print("Enter your details below.")
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")

        roles = ["boss", "manager", "employee"]
        for i in range(len(roles)):
            print(roles[i])
        ro_le = input("Enter your role: ")
        username = input("Enter your username: ")
        pass_word = input("Enter your password: ")
        salary = input("Enter your salary: $")
        user_national_id = input("Enter your national id: ")
        p = hashlib.md5(pass_word.encode()).hexdigest()

        with open(data_file, "r") as f:
            json_data = json.load(f)
            print(json_data)
            usernames = [data.get("username") for data in json_data]
            if username in usernames:
                print("Username already taken")
            else:
                if ro_le in roles:
                    data = {
                        "Firstname": first_name,
                        "lastname": last_name,
                        "role": ro_le,
                        "username": username,
                        "password": p,
                        "salary": salary,
                        "user_id": user_national_id
                    }
                    json_data.append(data)
                    with open(data_file, 'w') as f:
                        json.dump(json_data, f, indent=2)
                else:
                    print("Role is not available")
except KeyboardInterrupt:
    print("Information saved successfully")
