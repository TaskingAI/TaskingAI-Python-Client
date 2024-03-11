set -e
parent_dir="$(dirname "$(pwd)")"
export PYTHONPATH="${PYTHONPATH}:${parent_dir}"

echo "Starting tests..."

pytest  ./test/testcase/test_sync  --reruns 2 --reruns-delay 1
sleep 5
pytest  ./test/testcase/test_async  --reruns 2 --reruns-delay 1

echo "Tests completed."

