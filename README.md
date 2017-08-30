## etsy_py

Python2 & Python3 module for Etsy's API.


### Installation

```
pip install etsy_py
```

### API Usage

```
from etsy_py.api import EtsyAPI

api = EtsyAPI(api_key='secret key from etsy app')

# get a list of all top level Etsy categories
r = api.get('taxonomy/categories')

data = r.json()
```

Refer to Etsy's API documentation at https://www.etsy.com/developers/ for more information.
