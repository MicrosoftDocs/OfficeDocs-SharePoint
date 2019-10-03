---
title: "Claims authentication does not validate user in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 9/20/2017
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: c1bbb68a-f682-40cf-870f-d32219676e6e
description: "Because SharePoint Server recommends claims-based authentication for user access to web applications, this article describes the tools and techniques that you can use to troubleshoot failed claims-based user authentication attempts."
---

# Claims authentication does not validate user in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
  
When users try to connect to a web application, logs record failed authentication events. If you use tools that Microsoft provides and use a systematic approach to examine failures, you can learn about common issues that relate to claims-based authentication and resolve them.
  
Successful access to a SharePoint resource requires both authentication and authorization. When you are using claims, authentication verifies that the security token is valid. Authorization verifies that access to the resource is allowed, based on the set of claims in the security token and the configured permissions for the resource.
  
To determine whether authentication or authorization causes an access issue, look closely at the error message in the browser window.
  
- If the error message indicates that the user does not have access to the site, then the authentication was successful and the authorization failed. To troubleshoot authorization, try the following solutions:
    
  - The most common reason for failed authorization when you are using Security Assertion Markup Language (SAML) claims-based authentication is that the permissions were assigned to a user's Windows-based account (domain\user) instead of the user's SAML identity claim.
    
  - Verify that the user or a group to which the user belongs has been configured to use the appropriate permissions. For more information, see [User permissions and permission levels in SharePoint Server](/previous-versions/office/sharepoint-server-2010/cc721640(v=office.14)).
    
  - Use the tools and techniques in this article to determine the set of claims in the user's security token so that you can compare it with the configured permissions.
    
- If the message indicates that authentication failed, you have an authentication problem. If the resource is contained within a SharePoint web application that uses claims-based authentication, use the information in this article to start troubleshooting.
    
## Troubleshooting tools

The following are the primary troubleshooting tools that Microsoft provides to collect information about claims authentication in SharePoint Server:
  
- Use **Unified Logging System (ULS) logs** to obtain the details of authentication transactions. 
    
- Use **Central Administration** to verify the details of user authentication settings for SharePoint web applications and zones and configure levels of ULS logging. 
    
- If you are using Active Directory Federation Services 2.0 (AD FS) as your federation provider for Security Assertion Markup Language (SAML)-based claims authentication, you can use **AD FS logging** to determine the claims that are in security tokens that AD FS issues to web client computers. 
    
- Use **Network Monitor 3.4** to capture and examine the details of user authentication network traffic. 
    
### Setting the level of ULS logging for user authentication

The following procedure configures SharePoint Server to log the maximum amount of information for claims authentication attempts.
  
 **To configure SharePoint Server for the maximum amount of user authentication logging**
  
1. From Central Administration, click **Monitoring** on the Quick Launch, and then click **Configure diagnostic logging**.
    
2. In the list of categories, expand **SharePoint Foundation**, and then select **Authentication Authorization** and **Claims Authentication**.
    
3. In **Least critical event to report to the event log**, select **Verbose**.
    
4. In **Least critical event to report to the trace log**, select **Verbose**.
    
5. Click **OK**.
    
To optimize performance when you are not performing claims authentication troubleshooting, follow these steps to set user authentication logging to its default values.
  
 **To configure SharePoint Server for the default amount of user authentication logging**
  
1. From Central Administration, click **Monitoring** on the Quick Launch, and then click **Configure diagnostic logging**.
    
2. In the list of categories, expand **SharePoint Foundation**, and then select **Authentication Authorization** and **Claims Authentication**.
    
3. In **Least critical event to report to the event log**, select **Information**.
    
4. In **Least critical event to report to the trace log**, select **Medium**.
    
5. Click **OK**.
    
### Configuring AD FS logging

Even after you enable the maximum level of ULS logging, SharePoint Server doesn't record the set of claims in a security token that it receives. If you use AD FS for SAML-based claims authentication, you can enable AD FS logging and use Event Viewer to examine the claims for security tokens that SharePoint Server issues.
  
 **To enable AD FS logging**
  
1. On the AD FS server, from Event Viewer, click **View**, and then click **Show Analytic and Debug Logs**.
    
2. In the Event Viewer console tree, expand **Applications and Services Logs/AD FS 2.0 Tracing**.
    
3. Right-click **Debug**, and then click **Enable Log**.
    
4. Open the %ProgramFiles% **\Active Directory Federation Services 2.0** folder. 
    
5. Use Notepad to open the **Microsoft.IdentityServer.ServiceHost.Exe.Config** file. 
    
6. Click **Edit**, click **Find**, type **\<source name="Microsoft.IdentityModel" switchValue="Off"\>**, and then click **OK**.
    
7. Change **switchValue="Off"** to **switchValue="Verbose"**.
    
8. Click **File**, click **Save**, and then exit Notepad.
    
9. From the Services snap-in, right-click the ** AD FS 2.0 service **, and then click **Restart**.
    
You can now use Event Viewer on the AD FS server to examine details about claims from the Applications and Services Logs/AD FS 2.0 Tracing/Debug node. Look for events with Event ID 1001.
  
You can also enumerate claims with an HttpModule or web part or through OperationContext. For more information, see [How to Get All User Claims at Claims Augmentation Time in SharePoint 2010](https://go.microsoft.com/fwlink/p/?LinkId=275447). This information about SharePoint 2010 applies also to SharePoint 2013.
  
## Troubleshooting methodology for claims user authentication

The following steps can help you determine the cause of failed claims authentication attempts.
  
### Step 1: Determine the details of the failed authentication attempt

To obtain detailed and definitive information about a failed authentication attempt, you have to find it in the SharePoint ULS logs. These log files are stored in the %CommonProgramFiles%\Microsoft Shared\Web Server Extensions\15\LOGS folder.
  
You can find the failed authentication attempt in the ULS log files either manually or you can use the ULS Log Viewer.
  
 **To find the failed authentication attempt manually**
  
1. Obtain the user account name that produces the failed authentication attempt from the user.
    
2. On the server that is running SharePoint Server or SharePoint Foundation, find the %CommonProgramFiles% **\Microsoft Shared\Web Server Extensions\16\LOGS** or %CommonProgramFiles% **\Microsoft Shared\Web Server Extensions\15\LOGS** folder. 
    
3. In the **LOGS** folder, click **Date modified** to sort the folder by date, with the most recent at the top. 
    
4. Try the authentication task againl
    
5. In the **LOGS** folder window, double-click the log file at the top of the list to open the file in Notepad. 
    
6. In **Notepad**, click **Edit,** click **Find**, type **Authentication Authorization** or **Claims Authentication**, and then click **Find Next**.
    
7. Click **Cancel**, and then read the contents of the **Message** column. 
    
To use the ULS Viewer, download it from [ULS Viewer](https://www.microsoft.com/en-us/download/details.aspx?id=44020) and save it to a folder on the server that is running SharePoint Server or SharePoint Foundation. After it is installed, follow these steps to locate the failed authentication attempt. 
  
 **To find the failed authentication attempt with the ULS Viewer**
  
1. On the server that is running SharePoint Server or SharePoint Foundation, double-click **Ulsviewer** from the folder in which it is stored. 
    
2. In the **ULS Viewer**, click **File**, point to **Open From**, and then click **ULS**.
    
3. In the **Setup the ULS Runtime feed** dialog box, verify that %CommonProgramFiles% **\Common Files\Microsoft Shared\Web Server Extensions\16\LOGS folder** or **\Common Files\Microsoft Shared\Web Server Extensions\15\LOGS folder** is specified in **Use ULS feed from default log-file directory**. If not, click **Use directory location for real-time feeds** and specify the %CommonProgramFiles% **\Microsoft Shared\Web Server Extensions\16\LOGS folder** or **\Microsoft Shared\Web Server Extensions\15\LOGS folder** in **Log file location**.
    
    For %CommonProgramFiles%, substitute the value from the CommonProgramFiles environment variable of the server that is running SharePoint Server or SharePoint Foundation. For example, if the location is the C drive, %CommonProgramFiles% is set to C:\Program Files\Common Files.
    
4. Click **OK**.
    
5. Click **Edit**, and then click **Modify Filter**.
    
6. In the **Filter by** dialog box, in **Field**, click **Category**.
    
7. In **Value**, type **Authentication Authorization** or **Claims Authentication**, and then click **OK**.
    
8. Repeat the authentication attempt.
    
9. From the **ULS Viewer** window, double-click the displayed lines to view the **Message** portion. 
    
From the claims encoding part of the Message portion for non-OAuth requests, you can determine the authentication method and encoded user identity from the claims-encoded string (example: i:0#.w|contoso\chris). For more information, see [SharePoint 2013 and SharePoint 2010 claims encoding](https://go.microsoft.com/fwlink/p/?LinkId=275449).
  
### Step 2: Check configuration requirements

To determine how a web application or zone is configured to support one or more claims authentication methods, use the SharePoint Central Administration website.
  
 **To verify the authentication configuration for a web application or zone**
  
1. From Central Administration, click **Application Management** on the Quick Launch, and then click **Manage web applications**.
    
2. Click the name of the web application that the user is trying to access, and in the **Security** group of the ribbon, click **Authentication Providers**.
    
3. In the list of authentication providers, click the appropriate zone (such as **Default**).
    
4. In the **Edit Authentication** dialog box, in the **Claims Authentication Types** section, verify the settings for claims authentication. 
    
  - For Windows claims authentication, verify that **Enable Windows Authentication** and **Integrated Windows authentication** are selected, and that either **NTLM** or **Negotiate (Kerberos)** is selected as needed. Select **Basic authentication** if it is needed. 
    
  - For forms-based authentication, verify that **Enable Forms Based Authentication (FBA)** is selected. Verify the values in **ASP.NET Membership provider name** and **ASP.NET Role manager name**. These values must match the membership provider and role values that you configured in your web.config files for the the SharePoint Central Administration website, web application, and SharePoint Web Services\SecurityTokenServiceApplication. For more information, see [Configure forms-based authentication for a claims-based web application in SharePoint Server](/previous-versions/office/sharepoint-server-2010/ee806890(v=office.14)).
    
  - For SAML-based claims authentication, verify that **Trusted identity provider** and the correct trusted provider name are selected. For more information, see [Configure SAML-based claims authentication with AD FS in SharePoint Server](/previous-versions/office/sharepoint-server-2010/hh305235(v=office.14)).
    
  - In the **Sign In Page URL** section, verify the option for the sign-in page. For a default sign-in page, **Default Sign In Page** should be selected. For a custom sign-in-page, verify the specified URL of the custom sign-in page. To verify it, copy the URL, and then attempt to access it using a web browser. 
    
5. Click **Save** to save the changes to the authentication settings. 
    
6. Repeat the authentication attempt. For forms-based or SAML-based authentication, does the expected sign-in page appear with the correct sign-in options?
    
7. If authentication still fails, check the ULS logs to determine whether there is any difference between the authentication attempt before the authentication configuration change and after it.
    
### Step 3: Additional items to check

After you check the log files and web application configuration, verify the following:
  
- The web browser on the web client computer supports claims. For more information, see [Plan browser support in SharePoint Server 2016](../install/browser-support-planning-0.md).
    
- For Windows claims authentication, verify that the following:
    
  - The computer from which the user issues the authentication attempt is a member of the same domain as the server that hosts the SharePoint web application or a member of a domain that the hosting server trusts.
    
  - The computer from which the user issues the authentication attempt is logged on to its Active Directory Domain Services (AD DS) domain. Type **nltest /dsgetdc: /force** at a Command Prompt or the SharePoint Management Shell on the web client computer to make sure that it can access a domain controller. If no domain controllers are listed, troubleshoot the lack of discoverability and connectivity between the web client computer and an AD DS domain controller. 
    
  - The server that is running SharePoint Server or SharePoint Foundation is logged on to its AD DS domain. Type **nltest /dsgetdc: /force** at a Command Prompt or the SharePoint Management Shell on the server that is running SharePoint Server or SharePoint Foundation to make sure that it can access a domain controller. If no domain controllers are listed, troubleshoot the lack of discoverability and connectivity between the server that is running SharePoint Server or SharePoint Foundation and an AD DS domain controller. 
    
- For forms-based authentication, verify that the following:
    
  - The user credentials for the configured ASP.NET membership and role provider are correct.
    
  - The systems that host the ASP.NET membership and role provider are available on the network.
    
  - Custom sign-in pages correctly collect and convey the user's credentials. To test this, configure the web application to temporarily use the default sign-in page and verify that it works.
    
- For SAML-based claims authentication, verify that the following:
    
  - The user credentials for the configured identity provider are correct.
    
  - Systems that act as the federation provider (such as AD FS) and the identity provider (such as AD DS or a third-party identity provider) are available on the network.
    
  - Custom sign-in pages correctly collect and convey the user's credentials. To test this, configure the web application to temporarily use the default sign-in page and verify that it works.
    
### Step 4: Use a web debug tool to monitor and analyze web traffic

Use a tool such as [HttpWatch](https://go.microsoft.com/fwlink/p/?LinkId=275459) or [Fiddler](https://go.microsoft.com/fwlink/p/?LinkId=154773) to analyze the following types of HTTP traffic: 
  
- Between the web client computer and the server that is running SharePoint Server or SharePoint Foundation
    
    For example, you can monitor the HTTP Redirect messages that the server that is running SharePoint Server or SharePoint Foundation sends to inform the web client computer of the location of a federation server (such as AD FS).
    
- Between the web client computer and the federation server (such as AD FS)
    
    For example, you can monitor the HTTP messages that the web client computer sends and the responses of the federation server, which could include security tokens and their claims.
    
> [!NOTE]
> If you use Fiddler, the authentication attempt can fail after requiring three authentication prompts. To prevent this behavior, see [Using Fiddler With SAML and SharePoint to Get Past the Three Authentication Prompts](https://go.microsoft.com/fwlink/p/?LinkId=276792). 
  
### Step 5: Capture and analyze authentication network traffic

Use a network traffic tool, such as [Network Monitor 3.4](https://www.microsoft.com/en-us/download/details.aspx?id=4865), to capture and analyze traffic between the web client computer, the server that is running SharePoint Server or SharePoint Foundation, and the systems on which SharePoint Server or SharePoint Foundation relies for claims authentication. 
  
> [!NOTE]
> In many cases, claims authentication uses Hypertext Transfer Protocol Secure (HTTPS)-based connections, which encrypt the messages sent between computers. You cannot see the contents of encrypted messages with a network traffic tool without the aid of an add-in or extension. For example, for Network Monitor, you must install and configure the [Network Monitor Decryption Expert](https://go.microsoft.com/fwlink/p/?LinkId=276793). As an easier alternative to attempting to decrypt HTTPS messages, use a tool such as Fiddler on the server that hosts SharePoint Server or SharePoint Foundation, which can report on the unencrypted HTTP messages. 
  
An analysis of the network traffic can reveal the following:
  
- The exact set of protocols and messages that are being sent between the computers involved in the claims authentication process. Reply messages can contain error condition information, which you can use to determine additional troubleshooting steps.
    
- Whether request messages have corresponding replies. Multiple sent request messages that do not receive a reply can indicate that the network traffic is not reaching its intended destination. In that case, check for packet routing issues, packet filtering devices in the path (such as a firewall), or packet filtering on the destination (such as a local firewall).
    
- Whether multiple claims methods are being tried, and which are failing.
    
For Windows claims authentication, you can capture and analyze the traffic between the following computers:
  
- The web client computer and the server that is running SharePoint Server or SharePoint Foundation
    
- The server that is running SharePoint Server or SharePoint Foundation and its domain controller
    
For forms-based authentication, you can capture and analyze the traffic between the following computers:
  
- The web client computer and the server that is running SharePoint Server or SharePoint Foundation
    
- The server that is running SharePoint Server or SharePoint Foundation and the ASP.NET membership and role provider
    
For SAML-based claims authentication, you can capture and analyze the traffic between the following computers:
  
- The web client computer and the server that is running SharePoint Server or SharePoint Foundation
    
- The web client computer and its identity provider (such as an AD DS domain controller)
    
- The web client computer and the federation provider (such as AD FS)
    
## See also

#### Other Resources

[Configure forms-based authentication for a claims-based web application in SharePoint Server](/previous-versions/office/sharepoint-server-2010/ee806890(v=office.14))
  
[Configure SAML-based claims authentication with AD FS in SharePoint Server](/previous-versions/office/sharepoint-server-2010/hh305235(v=office.14))

