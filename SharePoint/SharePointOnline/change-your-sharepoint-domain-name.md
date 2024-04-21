---
ms.date: 04/08/2024
title: "Change your SharePoint domain name"
ms.reviewer: anfra
ms.author: ruihu
author: maggierui
manager: jtremper
recommendations: true
audience: Admin
f1.keywords:
- CSH
ms.topic: article
ms.custom:
- 'SPOTADNS'
- 'O365M_DomainsWizAdd_SPOUseMultiServices'
- 'O365M_DomainsProp_SPO'
- 'O365E_DomainsWizAdd_SPOUseMultiServices'
- 'O365E_DomainsProp_SPO'
- 'O365E_DomainsMain_PublicWebsite'
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection:  
- Strat_OD_admin
- M365-collaboration
search.appverid:
- SPO160
- MOE150
- MED150
- MBS150
- BCS160
- MET150
ms.assetid: 576325ad-8c40-4fe8-8a63-68c3b7d536cf
description: "Learn about changing the domain name in your SharePoint and OneDrive URLs."
---

# Change your SharePoint domain name

When you first signed up for Microsoft 365, you created an onmicrosoft.com domain. Even if you later added a custom domain, the original onmicrosoft.com domain is used for all your SharePoint and OneDrive URLs. 

If your organization has gone through a rebranding, merger, or acquisition and needs to change the domain in your SharePoint and OneDrive URLs, you can do this using PowerShell. For example, if your organization name changed from Contoso to Fabrikam, you can change your SharePoint URLs from `contoso.sharepoint.com` to `fabrikam.sharepoint.com`.

> [!VIDEO https://www.microsoft.com/videoplayer/embed/RWOnwY]

>[!IMPORTANT]
> - The standard version of this feature is currently available to organizations that have no more than 10,000 total SharePoint sites and OneDrive accounts combined.
> - Advanced Tenant Rename is available to organizations that have less than 100,000 total sites, available with SharePoint Advanced Management. See [Advanced Tenant Rename](change-your-sharepoint-domain-name.md#advanced-tenant-rename).

> [!NOTE]
> - This change affects only SharePoint and OneDrive URLs. It doesn't impact email addresses.
> - For info about changing a site address, for example, from `https://contoso.sharepoint.com/sites/sample1` to  `https://contoso.sharepoint.com/sites/sample2`, see [Change a site address](change-site-address.md). 
> - This feature isn't available for organizations that have set up multi-geo. 
> - If your organization uses special clouds or government clouds (GCC, GCC High, DoD, etc.), or still has a .de domain, your domain name can't be changed.
> - When you rename your SharePoint domain, we create a redirect at the previous address which will expire 1 year after the rename.
> - You can only rename your SharePoint domain once. If you need additional renames, submit a support request by selecting [Rename a SharePoint Tenant more than once](https://admin.microsoft.com/AdminPortal/?searchSolutions=Rename%20a%20SharePoint%20Tenant%20more%20than%20once).
> - Changing your SharePoint domain name back to the original name after you rename it isn't supported. For example, if you change your SharePoint domain from `contoso.sharepoint.com` to `fabrikam.sharepoint.com`, changing it back to `contoso.sharepoint.com` isn't supported.

## Limitations

### Low impact

|App/feature  |Limitation  |Action required  |
|---------|---------|---------|
| Hub site menu items | Although the menu items continue to work, items that contain absolute URLs aren't changed.  | Edit the menu items and if necessary, change the URLs to the new domain name. |
| Office "Recent" and "Pinned" lists | These lists are updated over time depending on usage. | None |
| Office.com | The URLs at https://www.office.com can take 24 hours to be updated. | None |
| OneDrive | Only the domain name portion in URLs is changed. The relative path based on the User Principle Name (UPN) isn't changed. | None |
| OneDrive sync app (OneDrive.exe) | Requires version 17.3.6943.0625 or later for all users. | Make sure the URLs "oneclient.sfx.ms" and "g.live.com." aren't blocked, and that all computers in your organization can reach them to apply updates. |
| OneDrive sync app (OneDrive.exe) | The organization name displayed in Office apps isn't changed. (For example, the app displays the old folder name C:\Users\Sophia\OneDrive – Contoso) | Users can disconnect and reconnect their account in the Office app. |  
| OneNote | Requires a recent version of OneNote. | Make sure all users have the following versions installed: <br> OneNote desktop app: Version 16.0.8326.2096 or later. <br> OneNote for Windows 10: Version 16.0.8431.1006 or later. <br> OneNote mobile app: Version 16.0.8431.1011 or later. |
| OneNote | While the domain name is being changed, users might receive a notebook sync error.| None |
| SharePoint mobile apps | Requires a recent version of the mobile app. | Make sure all users have the following versions installed:<br>iOS: 4.20.0 or later. <br> Android: 3.21.0 or later. |
| SharePoint mobile apps | While the domain name is being changed, users might receive a notebook sync error. | None | 
| Search and Delve | The search index might take a while to reflect new URL changes. | None |
| Search and Delve | Search results might not be complete or might return results for the original URLs until the search index is updated.| None |
| SharePoint content  | Although content (such as text on pages) that includes the domain name continues to work, it won't be updated to display the new name. | Search for the old domain name and edit content to display the new domain name. |

### Medium impact

|App/feature  |Limitation  |Action required  |
|---------|---------|---------|
| Custom apps and Group Policy objects | Absolute URLs embedded in these apps and objects aren't changed. | Edit custom apps and Active Directory Group Policy objects that contain absolute URLs and if necessary, change the URLs to the new domain name. Confirm with third-party app publishers that apps don't contain absolute URLs. |
| Custom and third-party apps | Some apps might not process the HTTP 308 direct correctly. | Edit custom apps and work with third-party app publishers to ensure that they handle HTTP 308 responses correctly. |
| Delve | It can take 24 hours before People profiles can be viewed. | None |
| eDiscovery | Holds can't be removed until you update the URLs. | In the Microsoft Purview compliance portal, change the eDiscovery hold URLs to the new domain name. |
| InfoPath forms | Forms that use a SharePoint connection as a data source won't work. | Reconnect these forms to SharePoint. |
| Microsoft 365 Archive | Archived sites won't be renamed. | Reactivate archived sites before the rename. <br>Avoid archiving any sites during the rename. |
| Microsoft Forms | Forms that have the option to upload attachments in responses won't work. | Remove the upload button and add it again in the form. |
| Office apps | While the domain name is being changed, users might experience an error when saving Word, Excel, and PowerPoint documents that are located in a site or OneDrive. | Attempt to save the document again and if necessary change the URL of the save location. |
| OneDrive | The Quick access links in OneDrive and SharePoint won't work. | No action is available.  |
| Power Automate | Request sign-off flows that use SharePoint as a connection won’t work. | Remove and re-create the Request sign-off flow. |
| Power Automate | Any flows deployed as solutions with managed layers that use SharePoint as a connection won’t work. | Remove and re-create the flows. |
| Power BI | Power BI reports using SharePoint connections as a data source won't work. |	Before changing your domain name, download the Power BI reports that are using SharePoint connections as a data source as a .pbix file. After you change the domain name, edit the connections in the Power BI Desktop app and republish the report. <br> Power BI reports that aren't created or maintained in the Power BI Desktop app will need to be recreated. |
| Project Online | Workflows that are "in flight" won't complete and will be orphaned. <br> New workflow instances can't be initiated. <br> Association to previous workflow instances isn't available and will be orphaned. | Before changing your domain name, make sure all “in flight” workflows are completed. After you change the domain name, republish the workflows. You can then reset them to "in flight" in Project Web App by going to PWA Settings > Change or Restart Workflows. |
| Project Online | URLs embedded in workflows aren't changed. For example, if a workflow contains the embedded URL `contoso.sharepoint.com`, it isn't changed. This might impact the functionality of the workflow. | Workflows that contain URLs referring to the original domain name might need to be updated to the new name. |
| Project Online | References to PWA sites in Project Online at https://project.microsoft.com won't work. | In Project Online at https://project.microsoft.com, change the URL of the PWA sites under Settings > My PWA Site. |
| Project Online | Custom Excel Reports that use Microsoft Project Data connections as a data source won't work. | These reports need to be reconnected. |
| Project Pro | The app won't work until you update the URL of the PWA site. | Before changing your domain name, make sure that all projects that are checked out in Project Pro are checked in. After you change the domain name, change the URL of the PWA site under File > Info > Manage Accounts. |
| SharePoint 2013 workflows | Workflows that are “in flight” won't complete and will be orphaned. <br> New 2013 Workflow instances can't be initiated. <br>Association to previous workflow instances isn't available and will be orphaned. | Before changing your domain name, make sure all “in flight” workflows are completed. After you change the domain name, republish the workflows. |
| SharePoint 2013 workflows | URLs embedded in workflows aren't changed. For example, if a workflow contains the embedded URL `contoso.sharepoint.com`, it isn't changed. This might impact the functionality of the workflow. | Workflows that contain URLs referring to the original domain name might need to be updated to the new name. |
| SharePoint add-ins | Add-ins might not function as expected. | The add-ins might need to be republished. <br>Review the App configuration settings in Microsoft Entra ID for the add-in and update any URLs to the new domain name. <br> For SPFx applications, in Microsoft Entra ID update the Authentication URLs to the new domain for the SharePoint Online Client Extensibility Web Application Principal. |
| SharePoint hub sites | Sites registered as hub sites won't work. | Unregister and register the affected sites as hub sites in the SharePoint admin center after the rename. |
| SharePoint web parts | Some web parts may not function as expected. | The web parts may rely on direct URL references. Update the web parts with the new URLs. |
| Site customizations and embedded code | Absolute URLs embedded in SharePoint customizations aren't updated. | Edit customizations that contain absolute URLs and if necessary, change the URLs to the new domain name. |
| Teams on the web and Teams desktop app | The first time someone tries to access the Files tab for a team or private channel, they receive an error. The tab will work for all users after that. | None |
| Teams on the web and Teams desktop app | It can take 72 hours for meeting notes to work (for both current and previous meetings). | None |
| Teams on the web and Teams desktop app | On the Files tab, any folders added with the "Add cloud storage" (which point to another SharePoint site) won't work.| Remove and re-add the folders. |
| Teams on the web and Teams desktop app | Document libraries added as a tab won't work. | Remove and re-add the tab. |
| Teams on the web and Teams desktop app | Embedded images in Wikis won't be displayed. | Edit the Wiki.mht file located in the SharePoint Site Teams Wiki Data library and if necessary, change the URLs of the embedded images to the new domain name. |
| Teams on the web and Teams desktop app | Personal Wikis won’t work. | In a one-on-one or group chat, attach and send a file to the chat. |
| Third-party apps including backup solutions | Absolute URLs embedded in these third-party apps (including backup solutions) aren't changed. | Confirm with third-party app publishers (including backup solutions) that they support tenant renames. |
| Isolated web parts and full page apps | Isolated components are not updated and will stop working. | Solutions that contain isolated components need to be republished in the tenant app catalog. The solution will start working again after that. |

### High impact

|App/feature  |Limitation  |Action required  |
|---------|---------|---------|
| Business Productivity Online Suite (BPOS) sites | If your tenant still has Microsoft Business Productivity Online Suite (BPOS) sites remaining in it, your domain name can't be changed. | BPOS sites and its configuration need to be removed before scheduling of tenant renaming can be attempted. Submit a support request by selecting [Rename a SharePoint Tenant with BPOS sites](https://admin.microsoft.com/AdminPortal/?searchSolutions=Rename%20a%20SharePoint%20Tenant%20with%20BPOS%20sites). |
| Deleted sites | Any sites that have been deleted can't be restored after the change. | Before changing your domain name, review the Deleted sites page in the SharePoint admin center and restore any sites that you might want to keep. |
| Historical German cloud (.de) tenants | If your tenant was originally in the German cloud with a .de domain, your domain name can't be changed. This applies even if your tenant was later migrated to the regular cloud but still retains the .de domain. | No action available. |
| Locked sites and OneDrive accounts | Any site or OneDrive that has been locked (the LockState is NoAccess) can't be renamed. | Before changing your domain name, review any sites and OneDrive accounts that have been locked to determine if the lock should be removed. [Lock and unlock sites](manage-lock-status.md)|
| Multi-Geo configurations | Your SharePoint domain name can't be changed if your organization is currently set up for Microsoft 365 Multi-Geo or was previously set up for it.  | No action available. |
| Point-in-time restoration | Restoring a site to a previous time before the domain name change isn't possible. | No action available.|
| Root site replacement | Your [root site](modern-root-site.md) can't be replaced (using either the SharePoint admin center or the PowerShell cmdlet Invoke-SPOSiteSwap) between the time you schedule your domain name change and when it completes. | Replace your root site before you schedule the domain name change or after it completes. |
| SharePoint public sites | If your tenant contains old SharePoint public sites, your SharePoint domain name change won't be allowed.| Public sites on the tenant need to be removed before scheduling of tenant renaming can be attempted. Submit a support request by selecting [Rename a SharePoint Tenant with Public site](https://admin.microsoft.com/AdminPortal/?searchSolutions=Rename%20a%20SharePoint%20Tenant%20with%20Public%20site). |
| Special and government clouds | If your organization uses special clouds or government clouds (GCC, GCC High, DoD, etc.), your domain name can't be changed. | No action available. |
| Vanity domain configurations | If your SharePoint domain is, for example, teams.contoso.com (versus contoso.sharepoint.com), your domain name can't be changed. | No action available. |

## Advanced Tenant Rename
If you have over 10,000 total sites in your organization or want to have greater control over the rename operation, you can consider Advanced Tenant Rename. It supports changing the SharePoint domain on tenants with up to 100,000 total sites currently and has the ability for admins to prioritize up to 4,000 sites in their organization for early execution within the overall rename. This allows for select business-critical or high-visibility sites to complete first and reduce any risk or concerns with its impact on daily operations. 

Advanced Tenant Rename is a part of SharePoint Advanced Management.

### Prerequisites
The limited preview can currently only support tenants meeting the following conditions:
- You must have SharePoint Advanced Management licenses purchased for all users in your organization.
- Your organization has <100,000 total sites.
- Your organization doesn’t have Microsoft365 Multi Geo enabled.
- Your organization doesn’t use government clouds, including GCC, GCC High and DoD.
- Your organization doesn’t use vanity domains (from the earlier MTE offering). 

### Prioritizing sites
With Advanced Tenant Rename, you can prioritize up to 4,000 sites for early execution. This can include both OneDrive for Business and SharePoint Online sites, excluding root sites (e.g., contoso.sharepoint.com, contoso-admin.sharepoint.com, contoso-my.sharepoint.com). 

Prioritized sites would be picked up for processing first, among all the sites in your organization. This allows them the opportunity to complete their renames sooner. You can make the most of this by planning your tenant rename to start at the beginning of a low impact period (weekends, holidays, etc.) and prioritize those sites that you believe are going to be important to have accessible at the start of the next business day. 

To manage prioritization, you can make use of the following PowerShell cmdlets.
- [Set-SPOTenantRenameSitePrioritization](/powershell/module/sharepoint-online/set-spotenantrenamesiteprioritization) – This allows you to prioritize the specified site for early execution.
- [Remove-SPOTenantRenameSitePrioritization](/powershell/module/sharepoint-online/remove-spotenantrenamesiteprioritization) – This allows you to remove prioritization for the specified site.
- [Get-SPOTenantRenameSitePrioritization](/powershell/module/sharepoint-online/get-spotenantrenamesiteprioritization) – This allows you to view the current list of prioritized sites.

> [!NOTE]
> The PowerShell cmdlets for prioritization should be used once the tenant rename has been scheduled. Changes to the list of prioritized sites will be supported up to 2 hours before the scheduled start time of the rename. Once the rename starts, further changes will not be accepted. 

## Step 1: Add the new domain name

1. Check the availability of the new domain you want. For example, if you want your SharePoint and OneDrive URLs to begin with `fabrikam.sharepoint.com`, enter `https://fabrikam.sharepoint.com` in a browser. If you get a message that the address couldn’t be found (404), it’s probably available. If you get a sign-in screen or a message that your username couldn’t be found in the fabrikam.sharepoint.com directory, then the domain has already been taken and you need to try a different one. If the domain is already registered by another customer, we can't provide any information or contact the customer. 

    -or-

    If you own the domain for another subscription, you need to [delete that tenant in Microsoft Entra ID](/azure/active-directory/enterprise-users/directory-delete-howto). Deleting a tenant typically takes three days to complete and to make the domain available. 

    > [!WARNING]
    > Do NOT use the domain to test this procedure in a test environment first. If you do, you won't be able to use the domain for your production environment.

2. Add your [new .onmicrosoft.com domain using the Domains page in the M365 Admin Center](/microsoft-365/admin/setup/add-or-replace-your-onmicrosoftcom-domain#add-a-new-onmicrosoftcom-domain). 
    > [!IMPORTANT]
    > - Do not use the "Add domain" option directly present in the Domains page, since that does not create a .onmicrosoft.com domain. Use the steps in the link above to correctly create one.
    > - Do not make this domain your fallback domain.

3. Go back to the Domains page and check that the newly added .onmicrosoft.com domain appears in a 'Healthy' state.

## Step 2: Use Microsoft PowerShell to rename your domain

> [!WARNING]
> Changing your SharePoint domain name might take several hours to days depending on the number of sites and OneDrive users that you have. We strongly recommend that you make this change during a period of low usage (like a weekend) and tell users to avoid accessing SharePoint and OneDrive content during the change. In addition, any actions that create new OneDrives and sites (such as creating a new team or private channel in Microsoft Teams) will be temporarily blocked during the rename. 
  
1. **REQUIRED** - [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!IMPORTANT]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall "SharePoint Online Management Shell".
    > 
    > Make sure you review the System Requirements and Install Instructions. The app isn't supported on Mac.
  
2. Connect to SharePoint as a [Global Administrator or SharePoint Administrator](./sharepoint-admin-role.md) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).

   Example: 

   `Connect-SPOService -Url "https://contoso-admin.sharepoint.com"`
    
3. Run the following command to specify the new domain name:
  
    ```PowerShell
    Start-SPOTenantRename -DomainName <DomainName> -ScheduledDateTime <YYYY-MM-DDTHH:MM:SS> [-WhatIf] [-Confirm] 
    ```

    Where "DomainName" is the part before "sharepoint.com" or "onmicrosoft.com" and "ScheduledDateTime" is at least 24 hours in the future, but not more than 30 days. The time you enter is based on the current date and time of the computer you're using.

    Example: 

    `Start-SPOTenantRename -DomainName "fabrikam" -ScheduledDateTime "2021-12-31T10:25:00"`

    > [!NOTE]
    > If the PowerShell command Start-SPOTenantRename is not found or nothing is returned, make sure you installed the latest SharePoint Online Management Shell. Before installing the latest version, you might need to uninstall all previous versions by running `Uninstall-Module Microsoft.Online.SharePoint.PowerShell -Force -AllVersions`. For more info about the Start-SPOTenantRename cmdlet, see [Start-SPOTenantRename](/powershell/module/sharepoint-online/start-spotenantrename)

To cancel a rename that hasn't started, you can run `Stop-SPOTenantRename`. [More info about this cmdlet](/powershell/module/sharepoint-online/start-spotenantrename)

## Step 3: Prioritize sites (premium)

If you had purchased SharePoint Advanced Management licenses for all users at the time of scheduling your rename, it would be automatically considered an Advanced Tenant Rename, with the ability to prioritize sites. 

You can prioritize individual sites using the Set-SPOTenantRenameSitePrioritization cmdlet. For example, to prioritize a site _‘projectx’_, you should run the following command: 

`Set-SPOTenantRenameSitePrioritization -SiteUrl https://contoso.sharepoint.com/sites/projectx`

If you have already identified the list of sites you’d want prioritized and want to perform the Set operation in bulk, you can populate them in a CSV file and then use PowerShell to import it and iteratively execute the cmdlets. The file should just have a single column with title as ‘SiteUrl’, and every subsequent row should be the full URL of the desired site.

Example:

`Import-Csv <Path> | ForEach-Object {Set-SPOTenantRenameSitePrioritization -SiteUrl  $_.SiteUrl}`

> [!NOTE]
> If you attempt this with a file that has the entire 4,000 sites in it, the complete execution of this cmdlet can take approximately 4-6 hours. If you want shorter waiting times, we recommend splitting your list of sites up and performing this in batches.

To view the list of sites prioritized currently, run the following command: 

`Get-SPOTenantRenameSitePrioritization`

And if you want to remove prioritization for a site, you can run the Remove-SPOTenantRenameSitePrioritization cmdlet. For example, to remove prioritization for the ‘projectx’ site, you should run the following command: 

`Remove-SPOTenantRenameSitePrioritization -SiteUrl https://contoso.sharepoint.com/sites/projectx`

Please note that prioritizing a site is not a guarantee that it will be completed first. There are several factors that can affect processing times, and multiple site renames are processed in parallel. Prioritized sites have a much higher chance of completing first. 

## Step 4: Monitor the status of the rename

You can get the status of the rename by running `Get-SPOTenantRenameStatus`. Make sure you open a new PowerShell window to sign in again. The date and time shown with this command is in UTC time (but will follow the local format of the system where the cmdlet is run). [More info about Get-SPOTenantRenameStatus](/powershell/module/sharepoint-online/get-spotenantrenamestatus)

During and after the rename, you can get the state of a site by running `Get-SPOSiteRenameState`. For more info about this cmdlet, see [Get-SPOSiteRenameState](/powershell/module/sharepoint-online/get-spositerenamestate). 

To verify success of the rename operation, please ensure that you review the status of the rename operation, and the count of renamed sites in comparison to total sites. The count of sites that can't be renamed to the new domain will be shown in the **Attention Required** field. To get more information on these sites, run `Get-SPOSiteRenameState` and pass the RenameJobID listed in the tenant rename status as the ParentOperationID, and the desired status (Success/Failed/Suspended). If you want to export these results to a CSV file, you can use the `Export-Csv` cmdlet.

 `Get-SPOSiteRenameState -ParentOperationID <RenameJobID> -State Failed | Export-Csv -Path <Path>`

## Step 5: Review features and settings after the rename

1. Review any firewall rules that might block access to the new domain.

2. Review organization browser settings to make sure  the new domain is a trusted location. This includes reviewing any Group Policy settings that might control browser settings.

3. Review any third-party apps, custom apps, and scripts that access SharePoint. They might need to be modified to use the new domain.

> [!IMPORTANT]
> If you have custom SharePoint Framework solutions that require access to an API, check the API access page in the SharePoint admin center to ensure that the new domain name can be used by SharePoint Framework components.

## Troubleshooting

- [Frequently asked questions](/sharepoint/troubleshoot/administration/domain-rename-faq)
- [Errors and how to fix them](/sharepoint/troubleshoot/administration/errors-when-renaming)
