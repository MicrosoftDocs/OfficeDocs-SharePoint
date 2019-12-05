---
title: "Add the Yammer Embed widget to a SharePoint page"
ms.reviewer: 
ms.author: mikeplum
author: MikePlumleyMSFT
manager: pamgreen
ms.date: 09/07/2018
audience: ITPro
ms.topic: article
ms.prod: sharepoint-server-itpro
localization_priority: Normal
ms.assetid: 48fa0391-b996-4a46-8744-4b1777db3d2f
description: "Learn how to use the Yammer Embed widget to include Yammer feeds on SharePoint pages."
---

# Add a Yammer feed to a SharePoint page

[!INCLUDE[appliesto-2013-2016-2019-xxx-md](../includes/appliesto-2013-2016-2019-xxx-md.md)] 
  
You can choose the type of Yammer feed to include.
| Type           |Description            | Example     |
|:--------------:|:----------------------|:-------------|
|Group           |The feed for one group | On a team intranet page.|
|Topic|All conversations tagged with one topic| On an benefits page on an intranet, show all conversations tagged with #EmployeeDiscount.|
|User|All conversations that include messages from the specified user|On a directory page for the user.|
|My Feed|The user's home feed|On a user's My site or home page. <br/> <br/>The Embed version of My feed shows slightly different messages than the ones included in the home feeds available in Yammer web, desktop, or mobile. In Embed My Feed, users will see messages from all threads in groups they are a member of and all threads in the All Company group. In Yammer web, desktop, and mobile, users can select Discovery, All, or Following feeds, but these aren't available in Embed. The Embed My Feed/Home feed type is closest to the All feed, but doesn't include public posts in public groups they don't belong to.|
|Open Graph|Connect a specific file or other OpenGraph object to Yammer|Collecting feedback page on a proposal.| 

For each feed type, you can select options including the size of the box displaying the feed, and whether the background is dark or light.

There are three steps to the process:
- Step 1: Collect the identifying information for the group, topic, or user from Yammer.
- Step 2: Generate the code to embed using the Yammer Embed configuration tool.
- Step 3: Embed the code in a Script Editor Web Part on the SharePoint page. You'll need a 400 pixel or wider web part.

When the Yammer widget is embedded in a SharePoint page, the specified feed is displayed if the user is signed in. If the user is not signed in, they will be prompted to sign in.

## Step 1: Collect the feed information from Yammer
How you collect the feed info depends on the feed type you select.

### Collect group feed information from Yammer

There are two options:

- **Get the entire widget from the group page in Yammer**

    Note: This code uses default settings for the embedded Yammer feed. 
    1. Go to the group in Yammer, and under **Access Options** at the bottom of the left panel, select **Embed this feed in your site**. 
    2. Copy the code. 

- **Get the group feed id to use with the Yammer Embed Configuration Tool**
    1. Using Yammer in a web browser, go to the group.
    2. Copy the feed ID from the URL. For example, in this URL, https://www.yammer.com/contoso.com/#/threads/inGroup?type=in_group&feedId=1170863, copy 1170863.

### Collect topic feed information from Yammer
1. Using Yammer in a web browser, search for the topic by entering #*topic_name* in the Search box. For example, if looking for all conversations tagged with the EmployeeVolunteering tag, search for #EmployeeVolunteering.
2. Select the topic, look at the URL, and copy the topic id. For example, in this URL,  https://www.yammer.com/contoso.com/topics/2084748#/Threads/AboutTopic?type=about_topic&feedId=2084748, copy 2084748.

### Collect user feed information from Yammer 
1. Using Yammer in a web browser, click the icon or name of the person from anywhere in Yammer. 
3. Copy the user ID from the URL. For example, in this URL, https://www.yammer.com/contoso.com/#/users/1906364, copy 1906364.

##Step 2: Generate the widget code using the Yammer Embed configuration tool

1. Go to the Yammer Embed configuration tool, at [https://www.yammer.com/widget/configure] (https://go.microsoft.com/fwlink/p/?LinkId=507500). 
2. Select the **Behavior** options:
    
    - **Network permalink**: Your domain name for Yammer, such as Contoso.com, or Contoso.onmicrosoft.com.
   
    - **Default group_id**: This is only needed for user and topic feeds. It specifies which group should be the default for new posts from the embedded feet.

    - **Custom prompt text**: The prompt that users will see when a group or My Feed type is selected. If left blank, the default "What are you working on?" prompt will be displayed.

    - **Feed type**: Select one of the following:

        - **Group**: The feed for one group.

        - **My Feed**: The user's home feed

        - **Topic**: All conversations tagged with one topic.

        - **User**: All conversations that include messages from the specified user.

        - **Open Graph**: Use this to show all conversations about a specific OpenGraph object such as a file or folder or image. It can also be used to embed a **Like** or **Follow** button on the page. For information about inserting these buttons, see  [Embed](https://go.microsoft.com/fwlink/p/?LinkId=507501) in the [Yammer Developer Center](https://go.microsoft.com/fwlink/p/?LinkId=507502). 

    - **Feed ID**: The ID you identified in Step 2 above for the specific Yammer group, topic, or user. This should be left blank if you select **My Feed** as the feed type.

    - **Default to canonical** Only use this option if you have external networks. If a user switches to an external network from a Yammer feed embedded on a SharePoint page, if this option is checked, when the user returns to the SharePoint page, they will start by seeing their home network. If this is unchecked, the user will go directly to the external network.

    - **Use SSO**: Configure redirection to your identity provider. The domain listed in the **Network permalink** field must be configured for federation in Office 365. For more information about this option, see [Embed](https://go.microsoft.com/fwlink/p/?LinkId=507501) in the [Yammer Developer Center](https://go.microsoft.com/fwlink/p/?LinkId=507502).

3. Select the **Appearance** options.
    The header and footer options only apply to some types of feeds. The preview will show you whether they apply to the feed type you have selected.
        - **Show header**:  Displays a header on the page. The content of the header depends on the **Hide network in header** setting.
        - **Show footer**: Displays a footer showing the person's name and a **log out** link.
        - **Hide network in header**: If selected, the header includes **Yammer conversations". If not selected, the header shows the company name 
        - **Theme** : Use a light or dark background for the embedded Yammer conversations. This does not work in all browsers.

4. If you selected an Open Graph feed, select the **OpenGraph settings** options.
    - **OpenGraphURL**  The URL you want to connect to Yammer.
    - **OpenGraph type** The type of object: **Page**, **Audio**, **Department**, **Document**, **File**, **Folder**, **mage**, **Person**, **Place**, **Project**, **Team**, or **Video**. 
    - **Show preview**
    - **Fetch metadata**
    - **Mark as "private"**
    - **Ignore canonical url**

5. Click **Apply**. You'll see a preview of what will be embedded.

6. Copy the code shown under **Example code**.

  ![Screenshot of the Yammer Embed configuration tool](../media/yammer-embed-preview.png)
  
  
## Step 3: Place the Yammer Embed widget in a SharePoint page

1. On the SharePoint page where you want the code, select **Edit Page**.
2. Select the spot on the page where you want this information to appear.
3. On the **Insert** tab, select **Embed Code**.

## See also

#### Concepts

[Integrate Yammer with on-premises SharePoint Server environments](integrate-yammer-with-on-premises-sharepoint-server-environments.md)

