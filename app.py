{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "980d9d6c",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://localhost:8080/ (Press CTRL+C to quit)\n",
      "127.0.0.1 - - [20/Dec/2021 21:25:57] \"\u001b[37mGET / HTTP/1.1\u001b[0m\" 200 -\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "from werkzeug.wrappers import Request, Response\n",
    "from PIL import Image\n",
    "from flask import Flask, request, jsonify, render_template\n",
    "import pickle\n",
    "import io\n",
    "import base64\n",
    "\n",
    "app = Flask(__name__, template_folder='templates')\n",
    "model = pickle.load(open('model.pkl', 'rb'))\n",
    "data = io.BytesIO()\n",
    "text = \"\"\n",
    "\n",
    "@app.route('/')\n",
    "def home():\n",
    "    return render_template(\"index.html\")\n",
    "\n",
    "@app.route('/dtPredict',methods=['POST'])\n",
    "def predict():\n",
    "    int_features = [int(x) for x in request.form.values()]\n",
    "    final_features = [np.array(int_features)]\n",
    "    prediction = model.predict(final_features)\n",
    "\n",
    "    output = round(prediction[0], 2)\n",
    "    \n",
    "    if output == 1: \n",
    "        text = \" not survive\"\n",
    "    else:\n",
    "        text= \"survive\"\n",
    "    \n",
    "    return render_template(\"index.html\", prediction_text='Based on the SVM model you most likely would {}'.format(text))\n",
    "\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    from werkzeug.serving import run_simple\n",
    "    run_simple('localhost', 8080, app)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "586e9b97",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "d40a445d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "10d011d3",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "3413f019",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "3e21a85c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
