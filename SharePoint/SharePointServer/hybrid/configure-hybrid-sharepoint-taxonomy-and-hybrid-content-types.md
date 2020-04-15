---
title: "Configure hybrid SharePoint taxonomy and hybrid content types"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 01/23/2018
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Priority
ms.collection:
- Ent_O365_Hybrid
- IT_Sharepoint_Server
- IT_SharePoint_Hybrid_Top
- Strat_SP_gtc
- M365-collaboration
- SPO_Content
ms.custom: 
ms.assetid: 0809325c-9b99-46bf-b98d-6d2f5e3d2a4b
description: "In this article, we look at how to configure hybrid SharePoint taxonomy and hybrid content types."
---

# Configure hybrid SharePoint taxonomy and hybrid content types

[!INCLUDE[appliesto-2013-2016-2019-SPO-md](../includes/appliesto-2013-2016-2019-SPO-md.md)]

In this article, we look at how to configure hybrid SharePoint taxonomy and hybrid content types.
  
Hybrid SharePoint taxonomy allows you to have a shared taxonomy between SharePoint Server and SharePoint Online. Hybrid content types allows you to have a shared set of content types between SharePoint Server and SharePoint Online.
  
Be sure to read [Plan hybrid SharePoint taxonomy and hybrid content types](plan-hybrid-sharepoint-taxonomy-and-hybrid-content-types.md) before you follow the procedures in this article. 
  
This feature is available in SharePoint Server 2013 and SharePoint Server 2016 with the following [SharePoint updates](/officeupdates/sharepoint-updates):
  
- Hybrid taxonomy requires the November 2016 public update or later.
    
- Hybrid content types requires the June 2017 public update or later.
    
The functionality and configuration procedures are the same for both versions of SharePoint Server.
  
## Video demonstration

This video shows a walkthrough of configuring hybrid taxonomy and hybrid content types.
  
**Video: Configure hybrid taxonomy and content types**

> [!VIDEO https://www.microsoft.com/videoplayer/embed/de549889-8831-4c29-a3f4-ffe8104dc0a5?autoplay=false]
## Migrate your taxonomy from SharePoint Server

If you have an existing taxonomy in SharePoint Server, the best practice is to copy any term groups you want to be part of the shared taxonomy to SharePoint Online before you configure hybrid SharePoint taxonomy. You can migrate additional taxonomy groups from SharePoint Server to SharePoint Online to add to the shared taxonomy later, but if you do you may need to run the configuration wizard again to include them in the shared taxonomy.
  
The migration process copies taxonomy groups from SharePoint Server to SharePoint Online. This is done by using the [Copy-SPTaxonomyGroups](/powershell/module/sharepoint-server/Copy-SPTaxonomyGroups?view=sharepoint-ps) PowerShell cmdlet. 
  
 **Active Directory groups**
  
While the copy process preserves most user information associated with term sets - such as owner and stakeholders - note, that the copy process does not work with Active Directory groups. If you use Active Directory groups in your term sets, there are two options for copying your taxonomy groups:
  
- You can replace the Active Directory groups with individual users within your taxonomy groups. The individual users will be copied when you copy your taxonomy groups.
    
- You can copy your taxonomy groups with the Active Directory groups in place. You will see a PowerShell warning and the Active Directory group assignments will be lost if you proceed. You can then assign an Microsoft 365 group in place of the Active Directory group after you've copied the taxonomy groups.
    
 **Copying taxonomy groups**
  
Copying taxonomy groups is done using the Copy-SPTaxonomyGroups PowerShell cmdlet. You need the following information to run the cmdlet:
  
- The name of your managed metadata service application in SharePoint Server.
    
- The URL of the SharePoint Server site where your taxonomy store is located.
    
- The URL of the SharePoint Online site where your term store is located (http://\<TenantName\>.sharepoint.com).

- Taxonomy groups in SharePoint Server to be copied to SharePoint Online.
    
- Your Microsoft 365 global administrator credentials.

>[!NOTE] 
> If you receive an HTTP 400 error when attempting to use the `Copy-SPTaxonomyGroups` cmdlet with correct credentials, switch to a cloud-based global administrator instead of an Active Directory synchronized account.
    
- A list of the taxonomy groups that you want to copy.
    
Run the cmdlet as a farm administrator from one of the servers in your SharePoint farm.
  
Use the following syntax to copy your taxonomy groups:
  
```
$credential = Get-Credential
```

```
Copy-SPTaxonomyGroups -LocalTermStoreName "<ManagedMetadataServiceApplication>" -LocalSiteUrl "<OnPremisesSiteURL>" -RemoteSiteUrl "SharePointOnlineSiteURL" -GroupNames "Group1","Group2" -Credential $credential
```

For example:
  
```
$credential = Get-Credential
```

```
Copy-SPTaxonomyGroups -LocalTermStoreName "Managed Metadata Service" -LocalSiteUrl "https://sharepoint" -RemoteSiteUrl "https://contoso.sharepoint.com" -GroupNames "Engineering","Marketing" -Credential $credential
```

Note that you can also simply run Copy-SPTaxonomyGroups and you will be prompted for the needed parameters.
  
 **Copying content types**
  
If you're planning to use hybrid content types, you can copy your SharePoint Server content types to SharePoint Online by using the [Copy-SPContentTypes](/powershell/module/sharepoint-server/copy-spcontenttypes?view=sharepoint-ps) cmdlet. For example: 
  
```
Copy-SPContentTypes -LocalSiteUrl http://localsite/ -LocalTermStoreName "managed metadata service application proxy" -RemoteSiteUrl https://contoso.sharepoint.com/ -ContentTypeNames @("ContentTypeA", "ContentTypeB") -Credential $credential
```

The content types will be copied into https://contoso.sharepoint.com/sites/contentTypeHub. If this site does not exist, it will be created for you and the Site Collection Feature Content Type Syndication Hub will be enabled. The site URL is hard coded and cannot be changed.

## Configure hybrid SharePoint taxonomy

Configuration of hybrid SharePoint taxonomy is done using the Hybrid Picker in the SharePoint Online admin center. The Hybrid Picker has a number of prerequisites. Be sure to read [Hybrid picker in the SharePoint Online admin center](hybrid-picker-in-the-sharepoint-online-admin-center.md) before you follow the procedures in this section. 
  
We also recommend that you back up your term store before you proceed.
  
 **Make the timer service account a term store admin**
  
For taxonomy replication to work properly, the account that runs the SharePoint Timer Service must be a term store administrator in SharePoint Server. (To find this account, check the Log On As account for the SharePoint Timer Service on your server.) Use the following procedure to add this account as a term store administrator.
  
 **To add a term store admin**
  
1. In the **Central Administration** website, under **Application Management**, select **Manage service applications**.
    
2. Select the link for the Managed Metadata service application.
    
3. Add the timer service account to the **Term Store Administrators** box, and then select **Save**.
    
 **Configure hybrid SharePoint taxonomy using the Hybrid Picker**
  
The next step is to configure hybrid SharePoint taxonomy by running the Hybrid Picker in the SharePoint Online admin center.
  
 **To configure hybrid SharePoint taxonomy**
  
1. Log on to a server in your SharePoint Server farm as the farm administrator. 
    
2. From your SharePoint Server computer, open a web browser, and log on to Microsoft 365 as a global administrator.
    
3. In the SharePoint Online Admin Center, select **configure hybrid**.
    
4. On the hybrid picker page, select **Hybrid Picker**.
    
5. Follow the wizard, and when prompted, select **Hybrid Taxonomy**. 
    
6. Provide the following information when prompted:
    
  - The URL of your SharePoint Server root site (for example, https://sharepoint).
    
  - The name of your SharePoint Server managed metadata service application (for example, Managed Metadata Service).
    
  - The names of the taxonomy groups that you want to replicate (for example, Engineering;Marketing).
    
    If you don't specify groups, then all groups except system and special groups are configured for replication.
    
After you've configured hybrid SharePoint taxonomy, the taxonomy replication timer job will poll SharePoint Online on a daily basis for changes to the taxonomy.
  
## Running the taxonomy replication timer job

Hybrid SharePoint taxonomy uses a timer job called Taxonomy Groups Replication to copy taxonomy information from SharePoint Online to SharePoint Server. The SharePoint Online APP Identity is used to authenticate to Microsoft 365. By default, this timer job replicates taxonomy on a daily basis.
  
Like other timer jobs in SharePoint, you can configure the Taxonomy Groups Replication job to run on a different schedule, or you can run it manually, by searcing for it in the timer job list in Central Administration.
  
## Stopping replication of taxonomy groups

If at any time you want to stop taxonomy replication between SharePoint Online and SharePoint Server, you can do so by using PowerShell. 
  
The [Stop-SPTaxonomyReplication](/powershell/module/sharepoint-server/Stop-SPTaxonomyReplication?view=sharepoint-ps) cmdlet will stop taxonomy replication. For example: 
  
```
$credential = Get-Credential
```

```
Stop-SPTaxonomyReplication -Credential $credential
```

The [Stop-SPContentTypeReplication](/powershell/module/sharepoint-server/?view=sharepoint-ps) cmdlet will stop content type replication: 
  
```
Stop-SPContentTypeReplication
```

If you wish to reenable taxonomy replication again, you must run the Hybrid Picker again.
  
If you simply want to reconfigure which taxonomy groups you are replicating, there's no need to stop replication. You can just run the hybrid picker again and specify the new taxonomy groups that you want to replicate.
  
## See also

#### Other Resources

[TechNet Forums - Hybrid Taxonomy](https://social.technet.microsoft.com/Forums/office/home?forum=hybridtaxonomy)

