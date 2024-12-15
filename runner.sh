#!/bin/bash

export PYTHONPATH=/PDP\ University/2-kurs/python\ backend\ 1/hotel_fastapi

uvicorn app.server.app:create_app --reload