---
title: "Configure Excel Services (SharePoint Server 2013)"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/14/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: a2ef35c4-6b29-4ad1-8652-48a019838ea0
description: "Deploy Excel Services to your SharePoint Server farm by creating an Excel Services service application by using Central Administration."
---

# Configure Excel Services (SharePoint Server 2013)

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)] 
  
> [!IMPORTANT]
> The steps in this article apply to SharePoint Server 2013 Enterprise. 
  
Excel Services is enabled by creating an Excel Services Application service application in Central Administration. This article walks you through the steps of deploying Excel Services in your SharePoint Server 2013 farm.
  
    
## Before you begin
<a name="begin"> </a>

Before you deploy Excel Services, we recommend that you review [Overview of Excel Services in SharePoint Server 2013](excel-services-overview.md) and its associated Excel Services planning articles. 
  
Before you begin this operation, review the following information about prerequisites:
  
- A domain account is required to run the Excel Services application pool.
    
- You must be a member of the Farm Administrators group to perform the procedures in this article.
    
## Video demonstration
<a name="VideoDemonstration"> </a>

This video shows the steps involved in creating an Excel Services service application, as described in this article.
  
**Video: Configure Excel Services in SharePoint Server 2013**

> [!VIDEO https://www.microsoft.com/videoplayer/embed/7f1bbb20-a1b5-43a6-a8a0-1412de5e76f1?autoplay=false]
## Configure the application pool account
<a name="proc1"> </a>

For better security, we recommend that you use a separate domain account to run the Excel Services application pool. Have your domain administrator create a domain account to use in running the Excel Services application pool. No specific domain privileges are required for this account.
  
Before you can use an account to run an application pool, you must register it as a managed account in SharePoint Server. Use the following procedure to register the account.
  
 **To register a managed account**
  
1. On the SharePoint Central Administration website home page, in the left navigation, click **Security**.
    
2. On the Security page, under **General Security**, click **Configure managed accounts**.
    
3. On the Managed Accounts page, click **Register Managed Account**.
    
4. Type the user name and password of the domain account that you are registering.
    
5. Optionally, select the **Enable automatic password change** check box if you want SharePoint Server to manage password changes for this account. 
    
6. Click **OK**.
    
### Grant content database access to the managed account
<a name="GrantAccess"> </a>

You must also grant access to the SharePoint content database for the account that you will use to run the Excel Services application pool. Use the following procedure for each web application that will be associated with Excel Services.
  
 **To grant content database access to the managed account**
  
1. On a SharePoint Server application server, click **Start**, click **All Programs**, click **Microsoft SharePoint 2013 Products**, right-click **SharePoint 2013 Management Shell**, and then click **Run as Administrator**.
    
2. At the Microsoft PowerShell Command Prompt, type the following (press Enter after each line):
    
  ```
  $w = Get-SPWebApplication -identity http://<WebApplication>
  $w.GrantAccessToProcessIdentity("<Domain>\<Username>")
  ```

> [!IMPORTANT]
> If in the future you add additional content databases, you must rerun these cmdlets to ensure that Excel Services has access to the new databases. 
  
Once you have granted content database access to the application pool account, the next step is to start the Excel Calculation Services service.
  
## Start the Excel Calculation Services service
<a name="proc2"> </a>

In order to use Excel Services, you must start the Excel Calculation Services service on at least one application server in the farm. Use the following procedure to start the service.
  
 **To start the Excel Calculation Services service**
  
1. On the Central Administration home page, in the **System Settings** section, click **Manage services on server**.
    
2. To select the server where you want to start the service, above the **Service** list, click the **Server** drop-down list, and then click **Change Server** and choose the appropriate server. 
    
3. In the **Service** list, click **Start** next to **Excel Calculation Services**.
    
After the Excel Calculation Services service has been started, the next step is to create an Excel Services service application.
  
## Create an Excel Services service application
<a name="proc3"> </a>

Use the following procedure to create an Excel Services service application.
  
 **To create an Excel Services service application**
  
1. On the Central Administration home page, under **Application Management**, click **Manage service applications**.
    
2. On the Manage Service Applications page, click **New**, and then click **Excel Services Application**.
    
3. In the **Name** section, type a name for the service application in the text box. 
    
4. Select the **Create new application pool** option and type a name for the application pool in the text box. 
    
5. Select the **Configurable** option, and from the drop-down list, select the account that you created to run the application pool. 
    
6. Click **OK**.
    
## Additional steps
<a name="more"> </a>

Once you have created the service application, you are ready to start using Excel Services. See the following articles for additional configuration steps.
  
- [Manage Excel Services global settings (SharePoint Server 2013)](manage-excel-services-global-settings.md)
    
- [Manage Excel Services trusted file locations (SharePoint Server 2013)](manage-excel-services-trusted-file-locations.md)
    
- [Manage Excel Services trusted data providers (SharePoint Server 2013)](manage-excel-services-trusted-data-providers.md)
    
- [Manage Excel Services trusted data connection libraries (SharePoint Server 2013)](manage-excel-services-trusted-data-connection-libraries.md)
    
- [Manage Excel Services user defined function assemblies (SharePoint Server 2013)](manage-excel-services-user-defined-function-assemblies.md)
    
- [Manage Excel Services data model settings (SharePoint Server 2013)](manage-excel-services-data-model-settings.md)
    
## See also
<a name="more"> </a>

#### Other Resources

[Excel Services cmdlets in SharePoint Server 2013](/powershell/module/sharepoint-server/?view=sharepoint-ps)

