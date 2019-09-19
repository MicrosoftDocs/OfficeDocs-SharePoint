---
title: "Migration Assessment Scan InfoPath"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: pamgreen
ms.date: 9/12/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection:
- IT_SharePoint_Hybrid_Top
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
- SPMigration
- M365-collaboration
ms.custom:
ms.assetid: ba57470a-7ef8-43ee-8ff6-8a428f6e55b9
description: "Learn how to mitigate issues with InfoPath during migration."
---

# Migration Assessment Scan: InfoPath

Learn how to mitigate issues with InfoPath during migration.
  
## Overview

InfoPath enables developers to build custom forms for accepting user input in a variety of locations throughout SharePoint. As part of the migration to the target environment, there are certain aspects of InfoPath forms that are not supported in the target environment.
  
## Data Migration

InfoPath forms (XSN files) will be migrated, but some forms may not function without remediation.
  
> [!IMPORTANT]
> Any site that is configured as "No Access" (locked), in SharePoint will be skipped. To see a list of locked site collections see the Locked Sites scan output. 
  
## Preparing for Migration

XSN files that leverage the following scenarios will need to be remediated. If remediation does not occur, these forms will fail post migration. The common scenarios are as follows:
  
- XSN or UDCX makes SOAP calls that are not supported in the target environment. These forms will need to be updated to call supported endpoints.
    
- XSN leverages managed code that will require remediation. Managed code is not supported on the target platform.
    
- InfoPath forms that leverage people picker fields. These fields need to be updated with the new user's identity post migration. This is because the on-premises identity (e.g. Windows claims) does not match the user's Azure AD/Office 365 identity.
    
## Post Migration

Ensure the updated InfoPath forms function correctly during the migration user acceptance testing phase.
  
## Scan Result Reports

The following table describes the columns in the **InfoPath-detail.csv** report. 
  
This scan report contains InfoPath forms that will require remediation prior to migration, or at a minimum, validation on the new platform.
  
|**Column**|**Description**|
|:-----|:-----|
|SiteId  <br/> |Unique identifier of the impacted site collection.  <br/> |
|SiteURL  <br/> |URL to the impacted site collection.  <br/> |
|SiteOwner  <br/> |Owner of the site collection.  <br/> |
|SiteAdmins  <br/> |List of people listed as site collection administrators.  <br/> |
|SiteSizeInMB  <br/> |Size of the size collection in megabytes [MB]  <br/> |
|NumOfWebs  <br/> |Number of webs that exist in the site collection.  <br/> |
|ContentDBName  <br/> |Name of the content database hosting the site collection.  <br/> |
|ContentDBServerName  <br/> |SQL Server hosting the content database.  <br/> |
|ContentDBSizeInMB  <br/> |Size of the content database hosting the site collection.  <br/> |
|LastContentModifiedDate  <br/> |Date/Time the site collection had content modified.  <br/> |
|TotalItemCount  <br/> |Total number of items found in the site collection.  <br/> |
|Hits  <br/> |Number of requests logged for the site collection. Relies on data from the usage logging service. If the usage logging service is disabled this row will show N/A.  <br/> |
|DistinctUsers  <br/> |Number of distinct users that have accessed the site collection. Relies on data from the usage logging service. If the usage logging service is disabled this row will show N/A.  <br/> |
|DaysOfUsageData  <br/> |Number of days the usage logging service retains data. This provides context for Hits and DistinctUsers. For example, if this is 14 days, the Hits and DistinctUsers data is for the last 14 days.  <br/> |
|URL  <br/> |Locations of the XSN.  <br/> |
|URN  <br/> |Unique identifier for the XSN file. Each XSN file will have a distinct URN.  <br/> |
|UnsupportedSoapCalls  <br/> |SOAP calls that are not explicitly listed as supported by the target environment.  <br/> |
|UnsupportedSoapCallsCount  <br/> |Number of unsupported SOAP calls found in the XSN file.  <br/> |
|UnsupportedDataConnectionTypes  <br/> |Data connections that are not supported on the new platform.  <br/> |
|UnsupportedDataConnectionCount  <br/> |Number of unsupported data connections.  <br/> |
|ManagedCode  <br/> |True - The XSN file has managed code associated with it. False - The XSN file does not have managed code associated with it.  <br/> |
|ManagedCodeState  <br/> |ValidationRequired - Managed code may work in the target environment. It will require validation during the migration testing phase to be sure.  <br/> RemediationRequired - The form has managed code that will require remediation.  <br/> |
|Mode  <br/> |The mode that the form was published in. For example, a mode of "Client" results in an InfoPath form that will only open in the InfoPath client. Whereas a mode of "Client Server" will open in both the browser and the InfoPath client. Forms with mode set to Client will not show up in this report.  <br/> |
|PeoplePickerCount  <br/> |Number of people picker fields found in the form.  <br/> |
|SolutionFormatVersion  <br/> |This field is no longer used and can be ignored.  <br/> |
|ProductVersion  <br/> |Version of InfoPath used to publish the form.  <br/> |
|ScanID  <br/> |Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool.  <br/> |
   

