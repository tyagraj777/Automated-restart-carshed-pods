#!/bin/bash

# Continuously monitor pods for CrashLoopBackOff
while true; do
  # Get pods in CrashLoopBackOff state
  crash_pods=$(kubectl get pods --field-selector=status.phase=Running -o json | \
               jq -r '.items[] | select(.status.containerStatuses[].state.waiting.reason=="CrashLoopBackOff") | .metadata.name')

  # Restart each pod in CrashLoopBackOff
  for pod in $crash_pods; do
    echo "Detected CrashLoopBackOff in pod: $pod. Restarting..."
    kubectl delete pod $pod
  done

  # Wait before checking again
  sleep 10
done
