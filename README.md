# Gmail Email Reader

This doesn't read your emails, it just marks them as read. Useful if you have tons of emails that you wan't to mark as read.

# Steps to run

1. Follow [this](https://developers.google.com/workspace/guides/create-project) guide to create a GCP project. Make sure to enable `Gmail API`

2. Follow [this](https://developers.google.com/workspace/guides/create-credentials) guide to create oauth credentials. Make sure to add the email you plan to use as a test user. Download your client secrets, and rename the JSON file to `credentials.json`.

3. Install deps

```bash
pip install -r requirements.txt # or pip3 if needed
```

4. Run script

```bash
python main.py # or python3 if needed
```

License: MIT
