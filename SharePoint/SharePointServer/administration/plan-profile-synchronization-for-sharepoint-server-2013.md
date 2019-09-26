---
title: "Plan profile synchronization for SharePoint Server 2013"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 2/27/2018
audience: ITPro
ms.topic: interactive-tutorial
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: 8451dde9-bbd1-4285-bc24-71bd795fb912
description: "Learn how to implement profile synchronization in SharePoint Server."
---

# Plan profile synchronization for SharePoint Server 2013

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)]
  
Profile synchronization (also known as "profile sync") allows you to create user profiles by importing information from other systems that are used in your organization. Before you read this article you should understand the concepts introduced in the article [Overview of profile synchronization in SharePoint Server 2013](profile-synchronization-in-sharepoint-server-2013.md). Profile synchronization is also used in server-to-server authentication which enables servers to access and request resources from one another server on behalf of users. For more information, see [Server-to-server authentication and user profiles in SharePoint Server](../security-for-sharepoint-server/server-to-server-authentication-and-user-profiles.md).
  
This article describes:
  
- How to get the information that you must have to configure profile synchronization.
    
- Who you must work with to collect the necessary information.
    
- The external content types that will have to be created, if any.
    
This article does not describe how to implement your plan. That information is covered in the article [Synchronize user and group profiles in SharePoint Server 2013](configure-profile-synchronization.md).
  
## Before you begin
<a name="beforeyoubegin"> </a>

Before you work through the planning tasks in this article, you should already:
  
- Know which users that you want to have profiles in SharePoint Server 2013.
    
- Know what properties a user profile will have, and fill out the User Profile Properties Planning worksheet as explained in the article [Plan user profiles in SharePoint Server](plan-user-profiles.md).
    
- Understand general concepts about directory services.
    
## About planning for profile synchronization
<a name="about"> </a>

As the first step towards planning for profile synchronization, you'll identify synchronization connections, and collect information that you will need when you create the connection. If you will need any external content types, you'll document the requirements for those external content types, provide the requirements to a developer, and receive the details that you'll use to specify a synchronization connection to the business system.
  
Next, you'll determine how to map user profile properties to information in the external systems so that they can be synchronized.
  
Finally, you'll answer more straightforward questions such as whether you'll synchronize groups, which server that you'll use to run the synchronization service, and how often you'll synchronize profile information.
  
## Plan synchronization connections
<a name="connections"> </a>

Each property in a user's profile can come from an external system. There are two types of external systems: directory services and business systems. Throughout this article, the phrase business system is used to mean an external system that is not a directory service. SAP, Siebel, SQL Server, and custom applications are all examples of business systems. 
  
> [!NOTE]
> For a list of supported directory services, see [Profile synchronization overview](profile-synchronization-in-sharepoint-server-2013.md). 
  
In SharePoint Server 2013, a synchronization connection is a way to obtain user profile information from an external system. To import profiles from one of the supported directory services, you create a synchronization connection to the directory service. To import additional profile properties from a business system, you create an external content type to bring the data from the business system into SharePoint Server 2013, and then create a synchronization connection to the external content type. The following sections explain how to collect the information that you will need about each synchronization connection. 
  
### Connections to directory services

Each user who you want to have a profile in SharePoint Server 2013 must have an identity in a directory service. (If users are not represented in a directory service, you can't synchronize user profiles.) Identify which directory services contain information about these users. Unless you can access the directory service yourself, you should also identify an administrator of the directory service. You will need this person's help to collect some information that will be needed to create synchronization connections.
  
The [Connection planning worksheet](https://go.microsoft.com/fwlink/p/?LinkID=268733) contains templates for the information that you need to collect for each type of connection. Each template is in a separate tab that is labeled with the name of the directory service provider to which it applies. Create a tab for each directory service that you identified. Copy the template for the type of directory service into the new tab. Then complete the information on each new tab according to the following table. 
  
|**Row name in worksheet**|**Applies to connection type**|**Instructions**|
|:-----|:-----|:-----|
|Synchronization connection name  <br/> |All  <br/> |Choose a name that will help you remember which directory service this is a connection to.  <br/> |
|Connection type  <br/> |All  <br/> |The type of directory service that this is a connection to.  <br/> This information is already filled in on each tab.  <br/> |
|Forest  <br/> |AD DS  <br/> |The name of the directory service forest.  <br/> |
|Domain controller  <br/> |AD DS  <br/> |The name of the preferred domain controller. You only have to identify the domain controller if there are multiple domain controllers in the forest and you want to synchronize with a specific domain controller.  <br/> |
|Authentication provider type  <br/> |All  <br/> | The type of authentication SharePoint Server 2013 should use to connect to the directory service. This is one of the following:  <br/>  Windows authentication  <br/>  Forms-based authentication  <br/>  Claims-based authentication  <br/>  The systems architect should be able to provide this information.  <br/> |
|Authentication provider  <br/> |All  <br/> |If forms-based authentication or claims-based authentication will be used, fill in the name of the trusted provider. The systems architect should be able to provide this information. An authentication provider is not needed for Windows authentication.  <br/> |
|Synchronization account  <br/> |All  <br/> |The account, including the domain, that will be used to connect to the directory service. It is likely that the directory service administrator will create an account to be used for synchronization.  <br/> **Note**: The permissions that the synchronization account must have are described in the [Plan account permissions](plan-profile-synchronization-for-sharepoint-server-2013.md#permission) section of this topic.  <br/> |
|Synchronization account password  <br/> |All  <br/> |The password for the synchronization account.  <br/> **Note**: You must know the password for the synchronization account. We recommend that you do not record the password in the worksheet.  <br/> |
|Connection port  <br/> |All  <br/> |The port that will be used to connect to the directory service.  <br/> |
|Use SSL?  <br/> |AD DS  <br/> |Whether to use an SSL-secured connection to connect to the directory service. SSL is only supported for connections to AD DS.  <br/> |
|Directory service server  <br/> |Tivoli, Sun, eDirectory  <br/> |The name of the directory service server.  <br/> |
|Username attribute  <br/> |Tivoli, Sun, eDirectory  <br/> |The name of the attribute in the directory service that serves as the unique identifier for each profile. In most cases, the default user name attribute of "uid" is correct.  <br/> |
|Containers  <br/> |All  <br/> |The names of the directory service containers, also known as organizational units (OU), that contain the profiles to synchronize.  <br/> |
|Filter for users  <br/> |All  <br/> |See the detailed instructions in the section [About exclusion filters](plan-profile-synchronization-for-sharepoint-server-2013.md#filters).  <br/> |
|Filter for groups  <br/> |All  <br/> |See the section [Synchronizing groups](plan-profile-synchronization-for-sharepoint-server-2013.md#groups).  <br/> |
   
#### About exclusion filters
<a name="filters"> </a>

SharePoint Server 2013 will synchronize all of the profiles from the containers that you identify unless you choose to exclude profiles by using a filter. For example, you might create a filter to exclude users whose accounts are disabled.
  
A filter consists of a set of clauses and the connector to use to join the clauses. Each clause has three parts:
  
- Attribute: The directory service attribute to compare.
    
- Value: The value to compare the attribute to.
    
- Operator: The type of comparison. 
    
There are two ways to join the clauses of an exclusion filter:
  
- All apply (AND): An account matches the filter if all of the clauses apply.
    
- Any apply (OR): An account matches the filter if any clause applies.
    
You can't mix ANDs and ORs in a filter.
  
For example, assume that temporary employees in your organization are given Active Directory accounts that begin with "T-". You want to synchronize profiles for all permanent (non-temporary) users whose accounts are not disabled. You could create a filter that uses the clauses in the following table.
  
> [!NOTE]
> After any changes are made to a filter, a full synchronization is required. 
  
|**Attribute**|**Operator**|**Value**|
|:-----|:-----|:-----|
|sAMAccountName  <br/> |starts with  <br/> |T-  <br/> |
|userAccountControl  <br/> |bit on equals  <br/> |2  <br/> |
   
The filter would join the clauses by using Any apply (OR).
  
> [!NOTE]
> In AD DS, **userAccountControl** is a bitmask that represents several useful aspects about the status of the user account. For a list of some of the more frequently-used filters that you can create by using the **userAccountControl** attribute, see [How to use the UserAccountControl flags to manipulate user account properties](https://go.microsoft.com/fwlink/p/?LinkId=217163). 
  
You can't create a filter that is based on membership in a directory service group, such as a distribution list. For alternatives to importing users based on group membership, see [Inability to import users based on group membership](https://go.microsoft.com/fwlink/p/?LinkId=220892).
  
### Connections to business systems

To import properties from a business system, you will need an external content type that brings the property value from the external system into SharePoint Server 2013. This article does not cover how to create an external content type. That task is usually done by a developer. This article describes the data that you must collect and give to the developer, and tells you what to do with the information that you receive. For developer information, see [External content types in SharePoint 2013](https://go.microsoft.com/fwlink/p/?LinkId=269635).
  
You can use the [External content type planning worksheet](https://go.microsoft.com/fwlink/p/?LinkId=268734) to specify the external content types to be created. Go through the User Profile Properties Planning worksheet that you completed when you read the article [Plan user profiles in SharePoint Server](plan-user-profiles.md). In the External Content Type Planning worksheet, create one row for each user profile property that comes from a business system. Fill in the first three columns of each row according to the instructions in the following table.
  
|**Column in worksheet**|**Instructions**|
|:-----|:-----|
|Business system  <br/> |A name that you choose that identifies the business system that contains the property.  <br/> |
|Item  <br/> |The data in the business system that corresponds to the property. Be as specific as possible. For example, if the business system is a database, provide the name of the table and column, if known.  <br/> |
|Possible identifiers  <br/> |A list of the user profile properties that could uniquely identify a user.  <br/> |
   
After you have filled in the first three columns of each row, give the worksheet to the external content type developer. The developer should follow these steps, and then return the worksheet:
  
- Create external content types to provide the external system data that is described in the worksheet.
    
- Choose an appropriate identifier for each external content type.
    
- If user profiles will have a one-to-one relationship with items of the external content type, create a specific finder method. An external content type that contains a user's birthdate is an example of a one-to-one relationship. Each user profile will match one item of the external content type.
    
- If user profiles will have a one-to-many relationship with items of the external content type, create a finder method and a comparison filter. An external content type that contains the license plate of a vehicle the user owns is an example of a one-to-many relationship. A user might own multiple vehicles. Therefore, each user profile might match more than one item of the external content type.
    
- Update the worksheet to describe the external content types that were created.
    
The Connection Planning worksheet ([User profile properties and profile synchronization planning worksheet](https://go.microsoft.com/fwlink/p/?LinkId=267109)) contains a tab for a connection to a business system. When you receive the information back from the external content type developer, group all user profile properties that share the same external content type. Create a tab in the Connection Planning worksheet for each external content type, and copy the information from the **Business systems** tab to each new tab. On each tab that you created, complete the information according to the instructions in the following table. 
  
|**Row in worksheet**|**Instructions**|
|:-----|:-----|
|Synchronization connection name  <br/> |Choose a name that will help you remember which business system this is a connection to.  <br/> |
|Connection type  <br/> |"Business data connectivity"  <br/> This information is already filled in.  <br/> |
|Business data connectivity entity  <br/> |The name of the external content type.  <br/> |
|One-to-one or one-to-many mapping  <br/> |The number of items of the external content type that might match a given user profile. Enter "one-to-one" or "one-to-many" as appropriate.  <br/> |
|Profile property to match against  <br/> |The name of the user profile property that corresponds to the external content type's identifier.  <br/> |
|Comparison filter  <br/> |The name of the comparison filter.  <br/> A filter is only required for one-to-many mappings.  <br/> |
   
## Identify property mappings
<a name="mappings"> </a>

To indicate that a user profile property comes from an external system, you map the property to a specific attribute of the external system. By default, certain user profile properties are mapped. You can only map a profile property to an attribute whose data type is compatible with the data type of the property. For example, you can't map the **SPS-HireDate** user profile property to the **homePhone** Active Directory attribute because **SPS-HireDate** is a date and **homePhone** is a Unicode string. For a list of which user profile property data types are compatible with which AD DS data types, see [User profile property data types in SharePoint Server 2013](/previous-versions/office/sharepoint-server-2010/hh227257(v=office.14)).
  
When you synchronize profile information, in addition to importing profile properties from external systems, you can also write data back to a directory service. You can't write data back to a business system. To indicate that SharePoint Server 2013 should export a user profile property, you map the property, and set the direction of the mapping to **Export**. Each property can only be mapped in one direction. You can't both import and export the same user profile property. The data that is exported overwrites any values that might already be present in the directory service. This is true for multivalued properties also—the exported value is not appended to the existing values, it overwrites them.
  
Examine the User Profile Properties Planning worksheet that you completed as you read the [Plan user profiles in SharePoint Server](plan-user-profiles.md) topic. For each row (property) whose value will be imported from an external system, fill in the final three columns according to the instructions in the following table. 
  
|**Row in worksheet**|**Instructions**|
|:-----|:-----|
|Direction  <br/> |"Import", indicating that the property will be imported into SharePoint Server 2013.  <br/> |
|Synchronization connection  <br/> |The name of the synchronization connection through which this property will be provided.  <br/> |
|Attribute  <br/> |The name of the external system element that will provide the value of the user profile property.  <br/> If the synchronization connection is to a directory service, this is the name of the directory service attribute.  <br/> If the synchronization connection is to a business system, this is the name of the column in the external content type.  <br/> |
   
> [!NOTE]
> You can't use a connection to a business system to map a binary property to a property that implements the **Stream** accessor method. 
  
For each row (property) whose value will be exported to a directory service, fill in the final three columns according to the instructions in the following table.
  
|**Row in worksheet**|**Instructions**|
|:-----|:-----|
|Direction  <br/> |"Export", indicating that the property will be exported from SharePoint Server 2013 to a directory service.  <br/> |
|Synchronization connection  <br/> |The name of the synchronization connection through which this property will be exported. This can only be a connection to a directory service.  <br/> |
|Attribute  <br/> |The name of the directory service attribute whose value should be updated with the value of the user profile property.  <br/> |
   
## Synchronizing groups
<a name="groups"> </a>

By default, SharePoint Server 2013 synchronizes groups, such as distribution lists, when it synchronizes user profiles. You can turn off this functionality from the Configure Synchronization Settings page of Central Administration. Synchronizing groups is only supported for AD DS.
  
If you synchronize groups in addition to users, SharePoint Server 2013 imports information about the groups and about which users are members of the groups. Synchronizing a group does not create a profile for the group, and causes no additional user profiles to be created. In SharePoint Server 2013, groups are only used to create audiences and to display which memberships a visitor has in common with the person whose My Site the person is visiting.
  
If you decide to synchronize groups, SharePoint Server 2013 will import information about all of the groups that exist in the directory service containers that you are synchronizing unless you choose to exclude groups by using a filter. The filter for excluding groups differs from the filter for excluding users, although both follow the same format.
  
Return to the Connection Planning worksheet and fill in the Filter for groups cell.
  
## Plan for the synchronization server
<a name="server"> </a>

In addition to determining the synchronization connections and identifying the property mappings, you also have to plan for the more straightforward aspects of synchronizing profiles. The first of these is identifying the synchronization server.
  
You can only run one instance of the User Profile Synchronization service on a farm. The computer on which the User Profile Synchronization service runs is called the synchronization server. You specify the synchronization server when you create the User Profile service application. SharePoint Server 2013 provisions a version of Microsoft Forefront Identity Manager (FIM) on this computer to participate in synchronization.
  
When SharePoint Server 2013 synchronizes profiles, it makes heavy use of the network to communicate between the synchronization server and the domain controllers. Choosing a synchronization server that is physically close to the domain controllers will reduce the time that is required to synchronize.
  
## Plan the synchronization schedule
<a name="schedule"> </a>

The first time that you synchronize profile information between SharePoint Server 2013 and external systems, you must run a full synchronization. After that, you should configure the User Profile Incremental Synchronization timer job to perform an incremental synchronization on a recurring schedule. You can configure the timer job to run every few minutes, hourly, daily, weekly, or monthly. By using the hourly, daily, weekly, and monthly options, you specify when you want the timer job to start.
  
The more often the synchronization timer job runs, the fewer changes there will be to synchronize, and the quicker the job will finish. The default frequency is daily. We recommend that you schedule synchronization to start at a time when the network is lightly used.
  
For instructions about how to configure the User Profile Incremental Synchronization timer job, see [Schedule profile synchronization in SharePoint Server](schedule-profile-synchronization.md).
  
## Plan account permissions
<a name="permission"> </a>

In the Connection Planning worksheet, you provided the name of a synchronization account for each directory service. These synchronization accounts must be granted specific permissions so that the synchronization service can obtain the information that it needs from the directory service. The following sections identify which permissions are needed for each type of directory service. Work with the administrator of the directory service to grant the accounts the appropriate permissions.
  
### Active Directory Domain Services (AD DS)

The synchronization account for a connection to Active Directory Domain Services (AD DS) must have the following permissions:
  
- It must have Replicate Directory Changes permission on the domain with which you'll synchronize.
    
    The Replicate Directory Changes permission allows an account to query for the changes in the directory. This permission does not allow an account to make any changes in the directory.
    
- If the domain controller is running Windows Server 2003, the synchronization account must be a member of the Pre-Windows 2000 Compatible Access built-in group. 
    
- If the NetBIOS name of the domain differs from the fully-qualified domain name, the synchronization account must have Replicate Directory Changes permission on the cn=configuration container. For example, if the NetBIOS domain name is contoso and the fully-qualified domain name is contoso-corp.com, you must grant Replicate Directory Changes permission on the cn=configuration container. 
    
- If you'll export property values from SharePoint Server 2013 to AD DS, the synchronization account must have Create Child Objects (this object and all descendants) and Write All Properties (this object and all descendants) permissions on the organizational unit (OU) with which you are synchronizing. 
    
### Novell eDirectory version 8.7.3

The synchronization account for a connection to Novell eDirectory must have the following permissions:
  
- Entry Rights: Browse rights for the specified tree.
    
- All Attributes Rights: Read, Write, and Compare rights for the specified tree.
    
### Sun Java System Directory Server version 5.2

The synchronization account for a connection to a Sun Java System Directory Server must have the following permissions:
  
- Read, Write, Compare, and Search permissions to the RootDSE.
    
- To perform incremental synchronization, the synchronization account must also have Read, Compare, and Search permissions to the change log (cn=changelog). If the change log does not exist, you must create it before synchronizing.
    
### IBM Tivoli version 5.2

The synchronization account for a connection to IBM Tivoli must have the following permission:
  
- The synchronization account must be a member of an administrative group.
    
### The farm account

The User Profile Synchronization service runs under the farm account. The farm account requires specific permissions to configure profile synchronization. A person with administrator rights on the synchronization server can grant these permissions.
  
- The account must be a member of the Administrators group on the synchronization server. You can remove this permission after you have configured the User Profile Synchronization service.
    
- The account must be able to log on locally to the synchronization server.
    
    > [!NOTE]
    > The farm account differs from the farm administrator account. To determine the farm account, from Central Administration, click **Configure service accounts**, and then click **Farm account**. 
  
If you'll synchronize user profiles with a business system by using an external content type, the farm account must also have permission to execute operations on the external content type. A farm administrator can use the procedure "[Set permissions on an external content type](/previous-versions/office/sharepoint-server-2010/ee524076(v=office.14)#setpermissions)" to give the farm account Execute permission on each external content type with which you'll synchronize.
  
## Next steps
<a name="next"> </a>

To implement your profile synchronization plan, follow the instructions in the article [Synchronize user and group profiles in SharePoint Server 2013](configure-profile-synchronization.md). After you have configured profile synchronization and synchronized profile information for the first time, implement the synchronization schedule by following the procedure that is described in the article [Schedule profile synchronization in SharePoint Server](schedule-profile-synchronization.md).
  
## Worksheets
<a name="worksheets"> </a>

To download the connection planning worksheet, the external content type planning worksheet, and the user profile planning worksheets, go to [User profile properties and profile synchronization planning worksheets for SharePoint Server 2013](https://go.microsoft.com/fwlink/p/?LinkID=268729).
  
## See also
<a name="worksheets"> </a>

#### Concepts
 
[Overview of profile synchronization in SharePoint Server 2013](profile-synchronization-in-sharepoint-server-2013.md)
  
[Plan user profiles in SharePoint Server](plan-user-profiles.md)
  
[Synchronize user and group profiles in SharePoint Server 2013](configure-profile-synchronization.md)
  
[Administer the User Profile service in SharePoint Server](user-profile-service-administration.md)
  
[User Profile service overview](../install/user-profile-service-overview.md)

