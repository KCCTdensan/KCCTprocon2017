import re
import math
import numpy

import GUI
from problem import problem

import QR
root_problem=problem(*QR.read_QR())
gui=GUI.GUI(root_problem)