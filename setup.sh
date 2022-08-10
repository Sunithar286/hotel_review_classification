{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "39b73d6e",
   "metadata": {},
   "outputs": [],
   "source": [
    "mkdir -p ~/.streamlit/\n",
    "\n",
    "echo \"\\\n",
    "[server]\\n\\\n",
    "headless = true\\n\\\n",
    "port = $PORT\\n\\\n",
    "enableCORS = false\\n\\\n",
    "\\n\\\n",
    "\" > ~/.streamlit/config.toml"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
