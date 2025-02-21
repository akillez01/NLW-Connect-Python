from cerberus import Validator
from src.http_types.http_response import HttpResponse

def subscribers_creator_validator(request: any) -> HttpResponse:
    body_validator = Validator({
        "data": {
            "type": "dict",
            "schema": {
                "name": {"type": "string", "required": True, "empty": False},
                "email": {"type": "string", "required": True, "empty": False},
                "link": {"type": "string", "required": False, "empty": False},
                "evento_id": {"type": "integer", "required": True, "empty": False},
            }
        }
    })
    
    response = body_validator.validate(request.json)
  
    if response is False:
        raise Exception(body_validator.errors)