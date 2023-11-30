# Simple BackEnd Lambda Application

 The sole reason for creating this application was to improve my understanding of AWS API Gateway, Lambda, and DynamoDB with terraform. I locally spin-up all of these using localstack. More work is yet to be done...

 To get started you need to run:

```
 docker compose up
 terraform init
 terraform apply
```
This will spin-up everything. How to run the application:

```
awslocal apigateway get-rest-apis
```
Fetch the ID you get from here, copy it, then:
```
curl -X POST -H "Content-Type: application/json" -d @data.json http://localhost:4566/restapis/<ID from above>/dev/_user_request_/test
```
data should be posted in the following format (an example file has been provided):
```
{
  "ToDo": "Your Item",
  "Done": false
}
```

As mentioned earlier, more functionality and ease of user-functionality needs to be added.