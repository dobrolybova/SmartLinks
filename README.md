# Smart links service
Depending on request parameters service redirects user to different links.
Redirecting rules are stored in DB. 
There are two services: <p>
1. Service to add/delete/update rules in DB (rule service) <p>
2. Service to handle incoming request according to stored rules and redirect user to needed link (redirect service). <p>

## BD

Table "rules" with the following structure: <p>
id - key (int) <p>
rule - rule name (string) <p>
priority - rule priority (int) <p>
property - should be checked in request (string) <p>
url - redirect link (string) <p>

example:

| id |  rule   | priority |  property |  url |
|:---|:-------:|---------:|----------:|-------:|
| 1  | browser |        1 |   Firefox |http://|
| 2  | browser |        1 |    Chrome | http:// |
| 3  |  host   |        2 | localhost | http:// |

## Rule Service
Ths service updates DB with new rules data. <p>
API: POST http://ip:port/api/v1/rule <p>
Request: <p>
```json
{
    "rule_type": "host",
    "priority": 2,
    "data": [
        {
            "property": "localhost", "url": "http://"
        }
    ]
}
```
Response:
```json
{
    "add_rule": "OK"
}
```
API: DELETE http://ip:port/api/v1/rule?rule_type=host
Response:
```json
{
    "delete_rule": "OK"
}
```

## Redirect Service
Ths service reads DB content and handles every rule according to rule type in priority order until url is not get. <p>
Every rule type has its own handler with logic how to handle property for received request. If current property is suitable,
corresponding url will be returned.
API: GET http://ip:port/api/v1/redirect <p>