## -- Importing External Modules -- ##
import uvicorn, os

## -- Importing Internal Modules -- ##
from app.routing import app

def main():
    port = int(os.environ.get("TD_PORT"))
    uvicorn.run(app, host = "0.0.0.0", port = port)

if __name__ == "__main__":
    main()