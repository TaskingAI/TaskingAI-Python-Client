set -e
parent_dir="$(dirname "$(pwd)")"
export PYTHONPATH="${PYTHONPATH}:${parent_dir}"

echo "Starting tests..."

pytest  -q  --tb=no

echo "Tests completed."

