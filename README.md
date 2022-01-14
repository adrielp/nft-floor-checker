# Floor Checker Discord Bot

This repository hosts a program that checks OpenSea for information with regards
to a collection. It simply requires the collection `name` and then finds out the
following information.

- Number of items listed as `Buy Now` in the collection
- Current accurate floor price of the collection
- Number of items listed at floor price within a % margin
- Evaluation of the floor (thin / very thin / ultra thin)
- Next floor price outside of the % margin
- Volume of purchases
- Transactions in the last 15 minutes

# Getting Started
To get started running this application locally, run the [run_me.sh](./run_me.sh)
script attached to setup your virtual environment, and download your necessary packages.
It will finish off by running the following developer command to bring your server
online: `uvicorn main:app --reload`

From here you can click one of the following links in order to view your API:
- [http://127.0.0.1:8000/docs#/](http://127.0.0.1:8000/docs#/)
- [http://127.0.0.1:8000/redocs#/](http://127.0.0.1:8000/redocs#/)
