---
ms.date: 07/19/2023
title: "Step 1 - Install the SharePoint Migration Tool (SPMT)"
ms.reviewer: 
ms.author: heidip
author: MicrosoftHeidi
manager: jtremper
recommendations: true
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: microsoft-365-migration
ms.localizationpriority: high
ms.collection: 
- IT_Sharepoint_Server_Top
- Strat_SP_gtc
- SPMigration
- M365-collaboration
- m365initiative-migratetom365
ms.custom:
- seo-marvel-apr2020
- admindeeplinkSPO
search.appverid: MET150
description: The SharePoint Migration Tool copies your files from SharePoint on-premises document libraries or regular file shares to SharePoint in Microsoft 365.
---

# Step 1:  Install the SharePoint Migration Tool (SPMT)


## Download and install

Download and install SPMT using one of the links listed below.  


| Public preview | First release | General Availability |
|:-----|:-----|:-----|
|[Install here](https://spmt.sharepointonline.com/betainstall/default.htm) |[Install here](https://aka.ms/spmt-ga-page)|[Install here](https://aka.ms/spmt-ga-page)|


### Before you begin

Before you begin using SPMT, review the required permissions, prerequisites, and endpoints.

|What|Description|
|:-----|:-----|
|Permissions required| **Global or SharePoint Admin.** To migrate at the organization-level, you must sign in as a Global or SharePoint admin in Microsoft 365.<br/>**Site Admin**. To migrate at the site collection level, you must be a site admin for that site collection.  Learn more: [Understanding permissions when using the SharePoint Migration Tool](understanding-permissions-when-migrating.md)<br/>|
|Prerequisites and Endpoints| Review the [SPMT system prerequisites and endpoints](spmt-prerequisites.md)|
|SPMT Settings|Review [SPMT settings](spmt-settings.md) to understand how settings can impact your migration|

### Understanding Custom scripts 

**Allow or prevent Custom Script (NoScript)**<br/>

In Microsoft 365, tenants can control if users can run custom script on personal sites and self-service created sites. 

During migration, some web parts require this setting set to **allow**.  Otherwise, the web part won't be migrated.

At least 24 hours before you start migration, do the following:

1. Go to <a href="https://go.microsoft.com/fwlink/?linkid=2185072" target="_blank">**Settings** in the SharePoint admin center</a>, and sign in with an account that has [admin permissions](/sharepoint/sharepoint-admin-role) for your organization.
2. At the bottom of the page, select **classic settings page**.
3. Under **Custom Script**, select:

   **Allow users to run custom script on personal sites**<br/>
   **Allow users to run customer script on self-service created sites**

   Leave these settings in place during your migration.

   > [!NOTE]
   > Changes to this setting might take up to 24 hours to take effect.

   For more info, see, [Allow or prevent custom script](/sharepoint/allow-or-prevent-custom-script).
  
      

## Proxy connections

Proxy connections aren't supported for either SharePoint or file share migrations. By default, SPMT doesn't use system proxy credentials and web requests fail if Internet Explorer proxy is configured. Examples of errors you may see include "SharePoint sign in fail" or "can't load document library". However, you can modify the SPMT app config file to follow your system proxy settings. 

If you wish to use your system proxy settings, use one of these methods:

**Update proxy** 

1. Download the latest version of SPMT. Start SPMT.
2. If SPMT doesn't connect to Microsoft 365, go to  **%localappdata%\Apps\SharePointMigrationTool\SPMT**.
3. Open the **microsoft.sharepoint.migrationtool.advancedapp.exe.config** file.
4. Uncomment the default proxy setting shown here:
    ![Edit the config file to comment out the proxy setting](media/spmt-proxy-edits.png)

5. Restart SPMT.

</br>

**If SPMT doesn't upgrade**

1. If SPMT can't upgrade itself, go to **%localappdata%\Apps\SharePointMigrationTool\InstallerClient.**
2. Open the **installclient.exe.config** file. 
3. Add the following configuration at line 31, just after the ```<appSettings></appSettings``` tag: 
</br>

   ![Edit the config file](media/spmt-proxy-edits.png)

4. Launch installclient.exe and SPMT should autoupgrade to latest SPMT release.
5. Open the **microsoft.sharepoint.migrationtool.advancedapp.exe.config** file.
6. Comment out the default proxy setting:

    ![Edit the config file to comment out the proxy setting](media/spmt-proxy-edits.png)

7. Restart SPMT.
</br></br>

## [**Step 2: Scan and assess a SharePoint site (site migration only)**](spmt-scan.md) 
</br></br>    

> [!NOTE]
> Currently, the **SharePoint Migration Tool** is not available for users of Office 365 operated by 21Vianet in China.

