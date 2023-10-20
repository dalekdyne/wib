# Mailing Service 📮

Used to send mails over SMTP relays.

## Development

The following are useful for development.

- `make`
- `docker`

### Developing the API locally

You can hot-reload the service by running:

```
$ make dev
```

This will use a local AGSI web server and launch the service on the first available port from `8000` in your `localhost`. 

## Deploying to a local cluster

You can test the service by loading in into a development cluster by running:

```
$ make cluster-dev
```

The target will spawn a local Kind cluster, build the image locally, and load the image to the Kind cluster's local registry. The helm chart will create the required resources for the service.

## API Docs

The documentation for the API that the service exposes is available at:

```
http:<hostname>:<api-port>/docs
```