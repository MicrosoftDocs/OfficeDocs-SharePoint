---
title: "Configure SQL Server security for SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
audience: ITPro
ms.topic: get-started-article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 2c727311-e83e-4f7b-b02c-9a0699a81e64
description: "Learn how to improve the security of SQL Server for SharePoint Server environments."
---

# Configure SQL Server security for SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-SPO-md](../includes/appliesto-2013-2016-2019-SPO-md.md)]
  
When you install SQL Server, the default settings help to provide a safe database. In addition, you can use SQL Server tools and Windows Firewall to add additional security to SQL Server for SharePoint Server environments. 
  
> [!IMPORTANT]
> The security steps in this topic are fully tested by the SharePoint team. There are other ways to help secure SQL Server in a SharePoint Server farm. For more information, see [Securing SQL Server](https://go.microsoft.com/fwlink/?linkid=865827). 
  
    
## Before you begin
<a name="begin"> </a>

Before you begin this operation, review the following tasks about how to secure your server farm:
  
- Block UDP port 1434.
    
- Configure named instances of SQL Server to listen on a nonstandard port (other than TCP port 1433 or UDP port 1434).
    
- For additional security, block TCP port 1433 and reassign the port that is used by the default instance to a different port.
    
- Configure SQL Server client aliases on all front-end web servers and application servers in the server farm. After you block TCP port 1433 or UDP port 1434, SQL Server client aliases are necessary on all computers that communicate with the computer that is running SQL Server.
    
## Configuring a SQL Server instance to listen on a non-default port
<a name="proc1"> </a>

SQL Server provides the ability to reassign the ports that are used by the default instance and any named instances. In SQL Server Service Pack 1 (SP1), you reassign the TCP port by using SQL Server Configuration Manager. When you change the default ports, you make the environment more secure against hackers who know default assignments and use them to exploit your SharePoint environment.
  
 **To configure a SQL Server instance to listen on a non-default port**
  
1. Verify that the user account that is performing this procedure is a member of either the sysadmin or the serveradmin fixed server role.
    
2. On the computer that is running SQL Server, open SQL Server Configuration Manager.
    
3. In the navigation pane, expand **SQL Server Network Configuration**.
    
4. Click the corresponding entry for the instance that you are configuring.
    
    The default instance is listed as **Protocols for MSSQLSERVER**. Named instances will appear as **Protocols for named_instance**.
    
5. In the main window in the **Protocol Name** column, right-click **TCP/IP**, and then click **Properties**.
    
6. Click the **IP Addresses** tab. 
    
    For every IP address that is assigned to the computer that is running SQL Server, there is a corresponding entry on this tab. By default, SQL Server listens on all IP addresses that are assigned to the computer.
    
7. To globally change the port that the default instance is listening on, follow these steps:
    
   - For each IP address except **IPAll**, clear all values for both **TCP dynamic ports** and **TCP Port**.
    
   - For **IPAll**, clear the value for **TCP dynamic ports**. In the **TCP Port** field, enter the port that you want the instance of SQL Server to listen on. For example, enter 40000. 
    
8. To globally change the port that a named instance is listening on, follow these steps:
    
   - For each IP address including **IPAll**, clear all values for **TCP dynamic ports**. A value of 0 for this field indicates that SQL Server uses a dynamic TCP port for the IP address. A blank entry for this value means that SQL Server will not use a dynamic TCP port for the IP address.
    
   - For each IP address except **IPAll**, clear all values for **TCP Port.**
    
   - For **IPAll**, clear the value for **TCP dynamic ports**. In the **TCP Port** field, enter the port that you want the instance of SQL Server to listen on. For example, enter 40000. 
    
9. Click **OK**. 
    
    A message indicates that the change will not take effect until the SQL Server service is restarted. Click **OK**.
    
10. Close SQL Server Configuration Manager.
    
11. Restart the SQL Server service and confirm that the computer that is running SQL Server is listening on the port that you selected. 
    
    You can confirm this by looking in the Event Viewer log after you restart the SQL Server service. Look for an information event similar to the following event:
    
    Event Type:Information
    
    Event Source:MSSQL$MSSQLSERVER
    
    Event Category:(2)
    
    Event ID:26022
    
    Date:3/6/2008
    
    Time:1:46:11 PM
    
    User:N/A
    
    Computer: _computer_name_
    
    Description:
    
    Server is listening on [ 'any' \<ipv4\>50000]
    
12. **Verification:** Optionally, include steps that users should perform to verify that the operation was successful. 
    
## Blocking default SQL Server listening ports
<a name="proc2"> </a>

Windows Firewall with Advanced Security uses Inbound Rules and Outbound Rules to help secure incoming and outgoing network traffic. Because Windows Firewall blocks all incoming unsolicited network traffic by default, you do not have to explicitly block the default SQL Server listening ports. For more information, see [Windows Firewall with Advanced Security](http://go.microsoft.com/fwlink/p/?LinkID=718056&amp;clcid=0x409) and [Configuring the Windows Firewall to Allow SQL Server Access](http://go.microsoft.com/fwlink/p/?LinkID=718059&amp;clcid=0x409).
  
## Configuring Windows Firewall to open manually assigned ports
<a name="proc3"> </a>

To access a SQL Server instance through a firewall, you must configure the firewall on the computer that is running SQL Server to allow access. Any ports that you manually assign must be open in Windows Firewall.
  
 **To configure Windows Firewall to open manually assigned ports**
  
1. Verify that the user account that is performing this procedure is a member of either the sysadmin or the serveradmin fixed server role.
    
2. In **Control Panel**, open **System and Security**.
    
3. Click **Windows Firewall**, and then click **Advanced Settings** to open the **Windows Firewall with Advanced Security** dialog box. 
    
4. In the navigation pane, click **Inbound Rules** to display the available options in the **Actions** pane. 
    
5. Click **New Rule** to open the **New Inbound Rule Wizard**.
    
6. Use the wizard to complete the steps that are required to allow access to the port that you defined in [Configuring a SQL Server instance to listen on a non-default port](#proc1).
    
    > [!NOTE]
    > You can configure the Internet Protocol security (IPsec) to help secure communication to and from your computer that is running SQL Server by configuring the Windows firewall. You do this by selecting **Connection Security Rules** in the navigation pane of the Windows Firewall with Advanced Security dialog box. 
  
## Configuring SQL Server client aliases
<a name="proc4"> </a>

If you block UDP port 1434 or TCP port 1433 on the computer that is running SQL Server, you must create a SQL Server client alias on all other computers in the server farm. You can use SQL Server client components to create a SQL Server client alias for computers that connect to SQL Server.
  
 **To configure a SQL Server client alias**
  
1. Verify that the user account that is performing this procedure is a member of either the sysadmin or the serveradmin fixed server role.
    
2. Run Setup for SQL Server on the target computer, and install the following client components:
    
   - **Connectivity Components**
    
   - **Management Tools**
    
3. Open SQL Server Configuration Manager.
    
4. In the navigation pane, click **SQL Native Client Configuration**.
    
5. In the main window under Items, right-click **Aliases**, and select **New Alias**.
    
6. In the **Alias - New** dialog box, in the **Alias Name** field, enter a name for the alias. For example, enter SharePoint  __alias_.
    
7. In the **Port No** field, enter the port number for the database instance. For example, enter 40000. Make sure that the protocol is set to TCP/IP. 
    
8. In the **Server** field, enter the name of the computer that is running SQL Server. 
    
9. Click **Apply**, and then click **OK**.
    
10. **Verification:** You can test the SQL Server client alias by using SQL Server Management Studio, which is available when you install SQL Server client components. 
    
11. Open SQL Server Management Studio.
    
12. When you are prompted to enter a server name, enter the name of the alias that you created, and then click **Connect**. If the connection is successful, SQL ServerManagement Studio is populated with objects that correspond to the remote database.
    
13. To check connectivity to additional database instances from SQL ServerManagement Studio, click **Connect**, and then click **Database Engine**.
    
## See also
<a name="proc4"> </a>

#### Other Resources

[SQL Server Security Blog](https://blogs.msdn.microsoft.com/sqlsecurity/)

[SQL Vulnerability Assessment](/sql/relational-databases/security/sql-vulnerability-assessment?view=sql-server-2017)
  
[Securing SharePoint: Harden SQL Server in SharePoint Environments](https://blogs.technet.com/b/rycampbe/archive/2013/10/14/securing-sharepoint-harden-sql-server-in-sharepoint-environments.aspx)
  
[Configure a Windows Firewall for Database Engine Access](http://go.microsoft.com/fwlink/p/?LinkID=718060&amp;clcid=0x409)
  
[Configure a Server to Listen on a Specific TCP Port (SQL Server Configuration Manager)](http://go.microsoft.com/fwlink/p/?LinkID=718061&amp;clcid=0x409)

