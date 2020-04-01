<br>
<p align="center">
  <img alt="StreetParty" src="docs/images/street-party-logo.png" width="25%"/>
</p>
<br>

[![HitCount](http://hits.dwyl.io/street-party/api.svg)](http://hits.dwyl.io/street-party/api)
[![GitHub stars](https://img.shields.io/github/stars/street-party/api.svg)](https://GitHub.com/street-party/api/stargazers/)
[![GitHub forks](https://img.shields.io/github/forks/street-party/api.svg)](https://GitHub.com/street-party/api/network/)
[![GitHub contributors](https://img.shields.io/github/contributors/street-party/api.svg)](https://GitHub.com/street-party/api/graphs/contributors/)
[![GitHub license](https://img.shields.io/github/license/street-party/api.svg)](https://github.com/street-party/api/blob/master/LICENSE)

🍺 Back-end RESTful service for StreetParty

## Requirements

1. Python 3.7+
2. docker-ce (as provided by docker package repos)
3. docker-compose (as provided by PyPI)

## Recommendations

Usage of [virtualenv](https://realpython.com/blog/python/python-virtual-environments-a-primer/) is recommended for package library / runtime isolation.

## Usage

To run the API, please execute the following commands from the root directory:

1. Setup virtual environment

2. Install dependencies

    ```bash
    pip3 install -r requirements.lock
    ```

3. Run the server as a docker container with docker-compose

    ```bash
    docker-compose up -d --build
    ```

## Run tests

1. Just run the following command

   ```
   python3 -m unittest discover -v
   ```

## Development

### Logging

For checking the logs of the whole stack in real time, the following command is recommend it:

```bash
docker-compose logs -f
```

### How to add a new test

Create a new Python file called `test_*.py` in `test.api` with the following structure:

```python
import unittest


class NewTest(unittest.TestCase):

    def test_v0(self):
        expected = 5
        result = 2 + 3
        self.assertEqual(expected, result)

# ...


if __name__ == '__main__':
    unittest.main()

```

## License

Apache-2.0 © StreetParty
