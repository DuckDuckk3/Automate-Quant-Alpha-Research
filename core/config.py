import os
from pathlib import Path

from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parents[1]
ENV_FILE = PROJECT_ROOT / ".env"

load_dotenv(ENV_FILE)


def load_credentials():

    username = os.getenv("WQ_BRAIN_USERNAME")
    password = os.getenv("WQ_BRAIN_PASSWORD")

    if not username:
        raise RuntimeError(
            f"WQ_USERNAME is not configured. "
            f"Checked: {ENV_FILE}"
        )

    if not password:
        raise RuntimeError(
            f"WQ_PASSWORD is not configured. "
            f"Checked: {ENV_FILE}"
        )

    return username, password
