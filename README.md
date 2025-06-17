#### View Revit Model in Browser

To create a simple 'View Revit Model in a Browser', use this prompt in Cursor:

```
Create a minimal Python Flask backend (with /api/token, /api/upload, /api/status/<urn>, and /api/list endpoints using .env containing APS client ID, secret, and bucket name in utils.py). 
Use `/signeds3upload` and `/batchcompleteupload` endpoint for the upload, encode the urn f"urn:adsk.objects:os.object:{BUCKET_KEY}/{urn}" and then translate to svf2.
Finally, create a index.html frontend with an upload button and a combo box to upload, translate, and view .rvt models using the Autodesk Viewer SDK. 
No comments or error checking, using only server.py, utils.py, and index.html.
```

#### Run it using:

```
python server.py
```



#### Grab some sample models (Revit, NWD, etc) from here:

Direct link: https://www.autodesk.com/revit-rac-basic-sample-project-2025-enu

Other Sample Revit models: https://help.autodesk.com/view/RVT/2025/ENU/?guid=GUID-61EF2F22-3A1F-4317-B925-1E85F138BE88

Navisworks sample: https://github.com/Autodesk-Forge/models.autodesk.io/tree/master/samples


#### Open a Browser

Finally, open your browser at

```
https://127.0.0.1:5000/
```
<img width="1149" alt="SCR-20250613-rdmq" src="https://gist.github.com/user-attachments/assets/ad08e6a9-1a9b-402f-b59e-7699f899d61a" />

and click the 'upload button' and select your RVT model.  Wait for it to upload and 'convert to SVF2'.

Finally, refresh the browser and select the model from the combo box.


#### Deploy to AWS App Runner

[Deploy to AWS App Runner](
  https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=my-apprunner-service&templateURL=https://public-blogs.s3.us-west-2.amazonaws.com/apprunner.yaml)


  

Anyone who clicks the badge:
	1.	Logs in (if not already).
	2.	Lands on Create stack with every field filled.  (fill in the environment variables for APS Client/Secret and Bucket)
	3.	Hits Create stack → CloudFormation builds the role & App Runner service.
