# square_database_helper

## about

helper to access the database layer for my personal server.

## installation

```shell
pip install square_database_helper
```

## usage

[reference python file](./example.py)

## env

- python>=3.12.0

## changelog

### v2.1.1

- edit_rows_v0 now uses patch method.

### v2.1.0

- compatible with v2.1.0 of square database.
- stricter type checking.
- added pydantic as a requirement.
- filters now passed in as a pydantic model instead of direct dictionary.

### v2.0.0

- added version numbers for all endpoints for better compatibility.

### v1.0.2

- add offset, limit and order by in get rows.

### v1.0.1

- fix typos.

### v1.0.0

- initial implementation.

## Feedback is appreciated. Thank you!
