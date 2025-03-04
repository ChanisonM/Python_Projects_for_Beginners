import pandas as pd

data = data = [
    {"Roll no": 1,
     "student": {"first_name": "Ram", "last_name": "kumar" , }
     },
    {"student": {"English": "95", "Math": "88"}
     },
    {"Roll no": 2,
     "student": {"first_name": "Joseph", "English": "90", "Science": "82"}
     },
    {"Roll no": 3,
     "student": {"first_name": "abinaya", "last_name": "devi"},
     "student": {"English": "91", "Math": "98"}
     },
]

df = pd.json_normalize(data)

print(df)

