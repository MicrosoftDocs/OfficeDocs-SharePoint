---
title: "Plan for managed metadata in SharePoint Server"
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/6/2017
audience: ITPro
ms.topic: concetpual
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: e580fcae-b768-4b81-afda-c037fbd7bd6d
description: "Learn about the decisions you need to make when planning for the managed metadata service in SharePoint Server."
---

# Plan for managed metadata in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
With managed metadata in SharePoint Server, you can create a unified taxonomy of terms that you can use throughout your SharePoint farm. In this article, we walk through the configuration decisions that you need to make before you configure the managed metadata service application in SharePoint Server.
  
Before you configure managed metadata, it's important to understand what managed metadata is and how it works in SharePoint. Before you read this article, be sure to read [Introduction to managed metadata](https://go.microsoft.com/fwlink/p/?LinkId=626754).
  
## Overview of the managed metadata service in SharePoint Server

In SharePoint Server, managed metadata is implemented through a service application and the Managed Metadata Web Service which runs on the Application and Front-end server roles. You can create multiple managed metadata service applications if you need separate term sets for specialized use. Each service application has its own database containing the term set, terms, keywords, and so on.
  
Connections between the managed metadata service application and your web applications are handled by managed metadata connections. Using these connections, you can map different managed metadata service applications to different web applications if needed, and configure features around keyword and term set creation policy.
  
If you have multiple SharePoint Server farms and you want to share a managed metadata term store between them, you can publish the service application in one farm and the others can connect to it. (This requires a trust relationship between the farms.)
  
The managed metadata service application also provides publishing functionality for content type hubs, which are site collections where you can create standard content types and share them among other site collections.
  
Let's look at the decisions you need to make in these areas before you configure managed metadata.
  
## Isolating managed metadata term sets
<a name="section1"> </a>

Within a term store, you can create a variety of different term sets. These term sets can be organized in groups. Groups offer some security isolation by allowing you to specify who can manage or contribute to them. However, users in general can access and use the terms themselves. If you want to restrict a term set to a specific group of users, there are two options.
  
First, you can allow users to create term sets that are local to a site collection. These term sets are not available in other site collections. (We talk more about this option in the next section.)
  
Second, you can provide even greater isolation for a term set by housing it in a separate managed metadata service application. This gives you a completely separate term store in a separate database which you can restrict to a particular set of users.
  
If you have sensitive areas such as legal or human resources where you want a term store with limited access, consider this second approach. Users of this term store can also be granted access to your main term store.
  
 **Decision**
  
Before you configure managed metadata in SharePoint, decide if you need more than one managed metadata service application for separate term stores. (You can add additional service applications in the future if needed.)
  
## Using local term sets
<a name="LocalTermSets"> </a>

Beyond the global term sets that are available across all of your site collections, you can create term sets that are local to a site collection. When users create a managed metadata column for a SharePoint list, they have the option of creating a new term set rather than using global term sets.
  
This can be useful if you want to use managed metadata in ways that don't apply to the entire organization, such as metadata for a particular project or event.
  
By using local term sets, different teams and business groups can create their own managed metadata without needing to request formal updates to a global term set, and you can keep the global term sets focused on core areas of your business.
  
If you don't want to allow users to create their own term sets that are local to site collections, you can disable this feature when you configure the managed metadata connection.
  
 **Decision**
  
Before you configure managed metadata in SharePoint, decide if you want to allow local term sets to be created. (You can have different setting for each service application that you create.)
  
## Managed metadata keywords and folksonomy
<a name="Keywords"> </a>

When you use a managed metadata column in a SharePoint list, users who fill out that column have to use one of the available values defined in the term store that the column is connected to. This is one of the primary advantages of managed metadata - you're certain the value was chosen from a predefined list.
  
However, SharePoint managed metadata also supports tagging functionality where users can tag SharePoint items such as documents with keywords that they create that aren't in the existing term store. These keywords accumulate in a list in the term store, and you can manage them by consolidating them and adding them to existing or new term sets as needed. This allows a folksonomy approach where users can create new keywords as needed without having to go through a formal process to update a particular term set.
  
If you want to take a more formal approach to managed metadata, you can disable this feature when you configure the managed metadata connection. In this case, users will have to pick from the existing terms in the term store and add those values to specific fields that you create for that purpose.
  
 **Decision**
  
Before you configure managed metadata in SharePoint, decide if you want to allow tagging of SharePoint items with keywords that are not in the term store.
  
## Publishing managed metadata content types
<a name="ContentTypes"> </a>

In addition to sharing managed metadata, you can also use the managed metadata service to share [content types](https://go.microsoft.com/fwlink/p/?LinkId=626926). By specifying a site collection as the [content type hub](https://go.microsoft.com/fwlink/p/?LinkId=626927) when you configure the managed metadata service application, you can share all content types in the site collection's content type gallery, making them available to other site collections. 
  
 **Decision**
  
Before you configure managed metadata in SharePoint, decide if you want to create a content type hub. (You can also add one later.)
  
## See also
<a name="SeeAlso"> </a>
For the SharePoint Online version of this article, see [Introduction to managed metadata](https://docs.microsoft.com/sharepoint/managed-metadata).

