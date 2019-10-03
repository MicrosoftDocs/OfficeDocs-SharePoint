---
title: "Change site collection administrators in SharePoint Server"
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
ms.assetid: b3d2f46d-783c-4f81-9c0a-d41a3486917e
description: "How to change site collection administrators for SharePoint Server site collections by using the SharePoint Central Administration website or Microsoft PowerShell."
---

# Change site collection administrators in SharePoint Server
[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
A site collection administrator in SharePoint Server can configure the appearance and behavior of the site, configure search settings and site directory settings, and allocate storage space. A site collection must have one primary site collection administrator and can have one secondary site collection administrator. The primary and secondary site collection administrators receive administrative email alerts for the site collection. The primary and secondary site collection administrators are automatically added to the SharePoint Site Collection Administrators group. You can add as many additional accounts as you want to the SharePoint Site Collection administrators group, but only the primary and secondary site collection administrators will receive administrative alerts for the site collection. All members of the SharePoint Site Collection Administrators group have full administrative permissions to the site collection. 
  
    
## Change the primary or secondary site collection administrator
<a name="section1"> </a>

Use this procedure when you want to make a user a primary or secondary site collection administrator for a specific site collection.
  
> [!CAUTION]
> A site collection can have only one primary site collection administrator and one secondary site collection administrator. The steps in this procedure describe how to change either of them. Any user who is removed as a site collection administrator is removed from the site collection administrators group for the site collection. 
  
### To change the primary or secondary site collection administrator by using Central Administration

1. Verify that you have the following administrative credentials:
    
   - To add a site collection administrator, you must be a member of the Farm Administrators group on the computer that is running Central Administration.
    
2. In Central Administration, click **Application Management**. On the **Application Management** page, in the **Site Collections** section, click **Change site collection administrators**.
    
3. On the **Site Collection Administrators** page, click the arrow next to the site collection name, and then select **Change Site Collection** if the site collection you want is not already selected. 
    
4. If the site collection to which you want to add an administrator is listed, select the URL of the site collection, and then click **OK**. If the site collection is not listed, click the arrow next to the web application name, click **Change Web Application**, select the name of the web application that contains the site collection, select the URL of the site collection, and then click **OK**.
    
5. In the **Primary site collection administrator** or **Secondary site collection administrator** area, either type the name of the user whom you want to add by using the format  _\<domain\>_\ _\<username\>_ or select the user by using the address book. 
    
6. Click **OK**.
    
### To add a primary or secondary site collection administrator by using Microsoft PowerShell

1. Verify that you meet the following minimum requirements: See [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps).
    
2. Open the SharePoint Management Shell.
    
3. At the PowerShell command prompt, type the following command to replace the secondary site collection administrator:
    
   ```powershell
   Set-SPSite -Identity "<SiteCollection>" -SecondaryOwnerAlias "<User>"
   ```

    Where:
    
   -  _\<SiteCollection\>_ is the URL of the site collection to which you want to add a site collection administrator. 
    
   -  _\<User\>_ is name of the user whom you want to add in the format  _\<domain\>_\ _\<username\>_.
    
The previous procedure shows a common way to use the **Set-SPSite** cmdlet to add a secondary site collection administrator. You can specify different parameters to configure different settings for a site collection. For more information, see [Set-SPSite](/powershell/module/sharepoint-server/set-spsite?view=sharepoint-ps). 

We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions.
  
## Remove a site collection administrator
<a name="section2"> </a>

Use this procedure to specify the user to be removed from the site collection administrator list. This procedure does not remove the user from Active Directory Domain Services (AD DS).
  
### To remove a site collection administrator by using Central Administration

1. Verify that you have the following administrative credentials:
    
   - To remove a site collection administrator, you must be a member of the Farm Administrators group on the computer that is running Central Administration.
    
2. In Central Administration, select **Application Management**. On the **Application Management** page, in the **Site Collections** section, click **Change site collection administrators**.
    
3. On the **Site Collection Administrators** page, click the arrow next to the site collection name, and then click **Change Site Collection**.
    
4. If the site collection from which you want to remove an administrator is listed, select the URL of the site collection, and then click **OK**. If the site collection is not listed, click the arrow next to the web application name, click **Change Web Application**, select the name of the web application that contains the site collection, select the URL of the site collection, and then click **OK**.
    
5. Every site collection must have a primary site collection administrator. If you want to remove the primary site collection administrator, you must replace it with a different primary site collection administrator. To do so, select the current administrator's name, press the Delete key, and then either type the name of the replacement site collection administrator by using the format  _\<domain\>_\ _\<username\>_ or select a replacement site collection administrator by using the address book. 
    
6. To remove the secondary site collection administrator, select the administrator's name, and then press the **Delete** key. 
    
7. Click **OK**.
    
## See also
<a name="section2"> </a>

#### Concepts

[Create a site collection in SharePoint Server](create-a-site-collection.md)
#### Other Resources

[Manage administrators for a site collection](https://go.microsoft.com/fwlink/?linkid=845358)

