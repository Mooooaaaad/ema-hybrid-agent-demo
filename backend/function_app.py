import json
import azure.functions as func

from app.maf_workflow import run_workflow

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


@app.route(route="start_workflow", methods=["GET", "POST"])
def start_workflow(req: func.HttpRequest) -> func.HttpResponse:
    try:
        body = req.get_json()
    except ValueError:
        body = {}

    result = run_workflow(body)

    return func.HttpResponse(
        json.dumps(result, ensure_ascii=False),
        mimetype="application/json",
        status_code=200
    )