---
title: "Configure the Secure Store Service in SharePoint Server"
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 7/14/2017
audience: ITPro
ms.topic: get-started-article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 29c0bc76-d835-401b-a2fb-abb069e84125
description: "Configure storage of authorization credentials in Secure Store Service on a SharePoint Server farm."
---

# Configure the Secure Store Service in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
This article describes how to configure the Secure Store Service on a SharePoint Server farm. Secure Store has important planning considerations associated with it. Be sure to read [Plan the Secure Store Service in SharePoint Server](/previous-versions/office/sharepoint-server-2010/ee806889(v=office.14)) before you begin the procedures in this article. 
  
    
## Configure Secure Store in SharePoint Server
<a name="section1"> </a>

The Secure Store service runs under the Application and Front-end server roles. It is autoprovisioned when you create a Secure Store service application.
  
To configure Secure Store, you perform the following steps:
  
1. Register a managed account in SharePoint Server to run the Secure Store application pool.
    
2. Start the Secure Store Service on an application server in the farm. (SharePoint Server 2013 only)
    
3. Create a Secure Store Service service application.
    
To run the application pool, you must have a standard domain account. No specific permissions are required for this account. Once the account has been created in Active Directory, follow these steps to register it with SharePoint Server.
  
 **To register a managed account**
  
1. On the SharePoint Central Administration Web site home page, in the left navigation, click **Security**.
    
2. On the Security page, in the **General Security** section, click **Configure managed accounts**.
    
3. On the Managed Accounts page, click **Register Managed Account**.
    
4. In the **User name** box, type the name of the account. 
    
5. In the **Password** box, type the password for the account. 
    
6. If you want SharePoint Server to handle changing the password for the account, select the **Enable automatic password change** box and specify the password change parameters that you want to use. 
    
7. Click **OK**.
    
If you are using SharePoint Server 2013, you must start the Secure Store Service on an application server in the farm. (If you are using SharePoint Server 2016, the service will be started automatically by MinRole.)
  
 **To start the Secure Store Service (SharePoint Server 2013)**
  
1. On the Central Administration home page, in the **System Settings** section, click **Manage services on server**.
    
2. Above the **Service** list, click the **Server** drop-down list, and then click **Change Server**.
    
3. Select the application server where you want to run the Secure Store Service.
    
4. In the **Service** list, click **Start** next to **Secure Store Service**.
    
Next, you must create a Secure Store Service service application. Use the following procedure to create the service application.
  
 **To create a Secure Store Service service application**
  
1. On the Central Administration home page, in the **Application Management** section, click **Manage service applications**.
    
2. On the Manage Service Applications page, click **New**, and then click **Secure Store Service**.
    
3. In the **Service Application Name** box, type a name for the service application (for example, Secure Store Service).
    
4. In the **Database Server** box, type the instance of SQL Server where you want to create the Secure Store database. 
    
    > [!NOTE]
    > Because the Secure Store database contains sensitive information, we recommend that you deploy the Secure Store database to a different instance of SQL Server from the rest of SharePoint Server. 
  
5. Select the **Create new application pool** option and type a name for the application pool in the text box. 
    
6. Select the **Configurable** option, and, from the drop-down list, select the account for which you created the managed account earlier. 
    
7. Click **OK**.
    
The Secure Store Service has now been configured. The next step is to generate an encryption key for encrypting the Secure Store database.
  
## Work with Secure Store encryption keys
<a name="section2"> </a>

Before using the Secure Store Service, you must generate an encryption key. The key is used to encrypt and decrypt the credentials that are stored in the Secure Store Service database. 
  
### Generate an encryption key

The first time that you access the Secure Store service application, your only option is to generate a new encryption key. Once the key has been generated, the rest of the Secure Store functionality becomes available.
  
 **To generate a new encryption key**
  
1. On the Central Administration home page, in the **Application Management** section, click **Manage service applications**.
    
2. Click the Secure Store service application.
    
3. In the **Key Management** group, click **Generate New Key**.
    
4. On the Generate New Key page, type a pass phrase string in the **Pass Phrase** box, and type the same string in the **Confirm Pass Phrase** box. This pass phrase is used to encrypt the Secure Store database. 
    
    > [!IMPORTANT]
    >  A pass phrase string must be at least eight characters and must have at least three of the following four elements: >  Uppercase characters >  Lowercase characters >  Numerals >  Any of the following special characters >  "! " # $ % &amp; ' ( ) \* + , - . / : ; \< = \> ? @ [ \ ] ^ _ ` { | } ~ 
  
    > [!IMPORTANT]
    > The pass phrase that you enter is not stored. Make sure that you write this down and store it in a safe place. You must have it to refresh the key, such as when you add a new application server to the server farm. 
  
5. Click **OK**.
    
For security precautions or as part of regular maintenance you may decide to generate a new encryption key and force the Secure Store Service to be re-encrypted based on the new key. You can use this same procedure to do this.
  
> [!CAUTION]
> You should back up the database of the Secure Store Service application before generating a new key. 
  
### Refresh the Secure Store encryption key
<a name="refresh"> </a>

Refreshing the encryption key propagates the key to all the application servers in the farm. You may be required to refresh the encryption key if any of the following things are true: 
  
- You add a new application server to the server farm.
    
- You restore a previously backed up Secure Store Service database and have since changed the encryption key.
    
- You receive an "Unable to get master key" error message.
    
 **To refresh the encryption key**
  
1. On the Central Administration home page, in the **Application Management** section, click **Manage service applications**.
    
2. Click the Secure Store service application.
    
3. In the **Key Management** group, click **Refresh Key**.
    
4. In the ** Pass Phrase ** box, type the pass phrase that you first used to generate the encryption key. 
    
    This phrase is either the pass phrase that you used when you initialized the Secure Store Service service application or one that you used when you created a new key by using the **Generate a New Key** command. 
    
5. Click **OK**.
    
## Store credentials in Secure Store
<a name="section3"> </a>

Storing credentials in Secure Store is accomplished by using a Secure Store target application. A target application maps the credentials of a user, group, or claim to a set of encrypted credentials stored in the Secure Store database. After a target application is created, you can associate it with an external content type or application model, or use it with a business intelligence service such as Excel Online or Visio Services to provide access to an external data source. When a SharePoint Server service application calls the target application, Secure Store confirms that the user making the request is an authorized user of the target application and then retrieves the encrypted credentials. The credentials are then used on the user's behalf by the SharePoint Server service application.
  
To create a target application, you must do the following:
  
1. Create the target application itself, specifying the type of credentials that you want to store in the Secure Store database, the administrators for the target application, and the credential owners.
    
2. Specify the credentials that you want to store.
    
### Create a target application
<a name="CreateTargetApp"> </a>

Target applications are configured on the Secure Store Service Application page in Central Administration. Use the following procedure to create a target application.
  
 **To create a target application**
  
1. On the Central Administration home page, in the **Application Management** section, click **Manage service applications**.
    
2. Click the Secure Store service application.
    
3. In the **Manage Target Applications** group, click **New**.
    
4. In the **Target Application ID** box, type a text string. 
    
    This is the unique string that you will use externally to identify this target application.
    
5. In the **Display Name** box, type a text string that will be used to display the identifier of the target application in the user interface. 
    
6. In the **Contact Email** box, type the e-mail address of the primary contact for this target application. 
    
    This can be any legitimate e-mail address and does not have to be the identity of an administrator of the Secure Store Service application.
    
7. When you create a target application of type Individual (see below), you can implement a custom Web page that lets users add individual credentials for the destination data source. This requires custom code to pass the credentials to the target application. If you did this, type the full URL of this page in the **Target Application Page URL** field. There are three options: 
    
  - **Use default page**: Any Web sites that use the target application to access external data will have an individual sign-up page that was added automatically. The URL of this page will be http:/<samplesite>/_layouts/SecureStoreSetCredentials.aspx?TargetAppId=<TargetApplicationID>, where <TargetApplicationID> is the string typed in the **Target Application ID** box. By publicizing the location of this page, you can enable users to add their credentials for the external data source. 
    
  - **Use custom page**: You provide a custom Web page that lets users provide individual credentials. Type the URL of the custom page in this field.
    
  - **None**: There is no sign-up page. Individual credentials are added only by a Secure Store Service administrator who is using the Secure Store Service application.
    
8. In the **Target Application Type** drop-down list, choose the target application type: **Group**, for group credentials, or **Individual**, if each user is to be mapped to a unique set of credentials on the external data source.
    
    > [!NOTE]
    >  There are two primary types for creating a target application: >  Group, for mapping all the members of one or more groups to a single set of credentials on the external data source. >  Individual, for mapping each user to a unique set of credentials on the external data source. 
  
9. Click **Next**.
    
10. Use the **Specify the credential fields for your Secure Store Target Application** page to configure the various fields which may be required to provide credentials to the external data source. By default, two fields are listed: **Windows User Name** and **Windows Password**.
    
    To add an additional field for supplying credentials to the external data source, on the **Specify the credential fields for your Secure Store Target Application** page, click **Add Field**.
    
    By default, the type of the new field is **Generic**. The following field types are available:
    
|**Field**|**Description**|
|:-----|:-----|
|**Generic** <br/> |Values that do not fit in any of the other categories.  <br/> |
|**User Name** <br/> |A user account that identifies the user.  <br/> |
|**Password** <br/> |A secret word or phrase.  <br/> |
|**PIN** <br/> |A personal identification number.  <br/> |
|**Key** <br/> |A parameter that determines the functional output of a cryptographic algorithm or cipher.  <br/> |
|**Windows User Name** <br/> |A Windows user account that identifies the user.  <br/> |
|**Windows Password** <br/> |A secret word or phrase for a Windows account.  <br/> |
|**Certificate** <br/> |A certificate.  <br/> |
|**Certificate Password** <br/> |The password for the certificate.  <br/> |
   
  - To change the type of a new or existing field, click the arrow that appears next to the type of the field, and then select the new type of field.
    
    > [!NOTE]
    > Every field that you add will be required to have data when you set the credentials for this target application. 
  
  - You can change the name that a user sees when interacting with a field. In the **Field Name** column of the **Specify the credential fields for your Secure Store Target Application** page, change a field name by selecting the current text and typing new text. 
    
  - When a field is masked, each character that a user types is not displayed but is replaced with a mask character such as the asterisk "*". To mask a field, click the check box for that field in the **Masked** column of the page. 
    
  - To delete a field, click the delete icon for that field in the **Delete** column of the page. 
    
    When you have finished editing the credential fields, click **Next**.
    
11. In the **Specify the membership settings** page, in the **Target Application Administrators Field**, list all users who have access to manage the target application settings. 
    
12. If the target application type is group, in the **Members** field, list the user groups to map to a set of credentials for this target application. 
    
13. Click **OK** to complete configuring the target application. 
    
### Set credentials for a Secure Store target application
<a name="section4"> </a>

After creating a target application, an administrator of that target application can set credentials for it. These credentials are used by the calling application to provide access to an external data source. If the target application is of type Individual, you can also enable users to supply their own credentials.
  
 **To set credentials for a target application**
  
1. On the Central Administration home page, in the **Application Management** section, click **Manage service applications**.
    
2. Click the Secure Store service application.
    
3. In the target application list, point at the target application for which you want to set credentials, click the arrow that appears, and then, in the menu, click **Set credentials**.
    
    If the target application is of type Group, type the credentials for the external data source. Depending on the information that is required by the external data source, the fields for setting credentials will vary.
    
    If the target application is of type Individual, type the user name of the individual who will be mapped to this set of credentials on the external data source, and type the credentials for the external data source. Depending on the information that is required by the external data source, the fields for setting credentials will vary.
    
4. Click **OK**.
    
Once you have set the credentials for the target application, it is ready to be used by a SharePoint Server service such as Business Connectivity Services, Excel Services, or Visio Services.
  
## Enable the Secure Store audit log
<a name="section5"> </a>

Audit entries for the Secure Store service are stored in the Secure Store Service database. By default, the audit log file is disabled.
  
An audit log entry stores information about a Secure Store Service action, such as when it was performed, whether it succeeded, why it failed if it didn't succeed, the Secure Store Service user who performed it, and optionally the Secure Store Service user on whose behalf it was performed. Therefore, a valid reason to enable an audit log file is to troubleshoot an authentication issue. 
  
 **To enable the audit log by using Central Administration**
  
1. On the Central Administration home page, in the **Application Management** section, click **Manage service applications**.
    
2. Select the Secure Store service application. (That is, select the service application, but do not click the link to go to the Secure Store Service application settings page.)
    
3. On the ribbon, click **Properties**.
    
4. From the **Enable Audit** section, click to select the **Audit log enabled** box. 
    
5. To change the number of days that entries will be purged from the audit log file, specify a number in days in the **Days Until Purge** field. The default value is 30 days. 
    
6. Click **OK**.
    
## See also
<a name="section5"> </a>

#### Other Resources

[Secure Store Service cmdlets in SharePoint 2013](/powershell/module/sharepoint-server/?view=sharepoint-ps)

