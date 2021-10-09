# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 20:07:07 2021

@author: home
"""

import os
import glob
import pandas as pd

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "Indian_Mutual_Funds_NAV_History.csv", index=False)