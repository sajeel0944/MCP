import requests

url = "http://127.0.0.1:8000/mcp/"

header = {
    "Accept": "application/json, text/event-stream"
}

body = {
  "jsonrpc": "2.0",
  "id": 2,
  "method": "tools/call",
  "params": {
    "name": "weather",
    "arguments": {
      "name": "sunny"
    }
  }
}

response = requests.post(url, headers=header, json=body)
print(response.text)
