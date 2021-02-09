import os
from Question import Question, auto_learning
from File import Module
from selenium import webdriver
from Question import found_matche

data = Module(input("path>"))
while 1:
    found_matche(input("phrase>"), data.data)
