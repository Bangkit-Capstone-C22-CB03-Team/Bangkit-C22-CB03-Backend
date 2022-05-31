# For Linux
# curl --location --request POST 'localhost:8080/' \
# --header 'Content-Type: application/json' \
# --data-raw '{
#     "chat": "What percent Peru hold amazon?"
# }'
# "chat": "Where amazon is?"

# "chat": "How wide amazon is?"

# "chat" : "Where the majority of the amazon is?"

# updated POST CURL
curl -X POST http://34.122.125.254:8080?msg=What%20percent%20Peru%20hold%20amazon?