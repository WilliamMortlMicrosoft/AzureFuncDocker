import azure.functions as func
import json
import logging

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Summation function processed a request")

    retVal = {}
    statusCode = 200
    try:
        req_body = req.get_json()
        values = req_body.get('values')
        if not values:
            raise Exception("programmatic exception")
        else:
            summation = 0.0
            for value in values:
                summation += value
            retVal["summation"] = summation
    except Exception:
        retVal["message"] = "Please pass a numeric array of \"values\" in order to sum them!"
        statusCode = 400

    return func.HttpResponse(json.dumps(retVal), mimetype = "application/json", status_code = statusCode)