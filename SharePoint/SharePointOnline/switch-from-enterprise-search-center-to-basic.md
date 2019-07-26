---
title: "Switch from an Enterprise Search Center to Basic in SharePoint Online"
ms.reviewer: 
ms.author: efrene
author: efrene
manager: pamgreen
ms.date: 7/25/2019
audience: Admin
ms.topic: article
ms.service: sharepoint-online
localization_priority: Normal
description: "Learn how to change your default search center from Enterprise back to Basic."
---

# Switch from an Enterprise Search Center to Basic in SharePoint Online

The Basic Search Center is a classic search experience. To offer your users a richer search experience, you can either switch from a Basic Search Center to an Enterprise Search Center or rely on the modern search experience that SharePoint Online comes with. [Learn about differences between classic and modern search](https://docs.microsoft.com/sharepoint/differences-classic-modern-search) and [when to choose which search experience](https://docs.microsoft.com/sharepoint/get-started-with-modern-search-experience) for your organization.

If you are currently using the Enterprise Search Center, you can easily switch to the Basic Search Center if needed.  This will result in your users seeing the classic search experience in their default search home page and default search results page.  You can use the [Invoke-SPOSiteSwap](https://docs.microsoft.com/en-us/powershell/module/sharepoint-online/invoke-spositeswap?view=sharepoint-ps) Windows PowerShell cmdlet in the SharePoint Online Management Console to do this. 

## How to use Invoke-SPOSiteSwap to switch your Search Center sites

>[!Note]
> You need to use version 16.0.8812.1200 or newer of the [Microsoft SharePoint Online Services Module for Windows PowerShell](https://www.microsoft.com/download/details.aspx?id=35588).

In your Microsoft SharePoint Online Services Module for Windows PowerShell, [connect to SharePoint Online](https://docs.microsoft.com/powershell/sharepoint/sharepoint-online/connect-sharepoint-online?view=sharepoint-ps) and then use the Invoke-SPOSiteSwap cmdlet with the following parameters:

```PowerShell  
Invoke-SPOSiteSwap  
  --SourceUrl
  --TargetUrl  
  --ArchiveUrl  
```

| Paramater   | Description                                   |
|-------------|-----------------------------------------------|
| -SourceUrl  | The site you want to promote.                 |
| -TargetUrl  | The site you want to replace.                 |
| -ArchiveUrl | URL that the target site will be archived to. |

  
Here's an example of how to use these parameters when switching from an existing Enterprise Search Center to Basic:

- **For your -SourceUrl**, you need the URL of your Basic Search Center site. The site must exist before running the cmdlet. For our example, we'll use <spam><spam>https://contoso.sharepoint.com/sites/SiteSearch<spam><spam>.

    You can [created a Basic Search Center site](https://support.office.com/en-ie/article/using-templates-to-create-different-kinds-of-sharepoint-sites-449eccec-ff99-4cf3-b62e-dcfee37e8da4) from an Enterprise site template.
- **For your -TargetUrl**, you need the URL of your Enterprise Search Center site that you want to replace. For our example, we'll use <spam><spam>https://contoso.sharepoint.com/search<spam><spam>.
- **For your -ArchiveUrl**, use a Url that does not currently exist at the location. Your Enterprise Search Center site will be archived to this site location. For our example, we'll use <spam><spam>https://contoso.sharepoint.com/sites/ArchivedEntSearch<spam><spam>. 

Here's how to use the examples above in the Invoke-SPOSiteSwap cmdlet:

```PowerShell  
Invoke-SPOSiteSwap -SourceUrl https://contoso.sharepoint.com/sites/SearchSite -TargetUrl https://contoso.sharepoint.com/search -ArchiveUrl https://contoso.sharepoint.com/sites/ArchivedEntSearch
```

Successfully running the cmdlet above would result in:
- Basic Search will be the default Search Center experience. When users go to <spam><spam>https://contoso.sharepoint.com/search<spam><spam>, they will now be using the Basic Search Center.
- The Enterprise Search Center site will no longer be available as the default Search Center experience.

>[!Tips]
> You can use the **-NoWait** parameter <Michael, can you mention again what the benefits are?>  


    
## See also
<a name="__toc347912381"> </a>

[Manage the Search Center in SharePoint Online](manage-search-center.md)
  


