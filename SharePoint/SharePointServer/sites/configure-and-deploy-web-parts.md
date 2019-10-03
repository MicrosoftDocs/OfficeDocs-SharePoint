---
title: "Configure and deploy web parts in SharePoint Server"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 2/8/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
- SharePoint_Online
ms.assetid: 0810018d-188b-4d42-b908-d794faeacd0a
description: "Learn about securing and deploying web parts in SharePoint Server."
---

# Configure and deploy web parts in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)]
SharePoint Server includes a set of web parts that users can add to pages after installing the product. If an organization needs custom web parts, a developer can write custom ASP.NET web parts and ask you to install them. This process typically requires testing and approval of the code before the web part can be deployed in a full-trust environment. A developer who uses Visual Studio can deploy a web part to SharePoint Server by right clicking the project and selecting **Deploy**. The destination for the web part is determined by the trust level established with the SharePoint server when the developer created the project in Visual Studio.
  
SharePoint Server uses some of the configuration management settings that are provided by the Microsoft .NET Framework. Some of these settings are stored in XML configuration files and they provide a broad range of settings that server administrators use to manage the Web application and its environment. For more information about ASP.NET configuration files, see [Machine.Config and Web.Config Explained](https://go.microsoft.com/fwlink/p/?LinkId=103450) in "Securing Your ASP.NET Application and Web Services". 
  
    
## Configuration options
<a name="BKMK_ConfigurationOptions"> </a>

ASP.NET web parts are deployed to either the SharePoint Server **bin directory** or to the **Global Assembly Cache (GAC)**. 
  
- **Bin directory** Stored in the bin folder under the root directory of your Web application. 
    
    Advantages of this location:
    
    A partial-trust location. By default, code that runs from this directory has a low level of code access security permissions. If the web part requires access across applications or more access than the default permissions allow, the administrator must explicitly raise permissions that are granted to a web part so that it can function correctly. Administrators might prefer that assemblies run in the Bin directory, with a known minimum set of required code access security permissions.
    
    Disadvantages of this location:
    
    To run your web part everywhere, you must deploy your assembly to the Bin directory on each SharePoint Server 2016 server with the MinRole Front-end and Application server roles, and each SharePoint 2013 server with web and application role installed.
    
- **Global Assembly Cache (GAC)** All standard web parts are automatically installed in the GAC, where the common language runtime of the .NET Framework is located, at %windir%\assembly. web parts stored in the GAC can be shared across applications. 
    
    Advantages of this location:
    
    A global location where you can deploy signed assemblies, which can run with full trust by default. Because the assemblies are installed globally, they work in any Web application.
    
    Disadvantages of this location:
    
    Generally, there are no code access security restrictions on code that is installed to the GAC; therefore, you lose the benefit of defense-in-depth security.
    
    Additionally, it can be difficult to deploy your program database (.pdb) files to assemblies in the GAC.
    
## Setting security attributes
<a name="BKMK_SettingSecurity"> </a>

ASP.NET web parts that are stored in the Bin directory have additional security attributes. You can decide whether to set these attributes for your web part, depending on how you plan to use it.
  
The Bin directory is a partial-trust location. Therefore, your web part is not automatically granted full trust code permissions when it is executed. Because the code that calls into your web part is granted only partial trust permissions, the web part developer must configure the **AllowPartiallyTrustedCallers** attribute on your ASP.NET web part. 
  
Marking a component as "safe" with the **AllowPartiallyTrustedCallers** attribute puts the responsibility for safe implementation on the development team. 
  
By default, the Bin directory and its contents are assigned minimal code access security permissions. You should test your web parts carefully to determine the correct level of permissions to assign, and to ensure that the web part does not present a security risk to your environment.
  
You can elevate permissions in either of two ways:
  
- (Recommended) Create a trust policy file and point your Web.config file at the new file. This option is more complex, but it enables you to set precise permissions for your web parts. For more information about trust policy files, see [Microsoft Windows SharePoint Services and Code Access Security](https://go.microsoft.com/fwlink/p/?LinkID=103436). 
    
- Raise the overall trust level of the Bin directory. In the Web.config file in the root directory of your Web application, locate the  `trust` element. The default value for the  `trust` element's  `level` attribute is **WSS_Minimal**. You can change this level to **WSS_Medium**. Although this option is simpler, it grants arbitrary new permissions that you might not need, and it is less secure than creating a trust policy file.
    
    > [!CAUTION]
    > The **WSS_Minimal** and **WSS_Medium** entries in the Web.config file are case sensitive. 
  
## Safe Controls list
<a name="BKMK_SafeControls"> </a>

The Safe Controls list contains the names of controls and web parts, specific to your SharePoint site, that server administrators can designate as safe for use on any .aspx page within a site. This list is part of the Web.config file in your Web application root. 
  
## Deploy and configure a web part
<a name="BKMK_DeployConfigure"> </a>

The method that you use to deploy a new web part will depend on the finished package that the developer provides. If the developer provided you with the web part as a single dynamic-link library (DLL) file, you can manually deploy the DLL by copying it to your Web application's Bin folder. If the developer provides you with a CAB file containing the web part, you can use Microsoft PowerShell to deploy the web part.
  
 **To manually deploy and configure a web part**
  
1. Verify that you have the following administrative credentials:
    
   - You must be a member of the local Administrators group on the server hosting SharePoint Server.
    
2. Copy the  _\<YourWebPartName\>_.dll assembly in the project's Bin directory to the Bin directory in your Web application root directory. For example: C:\inetpub\wwwroot\wss\VirtualDirectories\80\.
    
3. Locate the Web.config file in your application root directory and open it for editing.
    
4. Add the following safe-control entry for your custom assembly to the Web.config file: 
    
   ```
   <SafeControl Assembly="<YourWebPartName>, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null" Namespace="<YourWebPartNamespace>" TypeName="*" Safe="True" AllowRemoteDesigner="True"/>
   ```

   Where:
    
   -   _\<YourWebPartName\>_ is the name of the web part that is being deployed. 
    
   -  _\<YourWebPartNamespace\>_ is the namespace that is associated with your web part. 
    
An alternative to manually installing a web part to the Bin folder or manually changing the Web.config file is to use PowerShell to install the web part package. For this process to work, a developer or system administrator must create a CAB solution package for the web part. After you create a CAB file, follow these steps to deploy the web part.
  
 **To deploy the web part by using Microsoft PowerShell**
  
1. Verify that you meet the following minimum requirements: See [Add-SPShellAdmin](/powershell/module/sharepoint-server/Add-SPShellAdmin?view=sharepoint-ps).
    
2. Open SharePoint Management Shell.
    
3. At the PowerShell command prompt (PS C:\\>), type the following command, and then press ENTER:
    
   ```
   Install-SPWebPartPack -LiteralPath "<PathToCabFile>" -Name "<WebPartName>"
   ```

   Where:
    
   -  _\<PathToCabFile\>_ is the full path to the CAB file that is being deployed. 
    
   -  _\<WebPartName\>_ is the name of the web part that is being deployed. 
    
The previous procedure shows a common way to use **Install-SPWebPartPack** to deploy a web part. You can specify additional parameters to change the way the web part is deployed. For more information, see [Install-SPWebPartPack](/powershell/module/sharepoint-server/Install-SPWebPartPack?view=sharepoint-ps). 

We recommend that you use Microsoft PowerShell when performing command-line administrative tasks. The Stsadm command-line tool has been deprecated, but is included to support compatibility with previous product versions.
  
## Add a component to the Web Part Gallery
<a name="BKMK_AddWebGallery"> </a>

Every web part should have a .webpart file, which is an XML file that describes the web part. The .webpart file also causes your web part to appear in the Web Part gallery. The following procedure is the easiest way to create a .webpart file after you deploy your web part and register it in the Safe Control list.
  
 **To add a component to the Web Part Gallery**
  
1. Verify that you have the following administrative credentials:
    
   - You must be a member of the Farm Administrators group.
    
2. To create a .webpart file, navigate to http://\<MyServer\>/_layouts/newdwp.aspx, where \<MyServer\> is the name of the server on which your SharePoint site is deployed. 
    
3. Select the check box next to  _\<YourWebPartNamespace\>.\<YourWebPartName\>_.
    
4. Click **Populate Gallery** to add the  _YourWebPartName_ web part to the Team Site gallery. 
    
5. In the Web Part gallery, select **Edit** to edit the web part, and then click **Import**. 
    
    You are prompted to specify a location for the .webpart file. You can also export ASP.NET web parts and import them to SharePoint sites.
    
## See also
<a name="BKMK_AddWebGallery"> </a>

#### Concepts

[Manage web parts in SharePoint Server](manage-web-parts.md)
#### Other Resources

[How to: Deploy, Publish, and Upgrade SharePoint Solutions on a Remote Server](https://go.microsoft.com/fwlink/?linkid=858842)

