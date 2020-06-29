#DESCRITION: Import all necessary libraries. initialize pygame and set window dimensions.

import pygame as pg
import numpy as np
from random import randint
from math import exp, pi, log, tan, fmod, atan, asin
import json

pg.init()
myfont = pg.font.SysFont("Times New Roman", 14)
WIDTH, HEIGHT = 800, 600
screen = pg.display.set_mode((WIDTH, HEIGHT))