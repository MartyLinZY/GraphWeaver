# Spectrum-based Fault Localization

## Environment

- Developed & tested under Python 3.9
- To develop this module, set up the required dependencies:

  ```
  python -m pip install -r requirements.txt
  ```

Idea comes from [SBFL](https://github.com/Suresoft-GLaDOS/SBFL.git).

## Runtest

Use /tests/main.py

## Getting Started

```python
import numpy as np
import pandas as pd
from sbfl.base import SBFL
from scipy.stats import rankdata

x = np.array([
    [1,1,1,1,0,0,0],
    [0,1,0,0,1,0,0],
    [1,1,1,0,0,1,0],
    [0,1,0,0,0,0,1]
], dtype=bool)
y = np.array([0,0,1,1], dtype=bool)
formula='Dstar2'
sbfl = SBFL(formula=formula)
score=sbfl.fit_predict(x, y)
names = ['file', 'method']
elements = [
    ('m.c', 'm1'),
    ('m.c', 'm2'),
    ('m.c', 'm3'),
    ('t.c', 't1'),
    ('t.c', 't2'),
    ('t.c', 't3'),
    ('t.c', 't4'),
]
score_df = sbfl.to_frame(elements=elements, names=names)
print("Formula: "+formula)
print("-------------------------------------------------------")
print(score_df)
```

## Possible mutation testing choice

```bash
pip install mutmut
mutmut run
```
