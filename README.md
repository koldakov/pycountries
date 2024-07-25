# About The Project
[![PyPI](https://img.shields.io/pypi/v/pycountries?logo=python&logoColor=white)][pypi_proj]
[![PyPI - Downloads](https://img.shields.io/pypi/dm/pycountries?logo=python&logoColor=white)][pypi_proj]
[![PyPI - License](https://img.shields.io/pypi/l/pycountries?logo=open-source-initiative&logoColor=white)](https://github.com/AivGitHub/pycountries/blob/main/LICENSE.md)
[![docs](https://img.shields.io/readthedocs/pycountries?logo=readthedocs&logoColor=white)][documentation]

pycountries provides the ISO enums for the standards:

- [iso-4217](https://www.iso.org/iso-4217-currency-codes.html)
- [iso-3166](https://www.iso.org/iso-3166-country-codes.html)
- [iso-639](https://www.iso.org/iso-639-language-code)

pycountries can be used natively with pydantic >= 1.5 and python >= 3.8.
It makes really easy to use fastapi and other related libraries.

## Requirements

1. Python >= 3.8

## Installation

```bash
pip install pycountries
```

## Usage

Examples show how to use pycountries with pydantic + fastapi, but
you can use it with pydantic and any other libraries.

```bash
pip install fastapi
pip install pycountries
```

When you have all required libraries you can quickstart with this code:

```python
from decimal import Decimal

from fastapi import FastAPI
from pycountries import Country, Currency, Language
from pydantic import BaseModel, model_validator


app = FastAPI()


class IndexRequest(BaseModel):
    country: Country
    currency: Currency
    amount: Decimal
    language: Language

    @model_validator(mode="after")
    def validate_amount(self) -> "IndexRequest":
        # TODO: Keep in mind, you need to handle exceptions raised by clean_amount method,
        #  otherwise Internal Server Error will be raised.
        self.amount = self.currency.clean_amount(self.amount)
        return self


class IndexResponse(BaseModel):
    amount: Decimal


@app.post("/")
async def root(data: IndexRequest):
    return IndexResponse(**data.model_dump())
```

### Request Examples

```bash
curl -X POST -H "Content-Type: application/json" -d '{"country":"US", "currency":"USD", "amount":"20.20", "language":"eng"}' http://127.0.0.1:8000
{"amount":"20.20"}
curl -X POST -H "Content-Type: application/json" -d '{"country":"US", "currency":"USD", "amount":"-20.20", "language":"eng"}' http://127.0.0.1:8000
Internal Server Error
```

### Phones

I'm still not sure about the logic, if you have any ideas please create a task
[here](https://github.com/koldakov/pycountries/issues).

The problem here is that calling code is not unique per country. For example,
at least 3 countries have code +1: United States, Canada, Barbados. To determine the country
we need to see a prefix - N numbers after country code. And, looks like these prefixes are quite
dynamic, so should be managed accordingly.

For now logic is:
1. Return first calling code match if prefix is not provided.
2. If prefix is provided return first prefix match, or first "candidate" if there are no exact prefix matches.

It is very useful if you want to show phone dynamically. See an example below for more info.

```python
from pycountries import Phone

# Return first match with different types
Phone(1)  # Phone.BB
Phone("1")  # Phone.BB
Phone("+1")  # Phone.BB

# Result has changed, because results with prefixes in priority right now.
Phone(1, prefix=3)  # Phone.UM
Phone(1, prefix=32)  # Phone.UM
# Exact match found!
Phone(1, prefix=325)  # Phone.US
```

## Motivation

There is a great library [pycountry](https://github.com/pycountry/pycountry), but it is incompatible with enums,
for sure enums can be generated dynamically, but python does not work good with dynamic enums, for example, you can not
inherit from enums, annotations will be broken, etc. pycountries solves these issues and more.
Soon pycountries will be providing other ISO standards related to countries.

## Development

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Contributing

1. Fork the Project
2. Open a Pull Request
3. Or just read here: [contributing](https://docs.github.com/en/get-started/quickstart/contributing-to-projects)

<p align="right">(<a href="#top">back to top</a>)</p>

## Methodology

1. Do a lot, break a lot.
2. There are no difficult tasks, only interesting.
3. Mostly TBD.

<p align="right">(<a href="#top">back to top</a>)</p>

## Important

1. Quality.
2. Security.
3. Google first.

<p align="right">(<a href="#top">back to top</a>)</p>

## License

Distributed under the MIT License. See [LICENSE.md](LICENSE.md) for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

## Buy me a coffee if you want to support me

https://www.buymeacoffee.com/aivCoffee

## Contact

Hi all,

How are you? Hope You've enjoyed the project.

There are my contacts:

- [Linkedin](https://www.linkedin.com/in/aiv/)
- [Send an Email](mailto:coldie322@gmail.com?subject=[GitHub]-qworpa)

Project Link: https://github.com/koldakov/pycountries

Best regards,

[Ivan Koldakov](https://www.linkedin.com/in/aiv/)


[pypi_proj]: https://pypi.org/project/pycountries/
[documentation]: https://pycountries.readthedocs.io

## Visitor counter

<img src="https://profile-counter.glitch.me/pycountries/count.svg" />
