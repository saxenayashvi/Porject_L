import logging
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any

from adapters.tableau.adapter import TableauAdapter


logger = logging.getLogger(__name__)
router = APIRouter()

class ExecuteRequest(BaseModel):
    adapter: str
    config: Dict[str, Any]

@router.post("/execute")
async def execute_report(req: ExecuteRequest):
    # For now only support tableau adapter name 'tableau'
    if req.adapter != 'tableau':
        raise HTTPException(status_code=400, detail="Only 'tableau' adapter is supported in this prototype")

    adapter = TableauAdapter(req.config)
    try:
        resp = adapter.connect()
        # Validate sign-in result
        ok = False
        try:
            ok = bool(getattr(resp, 'ok', False))
        except Exception:
            ok = False
        if not ok:
            logger.error('Tableau sign-in failed: %s', resp)
            raise HTTPException(status_code=400, detail=f'Tableau sign-in failed: {resp}')

        outputs = adapter.execute_report()
        adapter.close()
        return {"status": "success", "outputs": outputs}
    except HTTPException:
        raise
    except Exception as e:
        logger.exception('Execution failed')
        raise HTTPException(status_code=500, detail=str(e))