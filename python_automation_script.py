import os
import subprocess
import pytest


def run_tests():
    # Run pytest
    result = pytest.main()

    return result

def merge_to_test():
    # Change to the project directory
    os.chdir("/users/admin/Documents/cal")

    # Check if the tests have passed
    test_result = run_tests()

    # If the tests passed, merge the dev branch to the test branch
