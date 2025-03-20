from flask import Flask, render_template, request
import os
import pdfplumber
import time
import nltk
import torch
from dotenv import load_dotenv
from bert_score import score as bert_score
from flask_sqlalchemy import SQLAlchemy
from models import db, Summary
from groq import Groq