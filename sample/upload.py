from google.cloud import storage

def upload_blob(bucket_name, source_file_name, destination_blob_name, project_id):
    """
    Uploads a file to a Google Cloud Storage bucket.
    
    Args:
        bucket_name (str): The name of the bucket to upload to.
        source_file_name (str): The path to the file to upload.
        destination_blob_name (str): The name to give the uploaded file in the bucket.
        project_id (str): The ID of the Google Cloud project.
    """
    # Initialize the client with the specified project ID
    client = storage.Client(project=project_id)

    # Get the bucket
    bucket = client.bucket(bucket_name)

    # Create a blob object
    blob = bucket.blob(destination_blob_name)

    # Upload the file
    blob.upload_from_filename(source_file_name)

    print(f"File {source_file_name} uploaded to {destination_blob_name}.")

if __name__ == "__main__":
    # Replace 'your-bucket-name' with your existing bucket name
    bucket_name = "altyn_bucket123"

    # Specify the local file to upload
    source_file_name = "/home/altyn/grafana-backup-tool/grafanaSettings.json"
    
    # Specify the name for the file in the bucket
    destination_blob_name = "file.txt"

    # Replace 'your-project-id' with your Google Cloud project ID
    project_id = "electric-wave-418217"

    # Upload the file to the bucket
    upload_blob(bucket_name, source_file_name, destination_blob_name, project_id)

