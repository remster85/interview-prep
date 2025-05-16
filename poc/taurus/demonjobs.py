from kubernetes import client, config
from import_manager import get_requested_imports

# Load the Kubernetes configuration
try:
    config.load_incluster_config()  # Use this if running inside the cluster
except:
    config.load_kube_config()  # Use this if running locally

# Initialize the BatchV1 API client
batch_v1 = client.BatchV1Api()

# Specify the namespace
namespace = "taurus"

# Step 1: Fetch jobs in the 'taurus' namespace from the Kubernetes API
jobs = batch_v1.list_namespaced_job(namespace=namespace)
queued_jobs = [job.metadata.name for job in jobs.items]

# Step 2: Get the list of imports with status = 'REQUESTED'
requested_imports = get_requested_imports()

# Step 3: Check if the k8s_job_request_name is present in the queued jobs
for import_item in requested_imports:
    k8s_job_request_name = import_item["k8s_job_request_name"]
    if k8s_job_request_name in queued_jobs:
        print(f"✅ Job '{k8s_job_request_name}' is queued in Kubernetes.")
    else:
        print(f"❌ Job '{k8s_job_request_name}' is NOT found in the Kubernetes job queue.")
