import azure.functions as func
import json
import logging

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Adding function processed a request")

    val1 = req.params.get('value1')
    val2 = req.params.get('value2')
    if not val1:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            val1 = req_body.get("value1")
            val2 = req_body.get("value2")

    if val1:
        added = val1 + val2
        retVal = {"message": f"{val1} + {val2} = {added}",
            "value": added}
        return func.HttpResponse(json.dumps(retVal), mimetype = "application/json")
    else:
        return func.HttpResponse(
             "Please pass \"value1\" and \"value2\" in order to add them!",
             status_code=400)