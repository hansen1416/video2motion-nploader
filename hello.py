import os
import json

from flask import Flask, request
from flask_cors import CORS

import numpy as np


app = Flask(__name__)

cors = CORS(app)  # Allow all origins for development


@app.route("/")
def hello_world():

    # filepath = os.path.join(
    #     os.path.expanduser("~"),
    #     "Documens",
    #     "video2motion",
    #     "results3d_dataset",
    #     "anim_euler_data.npy",
    # )

    idx = int(request.args.get("idx", 0))

    filepath = "anim_euler_data.npy"

    data = np.load(filepath, allow_pickle=True)

    return {
        "data": data[idx].tolist(),
    }
