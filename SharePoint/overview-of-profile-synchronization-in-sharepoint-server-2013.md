---
title: Overview of profile synchronization in SharePoint Server 2013
ms.prod: SHAREPOINT
ms.assetid: c20ca79f-2086-4a32-974a-ed2a720d57fe
---


# Overview of profile synchronization in SharePoint Server 2013
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013*  * **Topic Last Modified:** 2017-08-01* **Summary:** Learn about profile synchronization, also known as "profile sync," in SharePoint Server 2013.A user profile is a collection of properties that describes a SharePoint user. Features such as My Sites and People Search use user profiles to provide a rich, personalized experience for the users in your organization. You can create user profiles by importing data from directory services, such as Active Directory Domain Services (AD DS). You can augment user profiles by importing data from business systems, such as SAP or SQL Server. The process of importing profile data from external systems and writing data back to these systems is called  *profile synchronization*  .When you synchronize user profiles, you can also synchronize groups. Synchronizing groups gives SharePoint Server 2013 information about which users are members of which group.User profiles and groups are used by SharePoint Server 2013 through server-to-server authentication to access and request resources from one another on behalf of users. For more information about server-to-server authentication, see  [Server-to-server authentication and user profiles in SharePoint Server](html/server-to-server-authentication-and-user-profiles-in-sharepoint-server.md).This article provides required information about profile synchronization in SharePoint Server 2013.
> [!IMPORTANT:]

  
    
    

In this article:
-  [Synchronization components](overview-of-profile-synchronization-in-sharepoint-server-2016.md#components)
    
  
-  [Importing profiles from a directory service](overview-of-profile-synchronization-in-sharepoint-server-2016.md#importDS)
    
  
-  [Importing properties from a business system](overview-of-profile-synchronization-in-sharepoint-server-2016.md#importBusiness)
    
  
-  [Exporting properties to a directory service](overview-of-profile-synchronization-in-sharepoint-server-2016.md#export)
    
  
-  [Creating user profiles without synchronizing](overview-of-profile-synchronization-in-sharepoint-server-2016.md#noSync)
    
  
-  [Synchronizing groups](overview-of-profile-synchronization-in-sharepoint-server-2016.md#groups)
    
  
-  [Types of synchronization](overview-of-profile-synchronization-in-sharepoint-server-2016.md#types)
    
  
-  [Supported directory services](overview-of-profile-synchronization-in-sharepoint-server-2016.md#supported)
    
  

## Synchronization components
<a name="components"> </a>

Your solution must have a User Profile service application to use any of the social computing features in SharePoint Server 2013. When you create the User Profile service application, you can specify the  *synchronization server*  (also known as the *profile synchronization instance*  ), which is the computer that will be used to synchronize profile information. Creating the User Profile service application creates several databases, such as the profile database.
> [!NOTE:]

  
    
    

The User Profile Synchronization service is the core of the synchronization architecture in SharePoint Server 2013. When you start the User Profile Synchronization service on the synchronization server, SharePoint Server 2013 provisions a version of Microsoft Forefront Identity Manager (FIM) to participate in synchronization. A User Profile service application can only have one User Profile Synchronization service. A User Profile Synchronization service is associated with  *connections*  and *mappings*  .A connection is a way to access profile data in an external system. A User Profile Synchronization service can have multiple connections, and each external system requires its own connection. Connections can be divided into two types: connections to directory services, and connections to business systems.When you create a connection to a directory service, you specify which containers in the directory service contain the information that you want to synchronize. You can also create a  *filter*  to exclude users and groups that you do not want to import. For example, you could synchronize with the Users container in AD DS, but filter out users whose accounts are disabled.When you create a connection to a business system, you specify the external content type that represents the information from the business system.Mappings define how SharePoint user profile properties relate to data in external systems. A mapping for a particular user profile property consists of three things: 
- The connection that identifies the external system.
    
  
- The attribute from the external system to which the user profile property is related.
    
  
- The direction of the mapping, which can be either "import" for a property that receives its value from the external attribute, or "export" for an external attribute whose value is provided by the SharePoint user profile property.
    
  

## Importing profiles from a directory service
<a name="importDS"> </a>

You can create new profiles and import profile properties by synchronizing with a directory service. When you synchronize with a directory service, SharePoint Server 2013 does the following:
- Creates a user profile for each new user in the directory service containers that are being synchronized, and fills in the properties of each new profile with data from the directory service.
    
  
- Deletes the profile of any user who was removed from the directory service.
    
  
- For properties that are being imported, updates the property in the SharePoint user profile if the corresponding value in the directory service has changed.
    
  
If you synchronize with multiple directory services, each directory service must provide unique users. You cannot synchronize a single user profile with multiple directory services.
> [!NOTE:]

  
    
    


## Importing properties from a business system
<a name="importBusiness"> </a>

You can populate the properties of existing user profiles from a business system. You cannot create new user profiles in this manner, and you cannot write data back to a business system.To import data from a business system, you must first create an external content type to bring the data from the business system into SharePoint Server 2013. Then you can synchronize user profiles with the external content type. For more information about external content types, see  [Overview of Business Connectivity Services in SharePoint Server](html/overview-of-business-connectivity-services-in-sharepoint-server.md).There must be some information that is shared by the external content type and a user profile. SharePoint Server 2013 uses this shared information to match an instance of the external content type to the correct user profile during synchronization. When you define the external content type, you specify that the field to match against is the identifier for the external content type. You specify which user profile property to match against when you create a synchronization connection to a business system. For example, if the business system contains an employee's email address, birth date, and office location, you could specify the email address as the identifier of the external content type, and create a connection that matches against the WorkEmail profile property. For each user profile, SharePoint Server 2013 would synchronize information from the instance of the external content type whose email address matched the WorkEmail property of the user profile.
## Exporting properties to a directory service
<a name="export"> </a>

Once user profiles exist, you can let users modify the values of certain profile properties. You can configure these properties so that data that is changed in SharePoint Server 2013 will be written back to a directory service. Each property can be either imported or exported. You cannot both import and export the same property. You can only export data about a user to the directory service from which the user was imported. You cannot create new user accounts in the directory service by exporting user profile information.
## Creating user profiles without synchronizing
<a name="noSync"> </a>

You can create a custom solution that uses the SharePoint object model to create user profiles. If your solution does not use profile synchronization, you can remove the profile synchronization features from the SharePoint user interface by selecting the **Enable External Identity Manager** option on the **Configure Synchronization Settings** page of Central Administration.
## Synchronizing groups
<a name="groups"> </a>

If you synchronize groups in addition to users, SharePoint Server 2013 imports information about the groups that exist in the directory service containers with which you are synchronizing, and also about which SharePoint Server 2013 users are members of these groups. Each time that you synchronize, SharePoint Server 2013 updates the group and membership information. Groups do not have profiles, and you cannot manipulate them by using SharePoint Server 2013. You must manage groups and their membership in the directory service itself. Within SharePoint Server 2013, groups are only used to create audiences and to display the memberships that a visitor has in common with the person whose My Site the person is visiting (see  [Plan for My Sites in SharePoint Server](html/plan-for-my-sites-in-sharepoint-server.md)).
## Types of synchronization
<a name="types"> </a>

You can perform two kinds of synchronization: full and incremental. Full synchronization can take a long time—for directories that contain hundreds of thousands of users, it could take several days. Incremental synchronization only synchronizes data that has changed in the external system or SharePoint Server 2013, and is more efficient. You must perform a full synchronization the first time that you synchronize. After that, you can use incremental synchronization unless one of the following conditions is true:
- A mapped property has changed. For example, you mapped a new property, or added or changed a mapping associated with a property.
    
  
- You changed the containers that a connection uses to synchronize with a directory service.
    
  
- You changed or added a filter.
    
  
- An external content type that you are synchronizing with has changed.
    
  
- You added or deleted a connection.
    
  
You can configure a timer job to run an incremental synchronization on a set schedule, ranging from every few minutes through monthly. You can also start either a full synchronization or an incremental synchronization manually.
## Supported directory services
<a name="supported"> </a>

With SharePoint Server 2013 you can create connections to the following directory services:
- Active Directory Domain Services (AD DS) 2003 SP2 and AD DS 2008
    
  
- Sun Java System Directory Server version 5.2
    
  
- Novell eDirectory version 8.7.3
    
  
- IBM Tivoli version 5.2
    
  
You can use any of these directory services to synchronize users. Synchronizing groups is only supported for AD DS.All of these directory services support full synchronization. All except Novell eDirectory support incremental synchronization.You can also import data directly from Active Directory Domain Services (AD DS). For more information about how to import directly from AD DS, see  [Configure profile synchronization by using SharePoint Active Directory Import in SharePoint Server 2016](html/configure-profile-synchronization-by-using-sharepoint-active-directory-import-in.md).
# See also

#### 

 [Plan for My Sites and OneDrive for Business in SharePoint Server](html/plan-for-my-sites-and-onedrive-for-business-in-sharepoint-server.md)
  
    
    
 [Plan profile synchronization for SharePoint Server 2013](html/plan-profile-synchronization-for-sharepoint-server-2013.md)
  
    
    
 [Plan user profiles in SharePoint Server](html/plan-user-profiles-in-sharepoint-server.md)
  
    
    
 [Plan for My Sites in SharePoint Server](html/plan-for-my-sites-in-sharepoint-server.md)
  
    
    
 [Configure profile synchronization by using SharePoint Active Directory Import in SharePoint Server 2016](html/configure-profile-synchronization-by-using-sharepoint-active-directory-import-in.md)
  
    
    
 [Administer the User Profile service in SharePoint Server](html/administer-the-user-profile-service-in-sharepoint-server.md)
  
    
    
 [Overview of Business Connectivity Services in SharePoint Server](html/overview-of-business-connectivity-services-in-sharepoint-server.md)
  
    
    

  
    
    

