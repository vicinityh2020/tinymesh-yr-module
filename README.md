# TinyMesh Yr Weather Module
A simple module to parse the XML format and extract the `temperature` 
and the `precipitation` of the Norwegian YR weather station API.

## Installation

`pip install tinymesh-yr`

## Usage

The method `get_forecast` takes in 1 argument `Town` and 1 optional parameter 
`Country` which defaults to `'Norway'`. 
Returns the most recent temperature and precipitation forecast.

## Example

```python
from yr import Weather

yr = Weather()
t, p = yr.get_forecast('Oslo')  # second parameter defaults to Norway

```
## Attribution and Terms of Use
You should read and understand the YR.no terms of use 
which is only available in Norwegian.