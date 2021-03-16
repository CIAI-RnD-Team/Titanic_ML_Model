from marshmallow import Schema, fields
from marshmallow import ValidationError

import typing as t
import json


class InvalidInputError(Exception):
    """Invalid model input."""

class SurvivorDataRequestSchema(Schema):
    PassengerId = fields.Integer()
    PClass = fields.Integer()
    Name = fields.Str()
    Sex = fields.Str()
    Age = fields.Float(allow_none=True)
    SibSp = fields.Integer()
    Parch = fields.Integer()
    Ticket = fields.Str()
    Fare = fields.Float()
    Caabin = fields.Str(allow_none=True)
    Embarked = fields.Str(allow_none=True)


def _filter_error_rows(errors: dict,
                       validated_input: t.List[dict]
                       ) -> t.List[dict]:
    """Remove input data rows with errors."""

    indexes = errors.keys()
    
    for index in sorted(indexes, reverse=True):
        del validated_input[index]

    return validated_input


def validate_inputs(input_data):
    """Check prediction inputs against schema."""

    # set many=True to allow passing in a list
    schema = SurvivorDataRequestSchema(strict=True, many=True)

    errors = None
    try:
        schema.load(input_data)
    except ValidationError as exc:
        errors = exc.messages

    if errors:
        validated_input = _filter_error_rows(
            errors=errors,
            validated_input=input_data)
    else:
        validated_input = input_data

    return validated_input, errors
