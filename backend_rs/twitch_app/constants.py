from django.conf import settings
from pathlib import Path

# Define outputs_path relative to BASE_DIR
outputs_path = Path(settings.BASE_DIR, "twitch_app/resources", "outputs")
