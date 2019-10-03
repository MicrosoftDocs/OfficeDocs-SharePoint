---
title: "Create, edit, and delete quota templates in SharePoint Server"
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
ms.assetid: c2eda191-1814-423b-882f-1fdafe9df6c9
description: "How to create, edit, and delete site quota templates for a SharePoint Server site collection."
---

# Create, edit, and delete quota templates in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
You control how much data a site collection can hold and the quantity of resources it can use by using quotas. For more information about how to plan quotas, see [Quotas](plan-site-maintenance-and-management.md#section1).
  
> [!NOTE]
> When you apply a quota template to a site collection, the storage limit applies to the site collection as a whole. In other words, the storage limit applies to the sum of the content sizes for the top-level site and all subsites within the site collection. If versioning is enabled, the versions in a site and the content in the Recycle Bins count toward storage limits. You can also specify a percentage of storage limits for the second-stage Recycle Bin. 
  
    
## Before you begin
<a name="begin"> </a>

Before you perform this procedure, confirm the following:
  
- Outgoing email is configured. 
    
    For more information, see [Configure outgoing email for a SharePoint Server farm](../administration/outgoing-email-configuration.md).
    
- The Disk Quota Warning timer job is running.
    
    For more information about default timer jobs for SharePoint Server, see [Timer job reference for SharePoint Server](../technical-reference/timer-job-reference-for-sharepoint-server.md).
    
- The quota template options on the quota template page in Central Administration are available only if you have already created one or more quota templates. The first time that you use this page, you will be given only the option to create a new template.
    
## Create a quota template
<a name="Section1"> </a>

You might want to create a quota template to apply to sites that have storage and performance requirements that differ from most other sites in the site collection.
  
 **To create a quota template**
  
1. Verify that you have the following administrative credentials:
    
   - You are a member of the Farm Administrators group on the computer that is running the SharePoint Central Administration website.
    
2. On the Central Administration home page, click **Application Management**. On the Application Management page, in the **Site Collections** section, click **Specify quota templates**.
    
3. On the Quota Templates page, in the **Template Name** section, click **Create a new quota template**.
    
4. In the **New template name** box, type the name of the new template. 
    
    If you want to base your new template on an existing quota template, expand the **Template to start from** list, and then click the template that you want. 
    
5. In the **Storage Limit Values** section, set the values that you want to apply to the template. 
    
   - If you want to restrict how much data that can be stored, click the **Limit site storage to a maximum of** check box and type the storage limit in megabytes into the box. 
    
   - If you want an email message to be sent to the site collection administrator when a certain storage threshold is reached, click the **Send warning E-mail when Site Collection storage reaches** check box and type the threshold in megabytes into the box. 
    
6. In the Sandboxed Solutions with Code Limits section, set the values for a template for sandboxed solutions.
    
   - In the **Limit maximum usage per day to** box, type the daily usage in points. 
    
   - In the **Send warning e-mail when usage per day reaches** box, type the daily usage warning limit in points. 
    
    A point is a relative measurement of resource usage, for example, CPU cycles, memory, or page faults. Points enable comparisons between measurements of resource usage that could not be compared otherwise. 
    
    If you do not want to send a warning email message, clear the **Send warning e-mail when usage per day reaches** check box, and then click **OK**.
    
## Edit a quota template
<a name="Section2"> </a>

You might want to edit a quota template to increase the storage limit if you find that sites are exceeding the current storage limit on a regular basis.
  
 **To edit a quota template**
  
1. Verify that you have the following administrative credentials:
    
   - You are a member of the Farm Administrators group on the computer that is running the SharePoint Central Administration website.
    
2. On the Central Administration home page, click **Application Management**. On the Application Management page, in the **Site Collections** section, click **Specify quota templates**.
    
3. On the Quota Templates page, in the **Template Name** section, expand the **Template to modify** list, and then click the template that you want to edit. 
    
4. Change the settings as necessary, and then click **OK**.
    
## Delete a quota template
<a name="Section3"> </a>

You might want to delete a quota template when the site collection that required those specific settings is deleted.
  
Even though you can delete a quota template if necessary, we do not recommend that you do this. Since deleting a quota template will not delete quota values from sites that were created by using the quota template. Instead, we recommend that you use the object model to perform minor fixes in the quota template.
  
 **To delete a quota template**
  
1. Verify that you have the following administrative credentials:
    
   - You are a member of the Farm Administrators group on the computer that is running the SharePoint Central Administration website.
    
2. On the Central Administration home page, click **Application Management**. On the Application Management page, in the **Site Collections** section, click **Specify quota templates**.
    
3. In the **Template Name** section, expand the **Template to modify** list, and then click the template that you want to delete. 
    
4. At the bottom of the Quota Templates page, click **Delete**, and then click **OK**.
    
## Change the settings of a quota template
<a name="Section4"> </a>

> [!NOTE]
> A modified quota template is not automatically applied to any existing site collections that use the quota template. A member of the Farm Administrators group must manually apply all modified values to all existing sites that use the quota template. 
  
 **To change the settings of a quota template by using Central Administration**
  
1. Verify that you have the following administrative credentials:
    
   - You must be a member of the Farm Administrators group.
    
2. On the Central Administration home page, click **Application Management**. On the Application Management page, in the **Site Collections** section, click **Specify quota templates**.
    
3. On the Quota Templates page, in the **Template Name** section, in the **Template to modify** list, select the template that you want to change. 
    
4. In the **Storage Limit Values** section, specify the values that you want to apply to the template. 
    
   - If you want to modify the amount of data that can be stored in the database, leave the **Limit site storage to a maximum of** check box selected, and then type the new storage limit, in megabytes, in the box. 
    
   - If you want an email message to be sent to the site collection administrator when a storage threshold is reached, select the **Send warning E-mail when site storage reaches** check box, and then type the threshold, in megabytes, in the box. 
    
5. In the **Sandboxed Solutions With Code Limits** section, specify the values that you want to apply to the template. 
    
   - If you want to limit the maximum resource usage points per day for sandboxed solutions that contain code, type the new limit in the **Limit maximum usage per day to** box. The default limit is 300 points. 
    
   - If you want an email message to be sent to the site collection administrator when the usage per day threshold is reached, select the **Send warning e-mail when usage per day reaches** check box, and then type the threshold, in points, in the box. 
    
6. Click **OK**.
    
## Change the quota template for a site collection
<a name="Section5"> </a>

If a site collection is close to exceeding its storage limits and you want to increase its size, you can change the quota template that is applied to the site collection to another quota template with higher limits. This automatically updates the warning and storage limits for the site collection.
  
### To change the quota template for a site collection by using Central Administration

1. Verify that you have the following administrative credentials:
    
   - You must be a member of the Farm Administrators group.
    
2. On the Central Administration home page, click **Application Management**. On the Application Management page, in the **Site Collections** section, click **Configure quotas and locks**. 
    
3. On the Site Collection Quotas and Locks page, ensure that the correct site collection is displayed. If you want to change the site collection, expand the **Site Collection** list, and then click **Change Site Collection**. Use the Select Site Collection page to select a site collection.
    
4. In the **Site Quota Information** section, expand the **Current quota template** list, and select the new quota template to apply, and then click **OK**.
    
### To change the quota template for a site collection by using Microsoft PowerShell

1. Verify that you meet the following minimum requirements: See [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps).
    
2. Open the SharePoint Management Shell.
    
3. At the Microsoft PowerShell command prompt, type the following command:
    
   ```powershell
   Set-SPSite -Identity "<Site>" -QuotaTemplate "<Template>"
   ```

   Where:
    
   -  _\<Site\>_ is the URL or GUID of the site collection whose quota template that you want to change. 
    
   -  _\<Template\>_ is the name or GUID of the replacement quota template. 
    
For more information, see [Set-SPSite](/powershell/module/sharepoint-server/set-spsite?view=sharepoint-ps). 

We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions.
  
## Change the storage limits for a site collection
<a name="Section6"> </a>

Use these procedures to change the storage limits for a site collection.
  
### To change the storage limits for a site collection by using Central Administration

1. Verify that you have the following administrative credentials:
    
   - You must be a member of the Farm Administrators group.
    
2. On the Central Administration home page, click **Application Management**.
    
3. On the Application Management page, in the **Site Collections** section, click **Configure quotas and locks**. 
    
4. On the Site Collection and Quota Locks page, ensure that the correct site collection is displayed. If you want to change the site collection, expand the **Site Collection** list, and then click **Change Site Collection**. Use the Select Site Collection page to select a site collection.
    
5. If the site collection currently uses a quota template, do the following to specify an individual quota:
    
   - On the Site Collection Quotas and Locks page, in the **Site Quota Information** section, expand the **Current quota template** list, and then select **Individual Quota**.
    
6. Select the **Limit site storage to a maximum of** check box, and then type the new maximum value in megabytes. 
    
7. If you want to send site storage notification email messages to the site collection administrator, select the **Send warning e-mail when site storage reaches** check box, and then type the value in megabytes. 
    
8. If you want to limit the maximum resource usage points per day for sandboxed solutions, type the new limit in the **Limit maximum usage per day to** box. The default is 300 points. 
    
9. If you want an email message to be sent to the site collection administrator when the usage per day threshold is reached, select the **Send warning e-mail when usage per day reaches** check box, and then type the threshold, in points, in the box. The default is 100 points. 
    
10. Click **OK**.
    
### To change the storage limits for a site collection by using PowerShell

1. Verify that you meet the following minimum requirements: See [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps).
    
2. Open the SharePoint Management Shell.
    
3. At the Microsoft PowerShell command prompt, type the following command:
    
   ```powershell
   Set-SPSite -Identity "<Site>" -MaxSize <Limit>
   ```

    Where:
    
   -  _\<Site\>_ is the URL of the site collection whose storage limits you want to change. 
    
   -  _\<Limit\>_ is the new storage limit for the site collection, in bytes. 
    
    > [!NOTE]
    > The new storage limit overrides the limit set in the quota template that is currently applied to the site collection. 
  
    For more information, see [Set-SPSite](/powershell/module/sharepoint-server/set-spsite?view=sharepoint-ps).
    
    For information about how to use PowerShell and the SharePoint object model to set the maximum usage per day and the warning level threshold for sandboxed solutions, see "Using Windows PowerShell for Administration" in [Chapter 4: Sandboxed Solutions](https://go.microsoft.com/fwlink/p/?LinkId=219528), an excerpt from the book  *Inside Microsoft SharePoint 2010*  on MSDN. 
    
## See also
<a name="Section6"> </a>

#### Concepts

[Create a site collection in SharePoint Server](create-a-site-collection.md)
  
[Manage the lock status for site collections in SharePoint Server](manage-the-lock-status-for-site-collections.md)

