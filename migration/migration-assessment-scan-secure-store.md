---
title: "Migration Assessment Scan Secure Store"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 7/5/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection:
- IT_SharePoint_Hybrid_Top
- IT_Sharepoint_Server_Top
- SPMigration
- M365-collaboration
ms.custom:
ms.assetid: 8c63518d-4977-4bea-a376-09ec71b7ff56
description: "Learn how to mitigate issues with Secure Store during migration."
---

# Migration Assessment Scan: Secure Store

Learn how to mitigate issues with Secure Store during migration.
  
## Overview

Secure Store Service is a shared service that provides storage and mapping of credentials, such as account names and passwords. It enables you to securely store data that provides credentials required for connecting to external systems and associating those credentials to a specific identity or group of identities.
  
## Data Migration

Secure Store applications are not migrated to the target environment.
  
> [!IMPORTANT]
> Any site that is configured as "No Access" (locked), in SharePoint will be skipped. To see a list of locked site collections see the Locked Sites scan output. 
  
## Preparing for Migration

Determine if the Secure Store applications listed in the scan results are required on the target platform. If they are required, you will want to create them in Tenant Administration on the new platform during the migration testing.
  
> [!NOTE]
> The target environment only supports the Group Restricted type. 
  
## Post Migration

If you created Secure Store applications in the target environment, ensure they are working as expected.
  
## Scan Result Reports

 **SecureStoreApplications-detail.csv** This scan report contains the Secure Store applications configured in the source environment. The information provided should be enough for you to recreate the applications in the target environment, if necessary. 
  
> [!NOTE]
> If you see Secure Store application entries related to user profile, you should view the CustomProfilePropertyMappings output and remediation file to determine if those are in use and how to remediate. 
  
|**Column**|**Description**|
|:-----|:-----|
|ApplicationID  <br/> |Secure Store application ID.  <br/> |
|Name  <br/> |The name of the Secure Store application. This typically matches the Application ID.  <br/> |
|FriendlyName  <br/> |FriendlyName Friendly name for the Secure Store application.  <br/> |
|ContactEmail  <br/> |ContactEmail Contact email address associated with the Secure Store application.  <br/> |
|ApplicationType  <br/> |The type of the Secure Store application. The only supported option on vNext will be Group Restricted.  <br/> |
|CredentialManagementURL  <br/> |URL associated with managing credentials. This is typically not set by the user, but is provided for informational purposes  <br/> |
|TicketTimeout  <br/> |Ticket timeout associated with the Secure Store application.  <br/> |
|ScanID  <br/> |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool.  <br/> |
   

