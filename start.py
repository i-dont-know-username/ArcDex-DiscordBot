import threading
import uvicorn
from ballsdex.api.app import app  # FastAPI admin panel
from ballsdex.__main__ import main  # Bot entrypoint

def run_api():
    uvicorn.run(app, host="0.0.0.0", port=8080)

if __name__ == "__main__":
    # Run API in a thread
    api_thread = threading.Thread(target=run_api)
    api_thread.start()

    # Start the bot
    main()
