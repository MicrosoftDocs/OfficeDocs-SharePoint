---
title: "Network utilization planning for the OneDrive sync app"
ms.reviewer: 
ms.author: adjoseph
author: adeejoseph
manager: serdars
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: conceptual
ms.service: one-drive
ms.localizationpriority: medium
ms.collection: 
- Strat_OD_admin
- M365-collaboration
ms.custom:
- seo-marvel-apr2020
- onedrive-toc
search.appverid:
- ODB160
- ODB150
- GOB150
- GOB160
- MET150
ms.assetid: b664e743-ae8b-4a93-aefd-1b20c584a93a
description: "Learn how IT admins can estimate the network bandwidth that users will need to sync their files with the OneDrive sync app."
---

# Network utilization planning for the OneDrive sync app

This article is for IT admins planning to deploy the OneDrive sync app and wanting to estimate the network bandwidth users will need for syncing. If you're not an IT admin, follow the steps in this article to limit the network bandwidth used for syncing your files: [Change the OneDrive sync app upload or download rate](https://support.office.com/article/71cc69da-2371-4981-8cc8-b4558bdda56e).
  
## Estimate the network bandwidth you need in your organization

Follow these steps to estimate the bandwidth that will be used when you fully deploy the sync app.
  
1. Assess the number of users and computers per user to which you'll deploy the sync app. Each installation multiplies the bandwidth used, so a user who has three syncing computers uses three times the bandwidth as a user who has a single syncing computer.
    
2. [Assess the available bandwidth and network conditions](network-utilization-planning.md#AssessAvailableBandwidth).
    
3. [Measure the network utilization of the sync app for a pilot group](network-utilization-planning.md#MeasureNetworkUtilization).
    
When you deploy, [Control sync throughput](network-utilization-planning.md#ControlSyncThroughput).
  
### Assess the available bandwidth and network conditions
<a name="AssessAvailableBandwidth"> </a>

You can use third-party speed test tools, like Wireshark or Fiddler, to understand the actual download and upload throughput that the users experience. 
  
Packet loss, latency, and other factors can also impact OneDrive upload and download experience. For example, a high-latency network or network experiencing a lot of loss could result in a degraded OneDrive upload and download experience even on high-bandwidth networks (1000 Mbps, for example). The loss and latency will likely vary based on the number of users that are on the same network and what those users are doing (like downloading or uploading large files).
  
The bandwidth used by the sync app is predominantly file upload and download traffic and is usually closely correlated with file size and the number of files being synced. Therefore, the bandwidth used depends on the number of files in the user's OneDrive and in SharePoint document libraries they choose to sync, multiplied by the size of files, and then by the rate of change of any file. Other sync app traffic (such as checking for file changes and checking for app updates) is minimal.
  
### Measure the network utilization of the sync app for a pilot group
<a name="MeasureNetworkUtilization"> </a>

When you create a pilot group, make sure the users are representative of the different profiles of people in your organization as well as the different geographic locations. To establish a group:
  
- Estimate the number of files, typical file sizes, file types, total size of each library, how frequently files are modified, and how frequently new files are added.
    
- Evaluate network utilization during each sync state as described below.
    
- Use the measurements from the pilot group to extrapolate the entire organization's needs and re-test to validate the estimations. Each organization is different.
    
#### Initial deployment and initial sync of team sites

When users download locations for the first time, bandwidth usage will spike. To avoid this spike, enable [Learn about OneDrive Files On-Demand](https://support.office.com/article/0e6860d3-d9f3-4971-b321-7092438fb38e). This allows users to browse their files in File Explorer without downloading them.
  
The following image illustrates the network utilization over time with Files On-Demand enabled and not enabled.
  
![OneDrive Sync App Network Load Patterns](media/6c03ed78-0575-454a-9cf0-989c7ae7451a.png)
  
#### Operational sync

After the initial sync is complete, the network usage will decrease and then level out. 

The OneDrive sync app provides differential sync for all file types stored in OneDrive and SharePoint. Differential sync enables the sync app to sync only the parts of large files that have changed, instead of the entire file. During everyday usage, when users change files, only the changes are uploaded or downloaded and not the whole file. This makes the file synchronization process faster for these files. It reduces the time it takes to upload and download the file as well as the bandwidth sync consumes.

> [!NOTE]
> Windows Notification Service or WNS plays an important role in efficient network utilization. Instead of the sync app constantly pulling to check for remote changes, WNS ensures that any changes from the cloud get pushed down to the device as fast as possible. It saves both network bandwidth and device battery life. This benefits both Windows and macOS. Make sure the connection to the service is enabled. Work with your network team to make sure proxies allow network traffic to bypass \*.wns.windows.com and avoid HTTPS decryption for \*.wns.windows.com. 

A spike in upload traffic is expected if you deploy the Known Folder Move setting in your organization. If your organization is large and your users have a lot of files in their known folders, make sure you roll out the policies slowly to minimize the network impact of uploading files. For detailed deployment guidance on Known Folder Move, see [Redirect and move Windows known folders to OneDrive](./redirect-known-folders.md).
  
## Control sync throughput
<a name="ControlSyncThroughput"> </a>

If you need to control sync app traffic, we recommend using network throughput policies provided by the OneDrive sync app. You can also use your network quality of service (QoS) policies or Windows QoS policies, or let users choose their throughput settings. For info about the network settings you can make available to your users, see [Change the OneDrive sync app upload or download rate](https://support.office.com/article/71cc69da-2371-4981-8cc8-b4558bdda56e).

### Use OneDrive policies

You can use policies included with the OneDrive sync app to control network throughput. These policies are available in the OneDrive installation directory `%localappdata%\Microsoft\OneDrive\BuildNumber\adm\` where `BuildNumber` is the number displayed in sync app settings on the About tab.
  
For info about these policies, see:

 - [Enable automatic upload bandwidth management for OneDrive](use-group-policy.md#enable-automatic-upload-bandwidth-management-for-onedrive) - Recommended for best user experience 

 - [Limit the sync app upload speed to a fixed rate](use-group-policy.md#limit-the-sync-app-upload-speed-to-a-fixed-rate)
  
 - [Limit the sync app download speed to a fixed rate](use-group-policy.md#limit-the-sync-app-download-speed-to-a-fixed-rate)
  
 - [Limit the sync app upload rate to a percentage of throughput](use-group-policy.md#limit-the-sync-app-upload-rate-to-a-percentage-of-throughput)
    
### Prioritize traffic by using Windows Quality of Service (QoS) policy

To define the priority of outbound network traffic, you can configure a QoS policy with a specific differentiated services code point (DSCP) value. Network routers use the DSCP value to classify network packets and determine the appropriate queue. A higher value indicates a higher priority for the packet. The number of queues and their prioritization behavior needs to be designed as part of your organization's QoS strategy.

To manage the use of network bandwidth, you can configure a QoS policy with a specific throttle rate for outbound traffic. With throttling, a QoS policy will limit the outgoing network traffic to a specified rate.
  
1. Open the Group Policy Management Console.
    
2. Browse to the location where you want to create the new policy. For example, if all your client computers are located in an OU (Organizational Unit) named "Clients" then the new policy should be created in the "Clients" OU. 
    
3. Right-click the location, select **Create a GPO in this domain**, and then select **Link it here**. 
    
4. In the **New GPO** dialog, enter a name for the new Group Policy object in the **Name** box (for example, "OneDrive sync app") and then select **OK**. 
    
5. Right-click the policy, and then select **Edit**. 
    
6. In the Group Policy Management Editor, expand **Computer Configuration**, expand **Policies**, expand **Windows Settings**, right-click **Policy-based QoS**, and then select **Create new policy**. 
    
7. In the **Policy-based QoS** dialog, enter a name for the new policy in the **Name** box (for example, "OneDrive sync app"). 
    
8. Select **Specify DSCP Value** and set the appropriate value between 0 and 63 based on your organization's QoS strategy. 
    
9. In the **Outbound Throttle Rate** box, enter a rate in KBps, and select **Next**. 
    
10. Select **Only applications with this executable name** and to apply the QoS policy to only the OneDrive sync app process, enter "onedrive.exe". Select **Next**. 
    
11. Make sure that both **Any source IP address** and **Any destination IP address** are selected, and then select **Next**. These two settings ensure that packets will be managed regardless of which computer (IP address) sent those packets and which computer (IP address) will receive those packets. 
    
12. In the **Select the protocol this QoS policy applies to** list, select **TCP**. Leave **from any source port** and **to any destination** selected.

13. Select **Finish**.
  
## See also
<a name="ControlSyncThroughput"> </a>

[Network planning and performance tuning for Microsoft 365](/office365/enterprise/network-planning-and-performance)