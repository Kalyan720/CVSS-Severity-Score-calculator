
# Vulnerability CVSS Vector Analyzer

This Python script helps analyze Common Vulnerability Scoring System (CVSS) vectors for vulnerabilities listed in a CSV file.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/your-repository.git
Install dependencies:


pip install pandas cvss
Usage
Ensure your CSV file contains columns named 'vulnerability' and 'CVSS_Strings'.

Modify the script to include the correct path to your CSV file:


df = pd.read_csv(r"path of the file")
Run the script:


python analyze_vulnerabilities.py
Follow the prompts to enter a vulnerability name/identifier. The script will then display the corresponding CVSS vector, base score, and severity level.

Example
Suppose your CSV file (vulnerabilities.csv) looks like this:


vulnerability,CVSS_Strings
SQL Injection,CVSS:3.1/AV:N/AC:L/PR:H/UI:R/S:C/C:H/I:H/A:H
Cross-site Scripting,CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:C/C:L/I:L/A:L
Running the script:


Enter the name or identifier of the vulnerability: SQL Injection
CVSS Vector for SQL Injection: CVSS:3.1/AV:N/AC:L/PR:H/UI:R/S:C/C:H/I:H/A:H
Base Score: 9.8
Severity: Critical
Contributing
Contributions are welcome! If you find any issues or have suggestions, please open an issue or a pull request.
