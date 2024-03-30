from google.cloud import storage

def create_bucket(bucket_name, project_id):
    """
    Creates a new Google Cloud Storage bucket.
    
    Args:
        bucket_name (str): The name of the bucket to create.
        project_id (str): The ID of the Google Cloud project.
    
    Returns:
        str: The name of the created bucket.
    """
    # Initialize the client with the specified project ID
    client = storage.Client(project=project_id)

    # Create the bucket
    bucket = client.create_bucket(bucket_name)

    print(f"Bucket {bucket.name} created.")

    return bucket.name

if __name__ == "__main__":
    # Replace 'your-bucket-name' with your desired bucket name
    bucket_name = "altyn_bucket123"
    
    # Replace 'your-project-id' with your Google Cloud project ID
    project_id = "electric-wave-418217"

    # Create the bucket
    create_bucket(bucket_name, project_id)

