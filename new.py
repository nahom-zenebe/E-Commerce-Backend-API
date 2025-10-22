from fatapi import FastAPI,File,UploadFile,HTTPException
from fastapi.responses import JSONResponse

from typing import List

import origins
import shutil
from pathlib import Path