---
title: "SharePoint Migration Identity Mapping Tool"
ms.author: heidip
author: MicrosoftHeidi
manager: jtremper
recommendations: true
ms.date: 01/11/2018
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: microsoft-365-migration
ms.localizationpriority: medium
ms.collection:
- SPmigration
- M365-collaboration
- m365initiative-migratetom365
description: "Use the Identity Mapping feature of the SharePoint Migration Assessment Tool to help your Identity Migration."
---

# SharePoint Migration Identity Mapping Tool

Use the Identity Mapping feature of the SharePoint Migration Assessment Tool to help your Identity Migration.
  
> [!NOTE]
> To download the SharePoint Migration Tool, select: [Download the SharePoint Migration Assessment Tool](https://www.microsoft.com/download/details.aspx?id=53598)
  
## Introduction

Identity Migration is the process of mapping identities from the SharePoint on-premises environment to the target-state Microsoft Entra ID.
  
![Identity Mapping](media/acd1e636-0644-4848-bc2c-480b9cb29100.png)
  
Since user and group synchronization from AD to Microsoft Entra ID is new to many customers, it's essential to assign appropriate resources. Perform all internal planning and execute all identity migration-related tasks in unison with your overall on-premises migration plan.
  
The identity project's most important goal is verification that all needed users and groups are synchronized to Microsoft Entra ID. If you migrate without doing this analysis first, users could lose access to content. 
  
Reference this document for information about the process, roles and responsibilities, artifacts, and controls associated with the One-time Identity Migration process. 
  
## Overview

The goal of the identity migration is to synchronize all possible users and to disposition any remaining unmapped records with justification as to why they aren't synchronized. This synchronization and disposition process must be complete prior to preparation of user acceptance testing, which is *Dry Run 1*. All unmapped records must have valid justification and be approved by the Microsoft project team.
  
Run three different scans to perform identity mapping:
  
- [SharePoint Migration Identity Mapping Tool: SharePoint Identity Scan](sharepoint-migration-identity-mapping-tool-sharepoint-identity-scan.md)

- [SharePoint Migration Identity Mapping: Active Directory Identity Scan](sharepoint-migration-identity-mapping-active-directory-identity-scan.md)

- [SharePoint Migration Identity Mapping Tool: Microsoft Entra Identity Scan](sharepoint-migration-identity-mapping-tool-azure-active-directory-identity-scan.md)

## Process

Use this process for Users and Groups that have access to SharePoint found in the FullIdentityReport.csv report.
  
Care should be taken to ensure all required users and groups are included in the Microsoft Entra synchronization. If SharePoint content is owned by users who haven't been migrated, their user permissions won't be migrated.
  
The goal is to synchronize 100% of the identities that have access to the source SharePoint environment or provide reasons for any identities that aren't synchronized.
  
Initial preparation of all users and groups is needed to determine which users and groups to migrate.
  
- Ideally all users and groups have TypeOfMatch set to ExactMatch or PartialMatch.
    
- If there are exceptions, make notes in the MappingRationale field of the FullIdentityReport.csv file for tracking purposes.
    
 **Steps:**
  
1. Download the assessment tool to a computer in your SharePoint farm. To download, go here: [SharePoint Migration Assessment Tool](https://www.microsoft.com/download/details.aspx?id=53598)
    
2. Provide consent to allow the tool to access your Microsoft Entra ID.
    
3. Run: *SMAT.exe -GenerateIdentityMapping* 
    
4. Open **FullIdentityReport.csv** in Excel.
    
5. Filter on TypeOfMatch = NoMatch. These users and groups won't have access to content post migration. For example, contoso\johndoe is listed as NoMatch. AclExists is True. Post migration any content that contoso\johndoe had access to on the source will not work for that account post migration. A site owner needs to add contoso\johndoe's Microsoft Entra account back into permissions to resolve the issue.
    
6. Filter on TypeOfMatch = PartialMatch. Ensure the matches we found are correct. It is possible for partial matches to be incorrect if multiple people have the same Display Names or the User Principal Names changed from the source to target. 
    
7. Build a plan to remediate the gaps. For example, if you are using Windows identities and there are users and groups that have TypeOfMatch set to NoMatch or PartialMatch, then you'll typically want to sync those other users and groups to Microsoft Entra ID and rerun the identity mapping process. 
    
8. Sync other users and groups to Microsoft Entra ID. 
    
9. Repeat until you get a FullIdentityReport.csv that properly represents your expectations post migration. 
    
## Preflight validation checks

The tool performs a preflight validation check to ensure the operator has access to Microsoft Entra ID. Access to Microsoft Entra ID is required to perform the identity mapping process.
  
When prompted, enter Microsoft Entra credentials. If needed the sign in prompt asks for consent. Azure tenant admin consent is required for this application to read Microsoft Entra ID. 
  
If your sign-in fails or you're unable to provide consent, you'll see the following failure: 
  
![MigrationScanAssessmentTool-error-consent](media/df8a03a9-229d-4463-83a3-a23e04c97221.png)
  
If you say no at the prompt, the tool exits without performing any identity mapping scans.
  
If you choose to continue with the Identity Mapping process, you'll receive one more prompt when the Microsoft Entra ID scan runs. If you're unable to authenticate or provide consent at that point, the Microsoft Entra ID scan fails. You'll still receive the reports, but mapping won't be performed. The resulting output is representative of all the identities that have access to the source SharePoint environment.
  
## Configuration File

The identity mapping scans can be configured in the *ScanDef.json* file. This file is located in the same directory as SMAT.exe.
  
## Consent to read directory data

To generate the Identity Mapping Reports, you need to consent to allow assessment tool to read your Microsoft Entra directory. There are two methods available. 
  
 **Option 1:** Run the assessment tool with the -ConfigureIdentityMapping switch. 
  

This option gives the assessment tool access to your tenant's Enterprise Applications section. It allows anyone in your tenant to run the tool to perform identity mapping for migration in Microsoft 365.
  
1. Download the assessment tool from here: [SharePoint Migration Assessment Tool](https://www.microsoft.com/download/details.aspx?id=53598)
    
2. Run: SMAT.exe -ConfigureIdentityMapping
    
    > [!NOTE]
    > It is not required to run this step on the SharePoint environment. You can run the above command on any machine that has access to the Azure tenant.
  
3. When prompted with the Azure sign in dialog, enter your Azure tenant admin credentials.
    
4. When prompted for consent, select **Accept**.
    
5. The SMAT.exe application indicates the application was successfully registered. A SharePoint admin is now able to run the identity mapping process.
    
     ![Identity Mapping at the command prompt](media/c4f6fd7c-ff7c-4207-bb4f-549a350c2341.png)
  
 **Option 2:** Run the assessment tool as a user with Azure Tenant Admin rights. 
  
It's possible for a user with Azure tenant admin rights to run the tool and only provide consent for themselves.
  
1. Download the assessment tool from here: [SharePoint Migration Assessment Tool](https://www.microsoft.com/download/details.aspx?id=53598)
    
2. At the command line, type  `Run SMAT.exe -GenerateIdentityMapping`
    
3. When prompted with the Azure sign in dialog, enter your Azure Tenant Admin credentials. 
    
4. When prompted for consent, select **OK**. This will only consent the app for the sign in provided. 
    
5. The identity mapping will run and generate the needed reports. 
    
## Remove Consent

Follow the steps below to remove consent for the SharePoint Identity Mapping Application from your Azure Tenant. Once these steps have been performed, it will be necessary to provide consent the next time you run the identity mapping process. 
  
1. Browse https://portal.azure.com 
    
2. Sign in as an organization admin.
    
3. Locate Enterprise applications. 
    
4. Select **All applications**. 
    
5. In the list of applications, select **SharePoint Identity Mapping Tool**, and then select **Delete**. 
    
## Reports generated

There are two reports generated by the -GenerateIdentityMapping switch. Each report is used as part of the identity mapping process.
  
Both reports indicate users granted permissions to SharePoint content. 
  
## FullIdentityReport.csv

The *FullIdentityReport.csv* contains a dump of all the identity data we discovered about the users and groups that were listed as active in the SharePoint environment. The purpose of this report is to understand all the users and groups that have access to SharePoint and whether those identities have an associated Microsoft Entra identity.
  
If the identity isn't found in Active Directory, the Active Directory fields are empty. The *FoundInAD* field is false and *ReasonNotFoundInAD* will contain a reason code. 
  
If the identity wasn't found in Microsoft Entra ID, the Microsoft Entra ID fields will be empty. The FoundInAzureAD field will be false and ReasonNotFoundInAzureAD will contain a reason code. 
  
|**Column name**|**Source**|**Description**|
|:-----|:-----|:-----|
|UniqueID  <br/> |SharePoint  <br/> |For Windows accounts this will be a Security Identifier (SID). For non-Windows accounts, this will be the claim used to ACL SharePoint.  <br/> |
|TypeOfMatch  <br/> |Assessment Tool  <br/> |**ExactMatch** - The source identity is a Windows account and we were able to match the SID in SharePoint to the OnPremisesSecurityIdentifier in Microsoft Entra ID.  <br/> **PartialMatch** - The match was based on UserPrincipalName, Email, or Display Name. For groups, we only partial match on Display Name.  <br/> **NoMatch** - Unable to match the identity against any information.  <br/> |
|IsGroup  <br/> |SharePoint  <br/> |True if the identity is a group.  <br/> |
|ACLExists  <br/> |SharePoint  <br/> |True if the identity is associated with permissions in SharePoint. This indicates the identity has access to some piece of content.  <br/> |
|MySiteExists  <br/> |SharePoint  <br/> | True if the identity is a user and that user has a My Site/OneDrive associated with their profile.  <br/> |
|ClaimType  <br/> |SharePoint  <br/> |Type of claim authentication mode associated with the identity. This will be one of the following values Classic - These are classic Windows accounts. No claims are involved and the user was ACL'ed using a Windows Security Identifier [SID]. Windows - Windows claims. TrustedSTS - SAML claim provider. Forms - Forms authentication is used. ASPNetMembership - .NET Membership provider. ASPNetRole - .NET Role provider. ClaimProvider - Claims based provider. LocalSTS - Local SharePoint Token Service. https://social.technet.microsoft.com/wiki/contents/articles/13921.sharepoint-20102013-claims-encoding.aspx  <br/> |
|SharePointLoginName  <br/> |SharePoint  <br/> |Sign in name associated with the identity found in SharePoint.  <br/> |
|SharePointDisplayName  <br/> |SharePoint  <br/> |Display name associated with the identity found in SharePoint.  <br/> |
|SharePointProfileEmail  <br/> |SharePoint  <br/> |Email address associated with the user. This is only populated if the identity is a user, the user has a SharePoint profile, and that profile has an email set.  <br/> |
|ActiveDirectoryDisplayName  <br/> |Active Directory  <br/> |Display name found in Active Directory.  <br/> |
|ActiveDirectoryDomain  <br/> |Active Directory  <br/> |Domain name in which the identity was located.  <br/> |
|SamAccountName  <br/> |Active Directory  <br/> |Account name for the identity. This value will be empty for groups.  <br/> |
|GroupType  <br/> |Active Directory  <br/> |Type of group. This is empty for users.  <br/> |
|GroupMemberCount  <br/> |Active Directory  <br/> |Number of members in the group. This will not reflect nested group counts. For example, if there's a group that contains three other groups, this shows as 3. This value is empty for users.  <br/> |
|DistinguishedName  <br/> |Active Directory  <br/> |The distinguished name associated with the identity in Active Directory. Example: CN=Bob Smith,OU=UserAccounts,DC=contoso,DC=com  <br/> |
|AccountEnabled  <br/> |Active Directory  <br/> |True if the account is enabled in Active Directory. This is empty for groups.  <br/> |
|LastLoginTimeInAD  <br/> |Active Directory  <br/> |Date and time the user account last logged into Active Directory. This doesn't indicate the sign in was associated with SharePoint, but can be used to determine if this is an active user account. This is empty for groups.  <br/> |
|FoundInAD  <br/> |Active Directory  <br/> |True if the identity was found in Active Directory.  <br/> |
|ReasonNotFoundInAD  <br/> |Active Directory  <br/> |Reason why we didn't find the account in Active Directory. This is one of the following: BadCredentials - The username/password provided was invalid for the domain. DomainSidMatchNotFound - The SID found in SharePoint has a domain SID that doesn't match any of the located domains. InvalidSecurityIdentifier - The SID found in SharePoint is invalid. OnPremisesSidTranslationFailed - The SID appeared to be invalid, we tried to force a translation and that failed. UnableToConnect - Unable to connect to the domains. UnableToDetermine - We were unable to determine AD properties returned from the domain. UnknownException - An unexpected error occurred. Details are logged in the SMAT.log file. UserNotFoundInRemoteAd - We found a valid domain, but were unable to locate the identity using the SID. If FoundInAD is true, then this is empty.  <br/> |
|AzureObjectID  <br/> |Active Directory  <br/> |Object ID of the identity in Microsoft Entra ID.  <br/> |
|AzureUserPrincipalName  <br/> |Active Directory  <br/> |User principal name of the identity. This is only populated for users.  <br/> |
|AzureDisplayName  <br/> |Active Directory  <br/> |Display name associated with the identity in Microsoft Entra ID.  <br/> |
|FoundInAzureAD  <br/> |Active Directory  <br/> |True if the identity was located in Microsoft Entra ID.  <br/> |
|ReasonNotFoundInAzureAD  <br/> |Active Directory  <br/> |The reason why we didn't find the account in Microsoft Entra ID. The reason can be: PrincipalNotFound - Unable to locate the identity in Microsoft Entra ID. AdalExceptionFound - Authentication failure to Microsoft Entra ID. UnknownException - Unexpected error occurred. Details are in the SMAT.log file. This is empty if FoundInAzureAd is true.  <br/> |
|MappingRationale  <br/> |Active Directory  <br/> |Use this open notes field to track unmapped users.  <br/> |
|SanID  <br/> |Assessment Tool  <br/> |Unique identifier of a particular execution of the identity mapping process. Each time you run the tool, it generates a distinct ID.  <br/> |
   
## IdentityMapping.csv

IdentityMapping.csv is a pregenerated identity mapping file. All identities are represented in the file. Unmapped identities have blank values for TargetIdentity. 
  
|**Column name**|**Description**|
|:-----|:-----|
|UniqueIdentity  <br/> |Unique value to identify the object in the source environment. For Windows identities, this is the Security Identifier (SID). For all other identity types, this is the claim found in SharePoint.  <br/> |
|TargetIdentity  <br/> |Identity to map the source identity to.  <br/> For users, this value is the User Principal Name of the user in Microsoft Entra ID. For groups, this value is the Object ID of the group in Microsoft Entra ID.  <br/> |
|IsGroup  <br/> |True if the row represents a group.  <br/> |
   
## See also

#### Other Resources

[Download the SharePoint Migration Assessment Tool](https://www.microsoft.com/download/details.aspx?id=53598)
