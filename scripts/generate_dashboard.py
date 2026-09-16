import json
import os

def generate_dashboard():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_file = os.path.join(base_dir, "data", "sample_problems.json")
    output_file = os.path.join(base_dir, "index.html")

    with open(data_file, 'r', encoding='utf-8') as f:
        problems = json.load(f)

    table_rows = ""
    for prob in problems:
        badge_class = "badge-critical" if prob["severity"] == "Critical" else "badge-high" if prob["severity"] == "High" else "badge-medium"
        table_rows += f"""
        <tr>
            <td><strong>{prob['id']}</strong></td>
            <td>{prob['title']}</td>
            <td><span class="badge {badge_class}">{prob['severity']}</span></td>
            <td>{prob['industry']}</td>
            <td>{prob['region']}</td>
            <td>{prob['impact_score']}</td>
            <td>{prob['description']}</td>
        </tr>
        """

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Global Business Problem Discovery Dashboard</title>
    <style>
        :root {{
            --bg-color: #0f172a;
            --card-bg: #1e293b;
            --text-color: #f8fafc;
            --text-muted: #94a3b8;
            --border-color: #334155;
            --accent-color: #38bdf8;
            --critical-color: #ef4444;
            --high-color: #f97316;
            --medium-color: #eab308;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            margin: 0;
            padding: 2rem;
        }}
        .header {{
            margin-bottom: 2rem;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 1rem;
        }}
        .header h1 {{
            margin: 0 0 0.5rem 0;
            color: var(--accent-color);
        }}
        .header p {{
            margin: 0;
            color: var(--text-muted);
        }}
        .table-container {{
            background-color: var(--card-bg);
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
            border: 1px solid var(--border-color);
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            text-align: left;
        }}
        th, td {{
            padding: 1rem;
            border-bottom: 1px solid var(--border-color);
        }}
        th {{
            background-color: #111827;
            color: var(--accent-color);
            font-weight: 600;
        }}
        tr:hover {{
            background-color: #283548;
        }}
        .badge {{
            padding: 0.25rem 0.5rem;
            border-radius: 4px;
            font-size: 0.85rem;
            font-weight: 600;
            display: inline-block;
        }}
        .badge-critical {{ background-color: rgba(239, 68, 68, 0.2); color: var(--critical-color); border: 1px solid var(--critical-color); }}
        .badge-high {{ background-color: rgba(249, 115, 22, 0.2); color: var(--high-color); border: 1px solid var(--high-color); }}
        .badge-medium {{ background-color: rgba(234, 179, 8, 0.2); color: var(--medium-color); border: 1px solid var(--medium-color); }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Global Business Problem Discovery Dashboard</h1>
        <p>Real-time analytics and tracking of critical global business challenges</p>
    </div>
    <div class="table-container">
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Title</th>
                    <th>Severity</th>
                    <th>Industry</th>
                    <th>Region</th>
                    <th>Impact Score</th>
                    <th>Description</th>
                </tr>
            </thead>
            <tbody>
                {table_rows}
            </tbody>
        </table>
    </div>
</body>
</html>
"""

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"Dashboard generated successfully at: {output_file}")
    return True

if __name__ == "__main__":
    generate_dashboard()
