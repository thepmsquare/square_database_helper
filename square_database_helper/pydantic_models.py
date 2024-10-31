from typing import Any, Dict

from pydantic import BaseModel, RootModel


class FilterConditionsV0(BaseModel):
    eq: Any = None  # here default none makes sense only if I have multiple conditions.


class FiltersV0(RootModel):
    root: Dict[str, FilterConditionsV0]
