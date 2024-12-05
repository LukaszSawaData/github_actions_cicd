import json

def extract_value(json_string, key):
 
    try:
        # Parse the JSON string into a dictionary
        parsed_data = json.loads(json_string)

        # Ensure it's a dictionary and get the key's value
        if isinstance(parsed_data, dict):
            return parsed_data.get(key)
        else:
            print("Parsed data is not a dictionary.")
            return None
    except json.JSONDecodeError as e:
        print({e})
        return None

# Example usage
data = '{"links":[{"rel":"self","href":"https:dsadsadsa/2100","action":"GET"}],"status":0,"details":null,"jobId":2100,"jobStatus":"SUCCESS","logFileName":"outbox/logs/ABG_EDPExp_2100.log","outputFileName":"outbox/dasdsa.dat","processType":"COMM_LOAD_BALANCES","executedBy":"dddsx"}'

# Get JobID
job_id = extract_value(data, 'jobId')
print(f"Job ID: {job_id}")
print(f"Job ID: {job_id}")
# Get JobStatus
job_status = extract_value(data, 'jobStatus')
print(f"Job Status: {job_status}")
print(f"Job Status: {job_status}")
