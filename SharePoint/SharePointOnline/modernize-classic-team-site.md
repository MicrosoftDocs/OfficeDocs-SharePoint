---
title: "Enabling communication site experiences in classic team sites"
ms.reviewer: kaarins
ms.author: dipadur
author: dipadur
manager: pamgreen
audience: Admin
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
ms.collection:  
- Strat_SP_admin
- M365-collaboration
search.appverid:
- SPO160
- MET150
- BSA160

description: "Learn about enabling communication site experience on classic team sites."
---

A SharePoint communication site is a great tool for sharing information with others. You can share news, reports, statuses, and other information in a visually compelling format. Now, any classic team site can have this capability. With a simple powershell execution, any of your classic team sites can enjoy the fantastic features of communication sites. 

> [!NOTE]
> "Some functionality is introduced gradually to organizations that have set up the [targeted release for entire organization options in Microsoft 365](https://support.office.com/en-us/article/3b3adfa4-1777-4ff0-b606-fb8732101f47). This means that you may not yet see this feature."


### Limitations

1.	Once you enable communication site experience on a classic site, you cannot revert the change.
2.	You can execute this **only on classic team sites that are not O365 group connected (i.e. the STS #0 site template)**
3.	This command cannot be executed on sub sites of a site collection
4.	The SharePoint admin running the PowerShell should also have full owner permission on the target site 
5.	Test the experience with a minimally used classic site before executing on a heavily used classic site.
6.	The target site must not have 
    a.	[SharePoint Server Publishing Infrastructure](https://support.microsoft.com/en-us/office/enable-publishing-features-479677a6-8b33-4ac7-907d-071c1c7e4518) feature enabled at the site collection OR
    b.	[SharePoint Server Publishing](https://support.microsoft.com/en-us/office/enable-publishing-features-479677a6-8b33-4ac7-907d-071c1c7e4518) feature enabled at the site level OR
    c.	Pages library in the site contents of the site. See details [here](https://support.microsoft.com/en-us/office/features-enabled-in-a-sharepoint-online-publishing-site-3ab3810c-3c2c-4361-9d0e-0cbe666ea0b0)

### What to expect after CMDLET execution:

1.	A new modern home page will be created for the root site (only the root site web, not subsites of the root site) and will be set as the home page of the site. Open the site in a new browser tab to see the changes.
    a. Please note that any user that has access to the site will see the new out-of-box communication site home page immediately after the cmdlet is executed. You can immediately change the home page of the site back to the previous page until you are ready to launch the new communication site experience in this site. 
2.	Full width pages with horizontal nav will be available (top nav from classic view will be hidden, can be seen in classic pages like the site settings page)
    a.	You can now enable site footer, mega menu, multilingual publishing etc. on this site)
3.	NoScript will be turned ON
4.	Minor Versioning on the Site Pages library will be enabled
5.	Site Pages will be the default content type in the Site Pages library
6.	NO permissions will be changed on the site
7.	NO changes to SharePoint lists and libraries experience
8.	NO changes to content types enabled in the site

### Run the PowerShell cmdlet

You can either use SharePoint Online Management Shell as a SharePoint admin OR SharePoint PnP PowerShell as site admin to enable the communication site experience in a classic team site

#### SharePoint Admin instructions

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251). You must have  SPO tenant admin PowerShell version 20122.1200 or greater.
2. If you have an older version installed, please uninstall it from Windows Add/Remove programs or by running.
3. Uninstall-Module -Name Microsoft.Online.SharePoint.PowerShell in Windows PowerShell, run as administrator
4. Make sure that all old versions of the module are uninstalled before attempting to execute the cmdlet. You can check available versions by running 
5. Get-Module -Name Microsoft.Online.SharePoint.PowerShell -ListAvailable | Select Name,Version
6. Execute these commands below
 
$orgName="tenantname"
$adminUPN = "admin@$orgname.onmicrosoft.com" ( or whatever is the admin login id)
$userCredential = Get-Credential -UserName $adminUPN -Message "Type the password."
Connect-SPOService -Url https://$orgName-admin.sharepoint.com -Credential $userCredential
Enable-SPOCommSite -SiteUrl https://$orgName.sharepoint.com


#### Site Admin instructions

1.	Follow instructions here to get started with PnP.
2.	If you are using Windows 10, run this in PowerShell 
1.	Install-Module SharePointPnPPowerShellOnline
2.	Connect-PnPOnline –Url <Url of Targetsite> –Credentials (Get-Credential)
3.	Enable-PnPCommSite

For more info about this cmdlet, see [Enable-SPOCommSite](/powershell/module/sharepoint-online/Enable-SPOCommSite). 
