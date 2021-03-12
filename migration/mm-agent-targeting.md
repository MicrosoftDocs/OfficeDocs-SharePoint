---
title: Agent groups in Migration Manager"
ms.reviewer: 
ms.author: jhendr
author: JoanneHendrickson
manager: serdars
recommendations: true
audience: ITPro
f1.keywords:
- NOCSH
ms.topic: article
ms.service: sharepoint-online
mscollection: 
- SPMigration
- M365-collaboration
localization_priority: Normal
search.appverid: MET150
description: "Learn about creating and using agent groups in Migration Manager."
---
#  Agent groups in Migration Manager (preview)

>[!Important]
> This advanced feature is currently in private preview and subject to change without notice.


With Migration Manager, you can create "agent groups" and assign agents to them.  Agent groups are considered an advanced feature and not commonly used by most users.

When an Agent is created in Migration Manager, it is not assigned to any group other than the default location. With the introduction of Agent Groups, you can assign one or more agents to a specific group. A group maybe represent a particular geographical location or have a targeted purpose. Agent groups let you organize and prioritize your agents for a targeted purpose or regional goal.

|What|Why|
|:-----|:-----|
|Multi-geo| Organize your agents to be dedicated to specific geographic regions. | 
|Network scenarios|Create agent groups to optimize for network conditions |
|Prioritize migration jobs|Create agent groups so you can assign tasks according to groups by their priority |
|Assessment planning|Organize your tasks to run in a group that is used for isolating jobs that you just want to scan for early assessment.|



## Create an agent group

1. From the Agents tab in Migration Manager, highlight an agent from the list.  A side panel displays to the right.
2. Under Agent group, select **Edit.**
3. Select **Add or remove agent groups**.
4. Enter a name for your new agent group.  An agent group name cannot exceed 255 characters.
5. Click **Save**.


## Assign an agent to an agent group

1.  From the Agents tab in Migration Manager, highlight an agent from the list.  A side panel displays to the right.
2.  Select an agent group from the choices in the dropdown list.
3. Select **Save**.

>[!Note]
>You cannot assign multiple agents to a group at the same time. 



## Assign a task to an agent group

1. From the Configure settings pane, enter a Task name.
2. Select an agent group from the dropdown list.
3. Select **Save**.

