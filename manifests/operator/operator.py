from kubernetes import client, config, watch
import os

# Load Kubernetes config
config.load_kube_config()

# Create Kubernetes API client
v1 = client.CoreV1Api()

# Watch for pod events
def watch_pods():
    w = watch.Watch()
    for event in w.stream(v1.list_pod_for_all_namespaces):
        pod = event['object']
        if pod.status.container_statuses:
            for container_status in pod.status.container_statuses:
                if container_status.state.waiting and container_status.state.waiting.reason == "CrashLoopBackOff":
                    print(f"Detected CrashLoopBackOff in pod: {pod.metadata.name}. Restarting...")
                    v1.delete_namespaced_pod(name=pod.metadata.name, namespace=pod.metadata.namespace)

if __name__ == "__main__":
    watch_pods()
