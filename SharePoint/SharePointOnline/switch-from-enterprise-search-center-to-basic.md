---
title: "Switch from an Enterprise Search Center to Basic in SharePoint"
ms.reviewer: 
ms.author: serdars
author: SerdarSoysal
manager: serdars
recommendations: true
ms.date: 7/25/2019
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
ms.localizationpriority: medium
search.appverid:
- MET150
description: "Learn how to swap your default search center from Enterprise back to Basic."
---

# Switch from an Enterprise Search Center to Basic in SharePoint

>[!Important]
>This feature is gradually rolling out and might not be available yet for your organization.


The Basic Search Center is a classic search experience. To offer your users a richer search experience, you can either switch from a Basic Search Center to an Enterprise Search Center or rely on the modern search experience that SharePoint comes with. [Learn about differences between classic and modern search](./differences-classic-modern-search.md) and [when to choose which search experience](./get-started-with-modern-search-experience.md) for your organization.

If you are currently using the Enterprise Search Center, you can easily replace (swap) it with the Basic Search Center if needed.  This will result in your users seeing the classic search experience in their default search home page and default search results page.  You can use the [Invoke-SPOSiteSwap](/powershell/module/sharepoint-online/invoke-spositeswap) PowerShell cmdlet to do this.

## How to use Invoke-SPOSiteSwap to swap your Search Center sites

1. [Download the latest SharePoint Online Management Shell](https://go.microsoft.com/fwlink/p/?LinkId=255251).

    > [!NOTE]
    > If you installed a previous version of the SharePoint Online Management Shell, go to Add or remove programs and uninstall "SharePoint Online Management Shell." 

2. Connect to SharePoint as a [global admin or SharePoint admin](./sharepoint-admin-role.md) in Microsoft 365. To learn how, see [Getting started with SharePoint Online Management Shell](/powershell/sharepoint/sharepoint-online/connect-sharepoint-online).

3. Run the [Invoke-SPOSiteSwap](/powershell/module/sharepoint-online/invoke-spositeswap) cmdlet.

```PowerShell  
Invoke-SPOSiteSwap  
  -SourceUrl <string>
  -TargetUrl <string>
  -ArchiveUrl <string>
```

| Parameter   | Description                                   |
|-------------|-----------------------------------------------|
| -SourceUrl  | The site you want to promote.                 |
| -TargetUrl  | The site you want to replace.                 |
| -ArchiveUrl | URL that the target site will be archived to. |

  
Here's an example of how to use these parameters when swapping an existing Enterprise Search Center to Basic:

- **For your -SourceUrl**, you need the URL of your Basic Search Center site. The site must exist before running the cmdlet. For our example, we'll use \<spam\>\<spam\>https://contoso.sharepoint.com/sites/SiteSearch\<spam\>\<spam\>.

    You can [create a Basic Search Center site](https://support.office.com/article/449eccec-ff99-4cf3-b62e-dcfee37e8da4) from an Enterprise site template.
- **For your -TargetUrl**, you need the URL of your Enterprise Search Center site that you want to replace. For our example, we'll use \<spam\>\<spam\>https://contoso.sharepoint.com/search\<spam\>\<spam\>.
- **For your -ArchiveUrl**, use a Url that does not currently exist at the location. Your Enterprise Search Center site will be archived to this site location. For our example, we'll use \<spam\>\<spam\>https://contoso.sharepoint.com/sites/ArchivedEntSearch\<spam\>\<spam\>. 

Here's how to use the examples above in the Invoke-SPOSiteSwap cmdlet:

```PowerShell  
Invoke-SPOSiteSwap -SourceUrl https://contoso.sharepoint.com/sites/SearchSite -TargetUrl https://contoso.sharepoint.com/search -ArchiveUrl https://contoso.sharepoint.com/sites/ArchivedEntSearch
```

Successfully running the cmdlet above would result in:
- Basic Search will be the default Search Center experience. When users go to \<spam\>\<spam\>https://contoso.sharepoint.com/search\<spam\>\<spam\>, they will now be using the Basic Search Center.
- The Enterprise Search Center site will no longer be available as the default Search Center experience.


    
## See also
<a name="__toc347912381"> </a>

[Manage the Search Center in SharePoint](manage-search-center.md)