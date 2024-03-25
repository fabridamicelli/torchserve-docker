import json
import tempfile

from get_latest_tag import main

test_data = json.dumps(
    [
        {"tag": "v0.7.1"},
        {"tag": "v0.7.0"},
        {"tag": "v0.6.1"},
        {"tag": "v0.6.0"},
        {"tag": "v1.6.0"},
        {"tag": "v1.6.1"},
    ]
)

expected = "1.6.1"

with tempfile.NamedTemporaryFile() as file:
    file.write(test_data.encode())
    file.seek(0)
    assert main(file.name) == expected, "Wrong tag parsing"
