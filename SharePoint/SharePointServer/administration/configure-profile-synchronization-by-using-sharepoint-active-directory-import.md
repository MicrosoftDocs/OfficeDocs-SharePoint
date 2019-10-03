---
title: "Configure profile synchronization by using SharePoint Active Directory Import in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 2/28/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: 73ceb46e-d3aa-45bd-ac3e-77f58a9ab34d
description: "Learn how to import user profiles from Active Directory to SharePoint Server by using the Active Directory import tool for user profiles."
---

# Configure profile synchronization by using SharePoint Active Directory Import in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
You can use the SharePoint Active Directory import option (AD import) as an alternative to using Microsoft Identity Manager (MIM) to import user profile data from Active Directory Domain Services (AD DS) in your domain.
  
Import operations that use AD import are significantly faster than the same operations that use MIM. However, AD import only works with Active Directory Domain Services (AD DS) and does not work with other directory services. Additionally, if you choose to use AD Import, MIM or other external identity managers are not available for connections to other data sources such as business applications.
  
You must be a member of the Farm Administrators group to perform the procedures in this article. You also need domain credentials with synchronization permissions in order to configure the connection.
  
> [!NOTE]
> MIM is an external provider only available in SharePoint Server 2016. 
  
## Situations unsupported by AD import

Consider the following situations and note what the AD import option does not support when you determine whether to use this option:
  
- The AD import option does not perform bidirectional synchronization. That means changes made to SharePoint user profiles will not be synchronized back to the domain controller.
    
- Referential integrity among users and groups is only maintained within a single Active Directory forest.
    
- The AD import option lets you configure and use only a single, farm-wide property mapping.
    
- The AD import option does not automatically synchronize photos from Active Directory to SharePoint Server 2016.
    
- The AD import option does not support generic (non-AD) LDAP sources.
    
- The AD import option does not support Source Schema Discovery.
    
- The AD import option does not support multi-Forest scenarios such as:
    
  - If you have a trust between two forests, the trusted forest objects will not be imported.
    
  - AD import does support importing users from multiple forests provided you create one synchronization connection per forest. As an alternative, consider using Microsoft Identity Manager.
    
- The AD import option does not support Contact objects (also known as cross-object pointers).
    
- The AD import option does not support custom object classes besides User and Group.
    
- The AD import option does not filter user interface to create complex Boolean expressions.
    
- The AD import option does not provide object filtering based on object property values (you must use simple LDAP filters).
    
- The AD import option does not provide Logon and Resource Forest support. That is, custom joins of data from multiple sources.
    
- The AD import option does not support Business Connectivity Services Import.
    
- The AD import option does not support property mappings for complex types like pictures and special AD types.
    
- The AD import option does not support exporting data from SharePoint to Directory Sources.
    
- The AD import option does not support Upgrading/Translating FIM based connections or synchronizing configuration to AD import (or in reverse order).
    
- The AD import option does not ensure single-master of each object property (currently, the last writer wins).
    
- The AD import option does not perform per-tenant property mapping.
    
## Set up SharePoint Active Directory Import
<a name="proc1"> </a>

You perform three procedures in Central Administration to configure AD import.
  
In the first procedure, you configure SharePoint Server to use AD Import instead of an external identity manager such as MIM.
  
In the second procedure, you create a synchronization connection to AD DS. The connection identifies the items to synchronize and contains the credentials that are used to interact with AD DS. 
  
In the third procedure, you determine how the properties of user profiles in SharePoint Server map to the user information that is retrieved from AD DS. 
  
 **To configure SharePoint Server to use AD Import**
  
1. On the SharePoint Central Administration website, in the **Application Management** section, click **Manage service applications**.
    
2. On the **Manage Service Applications** page, click the link of the User Profile service application. 
    
3. On the **Manage Profile Service** page, in the **Synchronization** section, click **Configure Synchronization Settings**.
    
4. On the **Configure Synchronization Settings** page, in the **Synchronization Options** section, select the **Use SharePoint Active Directory Import** option, and then click **OK**.
    
To import profiles, you must have at least one synchronization connection to AD DS. You may have connections to multiple AD DS servers. Using the following procedure, create a synchronization connection to each AD DS server from which you want to import profiles. You can synchronize after you create each connection, or you can synchronize one time, after you have created all of the connections. Although synchronizing after each connection takes longer, doing this makes it easier to troubleshoot any problems that you might encounter.
  
 **To create a connection to a directory service for import**
  
1. On the SharePoint Central Administration website, in the **Application Management** section, click **Manage service applications**.
    
2. On the **Manage Service Applications** page, click the link of the User Profile service application. 
    
3. On the **Manage Profile Service** page, in the **Synchronization** section, click **Configure Synchronization Connections**.
    
4. On the **Synchronizations Connections** page, click **Create New Connection**.
    
5. On the **Add new synchronization connection** page, type the synchronization connection name in the **Connection Name** box. 
    
6. From the **Type** list, select **Active Directory Import**.
    
7. Fill in the **Connection Settings** section by completing the following steps: 
    
1. In the **Fully Qualified Domain Name** box, type the fully-qualified domain name of the domain. 
    
2. In the **Authentication Provider Type** box, select the type of authentication provider. 
    
3. If you select **Forms Authentication** or **Trusted Claims Provider Authentication**, select an authentication provider from the **Authentication Provider Instance** box. 
    
    The **Authentication Provider Instance** box lists only the authentication providers that are currently used by a web application. 
    
4. In the **Account name** box, type the name of the account you want the AD import tool to use to perform the synchronization. Use the form  _\<DOMAIN\>_\ _\<UserName\>_. The synchronization account must have Replicate Directory permissions or higher on the root OU of AD DS.
    
5. In the **Password** and **Confirm password** boxes, type the password for the account. 
    
6. In the **Port** box, type the connection port you want the AD import tool to use to connect to AD DS when it performs the synchronization. 
    
7. If a Secure Sockets Layer (SSL) connection is required to connect to the directory service, select **Use SSL-secured connection**.
    
    > [!IMPORTANT]
    > If you use an SSL connection, you must export the certificate of the domain controller from the AD DS server and import the certificate into the synchronization server. 
  
8. If you want to filter out users that are disabled in AD DS, select the **Filter out disabled users** check box. 
    
9. If you want to filter the objects that you import from the directory service, in the **Filter in LDAP syntax for Active Directory Import** box, type a standard LDAP query expression to define the filter. 
    
8. In the **Containers** section, click **Populate Containers**, and then select the containers from the directory service that you want to synchronize. All organizational units (OUs) that you select will be synchronized with their child OUs. There is currently no utility that allows you to select a parent OU while excluding any of its child OUs from synchronization.
    
9. Click **OK**.
    
    The newly created connection is listed on the **Synchronization Connections** page. 
    
    > [!TIP]
    > On the **Synchronization Connections** page, you can click the name of a synchronization connection, and then click **Edit** or **Delete** to edit or delete the connection. 
  
 **To map user profile properties**
  
1. On the SharePoint Central Administration website, in the **Application Management** section, click **Manage service applications**.
    
2. On the **Manage Service Applications** page, click link for the User Profile service application. 
    
3. On the **Manage Profile Service** page, in the **People** section, click **Manage User Properties**.
    
4. On the **Manage User Properties** page, click the name of the property that you want to map to a directory service attribute, and then click **Edit**.
    
5. To remove an existing mapping, in the **Property Mapping for Synchronization** section, select the mapping that you want to remove, and then click **Remove**.
    
6. To add a new mapping, do the following: 
    
1. In the **Add New Mapping** section, in the **Source Data Connection** list, select the data connection that represents the directory service to which you want to map the user profile property. 
    
2. In the **Attribute** box, type the name of the directory service attribute to which you want to map the property. 
    
3. Click **Add**.
    
    > [!NOTE]
    > You cannot add multiple mappings or edit a mapping. To change mapping settings for a property, you must first remove the existing mapping, and then create a new mapping. 
  
7. Click **OK**.
    
8. Repeat steps 4 through 7 to map additional properties.
    
 **To start profile synchronization**
  
1. On the SharePoint Central Administration website, in the **Application Management** section, click **Manage service applications**.
    
2. On the **Manage Service Applications** page, click the link for the User Profile service application. 
    
3. On the **Manage Profile Service** page, in the **Synchronization** section, click **Start Profile Synchronization**.
    
4. On the **Start Profile Synchronization** page, select **Start Full Synchronization** if this is the first time that you are synchronizing or if you have added or modified any synchronization connections since the last time that you synchronized. Select **Start Incremental Synchronization** to synchronize only information that has changed since the last time that you synchronized. 
    
5. Click **OK**.
    
    The **Manage Profile Service** page is displayed, showing the profile synchronization status in the right pane. 
    
## See also
<a name="proc1"> </a>

#### Concepts

[Manage user profile synchronization in SharePoint Server](manage-profile-synchronization.md)
  
[Plan profile synchronization for SharePoint Server 2013](plan-profile-synchronization-for-sharepoint-server-2013.md)
  
[Synchronize user and group profiles in SharePoint Server 2013](configure-profile-synchronization.md)
  
[Schedule profile synchronization in SharePoint Server](schedule-profile-synchronization.md)
#### Other Resources

[Update-SPProfilePhotoStore](/powershell/module/sharepoint-server/Update-SPProfilePhotoStore?view=sharepoint-ps)

