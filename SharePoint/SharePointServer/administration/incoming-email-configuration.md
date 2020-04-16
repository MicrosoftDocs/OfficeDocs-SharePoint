---
title: "Configure incoming email for a SharePoint Server farm"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/12/2018
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection: IT_Sharepoint_Server_Top
ms.assetid: 88317397-e0cb-47c7-9093-7872bc685213
description: "Learn how to install and configure the SMTP service, prepare your environment, and configure incoming email for a SharePoint Server 2016, SharePoint Server 2013, and SharePoint Foundation 2013 farm."
---

# Configure incoming email for a SharePoint Server farm

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
This article describes how to configure incoming email for SharePoint Server. This article also describes how to install and configure the SharePoint Migration Tool service to enable incoming email.
  
When incoming email is enabled, SharePoint sites can receive and store email messages and attachments in lists and libraries. This article describes two scenarios, one basic and one advanced. The basic scenario applies to a single-server farm environment and is recommended if you want to use default settings. The advanced scenario applies to a single-server farm or a multiple-server farm and contains several advanced options from which to choose. For more information, see [Plan incoming email for a SharePoint Server farm](incoming-email-planning.md).
  
    
## Before you begin
<a name="begin"> </a>

Before you begin this operation, make sure to review the following information:
  
- Your system is running SharePoint Server 2016, SharePoint Server 2013, or SharePoint Foundation 2013.
    
- Read and understand [Plan incoming email for a SharePoint Server farm](incoming-email-planning.md).
    
- For the basic scenario, each SharePoint application server must be running the Simple Mail Transfer Protocol (SMTP) service and the SharePoint Foundation Web Application service.
    
- For the advanced scenario, you can use one or more servers in the server farm to run the SMTP service and to have a valid SMTP server address. Alternatively, you must know the name of a server outside the farm that is running the SMTP service and the location of the email drop folder.
    
If you have not installed and configured the SMTP service and do not choose to use an email drop folder, you must complete the steps in [Install and configure the SMTP service](incoming-email-configuration.md#section2) before you configure incoming email. 
  
## Install and configure the SMTP service
<a name="section2"> </a>

Incoming email for SharePoint Server uses the SMTP service. You can use the SMTP service in one of two ways. You can install the SMTP service on one or more servers in the farm, or administrators can provide an email drop folder for email that is forwarded from the service on another server. For more information about the email drop folder option, see [Plan incoming email for a SharePoint Server farm](incoming-email-planning.md).
  
### Install the SMTP service

If you are not using a drop folder for email, the SMTP service must be installed on every application server in the farm that you want to configure for incoming email. To install the SMTP service, use the Add Roles and Features Wizard in Server Manager. After you complete the procedure, the SMTP service is installed on the application server.
  
 **To install the SMTP service**
  
1. Verify that the user account that is performing this procedure is a member of the Administrators group on the application server.
    
2. Open **Server Manager**, select **Manage**, and then select **Add Roles and Features**.
    
3. Select **Next** until the Select features page appears, select **SMTP Server**, select **Add Features**, and then select **Next**.
    
4. On the **Confirm Installation Selections** page, select **Install**.
    
5. On the **Installation Results** page, check that the installation finished successfully, and then select **Close**.
    
### Install IIS 6.0 Management tools

To manage the SMTP service on Windows Server 2012 R2, Windows Server 2016, Windows Server 2008, and Windows Server 2008 R2 you must use Internet Information Services (IIS) 6.0 Manager. However, if you install the SMTP service on Windows Server 2016, the Add Roles and Features Wizard automatically installs the IIS 6 Management tools.
  
 **To install IIS 6.0 Manager**
  
1. Verify that you have the following administrative credentials:
    
  - You must be a member of the Administrators group on the front-end web server.
    
2. Open **Server Manager**, select **Manage**, and then select **Add Roles and Features**.
    
3. Select **Next** until the Select server roles page appears, select **Management Tools** and **IIS 6 Management compatibility**, and then select **Install**.
    
4. In **Application Server** section, select **Add Role Services**.
    
5. On the Select Role Services page, select **Management Tools** and **IIS 6 Management compatibility**, and then select **Install**.
    
### Configure the SMTP service

After you install the SMTP service, you configure it to accept email from the mail server for the domain. You can decide to accept relayed email from all servers except those that you specifically exclude. Alternatively, you can block email from all servers except those that you specifically include. You can include servers individually, in groups by subnet, or in groups by domain.
  
After you configure the service, set it to start automatically.
  
### To configure the SMTP service

1. Verify that the user account that is performing this procedure is a member of the Administrators group on the application server. 
    
2. Open Server Manager, select **Tools**, and then select **Internet Information Services (IIS) 6.0 Manager**.
    
3. In IIS Manager, expand the server name that contains the SMTP server that you want to configure.
    
4. Right-click the SMTP virtual server that you want to configure, select **Start**, and then right-click the server again, and select **Properties**.
    
5. On the **Access** tab, in the **Access control** area, select **Authentication**.
    
6. In the **Authentication** dialog, verify that **Anonymous access** is selected, and select **OK**.
    
7. On the **Access** tab, in the **Relay restrictions** area, select **Relay**.
    
8. To enable relaying from any server, select **All except the list below**.
    
9. To accept relaying from one or more specific servers, follow these steps:
    
  - Select **Only the list below**.
    
  - Select **Add**, and then add servers one at a time by IP address, or in groups by using a subnet or domain.
    
  - Select **OK** three times to close the **Computer**, **Relay Restrictions**, and **Properties** dialogs. 
    
### To set the SMTP service to start automatically

1. Open Server Manager, select **Tools**, and then select **Services**.
    
2. In Services, right-click **Simple Mail Transfer Protocol (SMTP)**, and then select **Properties**.
    
3. In the **Simple Mail Transfer Protocol (SMTP) Properties** dialog, on the **General** tab, in the **Startup type** list, select **Automatic**, and select **OK**.
    
## Configure incoming email in a basic scenario
<a name="section3"> </a>

You can use the following procedure to configure incoming email in a basic scenario by selecting the **Automatic** settings mode and using the default settings. After you complete the procedure, users can send email to lists and libraries. 
  
 **To configure incoming email in a basic scenario**
  
1. Make sure the user account that is performing this procedure is a member of the Administrators group on the server that is running the **SharePoint Central Administration** website.
    
2. In Central Administration, select **System Settings**, and in the **E-Mail and Text Messages (SMS)** section, select **Configure incoming e-mail settings**.
    
3. To enable sites on this server to receive email, on the **Configure Incoming E-Mail Settings** page, in the **Enable Incoming E-Mail** section, select **Yes**.
    
4. Select the **Automatic** settings mode. 
    
5. In the **Incoming E-Mail Server Display Address** section, in the **E-mail server display address** box, enter a display name for the email server, for example, mail.fabrikam.com. 
    
6. Use the default settings for all other sections, and then select **OK**.
    
After you configure incoming email, users who have Manage Lists permissions can configure email-enabled lists and document libraries.
  
## Configure incoming email in an advanced scenario
<a name="section4"> </a>

The following procedure explains how to configure incoming email in an advanced scenario by selecting the **Advanced** settings mode and additional options that you want to use for your incoming email environment. After you complete the procedure, users can send email to lists and libraries. 
  
You can also use the **Automatic** settings mode in an advanced scenario. In the **Automatic** settings mode, you can select to receive email that has been routed through a safe-email server application. In the **Advanced** settings mode, you can instead specify a drop folder. For more information, see [Plan incoming email for a SharePoint Server farm](incoming-email-planning.md).
  
Several of these steps mention prerequisite procedures that are documented in [Prepare your environment for incoming email in an advanced scenario](#section5) later in this article. 
  
 <a name="ToConfigureEmailAdvanced"></a>**To configure incoming email in an advanced scenario**
  
1. Make sure the user account that is performing this procedure is a member of the Administrators group on the server that is running the SharePoint Central Administration website.
    
2. In the **Central Administration** website, select **System Settings**, in the **E-Mail and Text Messages (SMS)** section, select **Configure incoming e-mail settings**.
    
3. To enable sites on this server to receive email, on the **Configure Incoming E-mail Settings** page, in the **Enable Incoming E-Mail** section, select **Yes**.
    
4. Select the **Advanced** settings mode. 
    
    You can specify a drop folder instead of using an SMTP server. The default location of the drop folder is C:\inetpub\mailroot\drop. You can configure a different location if you want but this drop folder must be the same on all SharePoint Servers.
    
    > [!NOTE]
    > You can also select the **Automatic** settings mode and select whether to use Directory Management Service and whether to accept email from all email servers or from several specified email servers. For more information, see [Plan incoming email for a SharePoint Server farm](incoming-email-planning.md). 
  
5. If you want to connect to Directory Management Service, in the **Directory Management Service** section, select **Yes**.
    
    If you select this option, you must first configure Active Directory Domain Services (AD DS). If you use Exchange Server, you must also configure the DNS Manager and add an SMTP connector. For more info, see [Configure AD DS to be used with Directory Management Service](incoming-email-configuration.md#ConfigureADDSwithDMS), [Configure DNS Manager](incoming-email-configuration.md#ConfigureDNSManager), and [Add an SMTP connector in Microsoft Exchange Server 2016](incoming-email-configuration.md#AddSMTPconnector) later in this article. 
    
  - In the **Active Directory container where new distribution groups and contacts will be created** box, enter the name of the container in the format **OU=** _ContainerName_ **, DC=** _domain_ **, DC=** _com_, where  _ContainerName_ is the name of the OU in AD DS,  _domain_ is the second-level domain, and  _com_ is the top-level domain. 
    
    The application pool identity account for Central Administration must be delegated the **Create, delete, and manage user accounts** task for the container. Access is configured in the properties for the OU in AD DS. 
    
  - In the **SMTP mail server for incoming mail** box, enter the name of the SMTP mail server. The server name must match the FQDN in the A resource record entry for the mail server in DNS Manager. 
    
  - To accept messages only from authenticated users, for **Accept messages from authenticated users only**, select **Yes**; otherwise, select **No**.
    
  - To enable users to create distribution groups from SharePoint sites, for **Allow creation of distribution groups from SharePoint sites**, select **Yes**; otherwise, select **No**.
    
  - Under **Distribution group request approval settings**, select the actions that will require approval. Actions include the following:
    
  - **Create new distribution group**
    
  - **Change distribution group e-mail address**
    
  - **Change distribution group title and description**
    
  - **Delete distribution group**
    
6. If you want to use a remote Directory Management Service, select **Use remote** and complete the remainder of this step. Otherwise, select **No**, and proceed to step 8. 
    
    If you select this option and you are using Exchange Server, you must configure the DNS Manager and add an SMTP connector. For more info, see [Configure DNS Manager](incoming-email-configuration.md#ConfigureDNSManager), [Add an SMTP connector in Microsoft Exchange Server 2016](incoming-email-configuration.md#AddSMTPconnector), and [Add an SMTP connector in Microsoft Exchange Server 2010](incoming-email-configuration.md#AddSMTPcon) later in this article. The AD DS has most likely already been configured, so you do not need to do this. 
    
  - In the **Directory Management Service URL** box, enter the URL of the Directory Management Service that you want to use. The URL is typically in the following format: http://  _server:adminport_/_vti_bin/SharePointEmailWS.asmx.
    
  - In the **SMTP mail server for incoming mail** box, enter the name of the SMTP mail server. The server name must match the FQDN in the A resource record entry for the mail server in DNS Manager on the domain server. 
    
  - To accept messages from authenticated users only, for **Accept messages from authenticated users only**, select **Yes**; otherwise, select **No**.
    
  - To allow creation of distribution groups from SharePoint sites, for **Allow creation of distribution groups from SharePoint sites**, select **Yes**; otherwise, select **No**.
    
7. In the **Incoming E-Mail Server Display Address** section, in the **E-mail server display address** box, enter a display name for the email server (for example, mail.fabrikam.com). You typically use this option together with the Directory Management Service. 
    
    > [!TIP]
    > You can specify the email server address that is displayed when users create an incoming email address for a list or group. Use this setting together with Directory Management Service to provide an email server address that is easy to remember. 
  
8. In the **E-Mail Drop Folder** section, in the **E-mail drop folder** box, type the name of the folder from which the Windows SharePoint Services Timer service retrieves incoming email from the SMTP service. This option is available only if you selected **Advanced** settings mode. If you select this option, ensure that you configure the necessary permissions to the email drop folder. For more information, see [Configure permissions to the email drop folder](incoming-email-configuration.md#ConfigureDropFolderPerms) later in this article. 
    
    It is useful to have a dedicated email drop folder if the default email drop folder is full or almost full. The default location of the drop folder is C:\inetpub\mailroot\drop. You can configure a different location if you want but this drop folder must be the same on all SharePoint Servers.
    
    Ensure that the logon account for the SharePoint Timer service has Modify permissions on the email drop folder.  
    
9. In the **Safe E-Mail Servers** section, select whether you want to accept email from all email servers or from specific email servers. 
    
    This option is available only if you selected **Automatic** settings mode. 
    
10. Select **OK**.
    
After you configure incoming email, site administrators can configure email-enabled lists and document libraries.
  
If you selected Directory Management Service, contact addresses that are created for document libraries appear automatically in Active Directory Users and Computers. The addresses are displayed in the OU of AD DS for SharePoint Server and must be managed by the administrator of AD DS. The AD DS administrator can add more email addresses for each contact. For more information about AD DS, see [AD DS Getting Started](https://go.microsoft.com/fwlink/?linkid=858229). 
  
Alternatively, you can configure the computer running Exchange Server by adding a new Exchange Server Global recipient policy. The policy automatically adds external addresses that use the second-level domain name and not the subdomain or host name for SharePoint Server.
  
## Prepare your environment for incoming email in an advanced scenario
<a name="section5"> </a>

Before you configure incoming email in an advanced scenario, you need to perform additional procedures depending on how you want your incoming email environment to work.
  
If you want to use Directory Management Service, you must first configure AD DS, and if you use Exchange Server, you must also configure the DNS Manager and add an SMTP connector.
  
If you want to use a specific email drop folder, ensure that you configure the necessary permissions to the email drop folder.
  
In this section:
  
- [Configure AD DS to be used with Directory Management Service](incoming-email-configuration.md#ConfigureADDSwithDMS)
    
- [Configure DNS Manager](incoming-email-configuration.md#ConfigureDNSManager)
    
- [Add an SMTP connector in Microsoft Exchange Server 2016](incoming-email-configuration.md#AddSMTPconnector)
    
    [Add an SMTP connector in Microsoft Exchange Server 2010](incoming-email-configuration.md#AddSMTPcon)
    
- [Configure permissions to the email drop folder](incoming-email-configuration.md#ConfigureDropFolderPerms)
    
### Configure AD DS to be used with Directory Management Service
<a name="ConfigureADDSwithDMS"> </a>

If you plan to use Directory Management Service, you should first create an organizational unit (OU) and make the necessary configurations in AD DS.
  
To use Directory Management Service on a SharePoint farm, you must configure the application pool identity account for the SharePoint Central Administration website to have the **Create, delete, and manage user accounts** user right to the container that you specify in AD DS. The preferred way to do this is to assign the right to the application pool identity account for the SharePoint Central Administration website. An AD DS administrator must set up the OU and assign the **Create, delete, and manage user accounts** right to the container. The advantage of using Directory Management Service on a remote server farm is that you do not have to assign rights to the OU for multiple farm service accounts. 
  
The following procedures are performed on a domain controller that runs Windows Server 2008 and Windows Server 2012 R2 with DNS Manager. In some deployments, these applications might run on multiple servers in the same domain.
  
#### To create an OU in AD DS

1. Make sure the user account that is performing this procedure is a member of the Domain Administrators group or a delegated authority for domain administration on the domain controller that is running DNS Manager.
    
2. Open Server Manager, select **Tools**, and then select **Active Directory Users and Computers**.
    
3. In Active Directory Users and Computers, right-click the folder for the second-level domain that contains your server farm, point to **New**, and then select **Organizational Unit**.
    
4. Enter the name of the OU, and then select **OK**.
    
    After you create the OU, you must delegate the **Create, delete, and manage user accounts** right to the container of the OU to manage the user accounts. 
    
#### To delegate the right to the application pool identity account for Central Administration

1. Make sure the user account that is performing this procedure is a member of the Domain Administrators group or the Enterprise Administrators group in AD DS, or a delegated authority for domain administration.
    
2. In Active Directory Users and Computers, right-click the OU that you created, and then select **Delegate control**.
    
3. On the **Welcome** page of the Delegation of Control Wizard, select **Next**.
    
4. On the Users and Groups page, select **Add**, and then enter the name of the application pool identity account that the Central Administration uses.
    
5. In the **Select Users, Computers, and Groups** dialog, select **OK**.
    
6. On the **Users or Groups** page of the Delegation of Control Wizard, select **Next**.
    
7. On the **Tasks to Delegate** page of the Delegation of Control Wizard, select the **Create, delete, and manage user accounts** check box, and then select **Next**.
    
8. On the last page of the Delegation of Control Wizard, to exit the wizard, select **Finish**. 
    
To create and delete child objects, you must also delegate **Create all Child Objects** and **Delete all Child Objects** control of the OU to the application pool identity account for Central Administration. After you complete this procedure, the application pool identity account for Central Administration has **Create all Child Objects** and **Delete all Child Objects** control on the OU, and you can enable incoming email. 
  
#### To delegate Create all Child Objects and Delete all Child Objects control of the OU to the application pool identity account for Central Administration

1. Make sure the user account that is performing this procedure is a member of the Domain Administrators group or the Enterprise Administrators group in AD DS, or a delegated authority for domain administration.
    
2. Right-click the OU, and then select **Delegate control**.
    
3. In the Delegation of Control Wizard, select **Next**.
    
4. Select **Add**, and then enter the name of the application pool identity account for Central Administration, select **OK**, and then select **Next**.
    
5. On the **Tasks to Delegate** page of the Delegation of Control Wizard, select **Create a custom task to delegate**, and then select **Next**.
    
6. Select **This folder, existing objects in this folder, and creation of new objects in this folder**, and then select **Next**.
    
7. In the **Permissions** section, select **Create all Child Objects** and **Delete all Child Objects**, and then select **Next**.
    
8. On the last page of the Delegation of Control Wizard, to exit the wizard, select **Finish**. 
    
Delegating **Create all Child Objects** and **Delete all Child Objects** control of the OU to the application pool identity account for Central Administration enables administrators to enable email for a list. After these controls have been delegated, administrators cannot disable email for the list or document library because the Central Administration account tries to delete the contact from the whole OU instead of from the list. To avoid this problem, you must add **Delete Subtree** permissions for the application pool identity account for Central Administration. Use the following procedure to add these permissions. After this procedure is complete, you can disable incoming email for a list. 
  
#### To add Delete Subtree permissions for the application pool identity account for Central Administration

1. Make sure the user account that is performing this procedure is a member of the Domain Administrators group or the Enterprise Administrators group in AD DS, or a delegated authority for domain administration.
    
2. In Active Directory Users and Computers, select the **View** menu, and then select **Advanced Features**.
    
3. Right-click the OU, and then select **Properties**.
    
4. In the **Properties** dialog, select the **Security** tab, and then select **Advanced**.
    
5. In the **Permission Entries** area, double-click the application pool identity account for Central Administration. 
    
    If the application pool identity account is listed more than once, select the first one.
    
6. In the **Permissions** area, for **Delete Subtree**, select **Allow**.
    
7. Select **OK** three times to close the **Permissions**, **Properties** dialogs, and Active Directory Users and Computers. 
    
After you add these permissions, you must restart IIS for the farm.
  
### Configure DNS Manager
<a name="ConfigureDNSManager"> </a>

If you are using Exchange Server and are routing email internally in your organization, you must create a host (A) resource record in DNS Manager to associate DNS domain names of computers (or hosts) to their IP addresses. Your organization might already have a configured DNS Manager and an A resource record. If not, then use the following procedure.
  
 **<a name="AResourceSubdomain"></a>To create an A resource record for a subdomain**
  
1. Make sure the user account that is performing this procedure is a member of the Administrators group on the local computer.
    
2. In DNS Manager, select the forward lookup zone for the domain that contains the subdomain for SharePoint Server.
    
3. Right-click the zone, and then select **New Host (A or AAAA)**.
    
4. In the **New Host** dialog, in the **Name** text box, enter the host or subdomain name for SharePoint Server. 
    
5. In the **Fully qualified domain name (FQDN)** text box, enter the FQDN for the server that is running SharePoint Server. This is typically in the format  _subdomain.domain.com_.
    
6. Ensure that the domains that are listed under the SMTP server in IIS match the FQDN of the server that receives email. If they do not match, you must create a local domain. For instructions, see [To create a local domain](#CreateALocalDomain) later in this article. 
    
7. In the **IP address** text box, enter the IP address to which you want the FQDN to resolve. 
    
8. Select **Add Host**.
    
9. In the message that confirms the creation of the host record, select **OK**, and in the **New Host** dialog, select **Done**.
    
    The A resource record now appears in DNS Manager. 
    
If you use the **E-mail server display address** option andif the email address to which you are sending email messages is not the same as your server name, you must create a local domain. 
  
 **<a name="CreateALocalDomain"></a>To create a local domain**
  
1. Open Server Manager, select **Tools**, and then select **Internet Information Services (IIS) 6.0 Manager**.
    
2. In IIS Manager, expand the SMTP server, right-click **Domains**, and on the **Action** menu, point to **New**, and then select **Domain**.
    
3. In the **New SMTP Domain Wizard** dialog, select **Alias**, and then select **Next**.
    
4. In the **Domain Name** area, in the **Name** box, enter the address of the mail that is to be received by this domain. 
    
    This address must be the same as the one that you specified in step 4 in [To create an A resource record for a subdomain](#AResourceSubdomain), and in step 6b in [To configure incoming email in an advanced scenario](#ToConfigureEmailAdvanced).
    
5. Select **Finish**.
    
6. In the message that confirms the creation of the host record, select **OK**.
    
7. Restart the SMTP server so that all email messages that are still in the Queue folder move to the Drop folder. The messages are then sent by the Windows SharePoint Services Timer service to their destination list or library.
    
> [!NOTE]
> If you are routing email from outside your organization to an SMTP server, you must use an MX record. For more information, see [Add a mail exchanger (MX) resource record to a zone](https://go.microsoft.com/fwlink/p/?LinkId=150827). 
  
### Add an SMTP connector in Microsoft Exchange Server 2016
<a name="AddSMTPconnector"> </a>

An SMTP connector gives you more controlover the message flow in your organization. Other reasons to use an SMTP connector are to set delivery restrictions or to specify a specific address space. If you use Exchange Server to route incoming email to SharePoint lists and libraries, you must have an SMTP connector so that all mail that is sent to the SharePoint domain uses the servers that are running the SMTP service.
  
Use the following procedure to add an SMTP connector in Exchange Server. After you complete the procedure, the SMTP connector ensures that incoming email messages are sent to the correct list and library in the farm.
  
 **To add an SMTP connector in Exchange Server**
  
1. Verify that the user account that is performing this procedure is a member of the Administrators group on the server that is running Exchange Server.
    
2. In Exchange Admin Center, select **mail flow**, highlight **send connectors**, and to open the new send connector wizard, select the **+** (Add) icon. 
    
3. On the Introduction page, do the following, and then select **Next**. 
    
1. In the **Name** box, enter a name for the SMTP connector. 
    
2. In the **Select the intended use for this Send connector** box, select the **Custom** usage type for the connector. 
    
4. On the **Network settings** page, select **MX record associated with recipient domain**, and then select **Next**.
    
5. On the **Address Space** page, select the **+** (Add) icon, and in the **Address Space** webpage dialog, do the following: 
    
  - In the **Full Qualified Domain Name (FQDN)** box, enter an email domain for the connector. This is the FQDN for the SharePoint Server that runs the SMTP service. 
    
  - In the **Cost** box, assign an appropriate cost. By default, the cost is 1. 
    
6. To return to the **Address Space** page, select **Save**, and then select **Next**.
    
7. On the **Source Server** page, select the **+** (Add) icon. The **Select a Server** page appears.

8. Select **add**, and then select **OK**.

9. On the new send connector wizard, select **Finish**.
    
    The **Source server** page requires a server that contains transport roles.
    
For more info, see [Learn more about Send connector types](https://go.microsoft.com/fwlink/?linkid=858230) in the Exchange Server Technical Library. 
  
### Add an SMTP connector in Microsoft Exchange Server 2010
<a name="AddSMTPcon"> </a>

An SMTP connector gives you more control over the message flow in your organization. Other reasons to use an SMTP connector are to set delivery restrictions or to specify a specific address space. If you use Exchange Server to route incoming email to SharePoint lists and libraries, you must have an SMTP connector so that all mail that is sent to the SharePoint domain uses the servers that are running the SMTP service.
  
Use the following procedure to add an SMTP connector in Exchange Server. After you complete the procedure, the SMTP connector ensures that incoming email messages are sent to the correct list and library in the farm.
  
 **To add an SMTP connector in Exchange Server**
  
1. Verify that the user account that is performing this procedure is a member of the Administrators group on the server that is running Exchange Server.
    
2. In Exchange Management Console, expand the Organization Configuration group, right-click **Hub Transport**, and point to **New Send Connector**.
    
    The **New Send Connector** wizard appears. 
    
3. On the **Introduction** page, do the following and then select **Next**.
    
  - In the **Name** box, enter a name for the SMTP connector. 
    
  - In the **Select the intended use for this Send connector** box, select the **Custom** usage type for the connector. 
    
4. On the **Address Space** page, select **Add**, and then select **SMTP Address Space**.
    
5. In the **SMTP Address Space** dialog, do the following: 
    
  - In the **Address** box, enter an email domain for the connector. 
    
  - In the **Cost** box, assign an appropriate cost. By default, the cost is 1. 
    
6. To return to the Address Space page, select **OK**, and then select **Next**.
    
7. On the **Network settings** page, select **Use domain name system (DNS) "MX" records to route mail automatically**, and then select **Next**.
    
8. On the **Source Server** page, select **Next**.
    
    The **Source server** page only appears on Hub Transport servers. By default, the Hub Transport server that you are currently working on is listed as a source server.
    
9. On the New Connector page, review your options, and to create the new send connector, select **New**. 
    
10. On the **Completion** page, ensure that the send connector was created, and then select **Finish**.
    
    In the **Hub Transport** pane, you can see that the send connector has been enabled automatically.
    
For more info, see [Create an SMTP Send Connector](https://go.microsoft.com/fwlink/p/?LinkId=195321).
  
### Configure permissions to the email drop folder
<a name="ConfigureDropFolderPerms"> </a>

You can specify a particular email drop folder, which enables SharePoint Server to retrieve incoming email from a network share on another server. You can use this option if you do not want to use an SMTP service. However, the drawback of using this option is that SharePoint Server cannot detect configuration changes on the remote email server that is delivering email to the drop folder. The result is that SharePoint Server cannot retrieve email if the location of the email messages has changed. However, this feature is useful if the default email drop folder is full or almost full.
  
If you specified an email drop folder, you must ensure that the application pool identity accounts for Central Administration and for the web application have the required permissions to the email drop folder.
  
#### Configure email drop folder permissions for the application pool identity account for a web application

If your deployment uses different application pool identity accounts for Central Administration and for one or more web applications, each application pool identity account must have permissions to the email drop folder. If the application pool identity account for the web application does not have the required permissions, email will not be delivered to document libraries on that web application.
  
In most cases, when you configure incoming email and select an email drop folder, permissions are added for the following worker process groups:
  
- WSS_Admin_WPG, which includes the application pool identity account for Central Administration and the logon account for the SharePoint Timer service, and has Full Control permissions.
    
- WSS_WPG, which includes the application pool accounts for web applications, and has Read &amp; Execute, List Folder Contents, and Read permissions.
    
In some cases, these groups might not be configured automatically for the email drop folder. For example, if Central Administration is running as the Network Service account, the groups or accounts that are needed for incoming email will not be added when the email drop folder is created. Check to determine whether these groups have been added automatically to the email drop folder. If the groups have not been added automatically, you can add them or add the specific accounts that are required.
  
 **To configure email drop folder permissions for the application pool identity account for a web application**
  
1. Verify that the user account that is performing this procedure is a member of the Administrators group on the server that contains the email drop folder.
    
2. In File Explorer, right-click the drop folder, select **Properties**, and then select the **Security** tab. 
    
3. On the **Security** tab, under the **Group or user names** box, select **Edit**.
    
4. In the **Permissions for Drop** dialog, select **Add**.
    
5. In the **Select Users, Computers, Service Accounts, or Groups** dialog, in the **Enter the object names to select** box, enter the name of the worker process group or application pool identity account for the web application, and then select **OK**.
    
    This account is listed on the **Identity** tab of the **Properties** dialog for the application pool in IIS. 
    
6. In the **Permissions for** _User or Group_ box, next to **Modify**, select **Allow**.
    
7. Select **OK**.
    
#### Configure email drop folder permissions for the logon account for the SharePoint Timer service

Ensure that the logon account for the Windows SharePoint Services Timer service has Modify permissions on the email drop folder. If the logon account for the service does not have Modify permissions, email-enabled document libraries will receive duplicate email messages.
  
 **To configure email drop folder permissions for the logon account for the SharePoint Timer service**
  
1. Verify that the user account that is performing this procedure is a member of the Administrators group on the server that contains the email drop folder.
    
2. In File Explorer, right-click the drop folder, select **Properties**, and then select the **Security** tab. 
    
3. On the **Security** tab, under the **Group or user names** box, select **Edit**.
    
4. In the **Permissions for Drop** dialog, select **Add**.
    
5. In the **Select Users, Computers, Service Accounts, or Groups** dialog, in the **Enter the object names to select** box, enter the name of the logon account for the SharePoint Timer service, and then select **OK**.
    
    This account is listed on the **Log On** tab of the **Properties** dialog box for the service in the Services snap-in. 
    
6. In the **Permissions for** _User or Group_ box, next to **Modify**, select **Allow**.
    
7. Select **OK**.
    
## Are attachments missing from email messages that are sent to a SharePoint document library?
<a name="section6"> </a>

If attachments are missing from email messages that are sent to a SharePoint document library, it might be because you associated the document library with an email address. When you do this, Directory Management Service may not add the following two attributes to the user associated with the email address:
  
- **internet Encoding = 1310720**
    
- **mAPIRecipient = false**
    
You must use Active Directory Service Interfaces (ADSI) to manually add these two missing attributes.
  
On servers that are running Windows Server 2012 R2, Windows Server 2016, Windows Server 2008, or Windows Server 2008 R2, ADSI Edit is installed when you configure a server as a domain controller by installing the AD DS role.
  
 **To add attributes by using ADSI Edit**
  
1. Select **Start**, and then select **Run**.
    
2. In the **Run** dialog, enter **Adsiedit.msc**, and then select **OK**.
    
3. In the **ADSI Edit** window, expand **ADSI Edit**, expand **Domain [DomainName]**, expand **DC=DomainName, DC=com**, and then expand **CN=Users**. 
    
4. Right-click the user name to which you want to add the missing attributes, and then select **Properties**.
    
5. In the **Properties** dialog, on the **Attribute Editor** tab, double-click **Internet Encoding**. 
    
6. In the **Integer Attribute Editor** dialog, enter **1310720** in the **Value** box, and then select **OK**.
    
7. In the **Properties** dialog, on the **Attribute Editor** tab, double-click **mAPIRecipient**. 
    
8. In the **Boolean Attribute Editor** dialog, select **False**, and then select **OK** two times. 
    
## See also
<a name="section6"> </a>

#### Concepts

[Plan incoming email for a SharePoint Server farm](incoming-email-planning.md)

