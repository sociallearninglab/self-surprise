import pandas as pd
import json
import os

#----- Load JSON data -----#
with open('Which-block-structure-is-harder-to-build-_all-responses-identifiable.json', 'r') as json_file:
    data = json.load(json_file)
    # .json file name is that of file directly downloaded from childrenhelpingscience.com

# init spreadsheet rows
rows = []

# init list of participants to check for duplicates while processing
acceptedChildHashedIds = []

# Trial run hashedIds to exclude from data sheet
# pilotHashedIds = ["TTKT2V", "7JSGYc", "3SC55D", "S4RUKQ", "EDL4HE", "TYJ4RW", 
#                   "3ULWUU", "SLDZAV", "PXNJ4G", "VVP6Cd", "2EdMNU", "PS7SFK",
#                   "4d4FVZ",  "dJVLXS", "PVWU2P", "cWBZQX", "BT555P", "3SC55D",
#                   "AcXEDZ", "LAG4UL", "DKDdLX", "36TMYS", "UQYZSW", "65WU5P",
#                   "Y7Ec5G", "YKJc3F", "JT56FC", "Y3TXA2", "ZVRdN6", "RE7L2H",
#                   "JYCDJc", "cM7JEQ", "T37U5K", "CcSP7C", "FYPQ6J", "FUL5Y4",
#                   "MSVJPH", "ZcRdGd", "DYH253", "KBAAEX", "GESTTc", "B3YGAR",
#                   "R7VLW6", "BPLJVR", "N25L2L", "JS3LcY", "6LNL5D"]

# Specify segments to process
segments = ["7-color-check", "8-color-check", "9-warmup"] + [f"{i}-trials" for i in range(10, 24)] + ["24-attention-checks", "25-attention-checks", "28-exploratory-survey", "29-exit-survey"]

#----- For each participant, extract desired fields from JSON data -----#
for response_entry in data:
    childData = response_entry['child']
    hashedId = childData['hashed_id']
    responseData = response_entry['response']
    
    completed = responseData.get('completed', False)  # Value should be 'True'. Otherwise, default to 'False'.

    if str(responseData['date_created']).find('2024') > -1: # Filter out runs from before 2024 (should be none)
        if (hashedId not in acceptedChildHashedIds): # Filter out duplicates
            conditionData = responseData['conditions'][0]
            expData = response_entry['exp_data']
            
            # Iterate over specified segments and extract data (if available)
            for segment in segments:
                if segment in expData:
                    trialSegment = expData[segment]
                    selected = trialSegment.get('selectedImage', "MISSING")  # Default is to grab selectedImage value, and to list "MISSING" if there was no response
                    condition_list = "" # Initiate empty string for condition_list (the file name(s) of the stimuli the participants saw on screen)
                    questiontype = "harder" if "harder" in conditionData['parameterSet']['DIRECTORY'] else "easier" # log which question condition participant was in (either harder or easier)

                    if segment in ["7-color-check", "8-color-check", "9-warmup", "24-attention-checks", "25-attention-checks"]: # for non-test trials
                        for image in trialSegment['images']:
                            if image['id'] == selected:
                                condition_list = image['src'].split('/')[-1]  # Only grab filename part of the src value
                                break

                    elif segment.endswith("-trials"): # for test trials
                        for image in trialSegment['images']:
                            if image['id'] == selected:
                                condition_list = image['src'].split('/')[-1]  # Only grab filename part of the src value
                                break

                    elif segment == "28-exploratory-survey": # For exit survey
                        selected = trialSegment['formData']['freq']  # There were no images shown; grab only input value in survey from formData

                    elif segment == "29-exit-survey":
                        selected = trialSegment.get('feedback', "No feedback provided") # grab feedback if available, else print 'no feedback' message

                    # Construct rows for each participant
                    row = [
                        hashedId, # Children's hashed ID
                        response_entry['participant']['hashed_id'],  # Parents' hashed ID
                        completed, # Study completion status (true or false)
                        str(responseData['date_created']), # Date of participation
                        childData['birthday'], # Birth date
                        str(int(childData['age_rounded']) / 365)[:4], # Unrounded age in years (double)
                        round(int(childData['age_rounded']) / 365), # ROUNDED age in years
                        childData['age_rounded'], # Age in days
                        childData['gender'], # Gender
                        questiontype, # Question condition (harder or easier)
                        segment,  # Trial type
                        condition_list, # Stimulus shown in a given trial
                        selected # The response given in the respective trial
                    ]
                    rows.append(row)
                    
            acceptedChildHashedIds.append(hashedId)

    else:
        pilotHashedIds.append(hashedId)

# Define column headers
columns = [
    'child__hashed_id',
    'parent__hashed_id',
    'completed',
    'response__date_created',
    'birthday',
    'age', 
    'age_years',
    'child__age_rounded',
    'child__gender',
    'questiontype',
    'trial',
    'child__condition_list',
    'response'
]

# Create data frame
dfUnsorted = pd.DataFrame(rows, columns=columns)
df = dfUnsorted.sort_values(['age_years', 'response__date_created'], ascending=[True, True])

# Write data frame to Excel file
print(f"Total No of Participants: {len(acceptedChildHashedIds)}") # Message to be shown in terminal
output_file = 'lookit_blockbuilding_preprocessed_data.xlsx'
df.to_excel(output_file, index=False)
print(f"Data has been written to {output_file}") # Message to be shown in terminal

# Also save to data directory
additional_output_file = os.path.join('../../data/new_lookit', output_file)
df.to_excel(additional_output_file, index=False)
print(f"Data has also been written to {additional_output_file}") # Message to be shown in terminal