# python -m venv venv
# mac:     source venv/bin/activate
# windows: venv/bin/activate

import dotenv
import os
# .env doyasını yükle.
dotenv.load_dotenv(".env") 

# OUT
# username = "admin"
# password = "P1234"

# IN
username = os.getenv("DB_USER")
password = os.getenv("DB_PASS")

print(username)
print(password)