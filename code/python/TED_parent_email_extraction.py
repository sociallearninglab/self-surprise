import pandas as pd
import json

#----- Load JSON data -----#
with open('Which-block-structure-is-harder-to-build-_all-responses-identifiable.json', 'r') as json_file:
    data = json.load(json_file)

# init spreadsheet rows
rows = []

# init list of participants to check for duplicates while processing
acceptedChildHashedIds = []

# Trial run hashedIds to exclude from data sheet
pilotHashedIds = [""]

# Specify segments to process
segments = ["0-email-address"]

#----- For each participant, extract desired fields from JSON data -----#
for response_entry in data:
    childData = response_entry['child']
    hashedId = childData['hashed_id']
    responseData = response_entry['response']

    if str(responseData['date_created']).find('2024') > -1:
        if (hashedId not in acceptedChildHashedIds) and (hashedId not in pilotHashedIds):
            conditionData = responseData['conditions'][0]
            expData = response_entry['exp_data']
            
            # Iterate over specified segments and extract data if available
            for segment in segments:
                if segment in expData:
                    trialSegment = expData[segment]
                    selected = trialSegment['formData']['email']

                    # Construct row(s) per participant
                    row = [
                        segment,  # Trial type
                        hashedId,
                        response_entry['participant']['hashed_id'],  # Parents' hashed ID
                        str(responseData['date_created']), # Date of participation
                        selected
                    ]
                    rows.append(row)
                    
            acceptedChildHashedIds.append(hashedId)

    else:
        pilotHashedIds.append(hashedId)

# Define column headers
columns = [
    'trial',
    'child__hashed_id',
    'parent__hashed_id',
    'response__date_created',
    'email'
]
# Create data frame
dfUnsorted = pd.DataFrame(rows, columns=columns)
df = dfUnsorted.sort_values(['response__date_created'], ascending=[True])

# Write DataFrame to an Excel file
output_file = 'lookit_parent_emails.xlsx'
df.to_excel(output_file, index=False)
print(f"Data has been written to {output_file}") # Message to be shown in terminal
print(f"Total No of Emails: {len(acceptedChildHashedIds)}") # Message to be shown in terminal
