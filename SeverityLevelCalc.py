#import the libraries required
import pandas as pd #pandas is used to create dataframes and manipulation of data
from cvss import CVSS3 #cvss module is used to calculate the severity level

# insert the path of the DATA file
df = pd.read_csv(r"path of the file")

# Print the DataFrame to understand its structure
print(df)

# Prompt user for input vulnerability
vulnerability_name = input("Enter the name or identifier of the vulnerability: ")

# Find the corresponding CVSS vector based on user input
try:
    # Assuming your columns are named 'vulnerability' and 'CVSS_Strings'
    vector_column = 'CVSS_Strings'
    cvss_vector = df.loc[df['vulnerability'] == vulnerability_name, vector_column].values[0]
    print(f"CVSS Vector for {vulnerability_name}: {cvss_vector}")

    # Calculate scores using CVSS3 class
    c = CVSS3(cvss_vector)
    print(f"Base Score: {c.scores()}")
    print(f"Severity: {c.severities()}")
    
#Handling errors
except IndexError:
    print(f"No CVSS vector found for {vulnerability_name}")
except Exception as ex:
    print(f"Error: {ex}")
