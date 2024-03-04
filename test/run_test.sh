set -e
parent_dir="$(dirname "$(pwd)")"
export PYTHONPATH="${PYTHONPATH}:${parent_dir}"

echo "Starting tests..."

pytest  ./test/testcase/test_sync
sleep 5
pytest  ./test/testcase/test_async

echo "Tests completed."

