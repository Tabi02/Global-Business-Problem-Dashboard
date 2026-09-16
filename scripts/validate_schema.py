import json
import os
import sys

def validate_schema(data_path, schema_path):
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Data file not found: {data_path}")
    if not os.path.exists(schema_path):
        raise FileNotFoundError(f"Schema file not found: {schema_path}")

    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    with open(schema_path, 'r', encoding='utf-8') as f:
        schema = json.load(f)

    # Basic structural validation without requiring external libraries
    if not isinstance(data, list):
        raise ValueError("Data must be a list of objects")

    required_fields = schema.get("items", {}).get("required", [])
    valid_severities = schema.get("items", {}).get("properties", {}).get("severity", {}).get("enum", [])

    for idx, item in enumerate(data):
        for field in required_fields:
            if field not in item:
                raise ValueError(f"Item {idx} missing required field: {field}")
        if valid_severities and item.get("severity") not in valid_severities:
            raise ValueError(f"Item {idx} has invalid severity: {item.get('severity')}")
        impact = item.get("impact_score")
        if not isinstance(impact, (int, float)) or not (0 <= impact <= 100):
            raise ValueError(f"Item {idx} has invalid impact_score: {impact}")

    print("Schema validation successful! All records conform to the schema.")
    return True

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_file = os.path.join(base_dir, "data", "sample_problems.json")
    schema_file = os.path.join(base_dir, "schema", "schema.json")

    try:
        validate_schema(data_file, schema_file)
    except Exception as e:
        print(f"Schema validation failed: {e}")
        sys.exit(1)
