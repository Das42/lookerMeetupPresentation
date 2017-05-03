## Looker Cache Resetting Presentation

This is the code for the interactive demonstration of Looker cache resetting during the Denver Looker meetup on 5/2/2017.

The main event is the jupyter notebook that contains the example code. There are a couple of prerequisites in order to get the notebook to run:

## Setup

This repo contains a python virtualenv that contains all required packages. Clone this repo into a local directory, navigate to it, and run the following to activate the virtualenv:

`source ./lookAPI/bin/activate`

You will obviously need Python and, if you don't have it already, virtualenv. A good overview and setup guide can be found [here](http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/)

Once the environment is activated you can activate jupyter:

`jupyter notebook`

Before running the code you will need to create a YAML config file called config.yml with the following structure:

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
