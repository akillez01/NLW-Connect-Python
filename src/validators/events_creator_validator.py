from cerberus import Validator
from src.http_types.http_response import HttpResponse

def events_creator_validator(request: any) -> HttpResponse:
    body_validator = Validator({
        "data": {
            "type": "dict",
            "schema": {
                "name": {"type": "string", "required": True, "empty": False},
            }
        }
    })
    
    response = body_validator.validate(request.json)
  
    if response is False:
        print(body_validator.errors)
    