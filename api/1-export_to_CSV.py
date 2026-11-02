
ts for Base class."""
rt employee TODO list data to a CSV file."""

import csv
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    # Get employee information
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id
    )
    user = requests.get(user_url).json()

    # Get all employee tasks
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    todos = requests.get(
        todos_url, params={"userId": employee_id}
    ).json()

    # Create CSV file
    with open("{}.csv".format(employee_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        # Write all employee tasks
        for task in todos:
            writer.writerow([
                employee_id,
                user.get("username"),
                task.get("completed"),
                task.get("title")
            ])

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test Base class."""

    def test_auto_id(self):
        """Test automatic ID assignment."""

        b1 = Base()
        b2 = Base()

        self.assertEqual(b2.id, b1.id + 1)

    def test_given_id(self):
        """Test given ID."""

        b = Base(89)

        self.assertEqual(b.id, 89)

    def test_to_json_none(self):
        """Test None conversion."""

        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_empty(self):
        """Test empty list conversion."""

        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_list(self):
        """Test dictionary list conversion."""

        result = Base.to_json_string([{"id": 12}])

        self.assertEqual(result, '[{"id": 12}]')

    def test_from_json_none(self):
        """Test None conversion."""

        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_empty(self):
        """Test empty JSON list."""

        self.assertEqual(Base.from_json_string("[]"), [])
