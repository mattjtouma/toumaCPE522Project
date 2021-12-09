#!/bin/bash

g++ mattsPublish.cpp -o mattsPublish -lpaho-mqtt3c
g++ mattsSubscribe.cpp -o mattsSubscribe -lpaho-mqtt3c
