#!/bin/bash

git add . 

echo Hello Riya, Please add commit message?

read commitentry

git commit -m  "$commitentry"

git push

