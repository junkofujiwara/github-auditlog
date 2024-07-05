# GitHub Audit Log csv output generator tool

This tool is used to generate a csv file from the GitHub Audit Log API. The csv file contains the following columns:
- `timestamp_isoformat`: The timestamp of the audit log event in ISO format.
- `@timestamp`: The timestamp of the audit log event.
- `action`: The action performed in the audit log event.
- `actor`: The user who performed the action in the audit log event.
- `created_at`: The timestamp of the audit log event.
- `org`: The organization name.
- `repo`: The repository name.

## Prerequisites
- Python 3.6 or higher
- GitHub Personal Access Token

## Installation
1. Clone the repository
2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. settings.py
Modify settings.py to include the followings:
- OUTPUT_FILE: The name of the output csv file.
- LOG_FILE: The name of the log file.
- API_ENDPOINT: The GitHub API endpoint.
- SORT_ORDER: The sort order of the audit log events.
- EVENT_TYPE: The type of audit log events to retrieve.
- SEARCH_PHRASE: The search phrase to filter the audit log events.
Example<br>
`SEARCH_PHRASE = "action:workflows.completed_workflow_run AND created:>=2024-07-01"`

2. run the script
For Enterprise
```bash
python auditlog.py -t <github_personal_token> -e <enterprise_name>
```
For Organization
```bash
python auditlog.py -t <github_personal_token> -o <organization_name>
```

## References
https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/about-the-audit-log-for-your-enterprise