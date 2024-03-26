import requests
import os
import json
import time
import sys

# TODO github variables
user_key = sys.argv[2]
account_id = sys.argv[3]
bad_commit = "4330ccaa712b3f863b72d35b1657f57604697a72"
good_commit = "0132de8a95af3545882fa1cfa6a3edeb1f22f693"

def getEntityGuid(key, appname):

    print(f"Getting entity guid for {appname}")

    payload = '''
    {
        actor {
            account(id: '''+account_id+''') {
                nrql(query: "FROM Transaction SELECT entityGuid WHERE appName LIKE \''''+appname+'''\' LIMIT 1") {
                    results
                }
            }
        }
    }
    '''
    print(payload)

    # NerdGraph endpoint
    endpoint = "https://api.newrelic.com/graphql"
    headers = {'Content-Type': 'application/json', 'API-Key': f'{key}'}
    response = requests.post(endpoint, headers=headers, json={'query': payload})

    if response.status_code == 200:
        dict_response = json.loads(response.content)
        print(f"Success! Response: {dict_response}")
        entity_guid = dict_response['data']['actor']['account']['nrql']['results'][0]['entityGuid']
        # print(f"ENTITY GUID IS {entity_guid}")
    else:
        # raise an error with a HTTP response code
        print(response.content)
        raise Exception(f'NerdGraph query failed with a {response.status_code}.')
    return entity_guid

def sendMarker(guid, commit, msg, version):
    # user_key = self.environment.parsed_options.user_key
    # user_key = os.environ['new_relic_user_api_key']
    # guid = getEntityGuid(user_key, 'Superheroes Service')
    print(f"Sending deployment marker to guid {guid}")
    import datetime

    current_time = str(time.time_ns() // 1_000_000)

    payload = '''
    mutation {
        changeTrackingCreateDeployment(deployment: {commit: "'''+commit+'''", deploymentType: BASIC, description: "'''+msg+'''", entityGuid: "'''+guid+'''", user: "kspikowski@nrdemo.com", timestamp: '''+current_time+''', version: "'''+version+'''", groupId: "autodeploy"}) {
            entityGuid
        }
    }
    '''
    endpoint = "https://api.newrelic.com/graphql"
    headers = {'Content-Type': 'application/json', 'API-Key': f'{user_key}'}
    response = requests.post(endpoint, headers=headers, json={'query': payload})

    if response.status_code == 200:
        dict_response = json.loads(response.content)
        print(dict_response)
    else:
        print(response.content)
        # raise an error with a HTTP response code
        raise Exception(f'Nerdgraph request failed with a {response.status_code}.')
    return dict_response

if __name__ == '__main__':
    print("sanity check")
    type = sys.argv[1]
    
    if type == "":
        print("please provide an argument, badCommit or goodCommit")
        exit(0)
    # if type == "gatewayCommit":
    #     print("Sending bad commit")
    #     msg = "LaunchDarkly deployment event: Gateway updates"
    #     version = "v0.2.1"
    #     guid = getEntityGuid(user_key, "Gateway")
        # sendMarker(guid, bad_commit, msg, version)
    if type == "badCommit":
        print("Sending bad commit")
        msg = "LaunchDarkly deployment event: optimizations"
        version = "v0.2.1"
        guid = getEntityGuid(user_key, sys.argv[4])
        sendMarker(guid, bad_commit, msg, version)
    elif type == "goodCommit":
        print("Sending good commit")
        msg = "ARGOCD: Reverting previous deployment"
        version = "v0.2.2"
        guid = getEntityGuid(user_key, sys.argv[4])
        sendMarker(guid, bad_commit, msg, version)
    else:
        print("bad input")
