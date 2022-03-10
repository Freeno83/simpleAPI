# Simple API
Simple demonstration of flask

## set
```
localhost:5000/set/test/123
{
  "message": "Created new key: 'test' with value: 123"
}
```
## get
```
localhost:5000/get/test
{
  "value": "123"
}
```
## list
```
localhost:5000/list
{
  "keys": [
    "test"
  ]
}
```

## All availble methods can be see at the root url

```
http://localhost:5000/

{
  "getValue": "/get/k", 
  "listKeys": "/list", 
  "setValue": "/set/k/v"
}
```
