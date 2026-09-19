import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

sys.path.insert(0, str(ROOT))


from core.api_session import get_session


print("=" * 60)
print("BRAIN AUTHENTICATION TEST")
print("=" * 60)


brain = get_session()


print()
print("Authentication completed.")


response = brain.get(
    "/authentication"
)


print()
print("Authentication status:")
print(response.status_code)


if response.text:
    print(response.text)
