import requests
import rich

url = "http://127.0.0.1:8000/mcp/"

header = {
    "Accept": "application/json, text/event-stream"
}

#---------------------------------------------- read prompt  ------------------------------------------------------

body = {
  "jsonrpc": "2.0",
  "id": 2,
  "method": "prompts/list",
  "params": {}
}

print("\n\n\n Read All Prompt\n")

response = requests.post(url, headers=header, json=body)
rich.print(response.text)


#---------------------------------------------- cell prompt  ------------------------------------------------------

body_2 = {
  "jsonrpc": "2.0",
  "id": 2,
  "method": "prompts/get",
  "params": {
      "name": "greet",
      "arguments": {
          "user_name": "sajeel"
      }
  }
}

print("\n\n\n Cell greet Prompt\n")

response_2 = requests.post(url, headers=header, json=body_2)
rich.print(response_2.text)


# ---------------------------------------------------------------------------------------------

body_3 = {
    "jsonrpc": "2.0",
    "id": 2,
    "method": "prompts/get",
    "params": {
        "name": "greet_user",
        "arguments": {
            "user_name": "sajeel"
        }
    }
}

print("\n\n\n Cell greet_user Prompt\n")

response_3 = requests.post(url, headers=header, json=body_3)
rich.print(response_3.text)