---
title: "Overview of site policies in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 3ee1591b-6908-499f-9a39-e19bcfbec8a4
description: "Learn about SharePoint Server site closure and deletion policies and how they apply to SharePoint governance and self-service site creation."
---

# Overview of site policies in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
Even with good governance, SharePoint sites can multiply and quickly grow out of control. Sites are created as they are needed, but sites are rarely deleted. Sites that are no longer needed but aren't deleted, require storage space and they also might be unwanted for compliance reasons.
  
You can use site policies to help control site excess. A site policy defines the life-cycle of a site by specifying when the site will be closed and when it will be deleted. When you close or delete a site, any sub-sites are also closed or deleted. If an Exchange mailbox is associated with a site, the mailbox is deleted from Exchange Server when the site is deleted.
  
When you close a site, you specify that the site is no longer used so that the site can eventually be deleted according to a schedule. A closed site does not appear in other places where sites are aggregated — for example, Outlook, Outlook on the web (formerly known as Outlook Web App), or Project Server — but users can still modify a closed site and its content by using the URL to reach the site.
  
## SharePoint site policy options

A site policy specifies the conditions under which to close or delete a site automatically. These conditions have the following four options:
  
- **Do not close or delete the site automatically.** If a policy that has this option is applied to a site, the site owner must delete the site manually. 
    
- **Delete the site automatically.** If a policy that has this option is applied to a site, the site owner may close the site manually, but the site will be deleted automatically. A policy that deletes the site automatically specifies a rule for when to delete the site, and has the following options: 
    
  - What action triggers the site to be deleted, and how long to wait after the trigger occurs before deleting the site. The trigger can be either site creation or site closure. For example, you can create a policy that deletes a site three months after the site is closed, or a policy that deletes a site one year after the site is created.
    
  - Whether to have SharePoint Server send a notification email message to the site owner a specified amount of time before the site is scheduled to be deleted.
    
  - Whether to allow site owners to postpone deletion of the site.
    
- **Close the site automatically and delete the site automatically.** This option gives the same choices for how to delete the site automatically, and also requires you to specify how long after its creation time the site will be closed. 
    
    > [!NOTE]
    > A site owner can re-open a closed site by going to the Site Closure and Deletion page from the **Site Settings** menu. 
  
- **Run a workflow to close the site, and delete the site automatically.** This option gives the same choices for how to delete the site automatically, and also requires you to specify a workflow to run. When the workflow finishes running, SharePoint Server 2016 closes the site. You specify the name of the workflow, how long after the site is created to run the workflow, and whether to rerun the workflow periodically until the site is closed. 
    
A site policy can also specify that if it is applied to the root site in a site collection, when the root site is closed, the root site and all sub-sites become read-only.

Site policies are also available in SharePoint Server 2019 modern Team and Communication sites. You must first activate the **Site Polcy** feature before it appears on the **Site Settings** page. 
  
## Defining SharePoint site policies

You define site policies from the root site of a site collection by going to the **Site Policies** page from the **Site Collection Administration** menu. The policies are then available in every site in the site collection. Site owners can apply a policy to a site by going to the Site Closure and Deletion page from the **Site Settings** menu. Site owners can also close a site by using the Site Closure and Deletion page. 
  
> [!NOTE]
> To delete a site manually, a site owner must select **Delete this site** on the **Site Settings** menu. The Site Closure and Deletion page shows when a site will be deleted automatically. However, it does not provide an option for the site owner to delete the site manually. 
  
If the site collection in which you define site policies is a content type hub, then you can publish policies and share them across site collections.
  
## Using SharePoint site policies with self-service site creation

Site policies are especially valuable when you use them together with self-service site creation. When a farm administrator enables self-service site creation on a web application, the farm administrator can specify that users must classify each newly created site by selecting a policy to apply to the site. The farm administrator can specify that site classification is required, optional, or hidden from the user. By using site policies together with self-service site creation, you can let users create their own sites, but also make sure that the sites will be deleted after a certain time.
  
## See also

#### Other Resources

[Overview of document deletion policies in SharePoint Server](https://go.microsoft.com/fwlink/?linkid=845552)
  
[Overview of in-place hold in SharePoint Server](https://go.microsoft.com/fwlink/?linkid=845553)

