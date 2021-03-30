import os
from dotenv import load_dotenv

load_dotenv()

DATABASE=os.environ['DATABASE']
USER=os.environ['USER']
PASSWORD=os.environ['PASSWORD']
HOST=os.environ['HOST']
PORT=os.environ['PORT']

