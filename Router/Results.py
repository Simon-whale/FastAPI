import Services
import json

from fastapi import APIRouter, Depends
from CommonHeaders.ResultsCommon import CommonQueryParams

router = APIRouter()



@router.get('/results', tags=["Results"])
async def get_results():
    # While the code in these to calls are identical I want to
    # show the different ways of using the __init__ namespace
    return json.dumps(Services.DataGenerator.create())


@router.get("/results/", tags=["Results"])
async def results_dynamic(commons: CommonQueryParams = Depends(CommonQueryParams)):
    # While the code in these to calls are identical I want to
    # show the different ways of using the __init__ namespace
    return json.dumps(Services.generate_numbers(commons.start, commons.finish))
