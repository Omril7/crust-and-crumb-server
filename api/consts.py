import os
from dotenv import load_dotenv

load_dotenv()

# Environment vars
ADMIN_USER = os.getenv("ADMIN_USER", "admin")
ADMIN_PASS_HASH = os.getenv("ADMIN_PASS_HASH")