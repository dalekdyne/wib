set -e
echo "Starting application..."
uvicorn main:app --ws-ping-interval 5 --ws-ping-timeout 10 --forwarded-allow-ips "*", --host 0.0.0.0 --port ${PORT:-8000}
