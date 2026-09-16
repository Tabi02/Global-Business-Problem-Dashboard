import unittest
import os
import json
import sys

# Add root directory to sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.validate_schema import validate_schema
from scripts.generate_dashboard import generate_dashboard

class TestDashboard(unittest.TestCase):
    def setUp(self):
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.data_path = os.path.join(self.base_dir, "data", "sample_problems.json")
        self.schema_path = os.path.join(self.base_dir, "schema", "schema.json")
        self.index_path = os.path.join(self.base_dir, "index.html")

    def test_schema_validation(self):
        result = validate_schema(self.data_path, self.schema_path)
        self.assertTrue(result)

    def test_data_integrity(self):
        with open(self.data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

    def test_dashboard_generation(self):
        result = generate_dashboard()
        self.assertTrue(result)
        self.assertTrue(os.path.exists(self.index_path))
        with open(self.index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        self.assertIn("Global Business Problem Discovery Dashboard", content)

if __name__ == "__main__":
    unittest.main()
