# Automated-restart-carshed-pods
Creating an automated system to detect and restart Kubernetes pods stuck in a CrashLoopBackOff state.


## Folder structure
![image](https://github.com/user-attachments/assets/50e22567-8be4-43a7-9f33-1dd4e47ba35d)

## Test steps

Deploy the Crashy Application


1. **Apply the crashy-app.yaml manifest::**
   ```bash
   kubectl apply -f manifests/crashy-app.yaml
  

2. **Verify that the pod enters a CrashLoopBackOff state:**
   
   ```bash
   kubectl get pods

3. **Run the CrashLoop Detection Script**

4. **Make the script executable::**
   ```bash
   chmod +x scripts/watch_crashloop.sh

5. **Run the script:.**
   ```bash
   ./scripts/watch_crashloop.sh

   **Observe the script detecting and restarting the pod.**

6. **Deploy the CronJob (Optional)**
   
   Apply the restart_crashloop_cronjob.yaml manifest:
   
   ```bash
   kubectl apply -f scripts/restart_crashloop_cronjob.yaml
  
7. **Verify the CronJob:**
   ```bash
   kubectl get cronjobs

   **Deploy the Kubernetes Operator (Optional)**
   
8. **Build the operator Docker image:**
   ```bash
   docker build -t crashloop-operator:latest manifests/operator/

9. **Push the image to a container registry (e.g., Docker Hub):**
   ```bash
   docker tag crashloop-operator:latest your-dockerhub-username/crashloop-operator:latest
   docker push your-dockerhub-username/crashloop-operator:latest

10. **Deploy the operator to your Kubernetes cluster:**  
    ```bash
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: crashloop-operator
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: crashloop-operator
      template:
        metadata:
          labels:
            app: crashloop-operator
        spec:
          containers:
          - name: operator
            image: your-dockerhub-username/crashloop-operator:latest

 11. **Apply the operator deployment:**
     ```bash
     kubectl apply -f operator-deployment.yaml
     

 ## Expected Output
    The crashy-app pod enters a CrashLoopBackOff state.

    The script, CronJob, or operator detects the CrashLoopBackOff and restarts the pod.

    The pod is recreated and continues to crash, but the system ensures it is restarted automatically.
