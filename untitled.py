import scrapper as gs 
import pandas as pd 

path = '/Users/jeremyidogun/Documents/Data Science Job Market Project /chromedriver'

df = gs.get_jobs('data scientist', 1000, False, path, 20)
