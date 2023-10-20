# Start Caddy, listening on the port specified by the $PORT environment variable
caddy file-server --root /srv --listen :${PORT:-80}
