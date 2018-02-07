## Client Side Multipart Upload to S3 with GetFederationToken for Temporary Client Side Access.

### Intro

If you are building an application where you need to securely upload files directly to S3 from a javascript client(browser for example), this PoC is for you.

### Setup

1. Create an S3 Bucket.

2. Update CORS Config to

  ```
  <?xml version="1.0" encoding="UTF-8"?>
  <CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
  <CORSRule>
      <AllowedOrigin>*</AllowedOrigin>
      <AllowedMethod>POST</AllowedMethod>
      <AllowedMethod>GET</AllowedMethod>
      <AllowedMethod>PUT</AllowedMethod>
      <AllowedMethod>DELETE</AllowedMethod>
      <AllowedMethod>HEAD</AllowedMethod>
      <AllowedHeader>*</AllowedHeader>
  </CORSRule>
  </CORSConfiguration>
  ```

3. Change <your-bucket-name-here> to your bucket's name in the following files:

  1. templates/test.html
  2. app.py

4. Configure Access and Secret key in app.py

5. Run the flask app

  ```$ source ./bin/activate
  $ source ./bin/activate
  $ FLASK_APP=app.py flask run
  ```

6. Open http://localhost:5000/ in your browser.

7. Select a file and click upload. Check browser console for error messages if any.

8. Selected file should be uploaded to your bucket.

### Flow

1. Generate temporary credentials on the Server Side using **GetFederationToken** call to the **AWS STS** on the server side.
2. Pass the generated temporary credentials to the client side.
3. Use the AWS Javascript SDK for Browser on the client side to securely upload the file to S3.

### Misc

1. You can also use pre-signed URLs to securely upload to S3. But the maximum file size is 5GB - https://docs.aws.amazon.com/AmazonS3/latest/dev/PresignedUrlUploadObject.html
2. Currently, there is no way to combine pre-signed URLs with MultiPartUpload. If you are uploading large files, MultiPartUpload is preferable.
3. You can also leverage any of the other ways of creating temporary credentials - https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html & https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html

### Production Considerations

If you are using this for production setup
1. Reduce the scope of the policy that is defined in app.py to the least privilage required.
2. This is purely a PoC and is not recommended to be used as is in production setup.
3. The PoC uses Access & Secret Key hard coded into the app.py file. This is not a best practice. Where possible leverage IAM Roles - https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html

### References

1. https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html
2. https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html
3. https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/S3.html#upload-property
4. https://boto3.readthedocs.io/en/latest/reference/services/sts.html#STS.Client.get_federation_token
5. http://adventure-us.guide/uploading-images-s3-using-javascript-aws-sdk/
6. https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/s3-example-photo-album.html