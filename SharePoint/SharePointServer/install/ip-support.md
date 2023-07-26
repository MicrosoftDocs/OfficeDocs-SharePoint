---
title: "IP support in SharePoint Server"
ms.reviewer: 
ms.author: serdars
author: SerdarSoysal
manager: serdars
ms.date: 2/15/2018
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: interactive-tutorial
ms.service: sharepoint-server-itpro
ms.localizationpriority: medium
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: c5b49fbd-4c1a-4188-a509-373298e92c1b
description: "SharePoint Server supports Internet Protocol Version 4 (IPv4) and Internet Protocol Version 6 (IPv6)."
---

# IP support in SharePoint Server

[!INCLUDE[appliesto-2013-2016-2019-SUB-xxx-md](../includes/appliesto-2013-2016-2019-SUB-xxx-md.md)]
  
SharePoint Server supports the following environments:
  
- IPv4-only
    
    In an IPv4-only environment, the network infrastructure supports address assignment, name registration and resolution, and routing for only IPv4-based network traffic.
    > [!NOTE]
    > Even in an IPv4-only environment, the recommendation is that you leave IPv6 enabled on your Windows-based computers. If the network infrastructure doesn't support IPv6 traffic, SharePoint uses IPv4 traffic.
    
- Mixed IPv4 and IPv6
    
    In a mixed IPv4 and IPv6 environment, the network infrastructure supports address assignment, name registration and resolution, and routing for both IPv4 and IPv6-based network traffic.
    
- IPv6-only
    
    In an IPv6-only environment, the network infrastructure supports address assignment, name registration and resolution, and routing for only IPv6-based network traffic.
    
In a SharePoint environment, "mixed" can be defined as one of the following likely scenarios:
  
- Both IPv4 and IPv6 protocols are running on hosts. It's also known as a dual-stack environment, in which both the IPv4 and IPv6 protocol stacks are enabled and being used.
    
- Some of your client computers are using only IPv4, some of them are using only IPv6, and some of them are using both IPv4 and IPv6.
    
- Your client computers are using only IPv4, but the server computers are using both IPv4 and IPv6.

By default, the IPv6 protocol and the IPv4 protocol are both installed and enabled on Windows 7 or newer client operating systems, and Windows Server 2008 or newer server operating systems. When both IPv4 and IPv6 are enabled, IPv6 is preferred over IPv4 when you're using names and Domain Name System (DNS) name query responses contain both types of addresses. Additionally, you can remove the IPv4 protocol so that the computer runs only IPv6.
  
To determine which versions are being used on your network, you can use the IPConfig.exe tool. If the display of the [IPConfig](/previous-versions/windows/it-pro/windows-2000-server/cc940124(v=technet.10)) command at a Command Prompt contains rows named "IPv6 Address" or "Temporary IPv6 Address," you have IPv6 in your environment. If all of the IPv6 addresses begin with "fe80" and correspond to rows named "Link-Local IPv6 Address," you don't have IPv6 in your environment. For more information, see [IPConfig](/previous-versions/windows/it-pro/windows-2000-server/cc940124(v=technet.10)).
  
The following list shows other important considerations about IPv6:
  
- For any computer that is authenticated by using a domain controller and is only running IPv6 in a SharePoint Server environment, the domain controller must be running Windows Server 2008 or newer server operating systems. Ensure that you use the correct service pack and any other software prerequisites. For more information, see [Hardware and software requirements for SharePoint Server 2016](hardware-and-software-requirements.md).
    
- All versions of SQL Server supported for SharePoint Server also support IPv6. For more information about IPv6 support for SQL Server 2008, see [Connecting Using IPv6](https://go.microsoft.com/fwlink/p/?LinkId=183115). 
    
- When SharePoint Server uses the IPv6 protocol, all end-user URLs must be based on DNS names with AAAA records. For more information about AAAA records, see [Adding a Resource Record to a Forward Lookup Zone](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc816819(v=ws.10)).
    
- Browsing to SharePoint URLs that use IPv6 literal addresses isn't supported. An example of a literal address URL is http://[2001:db8:85a3:8d3:1319:8a2e:370:7344]. However, you can enter IPv6 literal addresses for certain farm administration tasks, such as entering the server name when you create or attach databases. For server names that use a literal address format, you must enclose the literal address within square brackets.

- Versions of SharePoint that are older than SharePoint Server 2016 don't support the configuration of IPv6 literal addresses when specifying an outbound Simple Mail Transfer Protocol (SMTP) server. For these versions, the recommendation is to specify a DNS name for the SMTP server, which can resolve to an IPv4 address OR an IPv6 address, or both. If you don't have a DNS name for the SMTP server and must supply an IPv6 address, you can configure the corresponding 'ipv6-literal.net' name for the address.

     To create an ipv6-literal.net name for an IPv6 address, convert the colons (:) in the address to dashes (-), then add the result to ipv6-literal.net. For example, for the IPv6 address 2001:db8:28:3:f98a:5b31:67b7:67ef, the corresponding ipv6-literal.net name is '2001-db8-28-3-f98a-5b31-67b7-67ef.ipv6-literal.net'.

    > [!NOTE]
    > Although SharePoint supports the configuration of IPv6 literal addresses when specifying an outbound SMTP server starting with SharePoint Server 2016, additional configuration settings may be required to successfully send emails. For example, if a TLS connection encryption is enabled, then the outbound SMTP server name specified in SharePoint must be present in the SMTP server certificate. Specifying an IPv6 literal address for the outbound SMTP server would require IPv6 literal address to be present in the SMTP server certificate.

- Some SharePoint features or components integrate with cloud services - such as SharePoint Help, SharePoint Translation Service, and SharePoint apps that use the Azure Access Control Service (ACS) - which might not yet be IPv6-capable. Therefore, ensure that your SharePoint servers are IPv4-capable, which includes both IPv4-only and mixed IPv4 and IPv6 environments until all of the SharePoint-dependent cloud services become IPv6-capable. For more info, see [IPv6 Support in Office 365 Services](/office365/enterprise/ipv6-support) and [Internet Protocol Version 6 (IPv6) Overview](/previous-versions/windows/it-pro/windows-8.1-and-8/hh831730(v=ws.11)).

For more information about IPv6 in Microsoft products, see the [IPv6 TechCenter](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd379473(v=ws.10)).
  
## See also

[IPv6 Survival Guide in the TechNet Wiki](https://go.microsoft.com/fwlink/p/?LinkId=237480)