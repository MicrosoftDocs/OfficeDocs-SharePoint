---
title: "Frequently asked questions about the Feed for Viva Connections"
ms.reviewer: 
ms.author: hokavian
author: Holland-ODSP
manager: pamgreen
audience: Admin
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
localization_priority: Priority
ms.collection:  
- Strat_SP_modern
- M365-collaboration
search.appverid:
- SPO160
- MET150
description: "Frequently asked questions about the Feed for Viva Connections"
---

# Get answers to common questions about the Viva Connections Feed 

**Question:** What do I expect to see on the Feed?

**Answer:** The Feed will give content publishers a reliable means of distributing important news and information that their users need within their organizations.  In addition, users will also see engaging content from sites they are a member of/follow and communities they follow. The list of content that users will see in their feed for the Viva Connections current release is listed in the question “Where is content sourced for the Feed?” As fresher content is added to your feed, older content will be pushed down the feed. 

However, we don’t rely on a pure chronological ranking. We will look at several factors to determine the content ranking and users will only be able to view content that they have permission to view. Refer to the question “How is the feed personalized and ranked?" for more information.



**Question:** Where is content sourced for the Feed?

**Answer:** In the current release of Viva Connections, Feed content will come from:
1. News published via SharePoint sites:
    - SharePoint News from [organizational news sites](organization-news-site.md) 
    - SharePoint News from sites you follow/sites you are a member of
    - Boosted SharePoint News from Org News Sites
    - User Targeted News from Org News site or sites you follow
    
2. Posts published in Yammer communities:
    - Yammer All Company Featured Posts
    - Yammer All Company Announcements 
    - Yammer All Company Posts
    - Yammer Followed Community Featured Posts
    - Yammer Followed Community Announcements
    - Yammer Followed Community Posts
    
3. [Stream videos](/stream/streamnew/new-stream) built on SharePoint or OneDrive 


Not all of the content will be given equal weight in the ranking, refer to the question “How is the feed personalized and ranked?" for more information.




**Question:** How often is Feed content refreshed? 

**Answer:** For mobile, the feed refreshes on each boot of the application. Users can also manually refresh the feed through the pull-down action. On the web, the feed automatically refreshes each time the web page is refreshed.



**Question:** When can we expect to see a post in the feed after creating it?

**Answer:** Posts will typically take up to a maximum of 1 hour to appear on a user’s feed.  Content from newly created Home sites is sometimes delayed for seven days after the site is initially created.  After that initial seven day period has passed, it will take the typical 1 hour to appear.




**Question:** How is the feed personalized and ranked?

**Answer:** We’re experimenting and rapidly iterating on the logic used:

- **Chronology** - Content is sorted into 3 buckets.
- **Promotion** - Boost & Featured is surfaced highly in each bucket.
- **Source Priority** - “Top Down” messaging is ranked slightly higher than organic content from people around you.
- **Engagement** - Ensure dynamic mix of content types within each bucket.


One of the primary goals of the feed is to give content publishers a reliable means of distributing important news and information. We can only do this if we convince most your organization to visit the feed regularly. To keep them interested and coming back regularly we’re trying to strike a balance between the engaging content, they want (from sites they are a member of/follow and communities they favorite/follow) and the information they need (SharePoint Org News and Yammer All Company).
To achieve this, we don’t rely on a pure chronological ranking.  

We look at several factors such as the content’s age, whether it’s been ‘promoted’ by the organization, the publishing source, and the author’s relationship to the reader to determine the content ranking. We want users to discover new content each time they open the Feed so it never gets boring or predictable. However, this relies on how often content is created on the SharePoint sites and Yammer communities.  

Over time, we plan on continuing to experiment with our ranking and to add new factors to the algorithm we use. We will be moving over to a machine learning model that is optimized for user engagement while preserving the ability for organizations to lift important content that is recent to the top of users Feeds. (Refer to “What controls do customers have over the Feed configuration?” for more information).

The content in the feed is personalized for each user based on their memberships and permissions. We always restrict what content the user sees to content they have permissions to view.  In addition to any org-wide memberships, we’ll include content from SharePoint sites and Yammer communities the user is optionally a member of.  All of this is toward the goal of having a fresh, dynamic, and engaging Feed to keep them coming back.


**Question:** Why don’t I see any content in the Feed?

**Answer:** If you’re not seeing any content in your feed, it could be because of a few reasons:
1. There needs to be some content published to a SharePoint site or Yammer community that you’re a member of.  
2. Yammer Posts that are not Featured or to All Company communities or Announcements may be removed and replaced in subsequent feed views to give users more dynamic content.
3. The SharePoint site you are publishing from (Home site or Org News site) is less than seven days old.  This issue will resolve itself and content will appear normally after the initial seven days after site creation.



**Question:** What controls do customers have over the Feed configuration?

**Answer:** There’s no configuration required to get the feed working.  For the current release, customers have the ability to affect content placement in the feed by targeting content, or by promoting it.

- **Promote important ‘official’ communications** - Use Boost to raise the visibility of crucial news posts.
- **Highlight community discussions** - Feature posts in public Yammer communities that you’d like seen by the entire organization.
- **Publish from official sources** - Where content is from, impacts the ranking.

On SharePoint News, more filtering is available through Audience Targeting, which allows publishers to designate content relevant to specific groups of individuals.  Examples might be employees in a specific region, building, or title.  This is done by enabling audience targeting on the site where content is being published, then using Azure Active Directory groups to define the target audience. However, if audience targeting is not applied, users will still get the SharePoint News on their feed. Publishers also have the ability to promote critical messages in the Feed.  News published from Org News sites has a Boost feature that explicitly tells the feed ‘this content is important’.  As a result, that content is artificially pushed to the top of the feed.

In Yammer, moderators of the All-Company community can Feature a post to indicate it’s significant and increase visibility within the organization.  Featured posts from Yammer are treated as important by our ranking algorithm. For communities that you are a member of, communication managers can also create Announcements within those communities, which will also be treated as important by our ranking algorithm.


**Question:** What actions can I take on the feed?

**Answer:** For the current release, users on the Feed can do the following actions on posts:
1.	Comment on a post.
2.	Reply to a comment on a post.
3.	Social Reactions – React to a post and comment.
4.	Share a post.
5.	Save a post for later.



**Question:** What can I do to keep content after I have viewed it?  

**Answer:** Users can keep content that they like for whatever intended purpose through the **Save for Later** feature. These items can then be accessed through the save for later feature in the Viva Connections mobile app in Teams.


## More resources

[Overview of Viva Connections](viva-connections-overview.md)

[Set up and launch Viva Connections](guide-to-setting-up-viva-connections.md)

[Use the Feed web part for Viva Connections](https://support.microsoft.com/office/use-the-feed-web-part-for-viva-connections-001fbe90-3778-4801-9ea9-71308711d330)
