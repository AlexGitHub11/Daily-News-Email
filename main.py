import requests
from send_email import send

api_key = "API_KEY"

topic = "tesla"

url = "https://newsapi.org/v2/everything?" \
       f"q={topic}&" \
       "sortBy=publishedAt" \
       "&apiKey=API_KEY" \
        "&language=en"

# Make request
request = requests.get(url)

# Get data into a dictionary
content = request.json()

# Access articles, titles and descriptions
body = ""

for article in content["articles"][:20]:
    if article["title"] is not None and article["description"] \
            is not None and article["url"] \
            is not None:
        body = "Subject: Today's news" \
                + "\n" + body + article["title"] + "\n" \
                + article["description"] \
                + "\n" + article["url"] + 2 *"\n"

body = body.encode("utf-8")
send(message=body)


