---
title: "Prepare your environment for the Business Connectivity Services hybrid scenario"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 6/22/2017
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- Ent_O365_Hybrid
- IT_Sharepoint_Server
- IT_SharePoint_Hybrid_Top
- M365-collaboration
- SPO_Content
ms.assetid: 3b4c9519-b68c-4247-8b58-674537f0c5fe
description: "Learn how to prepare the on-premises account and security group to control access to an OData endpoint for the Business Connectivity Services (BCS) hybrid scenario."
---

# Prepare your environment for the Business Connectivity Services hybrid scenario

[!INCLUDE[appliesto-2013-2016-2019-SPO-md](../includes/appliesto-2013-2016-2019-SPO-md.md)] 
  
This example of the Microsoft Business Connectivity Services (BCS) hybrid scenario shows you how to use standard Windows domain security to control access to the on-premises OData service endpoint. You configure one domain account with which to access the OData service endpoint, and one global security group for your federated user accounts. Then, you map the group to the account by using a Secure Store Service target application.
  
## 

 **To prepare on-premises security for the BCS hybrid scenario**
  
1. Identify all the user accounts in your on-premises domain that need to use the BCS hybrid solution and make sure that they are federated accounts. You will add these accounts to a domain global security group later in this procedure.
    
2. In your on-premises domain, [create a service account](https://go.microsoft.com/fwlink/?LinkId=287046) that will access the OData service endpoint. These procedures use an account named **ODataAccount**.
    
3. In your on-premises domain, [create a global security group](https://go.microsoft.com/fwlink/?LinkId=287048). These procedures use a group named **ODataGroup**.
    
4. Add the accounts that you identified in step 1 to the **ODataGroup** group. 
    
## Create and configure a Secure Store target application

 In this procedure, you link the **ODataGroup** to the **ODataAccount** by using a Secure Store target application. This way, users in the **ODataGroup** access the OData service endpoint through only one account, the **ODataAccount**.
  
In this procedure, you create and configure the on-premises Secure Store target application named **ODataApp** for the BCS hybrid scenario. (You can choose a different name if you want.) 
  
 **To create a target application**
  
1. On the Central Administration home page, in the **Application Management** section, select **Manage service applications**.
    
2. Select the Secure Store service application.
    
3. In the **Manage Target Applications** group, select **New**.
    
4. In the **Target Application ID** box, enter a text string. For example, ODataApp. 
    
5. In the **Display Name** box, enter a name for the target application. For example, ODataApp.
    
6. In the **Contact Email** box, enter a contact email. 
    
7. In the **Target Application Type** dropdown, select **Group**. This indicates the mapping of many user credentials or a security group to one credential. In this case, the **Target Application Page URL** is not needed and automatically selects **None**. Select **Next**.
    
8. On the **Create New Secure Store Target Application** page, for both **Field Name** and **Field Type**, accept the default values of **Windows User Name** and **Windows Password**. Select **Next**.
    
9. In the **Target Application Administrators** field, add the Farm Administrators account and an account that has farm administrator rights. In the **Members** field, add the domain security group you are using to control access to the BCS hybrid scenario solution; for example, **ODataGroup**.
    
10. Select **OK**.
    
Next, we need to add the credentials that we'll be using.
  
 **To set credentials for a target application**
  
1. In the target application list, point at the target application that you just created, select the arrow that appears, and then, in the menu, select **Set credentials**.
    
    If the target application is of type Group, enter the credentials for the external data source. Depending on the information that is required by the external data source, the fields for setting credentials will vary.
    
    If the target application is of type Individual, enter the user name of the individual who will be mapped to this set of credentials on the external data source, and type the credentials for the external data source. Depending on the information that is required by the external data source, the fields for setting credentials will vary.
    
2. In the **Windows User Name** box, enter the account name for the account that will have access to the OData service endpoint in  _domain\username_ format; for example, **Adventureworks\ODataAccount**.
    
3. Enter and confirm the password for that account, and then select **OK**.
    
## Create and configure the OData service endpoint

The BCS hybrid scenario supports connecting only to an OData source. If your external data already has an OData service endpoint, then you can skip the creating an OData service endpoint portions of this procedure. You will still need to configure permissions on the service endpoint for the **ODataAccount**. For the purposes of these procedures, we use the SQL Server[Adventureworks sample database](https://go.microsoft.com/fwlink/?LinkId=290978) and the [AdventureWorks 2012 LT sample data](https://go.microsoft.com/fwlink/?LinkId=290980) as the data source and create an OData service endpoint to make the data available to the BCS hybrid solution. You use Visual Studio 2012 to create and configure the OData service. 
  
To create and configure the OData service endpoint, perform the procedures in [How to: Create an OData data service that sends notifications to BCS in SharePoint 2013](https://go.microsoft.com/fwlink/?LinkId=290977) in the MSDN Library. You will need the **ODataAccount** account to secure the service endpoint in Internet Information Services (IIS) 7.0. 
  
## Prepare the SharePoint site and App Catalog

The BCS hybrid scenario publishes on-premises data to select users of SharePoint. You can present the data either through a SharePoint external list or through an app for SharePoint. In either case, you must identify or create a site in SharePoint through which the data will be offered. If you choose to use an app for SharePoint, you must also have a SharePointApp Catalog configured.
  
 **To prepare the SharePoint site and App Catalog**
  
1. Identify or [create a site](https://go.microsoft.com/fwlink/?LinkId=288864) in SharePoint for your external list or app for SharePoint. Ensure that all the federated users who will be using the BCS hybrid solution are added to the **Members** group for access to the site. (The easiest way to do this is to add your ODataGroup as a Member.) 
    
2. If you're going to be using a app for SharePoint, you must [enable the App Catalog](https://go.microsoft.com/fwlink/?LinkId=288886). 
    
    > [!NOTE]
    > This scenario shows you how to directly deploy your app for SharePoint into the site you have prepared. It is also possible to deploy your app for SharePoint into the App Catalog. 
  
## Set permissions on the BDC Metadata Store in SharePoint

The Business Data Connectivity service (BDC) Metadata Store holds external content types, external systems, and BDC model definitions for the BDC Service Application. In this procedure, you configure administrative permissions on the Metadata Store and everything that it will contain. Later in this scenario, if you are using the manual import of the external content type method, you will be using the BDC Metadata Store. This external content type will be available across SharePoint. If you will only be using the automated deployment of an app for SharePoint, then you will not use the BDC Metadata Store, and the external content type is scoped to the app only.
  
 **To set permissions on the BDC Metadata Store in SharePoint**
  
1. Go to the [More features page of the new SharePoint admin center](https://admin.microsoft.com/sharepoint?page=classicfeatures&modern=true), and sign in with an account that has [admin permissions](/sharepoint/sharepoint-admin-role) in Microsoft 365.

2. Under **BCS**, select **Open**.
    
3. Select **Manage BDC Models and External Content Types**.
    
4. Select **Set Metadata Store Permissions**, and add **All Authenticated Users** with at least **Execute** permissions. This will allow all users who authenticate to your SharePoint tenancy to use the external content types stored in the Metadata Store. 
    
5. Select the **Propagate permissions to all BCS Models, External Systems and External Content Types in the BDC Metadata Store. Doing so will overwrite existing permissions** check box. 
    
6. Select **OK**.
    
## Validate external access to reverse proxy published URL

At this point in deploying the BCS hybrid scenario, you should confirm that you can access your on-premises SharePoint Server farm that has been configured to receive hybrid calls from SharePoint. This site was already configured in the [SharePoint Server 2016 hybrid configuration roadmaps](configuration-roadmaps.md) procedures. Its URL is the one you published through your reverse proxy. 
  
Before you begin this procedure, make sure you have the following:
  
- The external URL, for example, if your on-premises farm web application was configured with an alternate access mapping of "hybridexternal.sharepoint.com" and you published out "https://hybridexternal.sharepoint.com" through the reverse proxy, you will use "https://hybridexternal.sharepoint.com" for this procedure.
    
- A computer to browse from that is in the extranet. For example, use a computer that is not on your corporate network and is not a member of your corporate domain.
    
- The Secure Channel certificate that is stored in the SharePointSecure Store Service target application. This target application was configured in the [SharePoint Server 2016 hybrid configuration roadmaps](configuration-roadmaps.md) procedures. In the example it was named **SecureChannelTargetApp**. You will need the password for the certificate as well.
    
- The credentials of a federated account.
    
 **To confirm access to external URL**
  
1. Copy the certificate to your extranet computer, and then click the certificate. You will be prompted for the certificate password. This adds the certificate to your personal certificate store.
    
2. Open a web browser and browse to the externally published URL of your on-premises farm. You should be prompted for credentials. If not, check your browser settings and make sure that your logged on credentials are not being automatically passed.
    
3. Provide the credentials of the federated user. This log on must succeed and you should see the published site. If this does not work, contact the administrators who set up your hybrid infrastructure. Do not proceed any further with the BCS hybrid scenario until this issue is resolved.
    
## Create and configure the connection settings object

Unlike BCS in SharePoint Server, BCS in SharePoint requires that you configure a connection settings object, which contains additional information to establish the connection to the external system and the OData source.
  
Before you begin this procedure, make sure you have the following:
  
- The URL or published service endpoint of the on-premises OData service that you configured.
    
- The ID of the Secure Store target application that you configured.
    
- The Internet-facing URL that Microsoft 365 uses to connect to the service address and that was published by the reverse proxy. This is the address that you used to browse to the external service in the last procedure, with the addition of /_vti_bin/client.svc.
    
- The ID of the Secure Store target application for the Secure Channel certificate in Microsoft 365.
    
 **To configure the connection settings object for the BCS hybrid scenario**
  
1. go to the [More features page of the new SharePoint admin center](https://admin.microsoft.com/sharepoint?page=classicfeatures&modern=true), and sign in with an account that has [admin permissions](/sharepoint/sharepoint-admin-role) in Microsoft 365. 

2. Under **BCS**, select **Open**.
    
3. Select **Manage connections to on-premises services**.
    
4. Select **Add**.
    
5. Give the connection settings object a name.
    
    > [!IMPORTANT]
    > Keep track of this name; you will use it when you create the external content type in the next procedure. 
  
6. In the **Service Address** box, enter the URL of the OData service endpoint that you created. 
    
7. For this scenario, select the **Use credentials stored in Sharepoint on-premises** as the authentication option, and then enter the name of target application ID that holds the group to account mapping. In this scenario, it is **ODataApp** that you created. 
    
8. In the **Authentication Mode** dropdown, select **Impersonate Window's Identity**.
    
9. In the **Internet-facing URL** box, enter the external URL with the /_vti_bin/client.svc extension. For example, https://hybridexternal.sharepoint.com/_vti_bin/client.svc.
    
10. In the **Secure Store Target Application ID** box, enter the ID of the target application that holds the Secure Channel certificate. For example, **SecureChannelTargetApp**.
    
11. Select **Create**.
    
## Create and configure the external content type

In every BCS solution, the external content type defines the external data to SharePoint Server. It includes descriptions of how the data is structured, how it is secured, the specific portions of the external data that you want to interact with, and the permitted operations. When an external list or app for SharePoint or business data Web Part makes a request for external data, the Business Data Connectivity service refers to the external content type for the list or app or Web Part to understand how to communicate with the external data source. 
  
In the BCS hybrid scenario, only OData sources are supported and the preferred way to make an external content type for an OData source is to use Visual Studio 2012. Visual Studio 2012 simplifies the external content type creation process by directly connecting to the OData source, reading it, and building the external content type XML for you. Once created, you have to make some minor changes to the XML, such as inserting which connection settings object to use and removing some of the boilerplate code, before you can deploy it to SharePoint for use in the BCS hybrid scenario.
  
Before you begin, make sure you have the following:
  
- Visual Studio 2012 installed on a computer that on your corporate network.
    
- The OData service endpoint URL
    
- Microsoft Office Tools for Visual Studio 2012
    
After you have all of that, complete the steps in [How to: Create an external content type from an OData source in SharePoint 2013](https://go.microsoft.com/fwlink/p/?LinkId=290982) in the MSDN Library. 
  
When you are done creating the external content type, [deploy the hybrid scenario to an external list](deploy-the-hybrid-scenario-as-an-external-list.md).
  
## See also

#### Concepts

[Deploy a Business Connectivity Services hybrid solution in SharePoint](deploy-a-business-connectivity-services-hybrid-solution.md)
  
[Overview of Business Connectivity Services security tasks in SharePoint Server](../administration/security-tasks-overview.md)

