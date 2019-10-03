---
title: "Enable TLS and SSL support in SharePoint 2013"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 3/5/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: 60913d6d-c069-4dfc-9399-71d5344da4e0
description: "This article describes how to enable Transport Layer Security (TLS) protocol versions 1.1 and 1.2 in a SharePoint environment."
---

# Enable TLS and SSL support in SharePoint 2013

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)]
  
TLS protocol version 1.1 and 1.2 support is not enabled by default in SharePoint Server 2013. To enable support, you'll have to install updates and change configuration settings  *once*  in each of the following locations: 
  
1. SharePoint servers in your SharePoint farm
    
2. Microsoft SQL Servers in your SharePoint farm
    
3. Client computers used to access your SharePoint sites
    
> [!IMPORTANT]
> If you do not update each of these locations, you run the risk of systems failing to ﻿connect to each other using TLS 1.1 or TLS 1.2. The systems will instead fall back to an older security protocol; and if the older security protocols are disabled, ﻿the systems may fail to connect entirely. > **Example:** SharePoint servers may fail to connect to ﻿SQL Server databases, or client computers may fail to connect to your SharePoint sites. 
  
## Summary of the update process

The following image shows the three step process necessary to enable TLS 1.1 and TLS 1.2 support on your SharePoint servers, SQL Servers, and client computers.
  
![Displays steps to enable TLS and SSL on SharePoint servers](../media/62083e41-98cd-4109-ac58-d3d63a78f707.png)
  
## Step 1: Update SharePoint servers in your SharePoint farm

Follow these steps to update your SharePoint server.
  
|**Steps for SharePoint Server**|**Windows Server 2008 R2**|**Windows Server 2012**|**Windows Server 2012 R2**|
|:-----|:-----|:-----|:-----|
|[1.1 - Enable TLS 1.1 and TLS 1.2 in Windows Schannel](/SharePoint/security-for-sharepoint-server/enable-tls-and-ssl-support-in-sharepoint-2013#EnableTLS) <br/> |Required  <br/> |N/A  <br/> |N/A  <br/> |
|[1.2 - Enable TLS 1.1 and TLS 1.2 support in WinHTTP](/SharePoint/security-for-sharepoint-server/enable-tls-and-ssl-support-in-sharepoint-2013#EnableTLSWinHTTP) <br/> |Required  <br/> |Required  <br/> |N/A  <br/> |
|[1.3 - Enable TLS 1.1 and TLS 1.2 support in Internet Explorer](/SharePoint/security-for-sharepoint-server/enable-tls-and-ssl-support-in-sharepoint-2013#enableIE) <br/> |Required  <br/> |Required  <br/> |N/A  <br/> |
|[1.4 - Install SQL Server 2008 R2 Native Client update for TLS 1.2 support](https://www.microsoft.com/en-us/download/details.aspx?id=57606#InstallSQL) <br/> |Required  <br/> |Required  <br/> |Required  <br/> |
|[1.5 - Install .NET Framework 4.6 or higher](/SharePoint/security-for-sharepoint-server/enable-tls-and-ssl-support-in-sharepoint-2013#InstallNET46) <br/> |Required  <br/> |Required  <br/> |Required  <br/> |
|[1.6 - Enable strong cryptography in .NET Framework 4.6 or higher](/SharePoint/security-for-sharepoint-server/enable-tls-and-ssl-support-in-sharepoint-2013#CryptoNet45) <br/> |Required  <br/> |Required  <br/> |Required  <br/> |
|The following ﻿steps are **recommended**. Although not directly required by SharePoint Server 2013, they may be necessary for other software ﻿that integrates with SharePoint Server 2013.  <br/> |
|[1.7 - Install .NET Framework 3.5 update for TLS 1.1 and TLS 1.2 support](/SharePoint/security-for-sharepoint-server/enable-tls-and-ssl-support-in-sharepoint-2013#InstallFrame46) <br/> |Recommended  <br/> |Recommended  <br/> |Recommended  <br/> |
|[1.8 - Enable strong cryptography in .NET Framework 3.5](/SharePoint/security-for-sharepoint-server/enable-tls-and-ssl-support-in-sharepoint-2013#EnableCryptoFrame35) <br/> |Recommended  <br/> |Recommended  <br/> |Recommended  <br/> |
|The following ﻿step is **optional**. You may choose to run this step based on your organization's security and compliance requirements.  <br/> |
|[1.9 - Disable earlier versions of SSL and TLS in Windows Schannel](/SharePoint/security-for-sharepoint-server/enable-tls-and-ssl-support-in-sharepoint-2013#DisableTLSSchannel) <br/> |Optional  <br/> |Optional  <br/> |Optional  <br/> |
   
## 1.1 - Enable TLS 1.1 and TLS 1.2 in Windows Schannel
<a name="EnableTLS"> </a>

SSL and TLS support are enabled or disabled in Windows Schannel by editing the Windows Registry. Each SSL and TLS protocol version can be enabled or disabled independently. You don't need to enable or disable one protocol version to enable or disable another protocol version.
  
The **Enabled** registry value defines whether the protocol version can be used. If the value is set to 0, the protocol version cannot be used, even if it is enabled by default or if the application explicitly requests that protocol version. If the value is set to 1, the protocol version can be used if enabled by default or if the application explicitly requests that protocol version. If the value is not defined, it will use a default value determined by the operating system. 
  
The **DisabledByDefault** registry value defines whether the protocol version is used by default. This setting only applies when the application doesn't explicitly request the protocol versions to be used. If the value is set to 0, the protocol version will be used by default. If the value is set to 1, the protocol version will not be used by default. If the value is not defined, it will use a default value determined by the operating system. 
  
 **To enable TLS 1.1 support in Windows Schannel**
  
1. From Notepad.exe, create a text file named **tls11-enable.reg**. 
    
2. Copy, and then paste the following text.
    
  ```
  Windows Registry Editor Version 5.00
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.1]
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.1\Client]
  "DisabledByDefault"=dword:00000000
  "Enabled"=dword:00000001
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.1\Server]
  "DisabledByDefault"=dword:00000000
  "Enabled"=dword:00000001
  ```

3. Save the **tls11-enable.reg** file. 
    
4. Double-click the **tls11-enable.reg** file. 
    
5. Click **Yes** to update your Windows Registry with these changes. 
    
6. Restart your computer for the change to take effect.
    
 **To enable TLS 1.2 support in Windows Schannel**
  
1. From Notepad.exe, create a text file named **tls12-enable.reg**. 
    
2. Copy, and then paste the following text.
    
  ```
  Windows Registry Editor Version 5.00
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2]
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Client]
  "DisabledByDefault"=dword:00000000
  "Enabled"=dword:00000001
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Server]
  "DisabledByDefault"=dword:00000000
  "Enabled"=dword:00000001
  ```

3. Save the **tls12-enable.reg** file. 
    
4. Double-click the **tls12-enable.reg** file. 
    
5. Click **Yes** to update your Windows Registry with these changes. 
    
6. Restart your computer for the change to take effect.
    
## 1.2 - Enable TLS 1.1 and TLS 1.2 support in WinHTTP
<a name="EnableTLSWinHTTP"> </a>

WinHTTP doesn't inherit its SSL and TLS encryption protocol version defaults from the Windows Schannel **DisabledByDefault** registry value. WinHTTP uses its own SSL and TLS encryption protocol version defaults, which vary by operating system. To override the defaults, you must install a KB update and configure Windows Registry keys. 
  
The WinHTTP ** DefaultSecureProtocols ** registry value is a bit field that accepts multiple values by adding them together into a single value. You can use the Windows Calculator program (Calc.exe) in Programmer mode to add the following hexadecimal values as desired. 
  
|**DefaultSecureProtocols value**|**Description**|
|:-----|:-----|
|0x00000008  <br/> |Enable SSL 2.0 by default  <br/> |
|0x00000020  <br/> |Enable SSL 3.0 by default  <br/> |
|0x00000080  <br/> |Enable TLS 1.0 by default  <br/> |
|0x00000200  <br/> |Enable TLS 1.1 by default  <br/> |
|0x00000800  <br/> |Enable TLS 1.2 by default  <br/> |
   
For example, you can enable TLS 1.0, TLS 1.1, and TLS 1.2 by default by adding the values 0x00000080, 0x00000200, and 0x00000800 together to form the value 0x00000A80.
  
To install the WinHTTP KB update, follow the instructions from the KB article [Update to enable TLS 1.1 and TLS 1.2 as a default secure protocols in WinHTTP in Windows](https://support.microsoft.com/kb/3140245)
  
 **To enable TLS 1.0, TLS 1.1, and TLS 1.2 by default in WinHTTP**
  
1. From Notepad.exe, create a text file named **winhttp-tls10-tls12-enable.reg**. 
    
2. Copy, and then paste the following text.
    
  ```
  Windows Registry Editor Version 5.00
  [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings\WinHttp]
  "DefaultSecureProtocols"=dword:00000A80
  [HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Internet Settings\WinHttp]
  "DefaultSecureProtocols"=dword:00000A80
  ```

3. Save the **winhttp-tls10-tls12-enable.reg** file. 
    
4. Double-click the **winhttp-tls10-tls12-enable.reg** file. 
    
5. Click **Yes** to update your Windows Registry with these changes. 
    
6. Restart your computer for the change to take effect.
    
## 1.3 - Enable TLS 1.1 and TLS 1.2 support in Internet Explorer
<a name="enableIE"> </a>

Internet Explorer versions earlier than Internet Explorer 11 did not enable TLS 1.1 or TLS 1.2 support by default. Support for TLS 1.1 and TLS 1.2 is enabled by default starting with Internet Explorer 11.
  
 **To enable TLS 1.1 and TLS 1.2 support in Internet Explorer**
  
1. From Internet Explorer, click **Tools** > **Internet Options** > **Advanced** or click ![Displays settings menu for Internet Explorer](../media/99f37da8-4659-4833-84e8-c5ebe23c3acb.jpg) > **Internet Options** > **Advanced**. 
    
2. In the **Security** section, verify that the following check boxes are selected, if not click the following check boxes: 
    
  - Use TLS 1.1
    
  - Use TLS 1.2
    
3. Optionally, if you want to disable support for earlier security protocol versions, uncheck the following check boxes:
    
  - Use SSL 2.0
    
  - Use SSL 3.0
    
  - Use TLS 1.0
    
    > [!NOTE]
    > Disabling TLS 1.0 may cause compatibility issues with sites that don't support newer security protocol versions. Customers should test this change before performing it in production. 
  
4. Click **OK**. 
    
## 1.4 - Install SQL Server 2008 R2 Native Client update for TLS 1.2 support
<a name="InstallSQL"> </a>

The SQL Server 2008 R2 Native Client doesn't support TLS 1.1 or TLS 1.2 by default. You must install the SQL Server 2008 R2 Native Client update for TLS 1.2 support.
  
To install the SQL Server 2008 R2 Native Client update, see [SQL 2008 and 2008 R2 TLS 1.2 SQL Native Client updates not available in Windows Catalog.](https://www.microsoft.com/en-us/download/details.aspx?id=57606)
  
## 1.5 - Install .NET Framework 4.6 or higher
<a name="InstallNET46"> </a>

SharePoint 2013 requires .NET Framework 4.6, .NET Framework 4.6.1, or .NET Framework 4.6.2 to support TLS 1.2. Microsoft recommends installing the latest version of .NET Framework for the latest functionality and reliability improvements.
  
To install .NET Framework 4.6.2, see the KB article [Microsoft .NET Framework 4.6.2 (Web Installer) for Windows](https://support.microsoft.com/en-us/kb/3120737)
  
To install .NET Framework 4.6.1, see the KB article [The .NET Framework 4.6.1 web installer for Windows ](https://support.microsoft.com/en-us/kb/3102438)
  
To install .NET Framework 4.6, see the KB article [Microsoft .NET Framework 4.6 (Web Installer) for Windows](https://support.microsoft.com/en-us/kb/3045560)
  
## 1.6 - Enable strong cryptography in .NET Framework 4.6 or higher
<a name="CryptoNet45"> </a>

.NET Framework 4.6 and higher doesn't inherit its SSL and TLS encryption protocol version defaults from the Windows Schannel **DisabledByDefault** registry value. Instead, it uses its own SSL and TLS encryption protocol version defaults. To override the defaults, you must configure Windows Registry keys. 
  
The **SchUseStrongCrypto** registry value changes the .NET Framework 4.6 and higher encryption protocol version default from **SSL 3.0 or TLS 1.0** to **TLS 1.0 or TLS 1.1 or TLS 1.2**. In addition, it restricts the use of encryption algorithms with TLS that are considered weak such as RC4. 
  
Applications compiled for .NET Framework 4.6 or higher will behave as if the **SchUseStrongCrypto** registry value is set to 1, even if it isn't. To ensure all .NET Framework applications will use strong cryptography, you must configure this Windows Registry value. 
  
 **To enable strong cryptography in .NET Framework 4.6 or higher**
  
1. From Notepad.exe, create a text file named **net46-strong-crypto-enable.reg**. 
    
2. Copy, and then paste the following text.
    
  ```
  Windows Registry Editor Version 5.00
  [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\.NETFramework\v4.0.30319]
  "SchUseStrongCrypto"=dword:00000001
  [HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\.NETFramework\v4.0.30319]
  "SchUseStrongCrypto"=dword:00000001
  ```

3. Save the **net46-strong-crypto-enable.reg** file. 
    
4. Double-click the **net46-strong-crypto-enable.reg** file. 
    
5. Click **Yes** to update your Windows Registry with these changes. 
    
6. Restart your computer for the change to take effect.
    
## 1.7 - Install .NET Framework 3.5 update for TLS 1.1 and TLS 1.2 support
<a name="InstallFrame46"> </a>

.NET Framework 3.5 doesn't support TLS 1.1 or TLS 1.2 by default. To add support for TLS 1.1 and TLS 1.2, you must install a KB update, and then manually configure Windows Registry keys.
  
SharePoint 2013 is built on .NET Framework 4.x and doesn't use .NET Framework 3.5. However, certain prerequisite components and third party software that integrates with SharePoint 2013 may use .NET Framework 3.5. Microsoft recommends installing and configuring this update to improve compatibility with TLS 1.2.
  
The **SystemDefaultTlsVersions** registry value defines which security protocol version defaults will be used by .NET Framework 3.5. If the value is set to 0, .NET Framework 3.5 will default to **SSL 3.0 or TLS 1.0**. If the value is set to 1, .NET Framework 3.5 will inherit its defaults from the Windows Schannel **DisabledByDefault** registry values. If the value is undefined, it will behave as if the value is set to 0. 
  
 ** For Windows Server 2008 R2 **
  
1. To install the .NET Framework 3.5.1 update for Windows Server 2008 R2, see the KB article [Support for TLS System Default Versions included in the .NET Framework 3.5.1 on Windows 7 SP1 and Server 2008 R2 SP1](https://support.microsoft.com/kb/3154518)
    
2. After the KB update is installed, manually configure the registry keys.
    
 **For Windows Server 2012**
  
1. To install the .NET Framework 3.5 update for Windows Server 2012, see the KB article [Support for TLS System Default Versions included in the .NET Framework 3.5 on Windows Server 2012](https://support.microsoft.com/kb/3154519)
    
2. After the KB update is installed, manually configure the registry keys.
    
 **For Windows Server 2012 R2**
  
1. To install the .NET Framework 3.5 SP1 update for Windows Server 2012 R2, see the KB article [Support for TLS System Default Versions included in the .NET Framework 3.5 on Windows 8.1 and Windows Server 2012 R2](https://support.microsoft.com/kb/3154520)
    
2. After the KB update is installed, manually configure the registry keys.
    
 **To manually configure the registry keys, do the following:**
  
1. From Notepad.exe, create a text file named **net35-tls12-enable.reg**. 
    
2. Copy, and then paste the following text.
    
  ```
  Windows Registry Editor Version 5.00
  [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\.NETFramework\v2.0.50727]
  "SystemDefaultTlsVersions"=dword:00000001
  [HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\.NETFramework\v2.0.50727]
  "SystemDefaultTlsVersions"=dword:00000001
  ```

3. Save the **net35-tls12-enable.reg** file. 
    
4. Double-click the **net35-tls12-enable.reg** file. 
    
5. Click **Yes** to update your Windows Registry with these changes. 
    
6. Restart your computer for the change to take effect.
    
## 1.8 - Enable strong cryptography in .NET Framework 3.5
<a name="EnableCryptoFrame35"> </a>

The **SchUseStrongCrypto** registry value restricts the use of encryption algorithms with TLS that are considered weak such as RC4. 
  
Microsoft has released an optional security update for .NET Framework 3.5 that will automatically configure the Windows Registry keys for you. 
  
 **Windows Server 2008 R2**
  
To enable strong cryptography in .NET Framework 3.5.1 on Windows Server 2008 R2, see the KB article [Description of the security update for the .NET Framework 3.5.1 on Windows 7 Service Pack 1 and Windows Server 2008 R2 Service Pack 1: May 13, 2014](https://support.microsoft.com/kb/2898851)
  
 **Windows Server 2012**
  
To enable strong cryptography in .NET Framework 3.5 on Windows Server 2012, see the KB article [Description of the security update for the .NET Framework 3.5 on Windows 8 and Windows Server 2012: May 13, 2014](https://support.microsoft.com/kb/2898845)
  
 **Windows Server 2012 R2**
  
To enable strong cryptography in .NET Framework 3.5 on Windows Server 2012 R2 see the KB article [Description of the security update for the .NET Framework 3.5 on Windows 8.1 and Windows Server 2012 R2: May 13, 2014](https://support.microsoft.com/kb/2898847)
  
## 1.9 - Disable earlier versions of SSL and TLS in Windows Schannel
<a name="DisableTLSSchannel"> </a>

SSL and TLS support are enabled or disabled in Windows Schannel by editing the Windows Registry. Each SSL and TLS protocol version can be enabled or disabled independently. You don't need to enable or disable one protocol version to enable or disable another protocol version.
  
> [!IMPORTANT]
> Microsoft recommends disabling SSL 2.0 and SSL 3.0 due to serious security vulnerabilities in those protocol versions. >  Customers may also choose to disable TLS 1.0 and TLS 1.1 to ensure that only the newest protocol version is used. However, this may cause compatibility issues with software that doesn't support the newest TLS protocol version. Customers should test such a change before performing it in production. 
  
The **Enabled** registry value defines whether the protocol version can be used. If the value is set to 0, the protocol version cannot be used, even if it is enabled by default or if the application explicitly requests that protocol version. If the value is set to 1, the protocol version can be used if enabled by default or if the application explicitly requests that protocol version. If the value is not defined, it will use a default value determined by the operating system. 
  
The **DisabledByDefault** registry value defines whether the protocol version is used by default. This setting only applies when the application doesn't explicitly request the protocol versions to be used. If the value is set to 0, the protocol version will be used by default. If the value is set to 1, the protocol version will not be used by default. If the value is not defined, it will use a default value determined by the operating system. 
  
 **To disable SSL 2.0 support in Windows Schannel**
  
1. From Notepad.exe, create a text file named **ssl20-disable.reg**. 
    
2. Copy, and then paste the following text.
    
  ```
  Windows Registry Editor Version 5.00
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\SSL 2.0]
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\SSL 2.0\Client]
  "DisabledByDefault"=dword:00000001
  "Enabled"=dword:00000000
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\SSL 2.0\Server]
  "DisabledByDefault"=dword:00000001
  "Enabled"=dword:00000000
  ```

3. Save the **ssl20-disable.reg** file. 
    
4. Double-click the **ssl20-disable.reg** file. 
    
5. Click **Yes** to update your Windows Registry with these changes. 
    
6. Restart your computer for the change to take effect.
    
 **To disable SSL 3.0 support in Windows Schannel**
  
1. From Notepad.exe, create a text file named **ssl30-disable.reg**. 
    
2. Copy, and then paste the following text.
    
  ```
  Windows Registry Editor Version 5.00
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\SSL 3.0]
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\SSL 3.0\Client]
  "DisabledByDefault"=dword:00000001
  "Enabled"=dword:00000000
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\SSL 3.0\Server]
  "DisabledByDefault"=dword:00000001
  "Enabled"=dword:00000000
  ```

3. Save the **ssl30-disable.reg** file. 
    
4. Double-click the **ssl30-disable.reg** file. 
    
5. Click **Yes** to update your Windows Registry with these changes. 
    
6. Restart your computer for the change to take effect.
    
 **To disable TLS 1.0 support in Windows Schannel**
  
1. From Notepad.exe, create a text file named **tls10-disable.reg**. 
    
2. Copy, and then paste the following text.
    
  ```
  Windows Registry Editor Version 5.00
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.0]
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.0\Client]
  "DisabledByDefault"=dword:00000001
  "Enabled"=dword:00000000
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.0\Server]
  "DisabledByDefault"=dword:00000001
  "Enabled"=dword:00000000
  ```

3. Save the **tls10-disable.reg** file. 
    
4. Double-click the **tls10-disable.reg** file. 
    
5. Click **Yes** to update your Windows Registry with these changes. 
    
6. Restart your computer for the change to take effect.
    
 **To disable TLS 1.1 support in Windows Schannel**
  
1. From Notepad.exe, create a text file named **tls11-disable.reg**. 
    
2. Copy, and then paste the following text.
    
  ```
  Windows Registry Editor Version 5.00
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.1]
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.1\Client]
  "DisabledByDefault"=dword:00000001
  "Enabled"=dword:00000000
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.1\Server]
  "DisabledByDefault"=dword:00000001
  "Enabled"=dword:00000000
  ```

3. Save the **tls11-disable.reg** file. 
    
4. Double-click the **tls11-disable.reg** file. 
    
5. Click **Yes** to update your Windows Registry with these changes. 
    
6. Restart your computer for the change to take effect.
    
## Step 2: Update your Microsoft SQL Servers in your SharePoint farm
<a name="DisableTLSSchannel"> </a>

Follow these steps to update your SQL Servers in your SharePoint farm.
  
|**Steps for your SQL Servers**|**Windows Server 2008 R2**|**Windows Server 2012**|**Windows Server 2012 R2**|
|:-----|:-----|:-----|:-----|
|[2.1 - Enable TLS 1.1 and TLS 1.2 in Windows Schannel](/SharePoint/security-for-sharepoint-server/enable-tls-and-ssl-support-in-sharepoint-2013#enableTLS11) <br/> |Required  <br/> |N/A  <br/> |N/A  <br/> |
|[2.2 - Enable TLS 1.1 and TLS 1.2 support in Microsoft SQL Server](/SharePoint/security-for-sharepoint-server/enable-tls-and-ssl-support-in-sharepoint-2013#EnableTLS_SQLSrvr) <br/> |Required  <br/> |Required  <br/> |Required  <br/> |
|The following step is **optional**. Run this step depending on your organization's security and compliance requirements.  <br/> |
|[2.3 - Disable earlier versions of SSL and TLS in Windows Schannel](/SharePoint/security-for-sharepoint-server/enable-tls-and-ssl-support-in-sharepoint-2013#DisableSSL) <br/> |Optional  <br/> |Optional  <br/> |Optional  <br/> |
   
## 2.1 - Enable TLS 1.1 and TLS 1.2 in Windows Schannel
<a name="enableTLS11"> </a>

SSL and TLS support are enabled or disabled in Windows Schannel by editing the Windows Registry. Each SSL and TLS protocol version can be enabled or disabled independently. You don't need to enable or disable one protocol version to enable or disable another protocol version.
  
The **Enabled** registry value defines whether the protocol version can be used. If the value is set to 0, the protocol version cannot be used, even if it is enabled by default or if the application explicitly requests that protocol version. If the value is set to 1, the protocol version can be used if enabled by default or if the application explicitly requests that protocol version. If the value is not defined, it will use a default value determined by the operating system. 
  
The **DisabledByDefault** registry value defines whether the protocol version is used by default. This setting only applies when the application doesn't explicitly request the protocol versions to be used. If the value is set to 0, the protocol version will be used by default. If the value is set to 1, the protocol version will not be used by default. If the value is not defined, it will use a default value determined by the operating system. 
  
 **To enable TLS 1.1 support in Windows Schannel**
  
1. From Notepad.exe, create a text file named **tls11-enable.reg**. 
    
2. Copy, and then paste the following text.
    
  ```
  Windows Registry Editor Version 5.00
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.1]
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.1\Client]
  "DisabledByDefault"=dword:00000000
  "Enabled"=dword:00000001
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.1\Server]
  "DisabledByDefault"=dword:00000000
  "Enabled"=dword:00000001
  ```

3. Save the **tls11-enable.reg** file. 
    
4. Double-click the **tls11-enable.reg** file. 
    
5. Click **Yes** to update your Windows Registry with these changes. 
    
6. Restart your computer for the change to take effect.
    
 **To enable TLS 1.2 support in Windows Schannel**
  
1. From Notepad.exe, create a text file named **tls12-enable.reg**. 
    
2. Copy, and then paste the following text.
    
  ```
  Windows Registry Editor Version 5.00
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2]
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Client]
  "DisabledByDefault"=dword:00000000
  "Enabled"=dword:00000001
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Server]
  "DisabledByDefault"=dword:00000000
  "Enabled"=dword:00000001
  ```

3. Save the **tls12-enable.reg** file. 
    
4. Double-click the **tls12-enable.reg** file. 
    
5. Click **Yes** to update your Windows Registry with these changes. 
    
6. Restart your computer for the change to take effect.
    
## 2.2 - Enable TLS 1.1 and TLS 1.2 support in Microsoft SQL Server
<a name="EnableTLS_SQLSrvr"> </a>

SQL Server versions earlier than SQL Server 2016 don't support TLS 1.1 or TLS 1.2 by default. To add support for TLS 1.1 and TLS 1.2, you must install updates for SQL Server.
  
To enable TLS 1.1 and TLS 1.2 support in SQL Server, follow the instructions from the KB article [TLS 1.2 support for Microsoft SQL Server](https://support.microsoft.com/kb/3135244)
  
## 2.3 - Disable earlier versions of SSL and TLS in Windows Schannel
<a name="DisableSSL"> </a>

SSL and TLS support are enabled or disabled in Windows Schannel by editing the Windows Registry. Each SSL and TLS protocol version can be enabled or disabled independently. You don't need to enable or disable one protocol version to enable or disable another protocol version.
  
> [!IMPORTANT]
> Microsoft recommends disabling SSL 2.0 and SSL 3.0 due to serious security vulnerabilities in those protocol versions. >  Customers may also choose to disable TLS 1.0 and TLS 1.1 to ensure that only the newest protocol version is used. However, this may cause compatibility issues with software that doesn't support the newest TLS protocol version. Customers should test such a change before performing it in production. 
  
The **Enabled** registry value defines whether the protocol version can be used. If the value is set to 0, the protocol version cannot be used, even if it is enabled by default or if the application explicitly requests that protocol version. If the value is set to 1, the protocol version can be used if enabled by default or if the application explicitly requests that protocol version. If the value is not defined, it will use a default value determined by the operating system. 
  
The **DisabledByDefault** registry value defines whether the protocol version is used by default. This setting only applies when the application doesn't explicitly request the protocol versions to be used. If the value is set to 0, the protocol version will be used by default. If the value is set to 1, the protocol version will not be used by default. If the value is not defined, it will use a default value determined by the operating system. 
  
 **To disable SSL 2.0 support in Windows Schannel**
  
1. From Notepad.exe, create a text file named **ssl20-disable.reg**. 
    
2. Copy, and then paste the following text.
    
  ```
  Windows Registry Editor Version 5.00
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\SSL 2.0]
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\SSL 2.0\Client]
  "DisabledByDefault"=dword:00000001
  "Enabled"=dword:00000000
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\SSL 2.0\Server]
  "DisabledByDefault"=dword:00000001
  "Enabled"=dword:00000000
  ```

3. Save the **ssl20-disable.reg** file. 
    
4. Double-click the **ssl20-disable.reg** file. 
    
5. Click **Yes** to update your Windows Registry with these changes. 
    
6. Restart your computer for the change to take effect.
    
 **To disable SSL 3.0 support in Windows Schannel**
  
1. From Notepad.exe, create a text file named **ssl30-disable.reg**. 
    
2. Copy, and then paste the following text.
    
  ```
  Windows Registry Editor Version 5.00
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\SSL 3.0]
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\SSL 3.0\Client]
  "DisabledByDefault"=dword:00000001
  "Enabled"=dword:00000000
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\SSL 3.0\Server]
  "DisabledByDefault"=dword:00000001
  "Enabled"=dword:00000000
  ```

3. Save the **ssl30-disable.reg** file. 
    
4. Double-click the **ssl30-disable.reg** file. 
    
5. Click **Yes** to update your Windows Registry with these changes. 
    
6. Restart your computer for the change to take effect.
    
 **To disable TLS 1.0 support in Windows Schannel**
  
1. From Notepad.exe, create a text file named **tls10-disable.reg**. 
    
2. Copy, and then paste the following text.
    
  ```
  Windows Registry Editor Version 5.00
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.0]
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.0\Client]
  "DisabledByDefault"=dword:00000001
  "Enabled"=dword:00000000
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.0\Server]
  "DisabledByDefault"=dword:00000001
  "Enabled"=dword:00000000
  ```

3. Save the **tls10-disable.reg** file. 
    
4. Double-click the **tls10-disable.reg** file. 
    
5. Click **Yes** to update your Windows Registry with these changes. 
    
6. Restart your computer for the change to take effect.
    
 **To disable TLS 1.1 support in Windows Schannel**
  
1. From Notepad.exe, create a text file named **tls11-disable.reg**. 
    
2. Copy, and then paste the following text.
    
  ```
  Windows Registry Editor Version 5.00
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.1]
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.1\Client]
  "DisabledByDefault"=dword:00000001
  "Enabled"=dword:00000000
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.1\Server]
  "DisabledByDefault"=dword:00000001
  "Enabled"=dword:00000000
  ```

3. Save the **tls11-disable.reg** file. 
    
4. Double-click the **tls11-disable.reg** file. 
    
5. Click **Yes** to update your Windows Registry with these changes. 
    
6. Restart your computer for the change to take effect.
    
## Step 3: Update your client computers used to access your SharePoint sites
<a name="DisableSSL"> </a>

Follow these steps to update your client computers that access your SharePoint site.
  
|**Steps for your client computers**|**Windows 7**|**Windows 8.1**|**Windows 10**|
|:-----|:-----|:-----|:-----|
|[3.1 - Enable TLS 1.1 and TLS 1.2 in Windows Schannel](/SharePoint/security-for-sharepoint-server/enable-tls-and-ssl-support-in-sharepoint-2013#EnableTLS1.1_1.2) <br/> |Required  <br/> |N/A  <br/> |N/A  <br/> |
|[3.2 Enable TLS 1.1 and TLS 1.2 support in WinHTTP](/SharePoint/security-for-sharepoint-server/enable-tls-and-ssl-support-in-sharepoint-2013#EnabledTLS11_12) <br/> |Required  <br/> |N/A  <br/> |N/A  <br/> |
|[3.3 - Enable TLS 1.1 and TLS 1.2 support in Internet Explorer](/SharePoint/security-for-sharepoint-server/enable-tls-and-ssl-support-in-sharepoint-2013#enableIE2013) <br/> |Required  <br/> |N/A  <br/> |N/A  <br/> |
|[3.4 - Enable strong cryptography in .NET Framework 4.5 or higher](/SharePoint/security-for-sharepoint-server/enable-tls-and-ssl-support-in-sharepoint-2013#enablestrongcrypto4.5) <br/> |Required  <br/> |Required  <br/> |Required  <br/> |
|[3.5 - Install .NET Framework 3.5 update for TLS 1.1 and TLS 1.2 support](/SharePoint/security-for-sharepoint-server/enable-tls-and-ssl-support-in-sharepoint-2013#NETFramework3.5x) <br/> |Required  <br/> |Required  <br/> |Required  <br/> |
|The following ﻿step is **recommended**. Although not directly required by SharePoint Server 2013, they provide better security by restricting the use of weak encryption algorithms.  <br/> |
|[3.6 - Enable strong cryptography in .NET Framework 3.5](/SharePoint/security-for-sharepoint-server/enable-tls-and-ssl-support-in-sharepoint-2013#Enablecrypto3.5x) <br/> |Recommended  <br/> |Recommended  <br/> |Recommended  <br/> |
|The following ﻿step is **optional**. You may choose to run this step based on your organization's security and compliance requirements.  <br/> |
|[3.7 - Disable earlier versions of SSL and TLS in Windows Schannel](/SharePoint/security-for-sharepoint-server/enable-tls-and-ssl-support-in-sharepoint-2013#DisableSSL_TLS) <br/> |Optional  <br/> |Optional  <br/> |Optional  <br/> |
   
## 3.1 - Enable TLS 1.1 and TLS 1.2 in Windows Schannel
<a name="EnableTLS1.1_1.2"> </a>

SSL and TLS support are enabled or disabled in Windows Schannel by editing the Windows Registry. Each SSL and TLS protocol version can be enabled or disabled independently. You don't need to enable or disable one protocol version to enable or disable another protocol version.
  
The **Enabled** registry value defines whether the protocol version can be used. If the value is set to 0, the protocol version cannot be used, even if it is enabled by default or if the application explicitly requests that protocol version. If the value is set to 1, the protocol version can be used if enabled by default or if the application explicitly requests that protocol version. If the value is not defined, it will use a default value determined by the operating system. 
  
The **DisabledByDefault** registry value defines whether the protocol version is used by default. This setting only applies when the application doesn't explicitly request the protocol versions to be used. If the value is set to 0, the protocol version will be used by default. If the value is set to 1, the protocol version will not be used by default. If the value is not defined, it will use a default value determined by the operating system. 
  
 **To enable TLS 1.1 support in Windows Schannel**
  
1. From Notepad.exe, create a text file named **tls11-enable.reg**. 
    
2. Copy, and then paste the following text.
    
  ```
  Windows Registry Editor Version 5.00
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.1]
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.1\Client]
  "DisabledByDefault"=dword:00000000
  "Enabled"=dword:00000001
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.1\Server]
  "DisabledByDefault"=dword:00000000
  "Enabled"=dword:00000001
  ```

3. Save the **tls11-enable.reg** file. 
    
4. Double-click the **tls11-enable.reg** file. 
    
5. Click **Yes** to update your Windows Registry with these changes. 
    
6. Restart your computer for the change to take effect.
    
 **To enable TLS 1.2 support in Windows Schannel**
  
1. From Notepad.exe, create a text file named **tls12-enable.reg**. 
    
2. Copy, and then paste the following text.
    
  ```
  Windows Registry Editor Version 5.00
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2]
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Client]
  "DisabledByDefault"=dword:00000000
  "Enabled"=dword:00000001
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Server]
  "DisabledByDefault"=dword:00000000
  "Enabled"=dword:00000001
  ```

3. Save the **tls12-enable.reg** file. 
    
4. Double-click the **tls12-enable.reg** file. 
    
5. Click **Yes** to update your Windows Registry with these changes. 
    
6. Restart your computer for the change to take effect.
    
## 3.2 Enable TLS 1.1 and TLS 1.2 support in WinHTTP
<a name="EnabledTLS11_12"> </a>

WinHTTP doesn't inherit its SSL and TLS encryption protocol version defaults from the Windows Schannel **DisabledByDefault** registry value. WinHTTP uses its own SSL and TLS encryption protocol version defaults, which vary by operating system. To override the defaults, you must install a KB update and configure Windows Registry keys. 
  
The WinHTTP ** DefaultSecureProtocols ** registry value is a bit field that accepts multiple values by adding them together into a single value. You can use the Windows Calculator program (Calc.exe) in Programmer mode to add the following hexadecimal values as desired. 
  
## 
<a name="EnabledTLS11_12"> </a>

|**DefaultSecureProtocols value**|**Description**|
|:-----|:-----|
|0x00000008  <br/> |Enable SSL 2.0 by default  <br/> |
|0x00000020  <br/> |Enable SSL 3.0 by default  <br/> |
|0x00000080  <br/> |Enable TLS 1.0 by default  <br/> |
|0x00000200  <br/> |Enable TLS 1.1 by default  <br/> |
|0x00000800  <br/> |Enable TLS 1.2 by default  <br/> |
   
For example, you can enable TLS 1.0, TLS 1.1, and TLS 1.2 by default by adding the values 0x00000080, 0x00000200, and 0x00000800 together to form the value 0x00000A80.
  
To install the WinHTTP KB update, follow the instructions from the KB article [Update to enable TLS 1.1 and TLS 1.2 as a default secure protocols in WinHTTP in Windows](https://support.microsoft.com/kb/3140245)
  
 **To enable TLS 1.0, TLS 1.1, and TLS 1.2 by default in WinHTTP**
  
1. From Notepad.exe, create a text file named **winhttp-tls10-tls12-enable.reg**. 
    
2. Copy, and then paste the following text.
    
    **For 64-bit operating system**
    
  ```
  Windows Registry Editor Version 5.00
  [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings\WinHttp]
  "DefaultSecureProtocols"=dword:00000A80
  [HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Internet Settings\WinHttp]
  "DefaultSecureProtocols"=dword:00000A80
  ```

    **For 32-bit operating system**
    
  ```
  [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings\WinHttp]
  "DefaultSecureProtocols"=dword:00000A80
  ```

3. Save the **winhttp-tls10-tls12-enable.reg** file. 
    
4. Double-click the **winhttp-tls10-tls12-enable.reg** file. 
    
5. Click **Yes** to update your Windows Registry with these changes. 
    
6. Restart your computer for the change to take effect.
    
## 3.3 - Enable TLS 1.1 and TLS 1.2 support in Internet Explorer
<a name="enableIE2013"> </a>

Internet Explorer versions earlier than Internet Explorer 11 did not enable TLS 1.1 or TLS 1.2 support by default. Support for TLS 1.1 and TLS 1.2 is enabled by default starting with Internet Explorer 11.
  
 **To enable TLS 1.1 and TLS 1.2 support in Internet Explorer**
  
1. From Internet Explorer, click **Tools** > **Internet Options** > **Advanced** or click ![Displays settings menu for Internet Explorer](../media/99f37da8-4659-4833-84e8-c5ebe23c3acb.jpg) > **Internet Options** > **Advanced**. 
    
2. In the **Security** section, verify that the following check boxes are selected. If not, click the following check boxes: 
    
  - Use TLS 1.1
    
  - Use TLS 1.2
    
3. Optionally, if you want to disable support for earlier security protocol versions, uncheck the following check boxes:
    
  - Use SSL 2.0
    
  - Use SSL 3.0
    
  - Use TLS 1.0
    
    > [!NOTE]
    > Disabling TLS 1.0 may cause compatibility issues with sites that don't support newer security protocol versions. Customers should test this change before performing it in production. 
  
4. Click **OK**. 
    
## 3.4 - Enable strong cryptography in .NET Framework 4.5 or higher
<a name="enablestrongcrypto4.5"> </a>

.NET Framework 4.5 and higher doesn't inherit its SSL and TLS encryption protocol version defaults from the Windows Schannel **DisabledByDefault** registry value. Instead, it uses its own SSL and TLS encryption protocol version defaults. To override the defaults, you must configure Windows Registry keys. 
  
The **SchUseStrongCrypto** registry value changes the .NET Framework 4.5 and higher security protocol version default from **SSL 3.0 or TLS 1.0** to **TLS 1.0 or TLS 1.1 or TLS 1.2**. In addition, it restricts the use of encryption algorithms with TLS that are considered weak such as RC4. 
  
Applications compiled for .NET Framework 4.6 or higher will behave as if the **SchUseStrongCrypto** registry value is set to 1, even if it isn't. To ensure all .NET Framework applications will use strong cryptography, you must configure this Windows Registry value. 
  
Microsoft has released an optional security update for .NET Framework 4.5, 4.5.1, and 4.5.2 that will automatically configure the Windows Registry keys for you. No updates are available for .NET Framework 4.6 or higher. You must manually configure the Windows Registry keys on .NET Framework 4.6 or higher.
  
 **For Windows 7 and Windows Server 2008 R2**
  
To enable strong cryptography in .NET Framework 4.5 and 4.5.1 on Windows 7 and Windows Server 2008 R2, see the KB article [Description of the security update for the .NET Framework 4.5 and the .NET Framework 4.5.1 on Windows 7 Service Pack 1 and Windows Server 2008 R2 Service Pack 1: May 13, 2014](https://support.microsoft.com/kb/2938782).
  
To enable strong cryptography in .NET Framework 4.5.2 on Windows 7 and Windows Server 2008 R2, see the KB article [Description of the security update for the .NET Framework 4.5.2 on Windows 7 Service Pack 1 and Windows Server 2008 R2 Service Pack 1: May 13, 2014](https://support.microsoft.com/kb/2954853).
  
 **For Windows Server 2012**
  
To enable strong cryptography in .NET Framework 4.5, 4.5.1, and 4.5.2 on Windows Server 2012, see the KB article [Description of the security update for the .NET Framework 4.5, the .NET Framework 4.5.1, and the .NET Framework 4.5.2 on Windows 8, Windows RT, and Windows Server 2012: May 13, 2014](https://support.microsoft.com/kb/2898849).
  
 **Windows 8.1 and Windows Server 2012 R2**
  
To enable strong cryptography in .NET Framework 4.5.1 and 4.5.2 on Windows 8.1 and Windows Server 2012 R2, see the KB article [Description of the security update for the .NET Framework 4.5.1 and the .NET Framework 4.5.2 on Windows 8.1, Windows RT 8.1, and Windows Server 2012 R2: May 13, 2014](https://support.microsoft.com/kb/2898850).
  
 **To enable strong cryptography in .NET Framework 4.6 or higher**
  
1. From Notepad.exe, create a text file named **net46-strong-crypto-enable.reg**. 
    
2. Copy, and then paste the following text.
    
    **For 64-bit operating system**
    
  ```
  Windows Registry Editor Version 5.00
  [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\.NETFramework\v4.0.30319]
  "SchUseStrongCrypto"=dword:00000001
  [HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\.NETFramework\v4.0.30319]
  "SchUseStrongCrypto"=dword:00000001
  ```

    **For 32-bit operating system**
    
  ```
  Windows Registry Editor Version 5.00
  [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\.NETFramework\v4.0.30319]
  "SchUseStrongCrypto"=dword:00000001
  ```

3. Save the **net46-strong-crypto-enable.reg** file. 
    
4. Double-click the **net46-strong-crypto-enable.reg** file. 
    
5. Click **Yes** to update your Windows Registry with these changes. 
    
6. Restart your computer for the change to take effect.
    
## 3.5 - Install .NET Framework 3.5 update for TLS 1.1 and TLS 1.2 support
<a name="NETFramework3.5x"> </a>

.NET Framework 3.5 doesn't support TLS 1.1 or TLS 1.2 by default. To add support for TLS 1.1 and TLS 1.2, you must install a KB update, and then manually configure Windows Registry keys for each of the operating systems listed in this section.
  
The **SystemDefaultTlsVersions** registry value defines which security protocol version defaults will be used by .NET Framework 3.5. If the value is set to 0, .NET Framework 3.5 will default to **SSL 3.0 or TLS 1.0**. If the value is set to 1, .NET Framework 3.5 will inherit its defaults from the Windows Schannel **DisabledByDefault** registry values. If the value is undefined, it will behave as if the value is set to 0. 
  
 **To enable .NET Framework 3.5 to inherit its encryption protocol defaults from Windows**
  
 **Windows 7 and Windows Server 2008 R2**
  
1. To install the .NET Framework 3.5.1 update for Windows 7 and Windows Server 2008 R2, see the KB article [Support for TLS System Default Versions included in the .NET Framework 3.5.1 on Windows 7 SP1 and Server 2008 R2 SP1](https://support.microsoft.com/kb/3154518) . 
    
2. After the KB update is installed, manually configure the registry keys.
    
 **For Windows Server 2012**
  
1. To install the .NET Framework 3.5 update for Windows Server 2012, see the KB article [Support for TLS System Default Versions included in the .NET Framework 3.5 on Windows Server 2012](https://support.microsoft.com/kb/3154519)
    
2. After the KB update is installed, manually configure the registry keys.
    
 **Windows 8.1 and Windows Server 2012 R2**
  
1. To install the .NET Framework 3.5 SP1 update for Windows 8.1 and Windows Server 2012 R2, see the KB article [Support for TLS System Default Versions included in the .NET Framework 3.5 on Windows 8.1 and Windows Server 2012 R2 ](https://support.microsoft.com/kb/3154520)
    
2. After the KB update is installed, manually configure the registry keys.
    
 **Windows 10 (Version 1507)**
  
- This functionality is not available in Windows 10 Version 1507. You must upgrade to Windows 10 Version 1511, and then install the [Cumulative Update for Windows 10 Version 1511 and Windows Server 2016 Technical Preview 4: May 10, 2016](https://support.microsoft.com/kb/3156421), or upgrade to Windows 10 Version 1607 or higher.
    
 **Windows 10 (Version 1511)**
  
1. To install the Cumulative Update for Windows 10 Version 1511 and Windows Server 2016 Technical Preview 4: May 10, 2016, see [Cumulative Update for Windows 10 Version 1511 and Windows Server 2016 Technical Preview 4: May 10, 2016](https://support.microsoft.com/kb/3156421).
    
2. After the KB update is installed, manually configure the registry keys.
    
 **Windows 10 (Version 1607) and Windows Server 2016**
  
No update needs to be installed. Configure the Windows Registry keys as described below.
  
 **To manually configure the registry keys, do the following:**
  
1. From Notepad.exe, create a text file named **net35-tls12-enable.reg**. 
    
2. Copy, and then paste the following text.
    
    **For 64-bit operating system**
    
  ```
  Windows Registry Editor Version 5.00
  [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\.NETFramework\v2.0.50727]
  "SystemDefaultTlsVersions"=dword:00000001
  [HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\.NETFramework\v2.0.50727]
  "SystemDefaultTlsVersions"=dword:00000001
  ```

    **For 32-bit operating system**
    
  ```
  Windows Registry Editor Version 5.00
  [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\.NETFramework\v2.0.50727]
  "SystemDefaultTlsVersions"=dword:00000001
  ```

3. Save the **net35-tls12-enable.reg** file. 
    
4. Double-click the **net35-tls12-enable.reg** file. 
    
5. Click **Yes** to update your Windows Registry with these changes. 
    
6. Restart your computer for the change to take effect.
    
## 3.6 - Enable strong cryptography in .NET Framework 3.5
<a name="Enablecrypto3.5x"> </a>

The **SchUseStrongCrypto** registry value restricts the use of encryption algorithms with TLS that are considered weak such as RC4. 
  
Microsoft has released an optional security update for .NET Framework 3.5 on pre-Windows 10 operating systems that will automatically configure the Windows Registry keys for you. No updates are available for Windows 10. You must manually configure the Windows Registry keys on Windows 10.
  
 **Windows 7 and Windows Server 2008 R2**
  
To enable strong cryptography in .NET Framework 3.5.1 on Windows 7 and Windows Server 2008 R2, see the KB article [Description of the security update for the .NET Framework 3.5.1 on Windows 7 Service Pack 1 and Windows Server 2008 R2 Service Pack 1: May 13, 2014](https://support.microsoft.com/kb/2898851)
  
 **For Windows Server 2012**
  
To enable strong cryptography in .NET Framework 3.5 on Windows Server 2012, see the KB article [Description of the security update for the .NET Framework 3.5 on Windows 8 and Windows Server 2012: May 13, 2014](https://support.microsoft.com/kb/2898845)
  
 **Windows 8.1 and Windows Server 2012 R2**
  
To enable strong cryptography in .NET Framework 3.5 on Windows 8.1 and Windows Server 2012 R2 see the KB article [Description of the security update for the .NET Framework 3.5 on Windows 8.1 and Windows Server 2012 R2: May 13, 2014](https://support.microsoft.com/kb/2898847)
  
 **To enable strong cryptography in .NET Framework 3.5 on Windows 10 and Windows Server 2016**
  
1. From Notepad.exe, create a text file named **net35-strong-crypto-enable.reg**. 
    
2. Copy, and then paste the following text.
    
    **For 64-bit operating system**
    
  ```
  Windows Registry Editor Version 5.00
  [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\.NETFramework\v2.0.50727]
  "SchUseStrongCrypto"=dword:00000001
  [HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\.NETFramework\v2.0.50727]
  "SchUseStrongCrypto"=dword:00000001
  ```

    **For 32-bit operating system**
    
  ```
  Windows Registry Editor Version 5.00
  [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\.NETFramework\v2.0.50727]
  "SchUseStrongCrypto"=dword:00000001
  ```

3. Save the **net35-strong-crypto-enable.reg** file. 
    
4. Double-click the **net35-strong-crypto-enable.reg** file. 
    
5. Click **Yes** to update your Windows Registry with these changes. 
    
6. Restart your computer for the change to take effect.
    
## 3.7 - Disable earlier versions of SSL and TLS in Windows Schannel
<a name="DisableSSL_TLS"> </a>

SSL and TLS support are enabled or disabled in Windows Schannel by editing the Windows Registry. Each SSL and TLS protocol version can be enabled or disabled independently. You don't need to enable or disable one protocol version to enable or disable another protocol version.
  
> [!IMPORTANT]
> Microsoft recommends disabling SSL 2.0 and SSL 3.0 due to serious security vulnerabilities in those protocol versions. >  Customers may also choose to disable TLS 1.0 and TLS 1.1 to ensure that only the newest protocol version is used. However, this may cause compatibility issues with software that doesn't support the newest TLS protocol version. Customers should test such a change before performing it in production. 
  
The **Enabled** registry value defines whether the protocol version can be used. If the value is set to 0, the protocol version cannot be used, even if it is enabled by default or if the application explicitly requests that protocol version. If the value is set to 1, the protocol version can be used if enabled by default or if the application explicitly requests that protocol version. If the value is not defined, it will use a default value determined by the operating system. 
  
The **DisabledByDefault** registry value defines whether the protocol version is used by default. This setting only applies when the application doesn't explicitly request the protocol versions to be used. If the value is set to 0, the protocol version will be used by default. If the value is set to 1, the protocol version will not be used by default. If the value is not defined, it will use a default value determined by the operating system. 
  
 **To disable SSL 2.0 support in Windows Schannel**
  
1. From Notepad.exe, create a text file named **ssl20-disable.reg**. 
    
2. Copy, and then paste the following text.
    
  ```
  Windows Registry Editor Version 5.00
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\SSL 2.0]
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\SSL 2.0\Client]
  "DisabledByDefault"=dword:00000001
  "Enabled"=dword:00000000
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\SSL 2.0\Server]
  "DisabledByDefault"=dword:00000001
  "Enabled"=dword:00000000
  ```

3. Save the **ssl20-disable.reg** file. 
    
4. Double-click the **ssl20-disable.reg** file. 
    
5. Click **Yes** to update your Windows Registry with these changes. 
    
6. Restart your computer for the change to take effect.
    
 **To disable SSL 3.0 support in Windows Schannel**
  
1. From Notepad.exe, create a text file named **ssl30-disable.reg**. 
    
2. Copy, and then paste the following text.
    
  ```
  Windows Registry Editor Version 5.00
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\SSL 3.0]
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\SSL 3.0\Client]
  "DisabledByDefault"=dword:00000001
  "Enabled"=dword:00000000
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\SSL 3.0\Server]
  "DisabledByDefault"=dword:00000001
  "Enabled"=dword:00000000
  ```

3. Save the **ssl30-disable.reg** file. 
    
4. Double-click the **ssl30-disable.reg** file. 
    
5. Click **Yes** to update your Windows Registry with these changes. 
    
6. Restart your computer for the change to take effect.
    
 **To disable TLS 1.0 support in Windows Schannel**
  
1. From Notepad.exe, create a text file named **tls10-disable.reg**. 
    
2. Copy, and then paste the following text.
    
  ```
  Windows Registry Editor Version 5.00
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.0]
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.0\Client]
  "DisabledByDefault"=dword:00000001
  "Enabled"=dword:00000000
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.0\Server]
  "DisabledByDefault"=dword:00000001
  "Enabled"=dword:00000000
  ```

3. Save the **tls10-disable.reg** file. 
    
4. Double-click the **tls10-disable.reg** file. 
    
5. Click **Yes** to update your Windows Registry with these changes. 
    
6. Restart your computer for the change to take effect.
    
 **To disable TLS 1.1 support in Windows Schannel**
  
1. From Notepad.exe, create a text file named **tls11-disable.reg**. 
    
2. Copy, and then paste the following text.
    
  ```
  Windows Registry Editor Version 5.00
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.1]
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.1\Client]
  "DisabledByDefault"=dword:00000001
  "Enabled"=dword:00000000
  [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.1\Server]
  "DisabledByDefault"=dword:00000001
  "Enabled"=dword:00000000
  ```

3. Save the **tls11-disable.reg** file. 
    
4. Double-click the **tls11-disable.reg** file. 
    
5. Click **Yes** to update your Windows Registry with these changes. 
    
6. Restart your computer for the change to take effect.
    

