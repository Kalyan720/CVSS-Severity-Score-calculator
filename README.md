
# Vulnerability CVSS Vector Analyzer

This Python script helps analyze Common Vulnerability Scoring System (CVSS) vectors for vulnerabilities listed in a CSV file.<br>

## Installation

1. Clone the repository:<br>

   ```bash
   git clone https://github.com/yourusername/your-repository.git
Install dependencies:<br>


pip install pandas cvss<br>
Usage
Ensure your CSV file contains columns named 'vulnerability' and 'CVSS_Strings'.
<br>
Modify the script to include the correct path to your CSV file:
<br>

df = pd.read_csv(r"path of the file")<br>
Run the script:
<br>

python analyze_vulnerabilities.py<br>
Follow the prompts to enter a vulnerability name/identifier. The script will then display the corresponding CVSS vector, base score, and severity level.
<br>
Example<br>
Suppose your CSV file (vulnerabilities.csv) looks like this:
<br>

vulnerability,CVSS_Strings<br>
SQL Injection,CVSS:3.1/AV:N/AC:L/PR:H/UI:R/S:C/C:H/I:H/A:H<br>
Cross-site Scripting,CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:C/C:L/I:L/A:L<br>
Running the script:
<br>

Enter the name or identifier of the vulnerability: SQL Injection<br>
CVSS Vector for SQL Injection: CVSS:3.1/AV:N/AC:L/PR:H/UI:R/S:C/C:H/I:H/A:H<br>
Base Score: 9.8<br>
Severity: Critical<br>
Contributing<br>
Contributions are welcome! If you find any issues or have suggestions, please open an issue or a pull request.
