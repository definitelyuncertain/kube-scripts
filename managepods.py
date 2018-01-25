from kubernetes import client, config
from prettytable import PrettyTable
from datetime import datetime, tzinfo


# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()

def getNamespaces():
    v1 = client.CoreV1Api()
    namespaces = v1.list_namespace()
    num_namespaces = len(namespaces.items)
    namespaces_list = []
    for i in range(num_namespaces):
        namespace = v1.list_namespace().items[i]
        name = namespace.metadata.name
        if '-namespace' not in name:
            continue
        namespaces_list.append(name)
    return namespaces_list

# Print a summary of pods
def getPods():
    current_time = datetime.now()
    v1 = client.CoreV1Api()
    pods = v1.list_pod_for_all_namespaces()

    results = []
    table = PrettyTable(["Pod", "Owner", "Node", "Start-Time", "Time-Elapsed (days)", "Status", "Reason", "GPUs"])
    for pod in pods.items:

        owner_namespace = pod.metadata.namespace
        if '-namespace' not in owner_namespace:
            continue
        owner = owner_namespace.split('-namespace')[0]

        pod_name = pod.metadata.name
        node = pod.spec.node_name
        status = pod.status.phase

        gpus = pod.spec.containers[0].resources.requests['alpha.kubernetes.io/nvidia-gpu']

        start_time = pod.status.start_time
        if start_time == None:
            time_elapsed = None
        else:
            start_time = start_time.replace(tzinfo = None)
            time_elapsed = (current_time - start_time).days

	if pod.status.container_statuses == None:
            reason = 'None'
        else:            
            pod_status = pod.status.container_statuses[0].state
            #print pod_status
            is_running = pod_status.running
            is_terminated = pod_status.terminated
            is_waiting = pod_status.waiting
            if is_running != None:
                status_obj = is_running
                reason = 'None'
            elif is_waiting != None:
                status_obj = is_waiting
                reason = status_obj.reason
            else:
                status_obj = is_terminated
                reason = status_obj.reason

        table.add_row([pod_name, owner, node, start_time, time_elapsed, status, reason, gpus])
        results.append((pod_name, owner, node, start_time, int(time_elapsed), status, reason, int(gpus)))
        
    print table
    return results

def deletePod(name, namespace):
    v1 = client.CoreV1Api()
    body = client.V1DeleteOptions()
    response = v1.delete_namespaced_pod(name, namespace, body)
    #print response

def deletePods(results):
    for result in results:
        pod_name, owner, node, start_time, time_elapsed, status, reason, gpus = result
        if status != 'Running' and time_elapsed >= 5:
            deletePod(pod_name, owner + '-namespace')
            print pod_name, owner, time_elapsed, status

def gpuWatchdog(results):
    for result in results:
        if result[-1] > 2:
            print result[0], result[1], result[2], result[-1]

results = getPods()
deletePods(results)
