import app.Services

import json

from fastapi import APIRouter, Depends, Response
from app.CommonHeaders.ResultsCommon import CommonQueryParams

router = APIRouter()



@router.get('/results', tags=["Results"])
async def get_results():
    # While the code in these to calls are identical I want to
    # show the different ways of using the __init__ namespace
    return json.dumps(app.Services.DataGenerator.create())


@router.get('/jsonResults', tags=["Results"])
async def get_json_results():
    # This will return the results as an actual json string
    return Response(content=json.dumps(app.Services.DataGenerator.create()), media_type="application/json")

@router.get("/results/", tags=["Results"])
async def results_dynamic(commons: CommonQueryParams = Depends(CommonQueryParams)):
    # While the code in these to calls are identical I want to
    # show the different ways of using the __init__ namespace
    return json.dumps(app.Services.generate_numbers(commons.start, commons.finish))
