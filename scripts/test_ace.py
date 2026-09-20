import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ACE_DIR = ROOT / "ace"

sys.path.insert(0, str(ACE_DIR))


import ace_lib as ace


print("ACE import successful.")


print()
print("Starting BRAIN session...")

s = ace.start_session()

print("Session created.")


s = ace.check_session_and_relogin(s)

print("Session authenticated successfully.")
