---
title: "Enable the communication site experience on classic team sites"
ms.reviewer: dipadur
ms.author: mikeplum
author: MikePlumleyMSFT
manager: serdars
recommendations: true
audience: Admin
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: medium
ms.collection:  
- Strat_SP_admin
- M365-collaboration
ms.custom: admindeeplinkSPO
ROBOTS: NOINDEX
search.appverid:
- SPO160
- MET150
- BSA160

description: "Learn how to modernize classic team sites by enabling the communication site experience."
---

# Enable the communication site experience on classic team sites
A SharePoint [communication site](https://support.office.com/en-us/article/94a33429-e580-45c3-a090-5512a8070732) is a great tool for sharing information with others in your organization. Your users can share news, reports, statuses, and other information in a visually compelling format. Now, any classic team site can have this capability too. By running a PowerShell cmdlet, you can bring modern communication site features to your classic team sites. 

## Requirements

- The site must be a **classic team site that's not connected to a Microsoft 365 group** (the STS #0 site template).
- The site must be the top-level site in the site collection. It can't be a subsite.
- The user who runs the PowerShell cmdlet must have full owner permission on the target site.
- The site must not have SharePoint Server Publishing Infrastructure enabled at the site collection level or SharePoint Server Publishing enabled at the site level. [Learn how to enable and disable publishing features](https://support.microsoft.com/office/479677a6-8b33-4ac7-907d-071c1c7e4518). If these features were previously enabled but have been deactivated, go to the [site contents page](https://support.microsoft.com/office/ba495c1e-00f4-475d-97c7-b518d546566b) and make sure it doesn't still contain a Pages library. [Learn more about features enabled on a publishing site](https://support.microsoft.com/office/3ab3810c-3c2c-4361-9d0e-0cbe666ea0b0)

## Effects of this change

- A new modern page is created in the site and set as the home page. Open the site in a new tab to see the changes. 
- Any user that has access to the site will see the new home page with the default web parts and content immediately. Until you're ready to launch the new communication site experience, you can change the home page back to the former page.
- Full width pages with horizontal navigation are available. (The top navigation from classic view is hidden, but can be seen on classic pages like the site settings page.) You can now [customize the navigation](https://support.office.com/article/Customize-the-navigation-on-your-SharePoint-site-3cd61ae7-a9ed-4e1e-bf6d-4655f0bf25ca) on this site.
- [Custom script](allow-or-prevent-custom-script.md) isn't allowed on the site.
- Minor versioning on the Site Pages library is enabled. [Learn more about versioning](https://support.microsoft.com/office/0f6cd105-974f-44a4-aadb-43ac5bdfd247)
- Site Pages are the default [content type](https://support.microsoft.com/office/e1277a2e-a1e8-4473-9126-91a0647766e5) in the Site Pages library
- No site permissions are changed.
- The SharePoint lists and libraries experience isn't changed.
- Any content types enabled in the site aren't changed.
- If the classic site collection had subsites, they aren't changed. 
- If you intend to launch this site as a high traffic portal experience or share the site with a large number of users, make sure to follow the [portal launch guidelines](portal-health.md).

## Run the PowerShell cmdlet

You can use either the SharePoint Online Management Shell **OR** SharePoint PnP PowerShell to enable the communication site experience on a classic team site. We recommend that you test the experience with a minimally used classic site before running it on popular classic sites in your organization.

> [!IMPORTANT]
> After you enable the communication site experience on a classic site, you can't undo the change.

### SharePoint admin instructions

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251). Version 20122.1200 or later is required.

    > [!NOTE]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall "SharePoint Online Management Shell." 

2. Connect to SharePoint as a [global admin or SharePoint admin](./sharepoint-admin-role.md) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).

3. Run the following command:

    ```PowerShell
    Enable-SPOCommSite -SiteUrl <URL of target site>
    ```

For more info about this cmdlet, see [Enable-SPOCommSite](/powershell/module/sharepoint-online/Enable-SPOCommSite). 

### Site admin instructions

1. [Learn how to use SharePoint PnP PowerShell commands](/powershell/sharepoint/sharepoint-pnp/sharepoint-pnp-cmdlets?view=sharepoint-ps&preserve-view=true).
2. In Windows 10, run the following commands in PowerShell:

    ```PowerShell
    Install-Module SharePointPnPPowerShellOnline
    Connect-PnPOnline –Url <Url of Targetsite> –Credentials (Get-Credential)
    Enable-PnPCommSite
    ```

## Frequently asked questions

**Will this cmdlet change all my classic sites?**

- No. The cmdlet can be run on one site at time.

**Will this cmdlet change the site template?**

- No. The cmdlet enables communication site features, but the site still has the STS#0 site template. The site will continue to appear as "Team site (classic experience)" in the <a href="https://go.microsoft.com/fwlink/?linkid=2185219" target="_blank">SharePoint admin center</a>.

**Why can't I use this cmdlet on publishing sites?**

- The modern communication site experience isn't compatible with SharePoint Server publishing features.

**Can I run this command on the root site in my organization?**

- Yes, if you meet the requirements listed at the beginning of this article.

**How can I get a list of all classic sites that have the communication site experience enabled?**

```PowerShell
function Get-CommsiteEnabledSites{
 
    $adminUrl = Read-Host "Enter the Admin URL of O365 (eg. https://<Tenant Name>-admin.sharepoint.com)" 
    $userName = Read-Host "Enter the username of O365 (eg. admin@<tenantName>.onmicrosoft.com)" 
    $password = Read-Host "Please enter the password for $($userName)" -AsSecureString
 
    # set credentials 
    $credentials = New-Object -TypeName System.Management.Automation.PSCredential -argumentlist $userName, $password 
    $SPOCredentials = New-Object Microsoft.SharePoint.Client.SharePointOnlineCredentials($userName, $password)
 
    #connect to to Office 365
 
    try{
 
        Connect-SPOService -Url $adminUrl -Credential $credentials 
        write-host "Info: Connected succesfully to Office 365" -foregroundcolor green
 
    }
 
    catch{
 
        write-host "Error: Could not connect to Office 365" -foregroundcolor red         
        Break connectToO365
 
    }
    get-siteCollections  
}
 

 
function get-siteCollections{
 
    write-host "----- List of classic sites with comm site feature enabled  -------" -foregroundcolor green

#Get all site collections
	$siteCollections = Get-SPOSite
	 
	#loop through all site collections
	foreach ($siteCollection in $siteCollections){
	 
		#set variable for a tab in the table
		$pixelsweb = 0
		$pixelslist = 0
		$enabledCommSite = Get-SPOIsCommSiteEnabled($siteCollection.url)
		$background = "white"
		if($enabledCommSite -ne ""){
			$background = "cyan"
		}		
	}
}

function Get-SPOIsCommSiteEnabled($url){
 
    #fill metadata information to the client context variable
    $featureID = "f39dad74-ea79-46ef-9ef7-fe2370754f6f"
    $context = New-Object Microsoft.SharePoint.Client.ClientContext($url)
    $context.Credentials = $SPOcredentials
    $web = $context.Web
    $context.Load($web)
    $context.load($web.Features)

    try{
 
        $context.ExecuteQuery()
        $isCommSiteEnabled = $web.Features | Where {$_.DefinitionID -eq $featureID}
		$webTemplate = $web.WebTemplate

		if($webTemplate -ne "SITEPAGEPUBLISHING" -AND $isCommSiteEnabled){
		    write-host "Found $($web.url)" -foregroundcolor green
			return "Enabled"
			
		}
    } 
    catch{
 
        write-host "Could not find web" -foregroundcolor red
 
    }

    return "" 
}

Get-CommsiteEnabledSites
```

## See also

For info about automatically modernizing the home page on classic sites, see [Classic home page modernization](disable-auto-modernization-classic-home-pages.md).