import boto3
import datetime



ecs = boto3.client('ecs')


def lambda_handler(event, context):
   main()
   
   
def get_cluster_name():
    print(f"Fetching clusters ...")

    cluster_arns = []
    clusters = []
    response = ecs.list_clusters()
    while 'nextToken' in response:
        cluster_arns += response['clusterArns']
        response = ecs.list_clusters(nextToken=response['nextToken'])
    cluster_arns += response['clusterArns']
    
    for arn in cluster_arns:
        clusters.append(arn.split('/')[-1])

    return clusters 

def downscale_service(service_name, cluster_name):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Downscaling service {service_name} in cluster {cluster_name}...")
    
    response = ecs.update_service(
        cluster=cluster_name,
        service=service_name,
        desiredCount=0
    )
    
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        ecs.untag_resource(
            resourceArn=response['service']['serviceArn'],
            tagKeys=[
               'Lifecycle',
               'Started_At_UTC',
               'Started_By',
               'Active_till_UTC',
               'Active_duration'
            ]
            )
        print(f"Service {service_name} downscaled successfully.")

 
def main():
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")
    cluster_name = get_cluster_name()
    if not cluster_name:
        return
    
    # for cluster in cluster
    for cluster in cluster_name:
        print(f"Listing services in cluster {cluster}...")
        response = ecs.list_services(
            cluster=cluster,
            maxResults=100
        )
    
        for service_arn in response['serviceArns']:
            service_name = service_arn.split('/')[-1]
            print(f"Checking service {service_name}...")
            response = ecs.list_tags_for_resource(
                resourceArn=service_arn
            )
            print(response)
            tags = response['tags']
            lifecycle_tag = next((tag for tag in tags if tag['key'] == 'Lifecycle'), None)
            active_till_tag = next((tag for tag in tags if tag['key'] == 'Active_till_UTC'), None)
            if lifecycle_tag and lifecycle_tag['value'] == 'true':
                if active_till_tag and active_till_tag['value'] < timestamp:
                    downscale_service(service_name, cluster)
                   