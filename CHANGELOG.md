# changelog

## v2.7.1

- bugfix: fix type of data in insert_rows_v0.
- bugfix: add proper model StandardResponse[*] instead of just * in all helper methods.
- qol: add overload for proper type hints.
- update test cases

## v2.7.0 (unstable)

- Add response pydantic models for all helper methods.
- return pydantic models instead of dict in all api helpers if response_as_pydantic=True.
- migrate from make_request_json_output to make_request from square_helper.
- update test cases.

## v2.6.4

- add unit tests.
- dependencies
    - add pytest, pytest-cov and black to all and dev optional sections.

## v2.6.3

- switch build-system to uv.
- update pypi publish github action.

## v2.6.2

- remove setup.py and switch to pyproject.toml

## v2.6.1

- docs
    - add GNU license v3.0.
    - update README.md.
    - move CHANGELOG to a separate file.

## v2.6.0

- update compatibility with square_database>=3.2.0.

## v2.5.0

- update compatibility with square_database>=3.1.0.

## v2.4.0

- update compatibility with square_database>=3.0.0.

## v2.3.1

- bump square_commons to >=2.0.0.

## v2.3.0

- use make_request_json_output to call api endpoints.

## v2.2.0

- expanded apply_filters to support additional conditions: ne, lt, lte, gt, gte, like, in_.

## v2.1.1

- edit_rows_v0 now uses patch method.

## v2.1.0

- compatible with v2.1.0 of square database.
- stricter type checking.
- added pydantic as a requirement.
- filters now passed in as a pydantic model instead of direct dictionary.

## v2.0.0

- added version numbers for all endpoints for better compatibility.

## v1.0.2

- add offset, limit and order by in get rows.

## v1.0.1

- fix typos.

## v1.0.0

- initial implementation.