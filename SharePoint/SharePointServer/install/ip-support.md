---
title: "IP support in SharePoint 2013"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 2/15/2018
audience: ITPro
ms.topic: interactive-tutorial
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.collection:
- IT_Sharepoint_Server
- IT_Sharepoint_Server_Top
ms.assetid: c5b49fbd-4c1a-4188-a509-373298e92c1b
description: "SharePoint 2013 supports Internet Protocol Version 4 (IPv4) and Internet Protocol Version 6 (IPv6)."
---

# IP support in SharePoint 2013

[!INCLUDE[appliesto-2013-xxx-xxx-xxx-md](../includes/appliesto-2013-xxx-xxx-xxx-md.md)] 
  
SharePoint Server 2013 supports the following environments:
  
- IPv4-only
    
    In an IPv4-only environment, the network infrastructure supports address assignment, name registration and resolution, and routing for only IPv4-based network traffic. Note that even in an IPv4-only environment, the recommendation is that you leave IPv6 enabled on your Windows-based computers. If the network infrastructure does not support IPv6 traffic, SharePoint will use IPv4 traffic.
    
- Mixed IPv4 and IPv6
    
    In a mixed IPv4 and IPv6 environment, the network infrastructure supports address assignment, name registration and resolution, and routing for both IPv4 and IPv6-based network traffic.
    
- IPv6-only
    
    In an IPv6-only environment, the network infrastructure supports address assignment, name registration and resolution, and routing for only IPv6-based network traffic.
    
In a SharePoint environment, "mixed" can be defined as one of the following likely scenarios:
  
- Both IPv4 and IPv6 protocols are running on hosts. This is also known as a dual-stack environment, in which both the IPv4 and IPv6 protocol stacks are enabled and being used.
    
- Some of your client computers are using only IPv4, some of them are using only IPv6, and some of them are using both IPv4 and IPv6.
    
- Your client computers are using only IPv4, but the server computers are using both IPv4 and IPv6.
    
By default, the IPv6 protocol and the IPv4 protocol are both installed and enabled in Windows 8, Windows Server 2012, Windows 7, Windows Server 2008 R2, Windows Vista, and Windows Server 2008. When both IPv4 and IPv6 are enabled, IPv6 is preferred over IPv4 when you are using names and Domain Name System (DNS) name query responses contain both types of addresses. Additionally, you can remove the IPv4 protocol so that the computer runs only IPv6.
  
To determine what versions are being used on your network, you can use the IPConfig.exe tool. If the display of the [IPConfig](https://go.microsoft.com/fwlink/p/?LinkId=507022) command at a Command Prompt contains rows named "IPv6 Address" or "Temporary IPv6 Address," you have IPv6 in your environment. If all of the IPv6 addresses begin with "fe80" and correspond to rows named "Link-Local IPv6 Address," you do not have IPv6 in your environment. For additional information, see [IPConfig](https://go.microsoft.com/fwlink/p/?LinkId=507022).
  
The following list shows other important considerations about IPv6:
  
- For any computer that is authenticated by using a domain controller and is only running IPv6 in a SharePoint Server 2013 environment, the domain controller must be running Windows Server 2012, Windows Server 2008, or Windows Server 2008 R2. Ensure that you use the correct service pack and any additional software prerequisites. For more information, see [Hardware and software requirements for SharePoint Server 2016](hardware-and-software-requirements.md).
    
- All versions of SQL Server supported for SharePoint Server 2013 also support IPv6. For more information about IPv6 support for SQL Server 2008, see [Connecting Using IPv6](https://go.microsoft.com/fwlink/p/?LinkId=183115) (https://go.microsoft.com/fwlink/p/?LinkId=183115). 
    
- When SharePoint Server 2013 uses the IPv6 protocol, all end-user URLs must be based on DNS names with AAAA records. For more information about AAAA records, see [Adding a Resource Record to a Forward Lookup Zone](https://go.microsoft.com/fwlink/p/?LinkId=507021).
    
- Browsing to SharePoint URLs that use IPv6 literal addresses is not supported. An example of a literal address URL is http://[2001:db8:85a3:8d3:1319:8a2e:370:7344]. However, you can enter IPv6 literal addresses for certain farm administration tasks, such as entering the server name when you create or attach databases. For server names that use a literal address format, you must enclose the literal address within square brackets.
    
- When specifying an outbound Simple Mail Transfer Protocol (SMTP) server, SharePoint does not support the configuration of IPv6 literal addresses. The recommendation is to specify a DNS name for the SMTP server, which can resolve to an IPv4 address, an IPv6 address, or both. If you do not have a DNS name for the SMTP server and must supply an IPv6 address, you can configure the corresponding ipv6-literal.net name for the address.
    
    To create an ipv6-literal.net name for an IPv6 address, convert the colons (:) in the address to dashes (-), then add the result to "ipv6-literal.net". For example, for the IPv6 address 2001:db8:28:3:f98a:5b31:67b7:67ef, the corresponding ipv6-literal.net name is 2001-db8-28-3-f98a-5b31-67b7-67ef.ipv6-literal.net.
    
- Some SharePoint features or components integrate with cloud services - such as SharePoint Help, SharePoint Translation Service, and SharePoint apps that use the Azure Access Control Service (ACS) - which might not yet be IPv6-capable. Therefore, make sure that your SharePoint servers are IPv4-capable, which includes both IPv4-only and mixed IPv4 and IPv6 environments, until all of the SharePoint-dependent cloud services become IPv6-capable. For more information, see [IPv6 Support in Office 365 Services] (https://docs.microsoft.com/en-us/office365/enterprise/ipv6-support) and [Internet Protocol Version 6 (IPv6) Overview](https://go.microsoft.com/fwlink/p/?LinkId=507023).
    
For additional information about IPv6 in Microsoft products, see the [IPv6 TechCenter](https://go.microsoft.com/fwlink/p/?LinkId=71543).
  
## See also

#### Other Resources

[IPv6 Survival Guide in the TechNet Wiki](https://go.microsoft.com/fwlink/p/?LinkId=237480)

