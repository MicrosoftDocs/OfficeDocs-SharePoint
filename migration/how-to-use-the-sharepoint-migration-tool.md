---
title: "How to use SharePoint Migration Tool"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
recommendations: true
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: high
ms.collection: 
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
- SPMigration
- M365-collaboration
ms.custom:
- seo-marvel-apr2020
search.appverid: MET150
description: The SharePoint Migration Tool copies your files from SharePoint on-premises document libraries or regular file shares to SharePoint in Microsoft 365.
---

# Step 1:  Install the SharePoint Migration Tool (SPMT)


## Download and install

Download and install SPMT using one of the links listed below.  


|**Public preview**|**First release**|**General Availability**|
|:-----|:-----|:-----|
|[Install here](https://spmt.sharepointonline.com/betainstall/default.htm) |[Install here](https://aka.ms/spmt-ga-page)|[Install here](https://aka.ms/spmt-ga-page)|


#### Before you begin

Before you begin using SPMT, review the required permissions, prequisites, and endpoints.

|What|Description|
|:-----|:-----|
|Permissions required| **Global or SharePoint Admin.** To migrate at the organization-level, you must sign in as a Global or SharePoint admin in Microsoft 365.</br>**Site Admin**. To migrate at the site collection level, you must be a site admin for that site collection.  Learn more: [Understanding permissions when using the SharePoint Migration Tool](understanding-permissions-when-migrating.md)</br>|
|Prerequisites and Endpoints| Review the [SPMT system prerequisites and endoints](spmt-prerequisites.md)|
|SPMT Settings|Review [SPMT settings](spmt-settings.md) to understand how settings can impact your migration|

##### Understanding Custom scripts 

**Allow or prevent Custom Script (NoScript)**</br>

In Microsoft 365, tenants can control if users can run custom script on personal sites and self-service created sites. 

During migration, some web parts require this setting set to **allow**.  Otherwise, the web part will not be migrated.

At least 24 hours before you start migration, do the following:

1. Go to the [Settings page of the new SharePoint admin center](https://admin.microsoft.com/sharepoint?page=migrationCenter&modern=true), and sign in with an account that has [admin permissions](/sharepoint/sharepoint-admin-role) for your organization.

   > [!NOTE]
   > If you have Office 365 Germany, [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=848041), then browse to the SharePoint admin center and open the Settings page. <br>If you have Office 365 operated by 21Vianet (China), [sign in to the Microsoft 365 admin center](https://go.microsoft.com/fwlink/p/?linkid=850627), then browse to the SharePoint admin center and open the **Settings** page.

2. At the bottom of the page, select **classic settings page**.

3. Under **Custom Script**, select:

   **Allow users to run custom script on personal sites**</br>
   **Allow users to run customer script on self-service created sites**

   Leave these settings in place for the duration of your migration.

   > [!NOTE]
   > Changes to this setting might take up to 24 hours to take effect.

   For more info, see, [Allow or prevent custom script](/sharepoint/allow-or-prevent-custom-script).
  
      
## Next step

[**Step 2: Create a migration task**](spmt-create-task.md) 
    


## Availability  
> [!NOTE]
> Currently, the **SharePoint Migration Tool** is not available for users of Office 365 operated by 21Vianet in China. </br></br> It is also not available for users of Microsoft 365 with the German cloud with the data trustee, *German Telekom*. However, we do support it for users in Germany whose data location is not in the German datacenter.

   
## Related Topics
<a name="BKMK_Settings"> </a>

[Introducing the SharePoint Migration Tool](introducing-the-sharepoint-migration-tool.md)
  
[How the SharePoint Migration Tool works](how-the-sharepoint-migration-tool-works.md)
  
[How to format your JSON or CSV file for data content migration](how-to-format-your-csv-file-for-data-content-migration.md)
  
[Create a user mapping file for data content migration](create-a-user-mapping-file-for-data-content-migration.md)
  
[SharePoint and OneDrive migration speed](sharepoint-online-and-onedrive-migration-speed.md)
  
[SharePoint Migration Tool Feedback and Support Forum](https://social.technet.microsoft.com/Forums/en-US/home?forum=SharePointMigrationTool)
