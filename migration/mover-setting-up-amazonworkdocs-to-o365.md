---
title: Mover Migration Tools overview and planning
author: JoanneHendrickson
manager: pamgreen
audience: ITPro
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
ms.collection: 
- SPMigration
- M365-collaboration
search.appverid: MET150
description: "Setting up migration from AmazonWorkDocs"
---
# Setting Up the Migration from AmazonWorkDocs

## Authorizing Amazon WorkDocs

To authorize or add an Amazon WorkDocs account as a Connector, follow these steps:

1. Find Your Amazon Region
In the AWS Console go to the WorkDocs service. In the top right-hand corner in between the account’s email address and the “Support” link, click the Region selector and note which region is highlighted.

Note Your Region

Use this table or the Amazon documentation page to get the Region Code for your WorkDocs installation.

Code	Name
us-east-1	US East (N. Virginia)
us-east-2	US East (Ohio)
us-west-1	US West (N. California)
us-west-2	US West (Oregon)
eu-west-1	EU (Ireland)
eu-central-1	EU (Frankfurt)
ap-northeast-1	Asia Pacific (Tokyo)
ap-northeast-2	Asia Pacific (Seoul)
ap-southeast-1	Asia Pacific (Singapore)
ap-southeast-2	Asia Pacific (Sydney)
ap-south-1	Asia Pacific (Mumbai)
sa-east-1	South America (São Paulo)
2. Find Your Directory ID
WorkDocs is backed by Amazon’s Directory Service. Each WorkDocs installation will have a Directory Service instance. We will need the Directory ID for the WorkDocs installation in order to grant the user access to it.

Click the Services Menu in the AWS Console and select “Directory Service”.
Find the Directory Name that corresponds to your WorkDocs installation. If you created the WorkDocs installation with the default “Simple AD” the name should be something like “corp.workdocssitename.com”.
Note the Directory ID in the first column or click the item and copy the ID from the details page.
Details page:

Find Your Directory ID

3. Set Your IAM Access Policy
The user you will create to give us access to your WorkDocs installation will need to be granted full access. This is accomplished using an IAM Access Policy.

In the AWS Console select “IAM” from the Services menu
Click “Policies” in the left-hand column
Click “Create Policy”
Set Your IAM Access Policy

Click the “Select” button next to “Create Your Own Policy”
Enter a policy name (e.g. “WorkDocsFullAccess”) and description
Copy and paste the following into the “Policy Document” section:
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "WorkDocsFullAccess",
            "Effect": "Allow",
            "Action": [
                "workdocs:*"
            ],
            "Resource": [
                "*"
            ],
            "Condition": {
                "StringEquals": {
                    "Resource.OrganizationId": "directory_id"
                }
            }
        }
    ]
}
view rawAmazon WorkDocs IAM hosted with ❤ by GitHub
Replace directory_id with the Directory ID noted earlier.
Click “Validate Policy”
Click “Create Policy”
Apply Policy

4. Create an IAM User
We need to create a user that will have access to WorkDocs in order to complete the migration. This user’s key and secret will be shared with our app.

In the AWS Console select “IAM” from the Services menu
Click “Users” in the left hand column
Click “Create New User”
Enter a user name. E.g. “workdocs_migration_access”
Create User

Click “Create Users”
Click “Show User Security Credentials”
Note the “Access Key ID” and “Secret Access Key”. The “Secret Access Key” will not be shown anywhere in the AWS Console again, but a new key and secret can be generated if needed.
Access Key

Click “Close” or “Download Credentials” to save a CSV file with the key and secret of the user created.
Click on the new user in the list of users
Click the “Permissions” tab
Click “Attach Policy”
Find the Policy created earlier (“WorkDocsFullAccess” if you used the suggested name)
Click “Attach Policy”
Attach Policy

The user should now have full access to WorkDocs.

5. Authorize With Us in App
In the Transfer Wizard click Authorize New Connector.
Auth New Connector
Find Amazon WorkDocs in the Connector list.
Click Authorize.
Amazon Connector List
A new window (tab) will open. Name your Connector (Optional).
Enter your Access Key ID and Secret Access Key.
Enter your Region and Directory ID.
Amazon Name Connector
Click Authorize again, and voila!

