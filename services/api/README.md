# podhustlr-api
podhustlr-api used from the podhustlr platform

## Development setup
### Requirements

- `python3`
- `pip3`
- `docker`
- `make`

### Installing dependencies

You can use `make` to install all the required dependencies. You may be asked to provide your `sudo` credentials.

```
make requirements
```

### Start the development MongoDB database

The API needs an active connection to a MongoDB database so that it can perform CRUD actions. Using the included `docker-compose.yml` you can create a container and a data volume to hold the data in your local machine.

```
make database
```

This will start a local MongoDB and will make it accessible on port `27017` to your `localhost`.

The connection string for local development should be `mongodb://localhost:27017`.


### Running API in hot-reload mode

There are some environment variables that are important for running the API.

- `MONGODB_HOST`
- `MONGODB_NAME`
- `GOOGLE_APPLICATION_CREDENTIALS`
- `GOOGLE_OAUTH_CLIENT_ID`
- `GOOGLE_OAUTH_CLIENT_SECRET`
- `FRONTEND_URL`

You should export those with the proper values. Usually they look like this:

```
export MONGODB_HOST="mongodb://localhost:27017"
export MONGODB_DBNAME="podhustlr-main"
...
```

We are using `Uvicorn` as our development server and it comes with a pretty neat capability of hot-reloading.

```
make dev
```

### Debug

You can use the debugging features of your IDE or editor. For VSCode the following config file can be used.

```json
```

### Lint & Format

Install `isort`, `black` and `pylint` as follows using pip:

```commandline
pip install isort
pip install black
pip install pylint
```

After that using the `make` command run:

```commandline
make fmt
make lint
```

