#### Vibe Code: "View my Revit Model in a Browser"

Result: [viewer.aps-autodesk.com](viewer.aps-autodesk.com)

To create a simple 'View Revit Model in a Browser', we are going to vibe code a solution, choosing [Python](https://www.python.org/downloads/) for the server and [Material Design Lite](https://getmdl.io) for the frontend, using this prompt in Cursor:


`Create a Flask server with minimal code without comments or error checking.  Use APS APIs to provide endpoints /api/token, /api/upload, /api/status/<urn>, /api/list using 2-legged OAuth credentials and APS_BUCKET_KEY stored in a sample.env. Put APS logic in utils.py class (APSClient with methods for token, upload, translate, status, list, ensure_bucket), server code in server.py. Use proper APS signed S3 upload workflow (GET /signeds3upload, PUT S3, then finally POST /signeds3upload as per the docs), translate to SVF2 with base64-encoded URNs.`

`Create viewer.html with MDL lite css component featuring top bar (title, translation status label, model dropdown, upload button) and Autodesk Viewer filling remaining screen space. When the model succeeds in translating, then load the models urn.  Write optimized, minimal code with async/await, without comments or error checking. Final result: complete 3D model upload, translation, and viewing application. Create a readme.md file with complete newbie instructions on signing up for APS, installing python and where to find sample revit models from autodesk`

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

<a href="https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=my-apprunner-service&templateURL=https://public-blogs.s3.us-west-2.amazonaws.com/apprunner.yaml">
  <img src="https://img.shields.io/badge/🚀%20Deploy%20to-AWS%20App%20Runner-FF9900?style=for-the-badge&labelColor=232F3E" alt="Deploy to AWS App Runner" width="300" height="60"/>
</a>


Anyone who clicks the badge:
	1.	Logs in (if not already).
	2.	Lands on Create stack with every field filled.  (fill in the environment variables for APS Client/Secret and Bucket)
	3.	Hits Create stack → CloudFormation builds the role & App Runner service.
