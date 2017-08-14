---
title: Configure and use the Documentum connector in SharePoint Server
ms.prod: SHAREPOINT
ms.assetid: b17a56ea-2e7f-43c6-9a17-00ae1f5c4089
---


# Configure and use the Documentum connector in SharePoint Server
 **We are in the process of combining the SharePoint Server 2013 and SharePoint Server 2016 content into a single content set. We appreciate your patience while we reorganize things. See the Applies To tag at the top of each article to find out which version of SharePoint an article applies to.** * **Applies to:** SharePoint Server 2013, SharePoint Server 2016*  * **Topic Last Modified:** 2017-07-14* This article describes how to install and configure the Microsoft SharePoint Server 2016 Indexing Connector for Documentum.The Microsoft SharePoint Server 2016 Indexing Connector for Documentum enables you to index content that is stored in the EMC Documentum system. This article describes how to install and configure the Indexing Connector for Documentum for use with SharePoint Server 2016.The Indexing Connector for Documentum:
- Is a 64-bit connector based on the SharePoint Server 2016 Search Connector Framework.
    
  
- Supports multiple versions of EMC Documentum Content Server. 
    
  
- Indexes Documentum objects and object metadata. See  [Supported and unsupported Documentum object types and properties in SharePoint Server](html/supported-and-unsupported-documentum-object-types-and-properties-in-sharepoint-s.md).
    
  
- Supports Documentum security definitions and policies.
    
  
- Supports Microsoft PowerShell for automated configuration and administration. See  [Using the SPEnterpriseSearchDCTMConnectorConfig cmdlet](#DCTM_cmdlet).
    
  
- Has a configurable search results URL to support multiple Documentum client applications.
    
  
- Supports file and folder exclusion for crawling. 
    
  
In this article:
-  [Before you begin](#begin)
    
  
-  [Overview](#DCTM_Overview)
    
  
-  [Prepare the SharePoint 2013 servers that host a crawl component](#DCTM_PrepareCrawlServer)
    
  
-  [Install and register the Indexing Connector for Documentum](#DCTM_InstallCon)
    
  
-  [Configure the Indexing Connector for Documentum](#DCTM_ConfigureConn)
    
  
-  [Create the Documentum crawled properties category](#BKMK_CrawledPropertiesCategory)
    
  
-  [Create a crawl rule for Documentum](#DCTM_Crawl_rule)
    
  
-  [Create a Documentum content source](#DCTM_Content_source)
    
  
-  [Using the SPEnterpriseSearchDCTMConnectorConfig cmdlet](#DCTM_cmdlet)
    
  

## Before you begin
<a name="begin"> </a>

Before you begin this operation, review the following system prerequisites and requirements:
- The supported operating systems are Windows Server 2008 R2, Windows Server 2008 Service Pack 2, and Windows Server 2012.
    
  
- One of the following SharePoint 2016 Products is installed and configured: 
    
  - Microsoft SharePoint Server 2016 Enterprise
    
  
  - Microsoft SharePoint Server 2016 Standard
    
  
- A Search service application is installed and configured. 
    
  
- A Documentum Foundation Services (DFS) Server with a version that is compatible with DFS Productivity Layer 6.7 SP2 is installed on a Windows host. 
    
  
- DFS Productivity Layer 6.7 SP2 is installed and you have access to the .NET assemblies that are included in the DFS Productivity Layer 6.7 SP2. The Indexing Connector for Documentum uses DFS as the connectivity API to access Documentum repositories. 
    
  
- Documentum Content Server is installed. The supported versions of Documentum Content Server are determined by DFS 6.7 SP2. You can find a detailed list in the DFS Productivity Layer 6.7 SP2 release notes. You can download the release notes from the EMC customer support site  [https://powerlink.emc.com](https://powerlink.emc.com).
    
  
- Configure the Indexing Connector for Documentum with  *-ACLTranslation "Claims"*  if you have to crawl Documentum repositories that have Documentum Trusted Content Services (TCS) enabled. You can also use this connector configuration to enable automatic mapping between Windows Active Directory users and Documentum users, regardless of whether the repository has TCS enabled.
    
  

## Overview
<a name="DCTM_Overview"> </a>

The following steps provide a high-level overview of the tasks that are involved to install and configure the Indexing Connector for Documentum for use with SharePoint Server 2016. 
1. Preparation:
    
1. Ensure that your system meets the system prerequisites and requirements in the section  [Before you begin](#begin).
    
  
2. Download the SharePoint Server 2016 Indexing Connector for Documentum from the  [Microsoft Download Center](https://go.microsoft.com/?linkid=9826867).
    
  
3.  [Decide which Documentum content access account to use for crawling](#DCTM_ContentAccess).
    
  
4.  [Prepare the SharePoint Server 2016 servers that host a crawl component](#DCTM_PrepareCrawlServer). On each server:
    
1.  [Set the DFS Productivity Layer .NET assemblies](#DCTM_Assemblies).
    
  
2.  [Edit the machine.config file](#DCTM_machineconfig) to set the Documentum bindings.
    
  
2. Install the Indexing Connector for Documentum.
    
1.  [Install the Indexing Connector for Documentum](#DCTM_Deployconn) on each SharePoint Server 2016 server in the farm that hosts a crawl component.
    
  
2.  [Register the Indexing Connector for Documentum to the Search service application](#DCTM_Registerconn) by using Microsoft PowerShell.
    
  
3.  [Configure the Indexing Connector for Documentum](#DCTM_ConfigureConn) on each SharePoint Server 2016 server in the farm that hosts a crawl component by using the Indexing Connector for Documentum PowerShell cmdlet. Choose one of the following configurations:
    
### 

Configuration ACL Translation Description See this section Support crawling EMC Documentum Trusted Content Services (TCS) content or regular Documentum content with automatic user mapping.  <br/> Claims  <br/> You enable automatic user mapping by configuring a separate Security Trimmer Sync Service and pre- and post-trimmers.  <br/>  [Configure the Indexing Connector for Documentum to support TCS and automatic user mapping](#DCTM_Configure_TCS) <br/> Support crawling Documentum content and use a manually created user mapping table.  <br/> UserMappingTable  <br/> You manually create a user mapping table in SQL Server to specify how the Documentum users are mapped to Active Directory Domain Services (AD DS) or Active Directory service users. You configure the connector by specifying in which database you have created the user mapping table by using Microsoft PowerShell.  <br/>  [Configure the Indexing Connector for Documentum using a user mapping table](#DCTM_UserMapping) <br/> Support crawling Documentum content when Documentum and Windows user accounts are the same.  <br/> SameAccountName  <br/> The Indexing Connector for Documentum assumes that Documentum and SharePoint users share the same account, such as a shared account in Active Directory. Once an account is found that is not valid, the Indexing Connector for Documentum discards the account permission.  <br/>  [Using the SPEnterpriseSearchDCTMConnectorConfig cmdlet](#DCTM_cmdlet) <br/> Support crawling Documentum content without security trimming the search results.  <br/> NoSecurity  <br/> All users will be able to see all Documentum search results. This can be useful if you have a public Documentum repository that everyone can access, for example.  <br/>  [Using the SPEnterpriseSearchDCTMConnectorConfig cmdlet](#DCTM_cmdlet) <br/> 4. Configure a Documentum crawl rule and content source in the Search service application by using Central Administration.
    
1.  [Create a crawl rule for Documentum](#DCTM_Crawl_rule).
    
  
2.  [Create a Documentum content source](#DCTM_Content_source)
    
  
3. Perform a full crawl. 
    
  

## Prepare the SharePoint Server 2016 servers that host a crawl component
<a name="DCTM_PrepareCrawlServer"> </a>

 **Decide which Documentum content access account to use for crawling**
1. You have to specify the Documentum content access account and the password later in the configuration procedure when you set up crawl rules. The Indexing Connector for Documentum uses the content access account to retrieve content from the Documentum repository. This account must have the following minimum permissions:
    
  - Read permission to documents that you want to crawl.
    
  
  - Browse permission to cabinets, folders, and records (documents with only metadata) that you want to crawl.
    
  
 **Set the DFS Productivity Layer .NET assemblies**
1. Locate the following DFS Productivity Layer .NET assemblies and verify that the version number is **6.7.2000.36** for all files. When extracted to the default path, these files are located in the%local%\\emc-dfs-sdk-6.7\\emc-dfs-sdk-6.7\\lib\\dotnet directory.
    
  - Emc.Documentum.FS.DataModel.Core.dll
    
  
  - Emc.Documentum.FS.DataModel.Shared.dll
    
  
  - Emc.Documentum.FS.runtime.dll
    
  
  - Emc.Documentum.FS.Services.Core.dll
    
  
2. On each server that hosts a crawl component, log on with an account that is a member of the Administrators group on that server and deploy the DFS Productivity Layer .NET assemblies to the global assembly cache %windir%\\assembly.
    
    > [!NOTE:]
      
The following procedure explains how to edit the machine.config file on each SharePoint Server 2016 server that hosts a crawl component to include WCF settings for the DFS Productivity Layer. This is done to make sure that the DFS Productivity Layer .NET assemblies function correctly.The WCF settings that you are about to set in  [Edit the machine.config file](#DCTM_machineconfig) allow a maximum of 30 megabytes (MB) per Documentum content object (the document file plus its metadata) transferred. The administrator can increase *maxReceivedMessageSize*  in *DfsDefaultService*  binding for larger content. **Edit the machine.config file**
1. On each server that hosts a crawl component, open the machine.config file. This file is located in the directory %windir%\\Microsoft.NET\\Framework64\\v4.0.30319\\Config.
    
  
2. Copy the following XML snippet to the **<configuration>** element:
    
  ```
  
<system.serviceModel>
<bindings>
<basicHttpBinding>
<binding name="DfsAgentService" closeTimeout="00:01:00"
 openTimeout="00:01:00" receiveTimeout="00:10:00" sendTimeout="00:01:00"
 allowCookies="false" bypassProxyOnLocal="false" hostNameComparisonMode="StrongWildcard"
 maxBufferSize="10000000" maxBufferPoolSize="10000000" maxReceivedMessageSize="10000000"
 messageEncoding="Text" textEncoding="utf-8" transferMode="Buffered"
 useDefaultWebProxy="true">
<readerQuotas maxDepth="32" maxStringContentLength="8192" maxArrayLength="16384"
  maxBytesPerRead="4096" maxNameTableCharCount="16384" />
<security mode="None">
<transport clientCredentialType="None" proxyCredentialType="None"
realm="" />
<message clientCredentialType="UserName" algorithmSuite="Default" />
</security>
</binding>

<binding name="DfsContextRegistryService" closeTimeout="00:01:00"
   openTimeout="00:01:00" receiveTimeout="00:10:00" sendTimeout="00:01:00"
   allowCookies="false" bypassProxyOnLocal="false" hostNameComparisonMode="StrongWildcard"
   maxBufferSize="10000000" maxBufferPoolSize="10000000" maxReceivedMessageSize="10000000"
   messageEncoding="Text" textEncoding="utf-8" transferMode="Buffered"
   useDefaultWebProxy="true">
<readerQuotas maxDepth="32" maxStringContentLength="8192" maxArrayLength="16384"
maxBytesPerRead="4096" maxNameTableCharCount="16384" />
<security mode="None">
<transport clientCredentialType="None" proxyCredentialType="None"
realm="" />
<message clientCredentialType="UserName" algorithmSuite="Default" />
</security>
</binding>
<binding name="DfsDefaultService" closeTimeout="00:01:00" openTimeout="00:10:00" receiveTimeout="00:20:00" sendTimeout="00:10:00" allowCookies="false" bypassProxyOnLocal="false" hostNameComparisonMode="StrongWildcard" maxBufferSize="10000000" maxBufferPoolSize="10000000" maxReceivedMessageSize="30000000" messageEncoding="Text" textEncoding="utf-8" transferMode="StreamedResponse" useDefaultWebProxy="true">
<readerQuotas maxDepth="32" maxStringContentLength="8192" maxArrayLength="16384" maxBytesPerRead="1048576" maxNameTableCharCount="16384"/>
<security mode="None">
<transport clientCredentialType="None" proxyCredentialType="None" realm=""/>
<message clientCredentialType="UserName" algorithmSuite="Default"/>
</security>
</binding>
</basicHttpBinding>
</bindings>
</system.serviceModel>

  ```


## Install and register the Indexing Connector for Documentum
<a name="DCTM_InstallCon"> </a>

 **Install the Indexing Connector for Documentum**
1. Download the Indexing Connector for Documentum from the  [Microsoft Download Center](https://go.microsoft.com/?linkid=9826867).
    
  
2. On each server in the farm that hosts a crawl component, install the Indexing Connector for Documentum by running the file DCTMIndexConn.exe. Follow the steps in the installation wizard.
    
  
 **Register the Indexing Connector for Documentum to the Search service application**
1. Run this procedure on a SharePoint Server 2016 server that hosts a crawl component to register the connector to the Search service application.
    
  
2. Start a SharePoint 2016 Management Shell.
    
  - For Windows Server 2008 R2:
    
  - On the **Start** menu, click **All Programs**, click **SharePoint 2016**, then right-click **SharePoint 2016 Management Shell** and then click **Run as administrator**.
    
  
  - For Windows Server 2012:
    
1. On the **Start** screen, right-click **SharePoint 2016 Management Shell** and then click **Run as administrator**.
    
    If **SharePoint 2016 Management Shell** is not on the **Start** screen:
    
  
2. Right-click **Computer**, click **All apps**, then right-click **SharePoint 2016 Management Shell** and then click **Run as administrator**.
    
  

    For more information about how to interact with Windows Server 2012, see  [Common Management Tasks and Navigation in Windows Server 2012](https://go.microsoft.com/fwlink/p/?LinkId=276950).
    
  
3. At the Microsoft PowerShell command prompt, type the following command(s):
    
  ```
  
New-SPEnterpriseSearchCrawlCustomConnector -SearchApplication "<name of your Search service application>" -Protocol "dctm" -ModelFilePath "<%CommonProgramFiles%\\Microsoft Shared\\Web Server Extensions\\15\\CONFIG\\SearchConnectors\\Documentum\\MODEL.xml>" -Name "Microsoft SharePoint 2016 Indexing Connector for Documentum"

  ```


    Where:
    
  -  *<name of your Search service application>*  is the name of the Search service application that you are registering the connector to.
    
  
  -  *<%CommonProgramFiles%\\Microsoft Shared\\Web Server Extensions\\15\\CONFIG\\SearchConnectors\\Documentum\\MODEL.xml>*  is the path of the Indexing Connector for Documentum model file. The default location is given in this example.
    
  

## Configure the Indexing Connector for Documentum
<a name="DCTM_ConfigureConn"> </a>

You configure the connector settings with the Indexing Connector for Documentum PowerShell cmdlet (Set-SPEnterpriseSearchDCTMConnectorConfig). The settings are stored in %CommonProgramFiles%\\Microsoft Shared\\Web Server Extensions\\15\\CONFIG\\SearchConnectors\\Documentum\\DCTMConfig.xml and must be the same on each SharePoint Server 2016 server that hosts a crawl component.Which PowerShell cmdlet parameters you use and which additional configuration steps you must perform depends on configuration mode you choose. 
## Configure the Indexing Connector for Documentum to support TCS and automatic user mapping
<a name="DCTM_Configure_TCS"> </a>

The following procedures explain how to configure the indexing connector for Documentum to support TCS. The procedures also show how to enable automatic user mapping by configuring the Security Trimmer Sync Service and create and deploy custom pre- and post-security trimmers. After completing these procedures, your Documentum user credentials will be automatically synced with Windows Active Directory Domain Services (AD), search results will be trimmed accordingly and users will only be able to retrieve Documentum search results that they have permission to see.The Security Trimmer Sync Service maps Documentum users to AD users by looking at the Documentum fields **user_os_domain**, **user_login_name**, **user_source** and **user_ldap_dn**. If the **user_ldap_dn** field is populated, the Security Trimmer Sync Service will try to extract a domain from the first DC value. For example, if the **user_ldap_dn** field is populated with " **CN=User Name, OU=Unit,DC=Domain,DC=Department,DC=Company**", the Security Trimmer Sync Service will extract the domain from **DC=Domain** and will ignore **DC=Department,DC=Company**. **To configure the connector to support TCS and automatic user mapping**
1. Start a SharePoint 2016 Management Shell on each server that hosts a crawl component.
    
  - For Windows Server 2008 R2:
    
  - On the **Start** menu, click **All Programs**, click **SharePoint 2016**, then right-click **SharePoint 2016 Management Shell** and then click **Run as administrator**.
    
  
  - For Windows Server 2012:
    
1. On the **Start** screen, right-click **SharePoint 2016 Management Shell** and then click **Run as administrator**.
    
    If **SharePoint 2016 Management Shell** is not on the **Start** screen:
    
  
2. Right-click **Computer**, click **All apps**, then right-click **SharePoint 2016 Management Shell** and then click **Run as administrator**.
    
  

    For more information about how to interact with Windows Server 2012, see  [Common Management Tasks and Navigation in Windows Server 2012](https://go.microsoft.com/fwlink/p/?LinkId=276950).
    
  
2. At the Microsoft PowerShell command prompt, type the following command(s):
    
  ```
  
Set-SPEnterpriseSearchDCTMConnectorConfig -Shared -ACLTranslation "Claims" -DisplayURLPatternForDocument "http://<MyWebTopServer:PortOfMyWebTopServer>/webtop/component/drl?objectId={ObjectId}&amp;format={Format}&amp;RepositoryName={RepositoryName}" -DisplayURLPatternForContainer "http://<MyWebTopServer:PortOfMyWebTopServer>/webtop/component/drl?objectId={ObjectId}&amp;RepositoryName={RepositoryName}"

Set-SPEnterpriseSearchDCTMConnectorConfig -Repository -RepositoryName "<MyRepository1>" -DFSWebServiceURL @("http://<DFSWebServices>:<30000>/services"), ("http://<DFSWebServices2>:<30000>/services")
 
Set-SPEnterpriseSearchDCTMConnectorConfig -Repository -RepositoryName "<MyRepository2>" -DFSWebServiceURL @("http://<DFSWebServices>:<30000>/services")

  ```


    Where:
    
  -  *<MyWebTopServer:PortOfMyWebTopServer>*  is the name and the port number of the DFS Web Top Server you are using.
    
  
  -  *<MyRepository n>*  is the name of Documentum repository that you want to crawl.
    
  
  -  *<DFSWebServices n>:<30000>*  is the name and the port number of the Documentum Web Services server that hosts the Documentum repository that you want to crawl.
    
  
3. Restart the OSearch15 service. This must be done before you create a content source for Documentum.
    
    > [!IMPORTANT:]
      

1. Verify that the user account that is performing this procedure is an administrator for the server that hosts the crawl component. 
    
  
2. Open a Command Prompt window.
    
  
3. To stop the OSearch15 service, type this command: **net stop osearch15**
    
  
4. To start the OSearch15 service, type this command: **net start osearch15**
    
  
 **To set up the Security Trimming Sync Service**
1. Open the file Microsoft.Office.Server.Search.Connector.Documentum.TrimmerSync.exe.config. This file is stored in the folder where you have installed the Indexing Connector for Documentum connector. The default location is %CommonProgramFiles%\\Microsoft Shared\\Web Server Extensions\\15\\CONFIG\\SearchConnectors\\Documentum.
    
  
2. Using the same information that you provided when you configured the Indexing Connector for Documentum, edit the configuration file as follows.
    
1. In the **Emc.Documentum** section, in the **ModuleInfo** element, do the following:
    
  - In the **host** attribute, type the host name of the Documentum server.
    
  
  - In the **port** attribute, type the port number of the Documentum server.
    
  
2. In the **Data Source: Documentum Settings** section, in the **Repositories** element, do the following:
    
  - In the **repository id** attribute, type the Documentum repository id.
    
  
  - In the **name** attribute, type the name of the Documentum repository.
    
  
  - In the **login** attribute, type the Documentum login name. Use the same login name as the Documentum content access account. This should be a user who has elevated user permissions on the Documentum Content Server. For more information, see [Determine which Documentum content access account to use](#DCTM_ContentAccess).
    
  
  - In the **dfs** attribute, type the location of the Documentum Foundation Services (DFS) by providing the URI for the DFS.
    
  
3. (Optional) If your Documentum connection requires SSL/HTTPS, you have to change the security mode. 
    
  - In the **Data Source: Documentum Settings** section, subsection **Documentum**, in the **basicHttpBinding** element, set the security mode attribute from *None*  to *Transport*  for the following bindings:
    
  - **DfsAgentService**
    
  
  - **DfsContextRegistryService**
    
  
  - **DfsDefaultService**
    
  
  - In the **Data Source: Documentum Settings** section, subsection **Documentum**, in the **netNamedPipeBinding** element, set the security mode attribute from *None*  to *Transport*  for the following bindings:
    
  - **localNamedPipeBinding**
    
  
3. Save and close the file. 
    
  
4. Copy the DFS Productivity Layer .NET assemblies to the server running the Security Trimming Sync Service.
    
1. Locate the following DFS Productivity Layer .NET assemblies and verify that the version number is **6.7.2000.36** for all files. When extracted to the default path, these files are located in the%local%\\emc-dfs-sdk-6.7\\emc-dfs-sdk-6.7\\lib\\dotnet directory.
    
  - Emc.Documentum.FS.DataModel.Core.dll
    
  
  - Emc.Documentum.FS.DataModel.Shared.dll
    
  
  - Emc.Documentum.FS.runtime.dll
    
  
  - Emc.Documentum.FS.Services.Core.dll
    
  
2. On the server that hosts the Security Trimming Sync Service, log on with an account that is a member of the Administrators group on that server and deploy the DFS Productivity Layer .NET assemblies to the global assembly cache %windir%\\assembly.
    
    > [!NOTE:]
      
5. Configure authentication for the Security Trimming Sync Service and install the service. 
    
1. Verify that the user account that is performing this procedure is a member of the Farm Administrators group.
    
  
2. Open a Command Prompt window on each server that hosts a query processing component. 
    
  
3. Type the following command: **Microsoft.Office.Server.Search.Connector.Documentum.TrimmerSync.exe -p**
    
    When prompted, enter the password for the account that you provided in the **login** attribute. Use the same login name as the Documentum content access account. The password will now automatically be encrypted and added to the Security Trimming Sync Service config file.
    
  
4. Install the Security Trimming Sync Service. Type the following command: **Microsoft.Office.Server.Search.Connector.Documentum.TrimmerSync.exe -i**
    
  
6. Start the Security Trimming Sync Service. 
    
1. Open **Windows Server Manager**.
    
  
2. Expand the **Configuration** menu and click **Services**.
    
  
3. Right-click the **SharePoint Documentum Security Sync** service and then click **Properties**. In the **LogOn** tab, select **This account** and provide the account details and credentials for the account that runs the SharePoint services. Click **OK**.
    
  
4. Right-click the **SharePoint Documentum Security Sync** service and then click **Start**.
    
  
5. Verify that the **Status** column changes to **Started**.
    
  
7. Verify that the service is running and that the security sync is completed. 
    
1. Run the command **Microsoft.Office.Server.Search.Connector.Documentum.TrimmerSync.exe -d** to write the Security Trimming Sync Service memory to a text file.
    
  
2. Verify that the Security Trimming Sync Service connects to the Documentum server. Read the file DCTMSecuritySync.log that is located in the directory <Microsoft Office Server path>\\15.0\\Data\\Office Server\\Applications\\Search\\Nodes. 
    
  
3. Verify that the membership information from the Documentum server is written to the file DCTMSecuritySync_Dump.txt that is located in the directory <Microsoft Office Server path>\\15.0\\Data\\Office Server\\Applications\\Search\\Nodes.
    
  
Before you can add the pre- and post- security trimmers, you must add one simple crawl rule for Documentum. Later, you can further specify or expand the crawl rules. **Create a simple crawl rule for Documentum**
1. Verify that the user account that is performing this procedure is an administrator for the Search service application. 
    
  
2. On the SharePoint Central Administration home page, in the **Application Management** section, click **Manage Service Applications**.
    
  
3. On the Manage Service Applications page, click the Search service application for which you want to create a crawl rule.
    
  
4. On the Search Administration page, in the **Crawling** section, click **Crawl Rules**.
    
  
5. On the Manage Crawl Rules page, click **New Crawl Rule**.
    
  
6. On the Add Crawl Rule page, specify the following information to create a crawl rule:
    
1. In **Path** box, type **dctm://***.
    
  
2. In **Crawl Configuration** section, select **Include all items in this path**, and then select **Crawl complex URLs (URLs that contain a question mark - ?)**.
    
  
3. In the **Specify Authentication** section, select **Specify a different content access account**, and then type the Documentum content access account and password in the appropriate boxes.
    
  
4. Make sure that the **Do not allow Basic Authentication** check box is cleared.
    
  
7. Click **OK** to add the crawl rule.
    
  
 **To add the Indexing Connector for Documentum pre- and post-security trimmers**
1. Start a SharePoint 2016 Management Shell on each server that hosts a query processing component.
    
  - For Windows Server 2008 R2:
    
  - On the **Start** menu, click **All Programs**, click **SharePoint 2016**, then right-click **SharePoint 2016 Management Shell** and then click **Run as administrator**.
    
  
  - For Windows Server 2012:
    
1. On the **Start** screen, right-click **SharePoint 2016 Management Shell** and then click **Run as administrator**.
    
    If **SharePoint 2016 Management Shell** is not on the **Start** screen:
    
  
2. Right-click **Computer**, click **All apps**, then right-click **SharePoint 2016 Management Shell** and then click **Run as administrator**.
    
  

    For more information about how to interact with Windows Server 2012, see  [Common Management Tasks and Navigation in Windows Server 2012](https://go.microsoft.com/fwlink/p/?LinkId=276950).
    
  
2. At the Microsoft PowerShell command prompt, type the following command(s):
    
  ```
  
New-SPEnterpriseSearchSecurityTrimmer -SearchApplication <name of your Search service application> -typeName "Microsoft.Office.Server.Search.Connector.Documentum.Trimmers.DctmTrimPre, Microsoft.Office.Server.Search.Connector.Documentum.Trimmers, Version=15.0.0.0,Culture=neutral, PublicKeyToken=48e046c834625a88, processorArchitecture=MSIL" -id 26 -RulePath dctm:\\*

New-SPEnterpriseSearchSecurityTrimmer -SearchApplication <name of your Search service application> -typeName "Microsoft.Office.Server.Search.Connector.Documentum.Trimmers.DctmTrimPost, Microsoft.Office.Server.Search.Connector.Documentum.Trimmers, Version=15.0.0.0,Culture=neutral, PublicKeyToken=48e046c834625a88, processorArchitecture=MSIL" -id 17 -RulePath dctm:\\*

  ```


    Where:
    
  -  *<name of your Search service application>*  is the name of the Search service application.
    
  
3. Restart the SharePoint Search Host Controller. 
    
1. Open a Command Prompt window. 
    
  
2. To stop the SharePoint Search Host Controller, type this command: **net stop spsearchhostcontroller**
    
  
3. To start the SharePoint Search Host Controller, type this command: **net start spsearchhostcontroller**
    
  
4. Continue with  [Create a Documentum content source](#DCTM_Content_source).
    
  

## Configure the Indexing Connector for Documentum using a user mapping table
<a name="DCTM_UserMapping"> </a>

The following procedures explain how to manually create a user mapping table that specifies how the Documentum users are mapped to Active Directory Domain Services (AD DS) or Active Directory service users, and how to configure the connector to support crawling Documentum content and use the user mapping table.
- The user mapping table must be in a SQL Server 2008 or a later version database.
    
  
- The OSearch15 service account must have at least read permission on the user mapping table data.
    
  
 **To create a user mapping table**
1. Create a user mapping table in SQL Server 2008 or a later version. The user mapping table must have the following format: 
    
### 

Column name SQL datatype Description DCTMCredentialDomain  <br/> nvarchar(255) NOT NULL  <br/> Domain name of a Documentum account. Populate this column when the account comes from the local computer or an LDAP system. The  *User Source*  property of the Documentum account should equal *None*  or *LDAP*  . Otherwise, leave the column empty. <br/> DCTMCredentialRepository  <br/> nvarchar (32) NOT NULL  <br/> Repository name of a Documentum account. Populate this column when the account comes from a Documentum repository.  <br/> DCTMCredentialLoginName  <br/> nvarchar (80) NOT NULL  <br/> Login name of the Documentum account.  <br/> NTCredential  <br/> nvarchar (255) NOT NULL  <br/> Windows domain user account that searches Documentum contents in SharePoint Server 2016.  <br/> 
    Use the following script to create a user mapping table:
    


  ```
  
CREATE TABLE <replace with your user mapping table name>
(
DCTMCredentialDomain nvarchar (255) NOT NULL , 
DCTMCredentialRepository nvarchar (32) NOT NULL , 
DCTMCredentialLoginName nvarchar (80) NOT NULL , 
NTCredential nvarchar (255) NOT NULL , 
CONSTRAINT PK_CredentialMapping PRIMARY KEY CLUSTERED 
( DCTMCredentialDomain, DCTMCredentialRepository, DCTMCredentialLogonName )
) 

  ```


    Alternatively, you can manually create the user mapping table using SQL Server Management Studio or an equivalent tool. If you create the table manually, make sure that you use the same schema as defined in the script.
    
  
2. Populate the user mapping table with Documentum/Windows NT credential pairs. The table in the previous step shows what kind of input is expected.
    
    Example:
    
    A Documentum repository user Dan Park has a logon that is linked to the Finance repository. Dan's Windows domain user account is Contoso\\dpark. In this case, the user mapping table entry for Dan should be:
    
### 

DCTMCredentialDomain  <br/> ''  <br/> DCTMCredentialRepository  <br/> Finance  <br/> DCTMCredentialLogonName  <br/> dpark  <br/> NTCredential  <br/> Contoso\\dpark  <br/> 
    > [!NOTE:]
      
3. Grant the OSearch15 account read access to the user mapping table.
    
  
 **To configure the connector using a user mapping table**
1. Start a SharePoint 2016 Management Shell on each server that hosts a crawl component.
    
  - For Windows Server 2008 R2:
    
  - On the **Start** menu, click **All Programs**, click **SharePoint 2016**, then right-click **SharePoint 2016 Management Shell** and then click **Run as administrator**.
    
  
  - For Windows Server 2012:
    
1. On the **Start** screen, right-click **SharePoint 2016 Management Shell** and then click **Run as administrator**.
    
    If **SharePoint 2016 Management Shell** is not on the **Start** screen:
    
  
2. Right-click **Computer**, click **All apps**, then right-click **SharePoint 2016 Management Shell** and then click **Run as administrator**.
    
  

    For more information about how to interact with Windows Server 2012, see  [Common Management Tasks and Navigation in Windows Server 2012](https://go.microsoft.com/fwlink/p/?LinkId=276950).
    
  
2. At the Microsoft PowerShell command prompt, type the following command(s):
    
  ```
  
Set-SPEnterpriseSearchDCTMConnectorConfig -Shared -ACLTranslation UserMappingTable -DisplayURLPatternForContainer "http://<MyWebTopServer:PortOfMyWebTopServer>/webtop/component/drl?objectId={ObjectId}&amp;RepositoryName={RepositoryName}" -DisplayURLPatternForDocument "http://<MyWebTopServer:PortOfMyWebTopServer>/webtop/component/drl?objectId={ObjectId}&amp;format={Format}&amp;RepositoryName={RepositoryName}" -UnmappedAccount "DiscardACE" -UserMappingTableSQLServer "<YourDatabaseServerName>" -UserMappingTableSQLInstance "<YourDatabaseInstanceName>" -UserMappingTableDBName "<YourMappingDatabaseName>" -UserMappingTableName "<YourMappingTableName>"

Set-SPEnterpriseSearchDCTMConnectorConfig -Repository -RepositoryName "<MyRepository1>" -DFSWebServiceURL @("http://<DFSWebServices>:<30000>/services", "http://<DFSWebServices2>:<30000>/services")

Set-SPEnterpriseSearchDCTMConnectorConfig -Repository -RepositoryName "<MyRepository2>" -DFSWebServiceURL @("http://<DFSWebServices>:<30000>/services")
  ```


    Where:
    
  -  *<MyWebTopServer:PortOfMyWebTopServer>*  is the name and the port number of the DFS Web Top Server you are using.
    
  
  -  *<YourDatabaseServerName>*  is the name of the database server on which you created the user mapping table.
    
  
  -  *<YourDatabaseInstanceName>*  is the name of the database instance of the database server on which you created the user mapping table.
    
  
  -  *<YourMappingDatabaseName>*  is the name of the database in which you created the user mapping table.
    
  
  -  *<YourMappingTableName>*  is the name of the user mapping table that you created.
    
  
  -  *<MyRepository n>*  is the name of Documentum repository that you want to crawl.
    
  
  -  *<DFSWebServices n>:<30000>*  is the name and port number of the Documentum Web Services server that hosts the Documentum repository that you want to crawl.
    
  
3. Restart the OSearch15 service. The server administrator of the server that hosts the crawl component must restart the OSearch15 service before a content source can be created for Documentum.
    
    > [!IMPORTANT:]
      

1. Verify that the user account that is performing this procedure is an administrator for the server that hosts the crawl component. 
    
  
2. Open a Command Prompt window.
    
  
3. To stop the OSearch15 service, type this command: **net stop osearch15**
    
  
4. To start the OSearch15 service, type this command: **net start osearch15**
    
  
Continue with  [Create a crawl rule for Documentum](#DCTM_Crawl_rule) and then continue with [Create a Documentum content source](#DCTM_Content_source).
## Create the Documentum crawled properties category
<a name="BKMK_CrawledPropertiesCategory"> </a>

You must create a crawled properties category that will contain the Documentum crawled properties. To do so, you use the **New-SPEnterpriseSearchMetadataCategory** cmdlet and specify the predefined value 34972762-7E3F-4f4f-AE5C-5ABBA92EC530 for the cmdlet's PropSet parameter. Use the following PowerShell code to create the crawled properties category in this way.
```

$ssa = Get-SPEnterpriseSearchServiceApplication
New-SPEnterpriseSearchMetadataCategory -Name "Documentum Connector" -SearchApplication $ssa -PropSet "34972762-7E3F-4f4f-AE5C-5ABBA92EC530" -DiscoverNewProperties $true
```


## Create a crawl rule for Documentum
<a name="DCTM_Crawl_rule"> </a>

Before a crawl, you must create at least one crawl rule to authenticate the crawler with the DFS Server. You can create more than one crawl rule to include or exclude specific content in Documentum. **To create a crawl rule for the Indexing Connector for Documentum**
1. Verify that the user account that is performing this procedure is an administrator for the Search service application. 
    
  
2. On the SharePoint Central Administration home page, in the **Application Management** section, click **Manage Service Applications**.
    
  
3. On the Manage Service Applications page, click the Search service application for which you want to create a crawl rule.
    
  
4. On the Search Administration page, in the **Crawling** section, click **Crawl Rules**.
    
  
5. On the Manage Crawl Rules page, click **New Crawl Rule**.
    
  
6. On the Add Crawl Rule page, specify the following information:
    
1. In the **Path** box, type the path to which the crawl rule will apply. You can use standard wildcard characters. To use regular expressions instead of wildcard characters, select **Use regular expression syntax for matching this rule**. For examples, see [Syntax to refer to a Documentum object](#DCTM_Syntax).
    
  
2. In **Crawl Configuration** section, select **Include all items in this path**, and then select **Crawl complex URLs (URLs that contain a question mark - ?)**.
    
  
3. In the **Specify Authentication** section, select **Specify a different content access account**, and then type the Documentum content access account and password in the boxes. See [Determine which Documentum content access account to use](#DCTM_ContentAccess) earlier in this article.
    
  
4. Make sure that the **Do not allow Basic Authentication** check box is cleared.
    
  
7. Click **OK** to add the crawl rule.
    
    > [!NOTE:]
      >  You can create multiple crawl rules for Documentum to include or exclude Documentum content.>  You can use different crawl rules to specify different content access accounts for different Documentum content. For example, you have two repositories and two content access accounts for each repository. The Documentum content access account specified in a crawl rule will only be applied to Documentum content covered by the path in that crawl rule. If you use the Security Trimming Sync Service, you must set up this service for each Documentum server.

## Create a Documentum content source
<a name="DCTM_Content_source"> </a>

You create a content source for Documentum content to specify which Documentum content repositories you want to crawl. **To create a content source for the Indexing Connector for Documentum**
1. Verify that the user account that is performing this procedure is an administrator for the Search service application.
    
  
2. On the SharePoint Central Administration home page, in the **Application Management** section, click **Manage Service Applications**.
    
  
3. Click the Search service application in which you want to create a content source. 
    
  
4. On the Search Administration Page, in the **Crawling** section, click **Content Sources**.
    
  
5. On the Manage Content Sources page, click **New Content Source**.
    
  
6. On the Add Content Source page, do the following:
    
1. In the **Name** box, type the name for the new content source.
    
  
2. In the **Content Source Type** section, select **Custom Repository**.
    
  
3. In the **Type of Repository** section, select **SharePoint 2016 Indexing Connector for Documentum**. Use the name that you specified when you registered the Indexing Connector for Documentum with the Search service application.
    
  
4. In the **Start Addresses** section, type the start addresses. The start address format is the same as the path pattern. You can type more than one start address for the content source, one per line. For examples, see [Syntax to refer to a Documentum object](#DCTM_Syntax).
    
  
5. In the **Crawl Schedules** section, select schedules from the **Full Crawl** and **Incremental Crawl** drop-down lists, or create schedules for each kind of crawl.
    
  
6. In the **Content Source Priority** section, assign a priority level to the content source according to your business requirements.
    
  
7. Click **OK**.
    
  
7. On the **Manage Content Sources** page, right-click the content source for Documentum and click **Start Full Crawl**.
    
  
The Documentum content source is configured and the system can crawl Documentum content repositories that are specified in the content source. SharePoint Server 2016 supports scalable architecture for performance scale-out. You can deploy more than one server that hosts a crawl component and you can configure multiple crawlers to crawl the EMC Documentum database at the same time.
## Syntax to refer to a Documentum object
<a name="DCTM_Syntax"> </a>

The format to refer to a Documentum object that you use for the path (when you set up a crawl rule) and the start address (when you set up a content source) is defined in the following table:
### 

Type of Documentum object Syntax for the path or the start address Repository  <br/> dctm://<clientapphostname>/<repository name>  <br/> Cabinet  <br/> dctm://<clientapphostname>/<repository name>/<cabinet name>  <br/> Folder  <br/> dctm://<clientapphostname>/<repository name>/<cabinet name>/<folder name>  <br/> Document  <br/> dctm://<clientapphostname>/<repository name>/<cabinet name>/<folder name>/…/<folder name>?DocSysID=<r_object_id> (where r_object_id is the object id of that document)  <br/>  *<clientapphostname>*  is the host name of your Documentum client application such as Webtop or DA. The *<clientapphostname>*  configured here must be the same as the one that is used in the content source. *<repository name>*  , *<cabinet name>*  , and *<folder name>*  are case-sensitive.
## Using the SPEnterpriseSearchDCTMConnectorConfig cmdlet
<a name="DCTM_cmdlet"> </a>

Use the following Microsoft PowerShell commands to display help and examples for the Indexing Connector for Documentum cmdlet:
- Get-help Set-SPEnterpriseSearchDCTMConnectorConfig -full shows full help.
    
  
- Get-help Set-SPEnterpriseSearchDCTMConnectorConfig -examples shows only examples.
    
  
The Set-SPEnterpriseSearchDCTMConnectorConfig cmdlet accepts three parameter sets. You use the  *Shared*  parameter set to change the configuration settings that affect all the Documentum repositories that you crawl. You use the *Repository*  parameter set to change the configuration settings that affect only a specific repository. You use the *Remove*  parameter set to remove a specific repository from the connector configuration.The following table shows which parameters are mandatory and which are optional. For parameter descriptions and examples, see **Set-SPEnterpriseSearchDCTMConnectorConfig**.
### 

Action Mandatory parameters Optional parameters Configure shared repository settings  <br/> Shared  <br/> DFSURL, UserMappingTableSQLServer, UserMappingTableSQLInstance, UserMappingTableDBName, UserMappingTableName, ACLTranslation, UnmappedAccount, DisplayURLPatternForDocument, DisplayURLPatternForContainer.  <br/> Configure settings for a specific repository  <br/> Repository, RepositoryName  <br/> DFSWebServiceURL, IndexAllVersions, ACLTranslation, UnmappedAccount, DisplayURLPatternForDocument, DisplayURLPatternForContainer.  <br/> Remove a repository from configuration  <br/> Remove, RepositoryName  <br/>  <br/> 
# See also

#### 

 [Supported and unsupported Documentum object types and properties in SharePoint Server](html/supported-and-unsupported-documentum-object-types-and-properties-in-sharepoint-s.md)
  
    
    

#### 

 **Set-SPEnterpriseSearchDCTMConnectorConfig**
  
    
    

  
    
    

