# Simple API
simple get and put demonstration

### "Home page" shows the available methods

```
{
  "getValue": "/get/k", 
  "listKeys": "/list", 
  "setValue": "/set/k/v"
}
```

### set method example use

```
localhost:5000/set/test/123

{
  "message": "Created new key: 'test' with value: 123"
}
```

### get method example use

```
localhost:5000/get/test

{
  "value": "123"
}
```

### list method example use

```
localhost:5000/list

{
  "keys": [
    "test"
  ]
}
```

### All availble methods can be see at the root url

```
http://localhost:5000/

{
  "getValue": "/get/k", 
  "listKeys": "/list", 
  "setValue": "/set/k/v"
}

```
