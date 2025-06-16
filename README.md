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
  https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?stackName=my-apprunner-service&templateURL=https://wallabyway.github.io/app-runner-template/apprunner.yaml)

[![Deploy to AWS App Runner](https://img.shields.io/badge/Deploy-to-AWS%20App%20Runner-orange?logo=amazon-aws&style=for-the-badge)](
https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review
  ?stackName=my-apprunner-service
  &templateBody=%0AAWSTemplateFormatVersion%3A%20%272010-09-09%27%0ADescription%3A%20One-click%20deploy%20this%20repo%20to%20AWS%20App%20Runner%0AParameters%3A%0A%20%20RepoUrl%3A%0A%20%20%20%20Type%3A%20String%0A%20%20%20%20Default%3A%20https%3A%2F%2Fgithub.com%2Fwallabyway%2Fapp-runner-template%0A%20%20Branch%3A%0A%20%20%20%20Type%3A%20String%0A%20%20%20%20Default%3A%20main%0AResources%3A%0A%20%20AppRunnerRole%3A%0A%20%20%20%20Type%3A%20AWS%3A%3AIAM%3A%3ARole%0A%20%20%20%20Properties%3A%0A%20%20%20%20%20%20AssumeRolePolicyDocument%3A%0A%20%20%20%20%20%20%20%20Version%3A%20%272012-10-17%27%0A%20%20%20%20%20%20%20%20Statement%3A%0A%20%20%20%20%20%20%20%20%20%20-%20Effect%3A%20Allow%0A%20%20%20%20%20%20%20%20%20%20%20%20Principal%3A%20%7B%20Service%3A%20tasks.apprunner.amazonaws.com%20%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20Action%3A%20sts%3AAssumeRole%0A%20%20%20%20%20%20ManagedPolicyArns%3A%0A%20%20%20%20%20%20%20%20-%20arn%3Aaws%3Aiam%3A%3Aaws%3Apolicy%2Fservice-role%2FAWSAppRunnerServicePolicyForECRAccess%0A%20%20MyService%3A%0A%20%20%20%20Type%3A%20AWS%3A%3AAppRunner%3A%3AService%0A%20%20%20%20Properties%3A%0A%20%20%20%20%20%20ServiceName%3A%20%21Sub%20%24%7BAWS%3A%3AStackName%7D%0A%20%20%20%20%20%20SourceConfiguration%3A%0A%20%20%20%20%20%20%20%20AuthenticationConfiguration%3A%20%7B%7D%0A%20%20%20%20%20%20%20%20AutoDeploymentsEnabled%3A%20true%0A%20%20%20%20%20%20%20%20CodeRepository%3A%0A%20%20%20%20%20%20%20%20%20%20RepositoryUrl%3A%20%21Ref%20RepoUrl%0A%20%20%20%20%20%20%20%20%20%20SourceCodeVersion%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20Type%3A%20BRANCH%0A%20%20%20%20%20%20%20%20%20%20%20%20Value%3A%20%21Ref%20Branch%0A%20%20%20%20%20%20%20%20%20%20CodeConfiguration%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20ConfigurationSource%3A%20REPOSITORY%0A)
  

Anyone who clicks the badge:
	1.	Logs in (if not already).
	2.	Lands on Create stack with every field filled.  (fill in the environment variables for APS Client/Secret and Bucket)
	3.	Hits Create stack → CloudFormation builds the role & App Runner service.
