import json
from flask import Flask, request, jsonify
app = Flask(__name__)


#Registering a voter
@app.route('/voter', methods=['POST'])
def create_record():
    record = json.loads(request.data)
    with open('./Data/voter_records.txt', 'r') as f:
        data = f.read()
    if not data:
        records = [record]
    else:
        records = json.loads(data)
        records.append(record)
    with open('./Data/voter_records.txt', 'w') as f:
        f.write(json.dumps(records, indent=2))
    return jsonify(record)


#Deregistering a voter
@app.route('/voter/<ID>', methods=['DELETE'])
def delete_record(ID):
    record = json.loads(request.data)
    new_records = []
    
    with open('./Data/voter_records.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for r in records:
            if r['ID'] == record['ID']:
                continue
            new_records.append(r)
    with open('./Data/voter_records.txt', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)


#Updating a voter's information
@app.route('/voter/<ID>', methods=['PUT'])
def update_record(ID):
    record = json.loads(request.data)
    new_records = []
    with open('./Data/voter_records.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
    for r in records:
        if r['ID'] == record['ID']:
            r['Name'] = record['Name']
            r['Year_Group'] = record['Year_Group']
            r['Major'] = record['Major']

        new_records.append(r)
    with open('./Data/voter_records.txt', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)


#Retrieving a registered voter
@app.route('/voter/<ID>', methods=['GET'])
def query_records(ID):
    with open('./Data/voter_records.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
    for record in records:
        if record['ID'] == ID:
            return record
    return jsonify({'error': 'data not found'}), 404



#Creating an election
@app.route('/election', methods=['POST'])
def create_election():
    record = json.loads(request.data)
    with open('./Data/election_data.txt', 'r') as f:
        data = f.read()
    if not data:
        records = [record]
    else:
        records = json.loads(data)
        records.append(record)
    with open('./Data/election_data.txt', 'w') as f:
        f.write(json.dumps(records, indent=2))
    return jsonify(record)


#Retrieving an election
@app.route('/election/<Election_ID>', methods=['GET'])
def query_elections(Election_ID):
    with open('./Data/election_data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
    for record in records:
        if record['Election_ID'] == Election_ID:
            return record
    return jsonify({'error': 'data not found'}), 404


#Deleting an election
@app.route('/election/<Election_ID>', methods=['DELETE'])
def delete_election(Election_ID):
    record = json.loads(request.data)
    new_records = []
    
    with open('./Data/election_data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
        for r in records:
            if r['Election_ID'] == Election_ID:
                continue
            new_records.append(r)
    with open('./Data/election_data.txt', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(record)



#Voting in an election
@app.route('/election/<Election_ID>/<Candidate_ID>', methods=['PATCH'])
def vote(Election_ID,Candidate_ID):
    new_records = []
    with open('./Data/election_data.txt', 'r') as f:
        data = f.read()
        records = json.loads(data)
    for r in records:
        if r['Election_ID'] == Election_ID:
            for c in r['Candidates']:
                if c['Candidate_ID'] == Candidate_ID:
                    c['Vote_Count'] += 1
        new_records.append(r)
    with open('./Data/election_data.txt', 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return jsonify(new_records)

app.run(debug=True)
