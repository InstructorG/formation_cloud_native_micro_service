from pathlib import Path

import yaml
from fastapi import FastAPI

from web.api.api import router

app = FastAPI(debug=True)
api_spec = yaml.safe_load((Path(__file__).parent.parent / "oas.yaml").read_text())

app.openapi = lambda: api_spec
app.include_router(router=router)