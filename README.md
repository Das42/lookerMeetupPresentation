## Looker Cache Resetting Presentation

This is the code for the interactive demonstration of Looker cache resetting during the Denver Looker meetup on 5/2/2017.

The main event is the jupyter notebook that contains the example code. There are a couple of prerequisites in order to get the notebook to run:

## Setup

To run this notebook you will need a few things:

1. Python, 2.7 or later (I only tested on python3 but should work with 2.7 as well)
2. A swagger-generated Looker API Python SDK. You can read a great tutorial [here](https://discourse.looker.com/t/generating-client-sdks-for-the-looker-api/3185)
3. I strongly recommend setting up a virtualenv. You can read more [here](http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/)
4. The pyYAML package and the jupyter package, both installable with pip.

Once your environment is set up, fire up a jupyter session with `jupyter notebook` and select the notebook in the browser.

Note: Before running the code you will need to create a YAML config file called config.yml with the following structure:

```YAML
connection:
  id: <your API id>
  secret: <your API key>
  endpoint: https://<your-looker-host-name>:19999/api/3.0/
```

This file should be placed in the same directory as the python notebook.

## Use

Feel free to modify the code to match your particular Looker test environment. Hope it inspires some good Looker API hacking!

## Additional help and info

For more information on getting started with the Looker API, please read their intro documentation [here](https://looker.com/docs/reference/api-and-integration/api-getting-started)
