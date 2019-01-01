# api-errors
A project to explore standardizing errors in Falcon. This originally started
as a project to standardize error responses. It turned into a project to
standardize all responses that have a body.

## General
- Messages can be null or string.
- `status` can be `success`, `fail` or `error`. `fail` is for client-related
failure, such as incorrectly formatted requests or validation errors.
`error` is for 5xx errors

## 2xx Responses
For returning a single object, such as the result of a detail view,
use `result` key. For list of results, such as for a results endpoint,
use `results`.

```json
{
  "message": null,
  "status": "success",
  "result": {
    "id": 4542,
    "something": 123
  }
}
```

## Error Responses
```json
{
  "title": "500 Server Error",
  "message": "Something bad happened on our end",
  "status": "error"
}
```