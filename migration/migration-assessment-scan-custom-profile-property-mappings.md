---
title: "Migration Assessment Scan Custom Profile Property Mappings"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
recommendations: true
ms.date: 7/5/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.subservice: sharepoint-migration
ms.localizationpriority: high
ms.collection:
- IT_SharePoint_Hybrid_Top
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
ms.custom:
ms.assetid: 5a94494c-dfb1-4849-bcee-afa95f1828c2
description: "Learn how to mitigate issues with Custom Profile Property mappings during migration."
---

# Migration Assessment Scan: Custom Profile Property Mappings

Learn how to mitigate issues with Custom Profile Property mappings during migration.
  
## Overview

In the source environment, it was possible to add other profile property mappings to the User Profile Service Application. The profile property mappings enable SharePoint to pull in profile property values from data sources outside of SharePoint. For example, you could map a profile property to an attribute in Active Directory. During a profile sync, SharePoint populated the user's profile with the value from Active Directory. Another scenario was to use Business Connectivity Services (BCS) to populate profile property values from a database or web service.
  
The target environment uses Azure Active Directory (Azure AD) to populate the SharePoint profile values. SharePoint synchronizes the most common profile data from Azure Active Directory into SharePoint. The target environment doesn't support extending the Azure AD schema and configuring other profile property mappings. If you need to populate data that is not provided by the out of the box profile property mappings, it is required to write a program that will push the values you want into the profile properties in the service.
  
For guidance on updating profile property values using the Client Side Object Model (CSOM), see:
  
- [SharePoint user profile properties now writable with CSOM](/archive/blogs/vesku/sharepoint-user-profile-properties-now-writable-with-csom)

This scan output provides you with a list of profile property mappings that won't be included in the target environment. This enables you to make a decision on the direction moving forward.
  
## Data Migration

The target environment contains the default profile property mappings for SharePoint.
  
> [!IMPORTANT]
> Any site that is configured as "No Access" (locked), in SharePoint will be skipped. To see a list of locked site collections see the Locked Sites scan output.
  
## Preparing for Migration

If the property mappings listed in the scan output are used in a SharePoint add-in or company portal, we advise you to look into the sync application discussed in the overview section to ensure that profile property data not included by default continues to be updated post migration.
  
## Post Migration

If you built a profile property sync tool, ensure the tool functions post migration.
  
## Scan Result Reports

The following table describes the columns in the **CustomProfilePropertyMappings-detail.csv** report. 
  
This scan report contains a list of all the profile property mappings that won't exist in the target environment. If you have multiple profile sync connections, you may see multiple mappings for a single profile property.
  
|Column|Description|
|---|---|
|ConnectionName|Name of the profile connection of which the property mapping is associated.|
|ConnectionType|Type of profile connection. This helps determine from where the profile property value is being pulled.|
|PropertyName|Name of the profile property. Once a profile property is created, this value can't be changed.|
|PropertyDisplayName|Display name of the profile property.|
|PropertyMapping|Attribute that the profile property is mapped to on the given connection.|
|Direction|Direction of the mapping. Either Import or Export. Import indicates the profile property value is pulled from a data source outside of SharePoint. Export indicates that the profile property value in SharePoint is pushed to an external data source.|
|PropertyLength|Length of the profile property.|
|PropertyUsage|Number of profiles that have a value for the particular property. This helps determine if this property mapping has profiles actively using it. For example, a value of 0 would indicate that no profiles have a value for the property. A value of 100,000 would indicate that 100,000 profiles have a value for the property.|
|ScanID|Unique identifier assigned to a specific execution of the SharePoint Migration Assessment Tool.|

> [!NOTE]
> Source environments will contain some properties that were previously used in a feature called Phonetic Search. This feature enabled you to search for a person's name, and the search results would return names that were similar to the name entered. This functionality no longer relies on these properties in the target environment, and as a result, they will be present in your report. If you are not explicitly using the following properties in any of your customization, you will not need to take any action on these entries. 
  
|Property Display Name|Property Name|Mapping|
|---|---|---|
|Phonetic First Name|SPS-PhoneticFirstName|MsDS-PhoneticFirstName|
|Phonetic Display Name|SPS-PhoneticDisplayName|MsDS-PhoneticDisplayName|
