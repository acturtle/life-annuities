import pandas as pd
from cashflower import ModelPointSet


assumption = {
  "INTEREST_RATE": 0.005,
  "DEATH_PROB": 0.003,
}


policy = ModelPointSet(data=pd.DataFrame({
    "payment": [1_000],
    "remaining_term": [36],
}))
