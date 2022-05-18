# dont forget to change this for linux env
# or add two seperate curl command for each OS
curl http://localhost:5000/ ^
-d @json.txt ^
-H "Content-Type: application/json" ^
-X POST
