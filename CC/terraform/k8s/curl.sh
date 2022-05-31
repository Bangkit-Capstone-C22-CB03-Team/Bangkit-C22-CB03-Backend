# For Linux
# curl --location --request POST 'http://34.122.125.254:8080/' \
# --header 'Content-Type: application/json' \
# --data-raw '{
#     "chat": "What percent Peru hold amazon?"
# }'
# "chat": "Where amazon is?"

# "chat": "How wide amazon is?"

# "chat" : "Where the majority of the amazon is?"

curl -X POST http://34.122.125.254:8080?msg=What%20percent%20Peru%20hold%20amazon?

# echo "load test the model"
# locust --headless --users 10 --spawn-rate 1 -H http://34.122.125.254:8080
